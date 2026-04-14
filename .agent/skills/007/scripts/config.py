import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent          
SCRIPTS_DIR = BASE_DIR / "scripts"
SCANNERS_DIR = SCRIPTS_DIR / "scanners"
ANALYZERS_DIR = SCRIPTS_DIR / "analyzers"
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = DATA_DIR / "reports"
PLAYBOOKS_DIR = DATA_DIR / "playbooks"
REFERENCES_DIR = BASE_DIR / "references"
ASSETS_DIR = BASE_DIR / "assets"

AUDIT_LOG_PATH = DATA_DIR / "audit_log.json"

SCORE_HISTORY_PATH = DATA_DIR / "score_history.json"

def ensure_directories() -> None:
    
    for directory in (DATA_DIR, REPORTS_DIR, PLAYBOOKS_DIR):
        directory.mkdir(parents=True, exist_ok=True)

SEVERITY = {
    "CRITICAL": 5,
    "HIGH":     4,
    "MEDIUM":   3,
    "LOW":      2,
    "INFO":     1,
}

SEVERITY_LABEL = {v: k for k, v in SEVERITY.items()}

SCORING_WEIGHTS = {
    "secrets":         0.20,   
    "input_validation": 0.15,  
    "authn_authz":     0.15,   
    "data_protection":  0.15,  
    "resilience":      0.10,   
    "monitoring":      0.10,   
    "supply_chain":    0.10,   
    "compliance":      0.05,   
}

SCORING_LABELS = {
    "secrets":          "Segredos & Credenciais",
    "input_validation": "Input Validation",
    "authn_authz":      "Autenticacao & Autorizacao",
    "data_protection":  "Protecao de Dados",
    "resilience":       "Resiliencia",
    "monitoring":       "Monitoramento",
    "supply_chain":     "Supply Chain",
    "compliance":       "Compliance",
}

VERDICT_THRESHOLDS = {
    "approved": {
        "min": 90,
        "max": 100,
        "label": "Aprovado",
        "description": "Pronto para producao",
        "emoji": "[PASS]",
    },
    "approved_with_caveats": {
        "min": 70,
        "max": 89,
        "label": "Aprovado com Ressalvas",
        "description": "Pode ir para producao com mitigacoes documentadas",
        "emoji": "[WARN]",
    },
    "partial_block": {
        "min": 50,
        "max": 69,
        "label": "Bloqueado Parcial",
        "description": "Precisa correcoes antes de producao",
        "emoji": "[BLOCK]",
    },
    "total_block": {
        "min": 0,
        "max": 49,
        "label": "Bloqueado Total",
        "description": "Inseguro, requer redesign",
        "emoji": "[CRITICAL]",
    },
}

def get_verdict(score: float) -> dict:
    
    score = max(0.0, min(100.0, score))
    for verdict in VERDICT_THRESHOLDS.values():
        if verdict["min"] <= score <= verdict["max"]:
            return verdict
    
    return VERDICT_THRESHOLDS["total_block"]

_SECRET_PATTERN_DEFS = [
    
    (
        "generic_api_key",
        r,
        "HIGH",
    ),
    
    (
        "aws_access_key",
        r,
        "CRITICAL",
    ),
    
    (
        "aws_secret_key",
        r,
        "CRITICAL",
    ),
    
    (
        "password_assignment",
        r,
        "HIGH",
    ),
    
    (
        "token_assignment",
        r,
        "HIGH",
    ),
    
    (
        "private_key",
        r,
        "CRITICAL",
    ),
    
    (
        "github_token",
        r,
        "CRITICAL",
    ),
    
    (
        "slack_token",
        r,
        "CRITICAL",
    ),
    
    (
        "generic_secret",
        r,
        "MEDIUM",
    ),
    
    (
        "db_connection_string",
        r,
        "HIGH",
    ),
    
    (
        "env_inline_secret",
        r,
        "HIGH",
    ),
]

SECRET_PATTERNS = [
    (name, re.compile(pattern), severity)
    for name, pattern, severity in _SECRET_PATTERN_DEFS
]

_DANGEROUS_PATTERN_DEFS = [
    
    ("eval_usage",              r,                                    "CRITICAL"),
    ("exec_usage",              r,                                    "CRITICAL"),
    ("subprocess_shell_true",   r,            "CRITICAL"),
    ("os_system",              r,                               "HIGH"),
    ("os_popen",               r,                                "HIGH"),
    ("pickle_loads",           r,                            "HIGH"),
    ("yaml_unsafe_load",       r,               "HIGH"),
    ("marshal_loads",          r,                           "MEDIUM"),
    ("shelve_open",            r,                              "MEDIUM"),
    ("compile_usage",          r,                      "HIGH"),

    
    ("importlib_import",       r,                                "MEDIUM"),
    ("importlib_module",       r,                  "MEDIUM"),

    
    ("shell_injection",        r,              "CRITICAL"),

    
    ("open_write",             r,                        "LOW"),

    
    ("requests_no_verify",     r,                               "HIGH"),
    ("ssl_no_verify",          r,        "HIGH"),

    
    ("sql_string_format",      r, "CRITICAL"),
    ("sql_percent_format",     r,"MEDIUM"),

    
    ("js_eval",                r,                                      "CRITICAL"),
    ("child_process_exec",     r,                    "CRITICAL"),
    ("innerHTML_assignment",   r,                                   "HIGH"),

    
    ("deserialize_untrusted",  r,  "MEDIUM"),
]

DANGEROUS_PATTERNS = [
    (name, re.compile(pattern), severity)
    for name, pattern, severity in _DANGEROUS_PATTERN_DEFS
]

SCANNABLE_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".mjs", ".cjs",
    ".java", ".kt", ".scala",
    ".go", ".rs", ".rb", ".php",
    ".sh", ".bash", ".zsh", ".ps1",
    ".yml", ".yaml", ".toml", ".ini", ".cfg", ".conf",
    ".json", ".env", ".env.example",
    ".sql",
    ".html", ".htm", ".xml",
    ".md",       
    ".txt",      
    ".dockerfile", ".docker-compose.yml",
}

SKIP_DIRECTORIES = {
    ".git", ".hg", ".svn",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    "node_modules", "bower_components",
    "venv", ".venv", "env", ".env",
    ".tox", ".nox",
    "dist", "build", "egg-info",
    ".next", ".nuxt",
    "vendor",
    "coverage", ".coverage",
    ".terraform",
}

TIMEOUTS = {
    "file_read_seconds":   10,    
    "scan_total_seconds":  300,   
    "network_seconds":     30,    
}

LIMITS = {
    "max_file_size_bytes": 5 * 1024 * 1024,   
    "max_files_per_scan":  10_000,              
    "max_findings_per_file": 200,               
    "max_report_findings":  1_000,              
}

LOG_FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

def setup_logging(name: str = "007", level: int = logging.INFO) -> logging.Logger:
    
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT))
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

def get_timestamp() -> str:
    
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def log_audit_event(
    action: str,
    target: str,
    result: str,
    details: dict | None = None,
) -> None:
    
    ensure_directories()
    event = {
        "timestamp": get_timestamp(),
        "action": action,
        "target": str(target),
        "result": result,
    }
    if details:
        event["details"] = details

    with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False) + "\n")

def calculate_weighted_score(domain_scores: dict[str, float]) -> float:
    
    total = 0.0
    for domain, weight in SCORING_WEIGHTS.items():
        score = domain_scores.get(domain, 0.0)
        total += score * weight
    return round(total, 2)

if __name__ == "__main__":
    
    print(f"BASE_DIR:       {BASE_DIR}")
    print(f"DATA_DIR:       {DATA_DIR}")
    print(f"REPORTS_DIR:    {REPORTS_DIR}")
    print(f"AUDIT_LOG_PATH: {AUDIT_LOG_PATH}")
    print()

    
    total_weight = sum(SCORING_WEIGHTS.values())
    assert abs(total_weight - 1.0) < 1e-9, f"Weights sum to {total_weight}, expected 1.0"
    print(f"Scoring weights sum: {total_weight} [OK]")

    
    print(f"Secret patterns loaded:    {len(SECRET_PATTERNS)}")
    print(f"Dangerous patterns loaded: {len(DANGEROUS_PATTERNS)}")

    
    for test_score in (95, 75, 55, 30):
        v = get_verdict(test_score)
        print(f"Score {test_score}: {v['emoji']} {v['label']}")

    
    print(f"Timestamp: {get_timestamp()}")

    print("\n007 config.py -- all checks passed.")
