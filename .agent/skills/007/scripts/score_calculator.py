import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import (  
    BASE_DIR,
    DATA_DIR,
    SCORING_WEIGHTS,
    SCORING_LABELS,
    SCORE_HISTORY_PATH,
    SEVERITY,
    SCANNABLE_EXTENSIONS,
    SKIP_DIRECTORIES,
    LIMITS,
    ensure_directories,
    get_verdict,
    get_timestamp,
    log_audit_event,
    setup_logging,
    calculate_weighted_score,
)

sys.path.insert(0, str(Path(__file__).resolve().parent / "scanners"))

import secrets_scanner  
import dependency_scanner  
import injection_scanner  

import quick_scan  

logger = setup_logging("007-score-calculator")

_SENSITIVE_FINDING_KEYS = {
    "snippet",
    "secret",
    "token",
    "password",
    "access_token",
    "app_secret",
    "authorization_code",
    "client_secret",
}

_AUTH_PATTERNS = [
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
]

_ENCRYPTION_PATTERNS = [
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
]

_RESILIENCE_PATTERNS = [
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
]

_MONITORING_PATTERNS = [
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
]

_INPUT_VALIDATION_PATTERNS = [
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
    re.compile(r),
]

def _collect_source_files(target: Path) -> list[Path]:
    
    files: list[Path] = []
    max_files = LIMITS["max_files_per_scan"]

    for root, dirs, filenames in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRECTORIES]
        for fname in filenames:
            if len(files) >= max_files:
                return files
            fpath = Path(root) / fname
            suffix = fpath.suffix.lower()
            name = fpath.name.lower()
            for ext in SCANNABLE_EXTENSIONS:
                if name.endswith(ext) or suffix == ext:
                    files.append(fpath)
                    break

    return files

def _count_pattern_matches(files: list[Path], patterns: list[re.Pattern]) -> int:
    
    count = 0
    for fpath in files:
        try:
            size = fpath.stat().st_size
            if size > LIMITS["max_file_size_bytes"]:
                continue
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        for pat in patterns:
            if pat.search(text):
                count += 1
                break  

    return count

def _deduplicate_findings(findings: list[dict]) -> list[dict]:
    
    seen: set[tuple] = set()
    unique: list[dict] = []

    for f in findings:
        key = (f.get("file", ""), f.get("line", 0), f.get("pattern", ""))
        if key not in seen:
            seen.add(key)
            unique.append(f)

    return unique

def _score_from_findings(findings: list[dict], max_deduction: int = 100) -> int:
    
    deductions = {"CRITICAL": 15, "HIGH": 8, "MEDIUM": 3, "LOW": 1, "INFO": 0}
    total_deduction = 0
    for f in findings:
        total_deduction += deductions.get(f.get("severity", "INFO"), 0)
    return max(0, min(100, max_deduction - total_deduction))

def _score_from_positive_signals(
    match_count: int,
    total_files: int,
    base_score: int = 30,
    max_score: int = 100,
) -> int:
    
    if total_files == 0:
        return base_score

    ratio = min(1.0, match_count / max(1, total_files * 0.1))
    return min(max_score, int(base_score + ratio * (max_score - base_score)))

def compute_domain_scores(
    secrets_findings: list[dict],
    injection_findings: list[dict],
    dependency_report: dict,
    quick_findings: list[dict],
    source_files: list[Path],
    total_source_files: int,
) -> dict[str, float]:
    
    scores: dict[str, float] = {}

    
    secret_only = [f for f in secrets_findings if f.get("type") == "secret"]
    scores["secrets"] = float(_score_from_findings(secret_only))

    
    
    injection_input_related = [
        f for f in injection_findings
        if f.get("injection_type") in (
            "sql_injection", "code_injection", "command_injection",
            "xss", "path_traversal",
        )
    ]
    negative_score = _score_from_findings(injection_input_related)
    positive_count = _count_pattern_matches(source_files, _INPUT_VALIDATION_PATTERNS)
    positive_score = _score_from_positive_signals(positive_count, total_source_files)
    scores["input_validation"] = float(min(100, (negative_score + positive_score) // 2))

    
    auth_count = _count_pattern_matches(source_files, _AUTH_PATTERNS)
    if total_source_files == 0:
        scores["authn_authz"] = 50.0  
    elif auth_count == 0:
        scores["authn_authz"] = 25.0  
    else:
        scores["authn_authz"] = float(_score_from_positive_signals(
            auth_count, total_source_files, base_score=40, max_score=95,
        ))

    
    enc_count = _count_pattern_matches(source_files, _ENCRYPTION_PATTERNS)
    
    data_exposure = [
        f for f in secrets_findings
        if f.get("pattern") in (
            "db_connection_string", "url_embedded_credentials",
            "hardcoded_public_ip",
        )
    ]
    negative_dp = _score_from_findings(data_exposure)
    positive_dp = _score_from_positive_signals(enc_count, total_source_files)
    scores["data_protection"] = float(min(100, (negative_dp + positive_dp) // 2))

    
    res_count = _count_pattern_matches(source_files, _RESILIENCE_PATTERNS)
    scores["resilience"] = float(_score_from_positive_signals(
        res_count, total_source_files, base_score=30, max_score=95,
    ))

    
    mon_count = _count_pattern_matches(source_files, _MONITORING_PATTERNS)
    scores["monitoring"] = float(_score_from_positive_signals(
        mon_count, total_source_files, base_score=20, max_score=95,
    ))

    
    dep_score = dependency_report.get("score", 50)
    scores["supply_chain"] = float(max(0, min(100, dep_score)))

    
    
    other_scores = [
        scores.get(k, 0.0) for k in SCORING_WEIGHTS if k != "compliance"
    ]
    if other_scores:
        scores["compliance"] = float(round(sum(other_scores) / len(other_scores), 2))
    else:
        scores["compliance"] = 50.0

    return scores

def _save_score_history(
    target: str,
    domain_scores: dict[str, float],
    final_score: float,
    verdict: dict,
) -> None:
    
    ensure_directories()

    entry = {
        "timestamp": get_timestamp(),
        "target": target,
        "domain_scores": domain_scores,
        "final_score": final_score,
        "verdict": {
            "label": verdict["label"],
            "description": verdict["description"],
            "emoji": verdict["emoji"],
        },
    }

    
    history: list[dict] = []
    if SCORE_HISTORY_PATH.exists():
        try:
            raw = SCORE_HISTORY_PATH.read_text(encoding="utf-8")
            if raw.strip():
                history = json.loads(raw)
                if not isinstance(history, list):
                    history = [history]
        except (json.JSONDecodeError, OSError):
            history = []

    history.append(entry)

    SCORE_HISTORY_PATH.write_text(
        json.dumps(history, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

def _bar(score: float, width: int = 20) -> str:
    
    filled = int(score / 100 * width)
    return "[" + "

def _redact_report_value(value):
    
    if isinstance(value, dict):
        return {key: _redact_report_value(value[key]) for key in value}
    if isinstance(value, list):
        return [_redact_report_value(item) for item in value]
    return value

def redact_findings_for_report(findings: list[dict]) -> list[dict]:
    
    redacted: list[dict] = []

    for finding in findings:
        safe_finding: dict = {}
        finding_type = str(finding.get("type", "")).lower()

        for key, value in finding.items():
            key_lower = key.lower()
            if key_lower in _SENSITIVE_FINDING_KEYS:
                safe_finding[key] = "[redacted]"
                continue
            if finding_type == "secret" and key_lower in {"entropy", "match", "raw", "value"}:
                safe_finding[key] = "[redacted]"
                continue
            safe_finding[key] = _redact_report_value(value)

        redacted.append(safe_finding)

    return redacted

def build_safe_scanner_summaries(scanner_summaries: dict[str, dict]) -> dict[str, dict]:
    
    safe_summaries: dict[str, dict] = {}

    for scanner_name, summary in scanner_summaries.items():
        safe_summaries[scanner_name] = {
            "findings": int(summary.get("findings", 0)),
            "score": float(summary.get("score", 0)),
        }

    return safe_summaries

def format_text_report(
    target: str,
    domain_scores: dict[str, float],
    final_score: float,
    verdict: dict,
    scanner_summaries: dict[str, dict],
    total_findings: int,
    elapsed: float,
) -> str:
    
    lines: list[str] = []

    lines.append("=" * 72)
    lines.append("  007 SECURITY SCORE REPORT")
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"  Target:          {target}")
    lines.append(f"  Timestamp:       {get_timestamp()}")
    lines.append(f"  Duration:        {elapsed:.2f}s")
    lines.append(f"  Total findings:  {total_findings} (deduplicated)")
    lines.append("")

    
    lines.append("-" * 72)
    lines.append("  SCANNER RESULTS")
    lines.append("-" * 72)
    for scanner_name, summary in scanner_summaries.items():
        findings_count = summary.get("findings", 0)
        scanner_score = summary.get("score", "N/A")
        lines.append(f"    {scanner_name:<25} findings={findings_count:<6} score={scanner_score}")
    lines.append("")

    
    lines.append("-" * 72)
    lines.append("  DOMAIN SCORES")
    lines.append("-" * 72)
    lines.append(f"    {'Domain':<30} {'Weight':>6}  {'Score':>5}  {'Bar'}")
    lines.append(f"    {'-' * 30} {'-' * 6}  {'-' * 5}  {'-' * 22}")

    for domain, weight in SCORING_WEIGHTS.items():
        score = domain_scores.get(domain, 0.0)
        label = SCORING_LABELS.get(domain, domain)
        weight_pct = f"{weight * 100:.0f}%"
        lines.append(
            f"    {label:<30} {weight_pct:>6}  {score:>5.1f}  {_bar(score)}"
        )
    lines.append("")

    
    lines.append("=" * 72)
    lines.append(f"  FINAL SCORE:  {final_score:.1f} / 100")
    lines.append(f"  VERDICT:      {verdict['emoji']} {verdict['label']}")
    lines.append(f"                {verdict['description']}")
    lines.append("=" * 72)
    lines.append("")

    return "\n".join(lines)

def build_json_report(
    target: str,
    domain_scores: dict[str, float],
    final_score: float,
    verdict: dict,
    scanner_summaries: dict[str, dict],
    all_findings: list[dict],
    total_findings: int,
    elapsed: float,
) -> dict:
    
    safe_findings = redact_findings_for_report(all_findings)
    return {
        "report": "score_calculator",
        "target": target,
        "timestamp": get_timestamp(),
        "duration_seconds": round(elapsed, 3),
        "total_findings": total_findings,
        "domain_scores": domain_scores,
        "final_score": final_score,
        "verdict": {
            "label": verdict["label"],
            "description": verdict["description"],
            "emoji": verdict["emoji"],
        },
        "scanner_summaries": scanner_summaries,
        "findings": safe_findings,
    }

def run_score(
    target_path: str,
    output_format: str = "text",
    verbose: bool = False,
) -> dict:
    
    if verbose:
        logger.setLevel("DEBUG")

    ensure_directories()

    target = Path(target_path).resolve()
    if not target.exists():
        logger.error("Target path does not exist: %s", target)
        sys.exit(1)
    if not target.is_dir():
        logger.error("Target is not a directory: %s", target)
        sys.exit(1)

    logger.info("Starting unified security score calculation for %s", target)
    start_time = time.time()
    target_str = str(target)

    
    
    

    scanner_summaries: dict[str, dict] = {}

    
    logger.info("Running secrets scanner...")
    try:
        secrets_report = secrets_scanner.run_scan(
            target_path=target_str,
            output_format="json",
            verbose=verbose,
        )
    except SystemExit:
        secrets_report = {"findings": [], "score": 50, "total_findings": 0}

    secrets_findings = secrets_report.get("findings", [])
    scanner_summaries["secrets_scanner"] = {
        "findings": len(secrets_findings),
        "score": secrets_report.get("score", 50),
    }

    
    logger.info("Running dependency scanner...")
    try:
        dep_report = dependency_scanner.run_scan(
            target_path=target_str,
            output_format="json",
            verbose=verbose,
        )
    except SystemExit:
        dep_report = {"findings": [], "score": 50, "total_findings": 0}

    dep_findings = dep_report.get("findings", [])
    scanner_summaries["dependency_scanner"] = {
        "findings": len(dep_findings),
        "score": dep_report.get("score", 50),
    }

    
    logger.info("Running injection scanner...")
    try:
        inj_report = injection_scanner.run_scan(
            target_path=target_str,
            output_format="json",
            verbose=verbose,
        )
    except SystemExit:
        inj_report = {"findings": [], "score": 50, "total_findings": 0}

    inj_findings = inj_report.get("findings", [])
    scanner_summaries["injection_scanner"] = {
        "findings": len(inj_findings),
        "score": inj_report.get("score", 50),
    }

    
    logger.info("Running quick scan...")
    try:
        quick_report = quick_scan.run_scan(
            target_path=target_str,
            output_format="json",
            verbose=verbose,
        )
    except SystemExit:
        quick_report = {"findings": [], "score": 50, "total_findings": 0}

    quick_findings = quick_report.get("findings", [])
    scanner_summaries["quick_scan"] = {
        "findings": len(quick_findings),
        "score": quick_report.get("score", 50),
    }

    
    
    
    all_findings_raw = secrets_findings + dep_findings + inj_findings + quick_findings
    all_findings = _deduplicate_findings(all_findings_raw)
    total_findings = len(all_findings)
    safe_findings = redact_findings_for_report(all_findings)
    safe_total_findings = len(safe_findings)
    safe_scanner_summaries = build_safe_scanner_summaries(scanner_summaries)

    logger.info(
        "Aggregated %d raw findings -> %d unique (deduplicated)",
        len(all_findings_raw), total_findings,
    )

    
    
    
    logger.info("Scanning for positive security signals...")
    source_files = _collect_source_files(target)
    total_source_files = len(source_files)
    logger.info("Collected %d source files for positive-signal analysis", total_source_files)

    
    
    
    domain_scores = compute_domain_scores(
        secrets_findings=secrets_findings,
        injection_findings=inj_findings,
        dependency_report=dep_report,
        quick_findings=quick_findings,
        source_files=source_files,
        total_source_files=total_source_files,
    )

    
    
    
    final_score = calculate_weighted_score(domain_scores)
    verdict = get_verdict(final_score)

    elapsed = time.time() - start_time
    logger.info(
        "Score calculation complete in %.2fs: final_score=%.1f, verdict=%s",
        elapsed, final_score, verdict["label"],
    )

    
    
    
    _save_score_history(target_str, domain_scores, final_score, verdict)

    log_audit_event(
        action="score_calculation",
        target=target_str,
        result=f"final_score={final_score}, verdict={verdict['label']}",
        details={
            "domain_scores": domain_scores,
            "total_findings": safe_total_findings,
            "scanner_summaries": safe_scanner_summaries,
            "duration_seconds": round(elapsed, 3),
        },
    )

    
    
    
    report = build_json_report(
        target=target_str,
        domain_scores=domain_scores,
        final_score=final_score,
        verdict=verdict,
        scanner_summaries=safe_scanner_summaries,
        all_findings=all_findings,
        total_findings=safe_total_findings,
        elapsed=elapsed,
    )

    if output_format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_text_report(
            target=target_str,
            domain_scores=domain_scores,
            final_score=final_score,
            verdict=verdict,
            scanner_summaries=safe_scanner_summaries,
            total_findings=safe_total_findings,
            elapsed=elapsed,
        ))

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "007 Score Calculator -- Unified security scoring engine.\n"
            "Runs all scanners and computes per-domain security scores."
        ),
        epilog=(
            "Examples:\n"
            "  python score_calculator.py --target ./my-project\n"
            "  python score_calculator.py --target ./my-project --output json\n"
            "  python score_calculator.py --target ./my-project --verbose"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Path to the directory to scan (required).",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format: 'text' (default) or 'json'.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose/debug logging.",
    )

    args = parser.parse_args()
    run_score(
        target_path=args.target,
        output_format=args.output,
        verbose=args.verbose,
    )
