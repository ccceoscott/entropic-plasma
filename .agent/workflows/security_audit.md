---
description: Advanced architectural penetration testing and global scope validation
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /security_audit
## Sovereign Penetration Testing & Zero-Trust Validation — MCP-First, Auto-Healing

> ⚡ **MANDATE**: Every vulnerability found is immediately triaged and auto-remediated where possible. Passive observation is a protocol violation.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
If stale → auto-upgrade (0b). If current → confirm (0c).

### Phase 0b — Auto-Upgrade
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```
Any `[ERROR]` → HALT.

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run. Clean only.

### Phase 0d — Confirmation
`✅ [UPGRADE GATE PASSED] Security audit commencing on clean codebase.`

---

## SECTOR 1 — Identity & Project Boundary Hardening

### 1a — Firebase MCP Re-Anchor + Project Lock (Law 22)
> ⛔ Re-anchor the `firebase-mcp-server` unconditionally FIRST — it drifts across workspaces.

Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

Then verify: `mcp_firebase-mcp-server_firebase_get_environment` → must show `gen-lang-client-0386732425`.
// turbo
```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"
```
All three must agree: `gen-lang-client-0386732425`. Any mismatch → **HALT**.

### 1b — Cross-Project Poison String Scan (MCP-first)
Use `grep_search` for: `CareKey|FirstPick|SARAH|Soul Contract|epi-hab|fleetlabs|infinity-press`
Include: `src/**`, `functions/src/**`, `scripts/**`, `*.json`, `*.md`
Exclude: `node_modules/`, `KNOWLEDGE.md` (historical context)
Any match → **HALT**. P0 cross-project bleed.

---

## SECTOR 2 — Secret & Credential Penetration (MCP-first)

### 2a — Hardcoded API Key Scan
Use `grep_search` with patterns:
- `AIza[0-9A-Za-z-_]{35}` (Firebase/GCP API keys)
- `sk-[a-zA-Z0-9]{40,}` (third-party API keys)
- `apiKey:\s*['"][A-Za-z0-9]` (JS config leaks)
- `"api_key"\s*:\s*"[A-Za-z0-9]` (JSON leaks)
- `PROTOCOL_PASSPHRASE\s*=\s*[^$]` (env literal leaks)
Include: `src/**`, `functions/src/**`, `public/**`
Exclude: `.env.example`, `node_modules/`, `*.test.ts`
Any match → **P0 HALT**. Rotate key immediately.

### 2b — .env File Audit
Use `list_dir` on project root — confirm `.env.local` exists but `.env` does not.
Use `grep_search` on `.gitignore` for `.env.local` — must be present.
If `.env.local` is tracked by git → **P0**: `git rm --cached .env.local`.

### 2c — Secret Manager Verification (MCP)
Use `mcp_gcloud_run_gcloud_command` with args:
`["secrets", "list", "--project=gen-lang-client-0386732425", "--format=json(name)", "--quiet"]`
Confirm required secrets: `PROTOCOL_PASSPHRASE`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `GEMINI_API_KEY`.
Any missing → document as P0.

### 2d — Service Account Key File Scan (MCP-first)
Use `grep_search` for: `"private_key_id"` across all non-test files.
Any match → **P0 IMMEDIATELY**. SA key files must never be in repo.

---

## SECTOR 3 — Firestore Rules Penetration Testing (MCP-first)

### 3a — Rules Export & Validation
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `firestore`.
Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `firestore` and `source_file: "firestore.rules"`.
Any syntax error → fix → re-validate.

### 3b — Zero-Trust Rule Analysis
Use `grep_search` on `firestore.rules` for these anti-patterns:

| Pattern | Severity | Action |
|---|---|---|
| `allow read, write: if true` | P0 | Replace immediately |
| `allow write: if true` | P0 | Replace immediately |
| `allow read: if true` | P1 | Replace with auth check |
| `allow write: if request.auth != null` (no ownership) | P1 | Add ownership validation |
| Missing `request.time < timestamp` on writes | P2 | Add TTL guard |

For each P0 → auto-generate corrected rule → apply via file edit tools → re-validate via MCP.
For each P1 → document exact location and generate corrected rule for user review.

### 3c — Storage Rules Penetration
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `storage`.
Apply same zero-trust analysis as 3b.

---

## SECTOR 4 — Cloud Functions Security (MCP-first)

### 4a — Function Inventory vs Auth Surface
Use `mcp_firebase-mcp-server_functions_list_functions`.
For each HTTP trigger function:
- Use `grep_search` to confirm it uses `corsMiddleware.ts` or equivalent
- Confirm it validates `request.auth` before data access
- Confirm no wildcard `*` CORS

### 4b — Recent Error Log Scan (MCP)
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "WARNING"` and `page_size: 50`.
For each warning/error:
1. Classify: auth failure / data validation error / crash / timeout
2. Identify pattern (is it a repeated attack vector?)
3. For authentication failures → check rate limiting is in place
4. For timeout errors → check function memory settings

### 4c — Function Secret Access Verification
Use `grep_search` in `functions/src/` for `process.env`:
- Confirm all env vars are loaded from Secret Manager, not hardcoded
- Any direct `process.env.STRIPE_SECRET_KEY = ` (assignment not read) → P0

---

## SECTOR 5 — Dependency Vulnerability Scan

### 5a — Root Dependencies
// turbo
```bash
npm audit --production 2>&1 | tail -20
```
For critical/high CVEs:
1. Run `npm audit fix --production` for auto-fixable
2. For manual fixes → document CVE ID, package name, and remediation path

### 5b — Functions Dependencies
// turbo
```bash
cd functions && npm audit --production 2>&1 | tail -20
```
Same remediation protocol as 5a.

---

## SECTOR 6 — Rate Limiting & DDoS Surface Analysis

### 6a — App Check Verification (MCP)
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Firebase App Check"`.
Confirm App Check is configured in `functions/src/` for all public-facing endpoints.
Any unenforced endpoint → flag as P1.

### 6b — Auth Rate Limiting
Use `grep_search` in `functions/src/` for authentication helper functions.
Confirm failed login rate limiting exists (e.g., Firestore-based attempt counters or Firebase Identity Platform settings).

---

## SECTOR 7 — Security Report & Remediation Priority

Generate impact table:

| Sector | Finding | Severity | Auto-Fixed | Requires Manual Action |
|---|---|---|---|---|
| Identity | | | | |
| Secrets | | | | |
| Firestore Rules | | | | |
| Storage Rules | | | | |
| Functions | | | | |
| Dependencies | | | | |
| App Check | | | | |

### 7a — Knowledge Graph Persistence
Use `mcp_knowledge-graph_add_observations` to record:
- All P0/P1 findings (even if fixed)
- All auto-remediation applied
- All patterns found (for cross-session learning)

### 7b — MISSION_STATE Update
If any P0/P1 findings unresolved → add to `Next Session Entry Point` in `MISSION_STATE.md`.

---

## ⚡ Phantom Purge (Final — ALWAYS)
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Phantom purge complete. Security audit sealed.`
