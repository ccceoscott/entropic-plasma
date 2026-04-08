---
description: Zero-trust security gate — secrets scan, Firebase rules pen-test, SA validation
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /security_scan
## Zero-Trust Security Gate — Pre-Commit, Pre-Deploy Guardian

> ⚡ **MANDATE**: This is the last line of defense before code leaves the workspace. Every check must pass clean. No warnings tolerated.

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

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run. Clean only.

---

## GATE 1 — Project Identity Lock (Re-Anchor + Dual Verification — Law 22)

> ⛔ Re-anchor the `firebase-mcp-server` unconditionally FIRST (Law 22).

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

---

## GATE 2 — Secret Leak Scan (MCP-first — NEVER run_command grep)

Use `grep_search` with each pattern separately:

**Pattern 1**: `AIza[0-9A-Za-z\-_]{35}`
Include: `src/**,functions/src/**,public/**,scripts/**`
Exclude: `node_modules/`

**Pattern 2**: `sk-[a-zA-Z0-9]{40}`
Include: `src/**,functions/src/**`

**Pattern 3**: `apiKey:\s*['"][A-Za-z0-9]`
Include: `src/**,public/**`
Exclude: `.env.example`

**Pattern 4**: `"private_key_id"`
Include all — this catches SA key files.

**Pattern 5**: `PROTOCOL_PASSPHRASE\s*=\s*[^{$]`
Include: `**/*.ts,**/*.js,**/*.env`

Any match → **P0 HALT**. Do not proceed. Remediate first.

---

## GATE 3 — Cross-Project Poison Strings (MCP-first)

Use `grep_search` with:
- Pattern: `CareKey|FirstPick|SARAH|Soul Contract|epi-hab`
- Include: `src/**,functions/src/**,scripts/**`
- Exclude: `node_modules/,KNOWLEDGE.md`

Any match → **HALT**. P0. Report exact file:line.

---

## GATE 4 — .gitignore Completeness

Use `view_file` on `.gitignore`. Confirm these entries exist:
```
.env.local
.env.*.local
serviceAccountKey*.json
*-firebase-adminsdk*.json
*.pem
*.key
```
Any missing → **auto-add** via file edit tools. Log: `🔧 [AUTO-FIXED] .gitignore missing: [entry]`

Use `grep_search` for `\\.env\\.local` in `.gitignore` — confirm it is excluded.

---

## GATE 5 — Firestore Rules Validation (MCP-first)

Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `firestore` and `source_file: "firestore.rules"`.
Any error → fix → re-validate. Zero syntax errors permitted.

Use `grep_search` on `firestore.rules` for `if true` — any match → **P0 HALT**. Open rules cannot ship.

---

## GATE 6 — Storage Rules Validation (MCP-first)

Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `storage` and `source_file: "storage.rules"`.
Any error → fix → re-validate.

Use `grep_search` on `storage.rules` for `if true` — any match → **P0 HALT**.

---

## GATE 7 — Node Memory Sovereignty

Use `view_file` on `package.json` — confirm ALL scripts have `NODE_OPTIONS=--max-old-space-size=4096`.
Use `view_file` on `functions/package.json` — same check.
Any script missing it → **auto-add** using file edit tools.

---

## GATE 8 — Functions Test (Final Pre-Commit Gate)
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -15
```
Any FAIL → **HALT**. Fix first. Re-run gate.

---

## GATE 9 — Final Verdict

Generate pass/fail table:

| Gate | Status | Action Taken |
|---|---|---|
| G1 — Project Identity | | |
| G2 — Secret Scan | | |
| G3 — Poison Strings | | |
| G4 — .gitignore | | |
| G5 — Firestore Rules | | |
| G6 — Storage Rules | | |
| G7 — Node Memory | | |
| G8 — Functions Tests | | |

**ALL GATES PASS** → `✅ SECURITY SCAN CLEARED. Safe to commit and deploy.`
**ANY GATE FAIL** → `❌ SECURITY SCAN BLOCKED. Resolve all failures before proceeding.`

---

## GATE 10 — Knowledge Graph Update (MCP)

Use `mcp_knowledge-graph_add_observations` to record:
- Run timestamp and result (PASS/BLOCK)
- Any auto-fixes applied
- Any P0 patterns found

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Security scan complete.`
