import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  

logger = config.setup_logging("007-injection-scanner")

_USER_INPUT_MARKERS_PY = re.compile(
    r
    r
    r
    r
    r
    r
    r,
    re.IGNORECASE,
)

_USER_INPUT_MARKERS_JS = re.compile(
    r
    r
    r
    r
    r
    r
    r
    r
    r
    r
    r,
    re.IGNORECASE,
)

_USER_INPUT_MARKERS = re.compile(
    _USER_INPUT_MARKERS_PY.pattern + r"|" + _USER_INPUT_MARKERS_JS.pattern,
    re.IGNORECASE,
)

_COMMENT_LINE_RE = re.compile(
    r, re.IGNORECASE
)

_TRIPLE_QUOTE_RE = re.compile(r)

_MARKDOWN_CODE_FENCE = re.compile(r)

def _is_comment_line(line: str) -> bool:
    
    return bool(_COMMENT_LINE_RE.match(line))

_TEST_FILE_RE = re.compile(
    r
    r
    r
)

def _is_test_file(filepath: Path) -> bool:
    
    return bool(_TEST_FILE_RE.search(filepath.name)) or bool(
        _TEST_FILE_RE.search(str(filepath))
    )

def _lower_severity(severity: str) -> str:
    
    order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]
    idx = order.index(severity) if severity in order else 0
    return order[min(idx + 1, len(order) - 1)]

def _has_user_input(line: str) -> bool:
    
    return bool(_USER_INPUT_MARKERS.search(line))

def _has_variable_interpolation(line: str) -> bool:
    
    
    if re.search(r, line):
        return True
    
    if ".format(" in line:
        return True
    
    if re.search(r, line) and "%" in line:
        return True
    return False

def _only_hardcoded_string(line: str) -> bool:
    
    
    if _has_variable_interpolation(line):
        return False
    
    if _has_user_input(line):
        return False
    
    
    paren = line.find("(")
    if paren == -1:
        return False
    inside = line[paren:]
    
    if re.match(r, inside):
        return True
    return False

_INJECTION_DEFS: list[tuple[str, str, str, str, str]] = [

    
    
    
    (
        "py_eval_user_input",
        r
        r,
        "CRITICAL",
        "code_injection",
        "eval() with potential user input",
    ),
    (
        "py_eval_any",
        r,
        "CRITICAL",
        "code_injection",
        "eval() usage -- verify input is not user-controlled",
    ),
    (
        "py_exec_any",
        r,
        "CRITICAL",
        "code_injection",
        "exec() usage -- verify input is not user-controlled",
    ),
    (
        "py_compile_external",
        r
        r,
        "CRITICAL",
        "code_injection",
        "compile() with potential user input",
    ),
    (
        "py_dunder_import_dynamic",
        r,
        "HIGH",
        "code_injection",
        "__import__() with dynamic name",
    ),
    (
        "py_importlib_dynamic",
        r,
        "HIGH",
        "code_injection",
        "importlib.import_module() with dynamic name",
    ),
    
    (
        "js_eval_any",
        r,
        "CRITICAL",
        "code_injection",
        "eval() in JavaScript -- verify input is not user-controlled",
    ),
    (
        "js_function_constructor",
        r,
        "CRITICAL",
        "code_injection",
        "Function() constructor -- equivalent to eval",
    ),
    (
        "js_vm_run",
        r,
        "HIGH",
        "code_injection",
        "vm.run*() -- verify input is not user-controlled",
    ),
    
    (
        "template_injection_fstring",
        r,
        "CRITICAL",
        "code_injection",
        "f-string in template rendering context (template injection)",
    ),
    (
        "template_injection_format",
        r,
        "CRITICAL",
        "code_injection",
        ".format() in template rendering context (template injection)",
    ),

    
    
    
    (
        "subprocess_shell_true",
        r
        r,
        "CRITICAL",
        "command_injection",
        "subprocess with shell=True -- command injection risk if input is variable",
    ),
    (
        "os_system_var",
        r,
        "CRITICAL",
        "command_injection",
        "os.system() -- always uses a shell; prefer subprocess without shell=True",
    ),
    (
        "os_popen_var",
        r,
        "HIGH",
        "command_injection",
        "os.popen() -- shell command execution",
    ),
    (
        "child_process_exec",
        r,
        "CRITICAL",
        "command_injection",
        "child_process.exec() in Node.js -- uses shell by default",
    ),
    (
        "shell_backtick_var",
        r,
        "HIGH",
        "command_injection",
        "Backtick execution with variable interpolation",
    ),

    
    
    
    (
        "sql_fstring",
        r
        r,
        "CRITICAL",
        "sql_injection",
        "f-string in SQL query (SQL injection)",
    ),
    (
        "sql_format_method",
        r
        r,
        "CRITICAL",
        "sql_injection",
        ".format() in SQL query string (SQL injection)",
    ),
    (
        "sql_concat",
        r,
        "HIGH",
        "sql_injection",
        "String concatenation in SQL query",
    ),
    (
        "sql_percent_format",
        r
        r,
        "CRITICAL",
        "sql_injection",
        "%-format in cursor.execute() (SQL injection)",
    ),
    (
        "sql_fstring_execute",
        r,
        "CRITICAL",
        "sql_injection",
        "f-string in execute() call (SQL injection)",
    ),

    
    
    
    (
        "prompt_injection_fstring",
        r
        r,
        "HIGH",
        "prompt_injection",
        "User input directly in LLM prompt via f-string",
    ),
    (
        "prompt_injection_concat",
        r
        r,
        "HIGH",
        "prompt_injection",
        "User input concatenated into LLM prompt",
    ),
    (
        "prompt_injection_openai",
        r
        r,
        "HIGH",
        "prompt_injection",
        "User variable in f-string near LLM API call",
    ),
    (
        "prompt_injection_format",
        r
        r,
        "HIGH",
        "prompt_injection",
        ".format() with user input in prompt template",
    ),
    (
        "prompt_no_sanitize_direct",
        r
        r,
        "MEDIUM",
        "prompt_injection",
        "User input passed directly to LLM messages without sanitization",
    ),

    
    
    
    (
        "xss_innerhtml",
        r,
        "HIGH",
        "xss",
        "innerHTML assignment with variable (XSS risk)",
    ),
    (
        "xss_document_write",
        r,
        "HIGH",
        "xss",
        "document.write() with variable content",
    ),
    (
        "xss_document_write_any",
        r,
        "MEDIUM",
        "xss",
        "document.write() usage -- verify no user content",
    ),
    (
        "xss_dangerously_set",
        r,
        "HIGH",
        "xss",
        "dangerouslySetInnerHTML in React (XSS risk)",
    ),
    (
        "xss_template_literal_html",
        r,
        "HIGH",
        "xss",
        "Template literal with interpolation in HTML context",
    ),
    (
        "xss_jquery_html",
        r,
        "HIGH",
        "xss",
        "jQuery .html() with variable content",
    ),

    
    
    
    (
        "ssrf_requests",
        r
        r
        r,
        "HIGH",
        "ssrf",
        "requests.get/post with potentially user-controlled URL",
    ),
    (
        "ssrf_urllib",
        r
        r
        r,
        "HIGH",
        "ssrf",
        "urllib with potentially user-controlled URL",
    ),
    (
        "ssrf_fetch",
        r
        r,
        "HIGH",
        "ssrf",
        "fetch() with potentially user-controlled URL",
    ),
    (
        "ssrf_axios",
        r
        r,
        "HIGH",
        "ssrf",
        "axios with potentially user-controlled URL",
    ),
    (
        "ssrf_no_allowlist",
        r,
        "MEDIUM",
        "ssrf",
        "HTTP request without visible URL allowlist/blocklist validation",
    ),

    
    
    
    (
        "path_traversal_open",
        r
        r,
        "HIGH",
        "path_traversal",
        "open() with user-controlled path (path traversal risk)",
    ),
    (
        "path_traversal_join",
        r
        r,
        "HIGH",
        "path_traversal",
        "os.path.join with user input (can bypass with absolute paths)",
    ),
    (
        "path_traversal_pathlib",
        r
        r,
        "MEDIUM",
        "path_traversal",
        "Path() with user input -- verify resolve() and containment check",
    ),
    (
        "path_traversal_send_file",
        r
        r,
        "HIGH",
        "path_traversal",
        "send_file() with user-controlled path",
    ),
    (
        "path_traversal_no_resolve",
        r,
        "MEDIUM",
        "path_traversal",
        "File open via path join without visible resolve()/realpath() check",
    ),
]

INJECTION_PATTERNS: list[tuple[str, re.Pattern, str, str, str]] = []
for _name, _pat, _sev, _itype, _desc in _INJECTION_DEFS:
    try:
        INJECTION_PATTERNS.append((_name, re.compile(_pat), _sev, _itype, _desc))
    except re.error as exc:
        logger.warning("Failed to compile pattern %s: %s", _name, exc)

def _should_scan_file(filepath: Path) -> bool:
    
    name = filepath.name.lower()
    suffix = filepath.suffix.lower()

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

def _snippet(line: str, match_start: int, context: int = 80) -> str:
    
    start = max(0, match_start - context // 4)
    end = min(len(line), match_start + context)
    raw = line[start:end].strip()
    if len(raw) > context:
        raw = raw[:context] + "..."
    return raw

def _is_in_docstring(lines: list[str], line_idx: int) -> bool:
    
    count = 0
    for i in range(line_idx):
        
        content = lines[i]
        count += len(re.findall(r, content))
    return count % 2 == 1

def scan_file(filepath: Path, verbose: bool = False) -> list[dict]:
    
    findings: list[dict] = []
    max_findings = config.LIMITS["max_findings_per_file"]
    file_str = str(filepath)
    is_test = _is_test_file(filepath)

    
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
    in_markdown_block = False

    
    
    
    _CONTEXT_WINDOW = 5
    line_has_user_input = [False] * len(lines)
    for idx, ln in enumerate(lines):
        if _has_user_input(ln):
            lo = max(0, idx - _CONTEXT_WINDOW)
            hi = min(len(lines), idx + _CONTEXT_WINDOW + 1)
            for j in range(lo, hi):
                line_has_user_input[j] = True

    
    
    line_patterns: dict[int, set[str]] = {}

    for line_idx, line in enumerate(lines):
        if len(findings) >= max_findings:
            break

        line_num = line_idx + 1
        stripped = line.strip()

        if not stripped:
            continue

        
        if _MARKDOWN_CODE_FENCE.match(stripped):
            in_markdown_block = not in_markdown_block
            continue

        
        if _is_comment_line(stripped):
            continue

        
        if in_markdown_block:
            continue

        
        if filepath.suffix.lower() == ".py" and _is_in_docstring(lines, line_idx):
            continue

        for pat_name, regex, base_severity, injection_type, description in INJECTION_PATTERNS:
            m = regex.search(line)
            if not m:
                continue

            
            
            if line_num not in line_patterns:
                line_patterns[line_num] = set()

            
            group_key = injection_type + ":" + pat_name.rsplit("_", 1)[0]
            if group_key in line_patterns.get(line_num, set()):
                continue

            
            if "user_input" in pat_name or "var" in pat_name:
                generic_group = injection_type + ":" + pat_name.replace("_user_input", "").replace("_var", "").rsplit("_", 1)[0]
                line_patterns[line_num].add(generic_group)

            line_patterns[line_num].add(group_key)

            
            adjusted_severity = base_severity

            
            if _only_hardcoded_string(line):
                adjusted_severity = "INFO"

            
            
            elif not line_has_user_input[line_idx] and not _has_user_input(line):
                if not _has_variable_interpolation(line):
                    adjusted_severity = _lower_severity(base_severity)
                    
                    if pat_name.endswith("_any"):
                        adjusted_severity = _lower_severity(adjusted_severity)

            
            if is_test:
                adjusted_severity = _lower_severity(adjusted_severity)

            findings.append({
                "type": "injection",
                "injection_type": injection_type,
                "pattern": pat_name,
                "severity": adjusted_severity,
                "file": file_str,
                "line": line_num,
                "snippet": _snippet(line, m.start()),
                "description": description,
                "has_user_input_nearby": line_has_user_input[line_idx],
            })

    return findings

SCORE_DEDUCTIONS = {
    "CRITICAL": 12,
    "HIGH":      6,
    "MEDIUM":    3,
    "LOW":       1,
    "INFO":      0,
}

def aggregate_by_severity(findings: list[dict]) -> dict[str, int]:
    
    counts: dict[str, int] = {sev: 0 for sev in config.SEVERITY}
    for f in findings:
        sev = f.get("severity", "INFO")
        if sev in counts:
            counts[sev] += 1
    return counts

def aggregate_by_injection_type(findings: list[dict]) -> dict[str, int]:
    
    counts: dict[str, int] = {}
    for f in findings:
        itype = f.get("injection_type", "unknown")
        counts[itype] = counts.get(itype, 0) + 1
    return counts

def aggregate_by_pattern(findings: list[dict]) -> dict[str, int]:
    
    counts: dict[str, int] = {}
    for f in findings:
        pattern = f.get("pattern", "unknown")
        counts[pattern] = counts.get(pattern, 0) + 1
    return counts

def compute_score(findings: list[dict]) -> int:
    
    score = 100
    for f in findings:
        deduction = SCORE_DEDUCTIONS.get(f["severity"], 0)
        score -= deduction
    return max(0, score)

_INJECTION_TYPE_LABELS = {
    "code_injection":    "Code Injection",
    "command_injection": "Command Injection",
    "sql_injection":     "SQL Injection",
    "prompt_injection":  "Prompt Injection",
    "xss":               "Cross-Site Scripting (XSS)",
    "ssrf":              "Server-Side Request Forgery (SSRF)",
    "path_traversal":    "Path Traversal",
}

def format_text_report(
    target: str,
    total_files: int,
    findings: list[dict],
    severity_counts: dict[str, int],
    type_counts: dict[str, int],
    pattern_counts: dict[str, int],
    score: int,
    verdict: dict,
    elapsed: float,
    include_low: bool = False,
) -> str:
    
    lines: list[str] = []

    lines.append("=" * 72)
    lines.append("  007 INJECTION SCANNER -- VULNERABILITY REPORT")
    lines.append("=" * 72)
    lines.append("")

    
    lines.append(f"  Target:         {target}")
    lines.append(f"  Timestamp:      {config.get_timestamp()}")
    lines.append(f"  Duration:       {elapsed:.2f}s")
    lines.append(f"  Files scanned:  {total_files}")
    lines.append(f"  Total findings: {len(findings)}")
    lines.append("")

    
    lines.append("-" * 72)
    lines.append("  SEVERITY DISTRIBUTION")
    lines.append("-" * 72)
    for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"):
        count = severity_counts.get(sev, 0)
        bar = "
        lines.append(f"    {sev:<10} {count:>5}  {bar}")
    lines.append("")

    
    if type_counts:
        lines.append("-" * 72)
        lines.append("  FINDINGS BY INJECTION TYPE")
        lines.append("-" * 72)
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        for itype, count in sorted_types:
            label = _INJECTION_TYPE_LABELS.get(itype, itype)
            lines.append(f"    {label:<40} {count:>5}")
        lines.append("")

    
    min_severity = config.SEVERITY["LOW"] if include_low else config.SEVERITY["MEDIUM"]

    displayed = [
        f for f in findings
        if config.SEVERITY.get(f.get("severity", "INFO"), 0) >= min_severity
    ]

    if displayed:
        
        by_type: dict[str, list[dict]] = {}
        for f in displayed:
            itype = f.get("injection_type", "unknown")
            by_type.setdefault(itype, []).append(f)

        
        
        type_order = [
            "code_injection", "command_injection", "sql_injection",
            "prompt_injection", "xss", "ssrf", "path_traversal",
        ]
        
        for t in by_type:
            if t not in type_order:
                type_order.append(t)

        for itype in type_order:
            itype_findings = by_type.get(itype, [])
            if not itype_findings:
                continue

            label = _INJECTION_TYPE_LABELS.get(itype, itype)
            lines.append("-" * 72)
            lines.append(f"  [{label.upper()}] ({len(itype_findings)} findings)")
            lines.append("-" * 72)

            
            for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
                sev_group = [f for f in itype_findings if f["severity"] == sev]
                if not sev_group:
                    continue

                for f in sorted(sev_group, key=lambda x: (x["file"], x.get("line", 0))):
                    taint_marker = " [TAINTED]" if f.get("has_user_input_nearby") else ""
                    lines.append(
                        f"    [{sev}] {f['file']}:L{f.get('line', 0)}{taint_marker}"
                    )
                    lines.append(f"           {f['description']}")
                    if f.get("snippet"):
                        lines.append(f"           > {f['snippet']}")
                    lines.append("")
    else:
        lines.append("  No injection findings above the display threshold.")
        lines.append("")

    
    lines.append("=" * 72)
    lines.append(f"  INJECTION SECURITY SCORE:  {score} / 100")
    lines.append(f"  VERDICT:                   {verdict['emoji']} {verdict['label']}")
    lines.append(f"                             {verdict['description']}")
    lines.append("=" * 72)
    lines.append("")

    return "\n".join(lines)

def build_json_report(
    target: str,
    total_files: int,
    findings: list[dict],
    severity_counts: dict[str, int],
    type_counts: dict[str, int],
    pattern_counts: dict[str, int],
    score: int,
    verdict: dict,
    elapsed: float,
) -> dict:
    
    return {
        "scan": "injection_scanner",
        "target": target,
        "timestamp": config.get_timestamp(),
        "duration_seconds": round(elapsed, 3),
        "total_files_scanned": total_files,
        "total_findings": len(findings),
        "severity_counts": severity_counts,
        "injection_type_counts": type_counts,
        "pattern_counts": pattern_counts,
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

    logger.info("Starting injection vulnerability scan of %s", target)
    start_time = time.time()

    
    files = collect_files(target)
    total_files = len(files)
    logger.info("Collected %d files for injection scanning", total_files)

    
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
        "Injection scan complete: %d files, %d findings in %.2fs",
        total_files, len(all_findings), elapsed,
    )

    
    severity_counts = aggregate_by_severity(all_findings)
    type_counts = aggregate_by_injection_type(all_findings)
    pattern_counts = aggregate_by_pattern(all_findings)
    score = compute_score(all_findings)
    verdict = config.get_verdict(score)

    
    config.log_audit_event(
        action="injection_scan",
        target=str(target),
        result=f"score={score}, findings={len(all_findings)}, verdict={verdict['label']}",
        details={
            "total_files": total_files,
            "severity_counts": severity_counts,
            "injection_type_counts": type_counts,
            "pattern_counts": pattern_counts,
            "duration_seconds": round(elapsed, 3),
        },
    )

    
    report = build_json_report(
        target=str(target),
        total_files=total_files,
        findings=all_findings,
        severity_counts=severity_counts,
        type_counts=type_counts,
        pattern_counts=pattern_counts,
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
            type_counts=type_counts,
            pattern_counts=pattern_counts,
            score=score,
            verdict=verdict,
            elapsed=elapsed,
            include_low=include_low,
        ))

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "007 Injection Scanner -- Specialized scanner for injection "
            "vulnerabilities (code injection, SQL injection, command injection, "
            "prompt injection, XSS, SSRF, path traversal)."
        ),
        epilog=(
            "Examples:\n"
            "  python injection_scanner.py --target ./my-project\n"
            "  python injection_scanner.py --target ./my-project --output json\n"
            "  python injection_scanner.py --target ./my-project --verbose --include-low"
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
