import argparse
import base64
import json
import math
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  

logger = config.setup_logging("007-secrets-scanner")

_EXTRA_PATTERN_DEFS = [
    
    (
        "url_embedded_credentials",
        r,
        "HIGH",
    ),
    
    (
        "stripe_key",
        r,
        "CRITICAL",
    ),
    
    (
        "google_api_key",
        r,
        "HIGH",
    ),
    
    (
        "twilio_key",
        r,
        "HIGH",
    ),
    
    (
        "heroku_api_key",
        r,
        "HIGH",
    ),
    
    (
        "sendgrid_key",
        r,
        "CRITICAL",
    ),
    
    (
        "npm_token",
        r,
        "CRITICAL",
    ),
    
    (
        "connection_string",
        r,
        "HIGH",
    ),
    
    (
        "jwt_token",
        r,
        "MEDIUM",
    ),
    
    (
        "azure_storage_key",
        r,
        "CRITICAL",
    ),
]

EXTRA_PATTERNS = [
    (name, re.compile(pattern), severity)
    for name, pattern, severity in _EXTRA_PATTERN_DEFS
]

ALL_SECRET_PATTERNS = list(config.SECRET_PATTERNS) + EXTRA_PATTERNS

ENV_FILE_PATTERNS = {
    ".env", ".env.local", ".env.production", ".env.staging",
    ".env.development", ".env.test", ".env.example", ".env.sample",
    ".env.defaults", ".env.template",
}

CONFIG_EXTENSIONS = {".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf"}

SHELL_EXTENSIONS = {".sh", ".bash", ".zsh", ".ps1", ".bat", ".cmd"}

DOCKER_PREFIXES = ("Dockerfile", "dockerfile", "docker-compose")

CICD_PATTERNS = {
    ".github/workflows",
    ".gitlab-ci.yml",
    "Jenkinsfile",
    ".circleci/config.yml",
    ".travis.yml",
    "azure-pipelines.yml",
    "bitbucket-pipelines.yml",
}

PRIVATE_KEY_EXTENSIONS = {".pem", ".key", ".p12", ".pfx", ".jks", ".keystore"}

_TEST_FILE_PATTERNS = re.compile(
    r
)

_PLACEHOLDER_PATTERN = re.compile(
    r
    r
    r
)

def shannon_entropy(s: str) -> float:
    
    if not s:
        return 0.0

    length = len(s)
    freq: dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    entropy = 0.0
    for count in freq.values():
        probability = count / length
        if probability > 0:
            entropy -= probability * math.log2(probability)

    return entropy

_BASE64_RE = re.compile(
    r
)

_BASE64_URL_RE = re.compile(
    r
)

def _check_base64_secret(token: str) -> bool:
    
    
    padded = token + "=" * (-len(token) % 4)
    try:
        decoded = base64.b64decode(padded, validate=True)
        decoded_str = decoded.decode("ascii", errors="replace")
        
        return shannon_entropy(decoded_str) > 4.0 and len(decoded) >= 12
    except Exception:
        return False

_IP_RE = re.compile(
    r
)

_SAFE_IP_PREFIXES = (
    "127.",       
    "0.",         
    "10.",        
    "192.168.",   
    "169.254.",   
    "255.",       
)

def _is_private_or_localhost(ip: str) -> bool:
    
    if ip.startswith(_SAFE_IP_PREFIXES):
        return True
    
    parts = ip.split(".")
    try:
        if parts[0] == "172" and 16 <= int(parts[1]) <= 31:
            return True
    except (IndexError, ValueError):
        pass
    return False

_COMMENT_LINE_RE = re.compile(
    r, re.IGNORECASE
)

_MARKDOWN_CODE_FENCE = re.compile(r)

def _is_comment_line(line: str) -> bool:
    
    return bool(_COMMENT_LINE_RE.match(line))

def _is_test_file(filepath: Path) -> bool:
    
    return bool(_TEST_FILE_PATTERNS.search(filepath.name)) or bool(
        _TEST_FILE_PATTERNS.search(str(filepath))
    )

def _is_placeholder_value(line: str) -> bool:
    
    return bool(_PLACEHOLDER_PATTERN.search(line))

def _is_env_example(filepath: Path) -> bool:
    
    name = filepath.name.lower()
    return name in (".env.example", ".env.sample", ".env.template", ".env.defaults")

def _classify_file(filepath: Path) -> str:
    
    name = filepath.name.lower()
    suffix = filepath.suffix.lower()

    
    if name.startswith(".env") or name in ENV_FILE_PATTERNS:
        return "env"

    
    if suffix in PRIVATE_KEY_EXTENSIONS:
        return "private_key"

    
    if suffix in CONFIG_EXTENSIONS:
        return "config"

    
    if suffix in SHELL_EXTENSIONS:
        return "shell"

    
    if any(name.startswith(prefix) for prefix in DOCKER_PREFIXES):
        return "docker"

    
    filepath_str = str(filepath).replace("\\", "/")
    for cicd_pattern in CICD_PATTERNS:
        if cicd_pattern in filepath_str:
            return "cicd"

    
    if suffix in config.SCANNABLE_EXTENSIONS:
        return "source"

    return "other"

def _should_scan_file(filepath: Path) -> bool:
    
    name = filepath.name.lower()
    suffix = filepath.suffix.lower()

    
    if name.startswith(".env"):
        return True

    
    if suffix in PRIVATE_KEY_EXTENSIONS:
        return True

    
    if any(name.startswith(prefix) for prefix in DOCKER_PREFIXES):
        return True

    
    filepath_str = str(filepath).replace("\\", "/")
    for cicd_pattern in CICD_PATTERNS:
        if cicd_pattern in filepath_str or name == Path(cicd_pattern).name:
            return True

    
    for ext in config.SCANNABLE_EXTENSIONS:
        if name.endswith(ext):
            return True
    if suffix in config.SCANNABLE_EXTENSIONS:
        return True

    return False

def collect_files(target: Path) -> list[Path]:
    
    files: list[Path] = []
    max_files = config.LIMITS["max_files_per_scan"]

    for root, dirs, filenames in os.walk(target):
        dirs[:] = [d for d in dirs if d not in config.SKIP_DIRECTORIES]

        for fname in filenames:
            if len(files) >= max_files:
                logger.warning(
                    "Reached max_files_per_scan limit (%d). Stopping.", max_files
                )
                return files

            fpath = Path(root) / fname
            if _should_scan_file(fpath):
                files.append(fpath)

    return files

def _redact(text: str, keep: int = 6) -> str:
    
    text = text.strip()
    if len(text) <= keep:
        return text
    return text[:keep] + "****"

def _snippet(line: str, match_start: int, context: int = 50) -> str:
    
    start = max(0, match_start - context // 2)
    end = min(len(line), match_start + context)
    raw = line[start:end].strip()
    return _redact(raw)

def scan_file(filepath: Path, verbose: bool = False) -> list[dict]:
    
    findings: list[dict] = []
    max_findings = config.LIMITS["max_findings_per_file"]
    file_str = str(filepath)
    file_category = _classify_file(filepath)
    is_test = _is_test_file(filepath)
    is_env_ex = _is_env_example(filepath)

    
    if filepath.suffix.lower() in PRIVATE_KEY_EXTENSIONS:
        sev = "MEDIUM" if is_test else "CRITICAL"
        findings.append({
            "type": "secret",
            "pattern": "private_key_file",
            "severity": sev,
            "file": file_str,
            "line": 0,
            "snippet": f"Private key file detected: {filepath.name}",
            "category": file_category,
        })
        
        

    
    try:
        size = filepath.stat().st_size
    except OSError:
        return findings

    if size > config.LIMITS["max_file_size_bytes"]:
        if verbose:
            logger.debug("Skipping oversized file: %s (%d bytes)", filepath, size)
        return findings

    
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        if verbose:
            logger.debug("Cannot read %s: %s", filepath, exc)
        return findings

    lines = text.splitlines()
    in_markdown_code_block = False

    for line_num, line in enumerate(lines, start=1):
        if len(findings) >= max_findings:
            break

        stripped = line.strip()
        if not stripped:
            continue

        
        if _MARKDOWN_CODE_FENCE.match(stripped):
            in_markdown_code_block = not in_markdown_code_block
            continue

        
        is_comment = _is_comment_line(stripped)
        is_placeholder = _is_placeholder_value(stripped)

        
        for pattern_name, regex, severity in ALL_SECRET_PATTERNS:
            m = regex.search(line)
            if not m:
                continue

            
            skip = False
            adjusted_severity = severity

            if is_comment and not file_category == "env":
                
                
                skip = True

            if in_markdown_code_block:
                skip = True

            if is_placeholder:
                skip = True

            if is_test:
                
                sev_weight = config.SEVERITY.get(severity, 1)
                if sev_weight >= config.SEVERITY["HIGH"]:
                    adjusted_severity = "MEDIUM"
                elif sev_weight >= config.SEVERITY["MEDIUM"]:
                    adjusted_severity = "LOW"

            if is_env_ex:
                
                
                if not is_placeholder:
                    adjusted_severity = "MEDIUM"  
                else:
                    skip = True  

            if skip:
                continue

            findings.append({
                "type": "secret",
                "pattern": pattern_name,
                "severity": adjusted_severity,
                "file": file_str,
                "line": line_num,
                "snippet": _snippet(line, m.start()),
                "category": file_category,
            })

        
        
        for token_match in re.finditer(r, line):
            if len(findings) >= max_findings:
                break

            token = token_match.group(1)
            ent = shannon_entropy(token)

            if ent > 4.5:
                
                
                already_found = any(
                    f["file"] == file_str and f["line"] == line_num
                    for f in findings
                )
                if already_found:
                    continue

                if is_comment or in_markdown_code_block or is_placeholder:
                    continue

                sev = "MEDIUM"
                if ent > 5.0:
                    sev = "HIGH"
                if is_test:
                    sev = "LOW"

                findings.append({
                    "type": "secret",
                    "pattern": "high_entropy_string",
                    "severity": sev,
                    "file": file_str,
                    "line": line_num,
                    "snippet": _redact(token),
                    "category": file_category,
                    "entropy": round(ent, 2),
                })

        
        for b64_match in _BASE64_RE.finditer(line):
            if len(findings) >= max_findings:
                break

            token = b64_match.group(0)
            if len(token) < 20:
                continue

            
            already_found = any(
                f["file"] == file_str and f["line"] == line_num
                for f in findings
            )
            if already_found:
                continue

            if is_comment or in_markdown_code_block or is_placeholder:
                continue

            if _check_base64_secret(token):
                sev = "MEDIUM" if is_test else "HIGH"
                findings.append({
                    "type": "secret",
                    "pattern": "base64_encoded_secret",
                    "severity": sev,
                    "file": file_str,
                    "line": line_num,
                    "snippet": _redact(token),
                    "category": file_category,
                })

        
        
        

        
        for ip_match in _IP_RE.finditer(line):
            if len(findings) >= max_findings:
                break

            ip = ip_match.group(1)
            if _is_private_or_localhost(ip):
                continue

            
            parts = ip.split(".")
            try:
                if not all(0 <= int(p) <= 255 for p in parts):
                    continue
            except ValueError:
                continue

            if is_comment or in_markdown_code_block:
                continue

            sev = "LOW"
            if is_test:
                continue  

            findings.append({
                "type": "hardcoded_ip",
                "pattern": "hardcoded_public_ip",
                "severity": sev,
                "file": file_str,
                "line": line_num,
                "snippet": ip,
                "category": file_category,
            })

    return findings

SCORE_DEDUCTIONS = {
    "CRITICAL": 10,
    "HIGH": 5,
    "MEDIUM": 2,
    "LOW": 1,
    "INFO": 0,
}

def aggregate_by_severity(findings: list[dict]) -> dict[str, int]:
    
    counts: dict[str, int] = {sev: 0 for sev in config.SEVERITY}
    for f in findings:
        sev = f.get("severity", "INFO")
        if sev in counts:
            counts[sev] += 1
    return counts

def aggregate_by_pattern(findings: list[dict]) -> dict[str, int]:
    
    counts: dict[str, int] = {}
    for f in findings:
        pattern = f.get("pattern", "unknown")
        counts[pattern] = counts.get(pattern, 0) + 1
    return counts

def aggregate_by_category(findings: list[dict]) -> dict[str, int]:
    
    counts: dict[str, int] = {}
    for f in findings:
        cat = f.get("category", "other")
        counts[cat] = counts.get(cat, 0) + 1
    return counts

def compute_score(findings: list[dict]) -> int:
    
    score = 100
    for f in findings:
        deduction = SCORE_DEDUCTIONS.get(f["severity"], 0)
        score -= deduction
    return max(0, score)

def format_text_report(
    target: str,
    total_files: int,
    findings: list[dict],
    severity_counts: dict[str, int],
    pattern_counts: dict[str, int],
    category_counts: dict[str, int],
    score: int,
    verdict: dict,
    elapsed: float,
    include_low: bool = False,
) -> str:
    
    lines: list[str] = []

    lines.append("=" * 72)
    lines.append("  007 SECRETS SCANNER -- DEEP SCAN REPORT")
    lines.append("=" * 72)
    lines.append("")

    
    lines.append(f"  Target:         {target}")
    lines.append(f"  Timestamp:      {config.get_timestamp()}")
    lines.append(f"  Duration:       {elapsed:.2f}s")
    lines.append(f"  Files scanned:  {total_files}")
    lines.append(f"  Total findings: {len(findings)}")
    lines.append("")

    
    lines.append("-" * 72)
    lines.append("  FINDINGS BY SEVERITY")
    lines.append("-" * 72)
    for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"):
        count = severity_counts.get(sev, 0)
        bar = "
        lines.append(f"    {sev:<10} {count:>5}  {bar}")
    lines.append("")

    
    if pattern_counts:
        lines.append("-" * 72)
        lines.append("  FINDINGS BY TYPE")
        lines.append("-" * 72)
        sorted_patterns = sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)
        for pattern_name, count in sorted_patterns[:20]:
            lines.append(f"    {pattern_name:<35} {count:>5}")
        lines.append("")

    
    if category_counts:
        lines.append("-" * 72)
        lines.append("  FINDINGS BY FILE CATEGORY")
        lines.append("-" * 72)
        sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
        for cat_name, count in sorted_cats:
            lines.append(f"    {cat_name:<20} {count:>5}")
        lines.append("")

    
    min_severity = config.SEVERITY["LOW"] if include_low else config.SEVERITY["MEDIUM"]

    displayed = [
        f for f in findings
        if config.SEVERITY.get(f.get("severity", "INFO"), 0) >= min_severity
    ]

    if displayed:
        
        by_severity: dict[str, list[dict]] = {}
        for f in displayed:
            sev = f.get("severity", "INFO")
            by_severity.setdefault(sev, []).append(f)

        for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
            sev_findings = by_severity.get(sev, [])
            if not sev_findings:
                continue

            lines.append("-" * 72)
            lines.append(f"  [{sev}] FINDINGS ({len(sev_findings)})")
            lines.append("-" * 72)

            
            by_file: dict[str, list[dict]] = {}
            for f in sev_findings:
                by_file.setdefault(f["file"], []).append(f)

            for filepath, file_findings in sorted(by_file.items()):
                lines.append(f"  {filepath}")
                for f in sorted(file_findings, key=lambda x: x.get("line", 0)):
                    loc = f"L{f['line']}" if f.get("line") else ""
                    snippet_part = f"  [{f['snippet']}]" if f.get("snippet") else ""
                    entropy_part = f"  (entropy={f['entropy']})" if f.get("entropy") else ""
                    lines.append(
                        f"    {loc:>6}  {f['pattern']}{snippet_part}{entropy_part}"
                    )
                lines.append("")
    else:
        lines.append("  No findings above the display threshold.")
        lines.append("")

    
    lines.append("=" * 72)
    lines.append(f"  SECRETS SCORE:  {score} / 100")
    lines.append(f"  VERDICT:        {verdict['emoji']} {verdict['label']}")
    lines.append(f"                  {verdict['description']}")
    lines.append("=" * 72)
    lines.append("")

    return "\n".join(lines)

def build_json_report(
    target: str,
    total_files: int,
    findings: list[dict],
    severity_counts: dict[str, int],
    pattern_counts: dict[str, int],
    category_counts: dict[str, int],
    score: int,
    verdict: dict,
    elapsed: float,
) -> dict:
    
    return {
        "scan": "secrets_scanner",
        "target": target,
        "timestamp": config.get_timestamp(),
        "duration_seconds": round(elapsed, 3),
        "total_files_scanned": total_files,
        "total_findings": len(findings),
        "severity_counts": severity_counts,
        "pattern_counts": pattern_counts,
        "category_counts": category_counts,
        "score": score,
        "verdict": {
            "label": verdict["label"],
            "description": verdict["description"],
            "emoji": verdict["emoji"],
        },
        "findings": findings,
    }

def run_scan(
    target_path: str,
    output_format: str = "text",
    verbose: bool = False,
    include_low: bool = False,
) -> dict:
    
    if verbose:
        logger.setLevel("DEBUG")

    config.ensure_directories()

    target = Path(target_path).resolve()
    if not target.exists():
        logger.error("Target path does not exist: %s", target)
        sys.exit(1)
    if not target.is_dir():
        logger.error("Target is not a directory: %s", target)
        sys.exit(1)

    logger.info("Starting deep secrets scan of %s", target)
    start_time = time.time()

    
    files = collect_files(target)
    total_files = len(files)
    logger.info("Collected %d files for deep scanning", total_files)

    
    all_findings: list[dict] = []
    max_report = config.LIMITS["max_report_findings"]

    for fpath in files:
        if len(all_findings) >= max_report:
            logger.warning(
                "Reached max_report_findings limit (%d). Truncating.", max_report
            )
            break

        file_findings = scan_file(fpath, verbose=verbose)
        remaining = max_report - len(all_findings)
        all_findings.extend(file_findings[:remaining])

    elapsed = time.time() - start_time
    logger.info(
        "Deep scan complete: %d files, %d findings in %.2fs",
        total_files, len(all_findings), elapsed,
    )

    
    severity_counts = aggregate_by_severity(all_findings)
    pattern_counts = aggregate_by_pattern(all_findings)
    category_counts = aggregate_by_category(all_findings)
    score = compute_score(all_findings)
    verdict = config.get_verdict(score)

    
    config.log_audit_event(
        action="secrets_scan",
        target=str(target),
        result=f"score={score}, findings={len(all_findings)}, verdict={verdict['label']}",
        details={
            "total_files": total_files,
            "severity_counts": severity_counts,
            "pattern_counts": pattern_counts,
            "category_counts": category_counts,
            "duration_seconds": round(elapsed, 3),
        },
    )

    
    report = build_json_report(
        target=str(target),
        total_files=total_files,
        findings=all_findings,
        severity_counts=severity_counts,
        pattern_counts=pattern_counts,
        category_counts=category_counts,
        score=score,
        verdict=verdict,
        elapsed=elapsed,
    )

    
    if output_format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_text_report(
            target=str(target),
            total_files=total_files,
            findings=all_findings,
            severity_counts=severity_counts,
            pattern_counts=pattern_counts,
            category_counts=category_counts,
            score=score,
            verdict=verdict,
            elapsed=elapsed,
            include_low=include_low,
        ))

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="007 Secrets Scanner -- Deep scanner for secrets and credentials.",
        epilog=(
            "Examples:\n"
            "  python secrets_scanner.py --target ./my-project\n"
            "  python secrets_scanner.py --target ./my-project --output json\n"
            "  python secrets_scanner.py --target ./my-project --verbose --include-low"
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
    parser.add_argument(
        "--include-low",
        action="store_true",
        default=False,
        help="Include LOW severity findings in text output (hidden by default).",
    )

    args = parser.parse_args()
    run_scan(
        target_path=args.target,
        output_format=args.output,
        verbose=args.verbose,
        include_low=args.include_low,
    )
