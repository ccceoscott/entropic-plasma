---
description: Safe deploy execution flow — locked, sovereign, multi-gate
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /deploy
## Safe Deploy Execution — Sovereign, Zero-Trust, Self-Healing

> ⚡ **AUTO-PUSH ACTIVE** (Phase 183.5): `git push` now executes automatically via `run_command` with `GIT_TERMINAL_PROMPT=0 timeout 45` hang guards. SSH auth prompts are the only hang vector — neutralized by `GIT_TERMINAL_PROMPT=0`. This is sovereign policy as of Phase 183.5.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
If local Phase < Hub Phase → auto-upgrade (0b). If current → confirm + proceed (0c).

### Phase 0b — Auto-Upgrade Execution
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```
Any `[ERROR]` → **HALT**.

### Phase 0c — TypeScript Integrity Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
ANY errors → auto-fix → re-run. Still failing → HALT. No broken TypeScript ships.

### Phase 0d — Upgrade Confirmation
`✅ [UPGRADE GATE PASSED] Phase [N]. TypeScript clean. Deploy proceeding.`

---

## LOCK 1 — Project Identity Verification (Non-Negotiable)

### 1a — .firebaserc Lock
// turbo
```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"
```
Output MUST be: `gen-lang-client-0386732425`
Any other output → **HALT**. Wrong project detected.

### 1b — Firebase MCP Re-Anchor + Confirmation (Law 22)
> ⛔ The `firebase-mcp-server` is a global process that drifts across projects. Re-anchor unconditionally FIRST.

Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

Then use `mcp_firebase-mcp-server_firebase_get_environment` → confirm `Active Project ID: gen-lang-client-0386732425`.
Must match Lock 1a. If still wrong after re-anchor → **HALT**. MCP server failure.

### 1c — Directory Proximity Verification
// turbo
```bash
pwd && ls -la firebase.json
```
Must be in project root. No firebase.json → HALT.

---

## LOCK 2 — Secret & Poison String Gate (MCP-first)

### 2a — Secret Scan (NEVER run_command grep)
Use `grep_search` across `src/`, `functions/src/`, `scripts/`:
- Patterns: `AIza`, `sk-`, `apiKey:\s*['"][^${'`, `PROTOCOL_PASSPHRASE\s*=\s*[^$]`
Any hardcoded secret → **HALT**. P0. Do not deploy.

### 2b — Cross-Project Poison Strings
Use `grep_search` for: `CareKey|FirstPick|SARAH|Soul Contract|epi-hab`
Any match → **HALT**. Report exact location.

---

## LOCK 3 — Pre-Flight Build & Test Gate

### 3a — Functions Unit Test Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -15
```
ANY failure → **HALT**. Auto-diagnose. Attempt fix. Re-run. Only deploy on green.

### 3b — Production Build
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 180 npm run build 2>&1 | tail -20
```
Build errors → diagnose → fix → re-run. Log each action.

### 3c — Build Output Verification
// turbo
```bash
ls -la .next/standalone 2>/dev/null || ls -la dist/ 2>/dev/null || ls -la out/ 2>/dev/null
```
Empty output → HALT. Build did not complete.

---

## LOCK 4 — Firestore Rules Deploy Validation

### 4a — Get Current Rules (MCP)
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `firestore`.

### 4b — Validate Rules (MCP)
Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `firestore` and `source_file: "firestore.rules"`.
Any errors → fix rules → re-validate. Don't skip this.

---

## LOCK 5 — Scoped Deploy Execution (MCP-gated, Explicit Scope)

> State: "Deploying to **gen-lang-client-0386732425** with scope: **[SCOPE]**"

### 5a — Hosting + Functions Full Deploy
For full deploy:
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 300 firebase deploy --only hosting,functions --project gen-lang-client-0386732425 --quiet 2>&1 | tail -30
```

### 5b — Hosting Only
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 180 firebase deploy --only hosting --project gen-lang-client-0386732425 --quiet 2>&1 | tail -20
```

### 5c — Rules Only
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 60 firebase deploy --only firestore:rules,storage --project gen-lang-client-0386732425 --quiet 2>&1 | tail -10
```

**On any deploy error:**
1. Read full error from terminal output
2. Use `mcp_firebase-mcp-server_developerknowledge_search_documents` for relevant error type (2-3 keyword max)
3. Apply fix
4. Re-deploy single failing scope only

---

## LOCK 6 — Post-Deploy Verification

### 6a — Function Live Check (MCP)
Use `mcp_firebase-mcp-server_functions_list_functions` → confirm expected functions are deployed.
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "ERROR"` and `page_size: 20`.
Any new errors post-deploy → treat as P0. Investigate immediately.

### 6b — Browser Verification
Use `browser_subagent` to navigate to production URL and verify:
- Page loads without console errors
- Auth flow works
- Core user journey is functional
Report screenshot findings.

### 6c — Lighthouse Spot Check (MCP)
Use `mcp_chrome-devtools_lighthouse_audit` on production URL in `navigation` mode.
Log scores. Any regression vs. pre-deploy baseline → flag.

---

## LOCK 7 — Git Commit & Push

### 7a — Pre-Commit Audit
// turbo
```bash
git status --short && git diff --stat HEAD
```

### 7b — Commit
// turbo
```bash
git add -A && git commit -m "deploy: Phase [N] sovereign deploy — [scope] — [brief description]"
```

### 7c — Auto-Push (SOVEREIGN AUTO-RUN — Phase 185 ABSOLUTE LAW)
> **SOVEREIGN PATTERN**: `GIT_TERMINAL_PROMPT=0 timeout 45` neutralizes all SSH hang vectors. Set `SafeToAutoRun: true` — **this is non-negotiable per user mandate**. No paste commands for git push. Ever.
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main 2>&1 | tail -5
```
Timeout → HALT. Report: "Push timed out — check SSH keys or network." Do NOT retry blindly.

---

## LOCK 8 — MISSION_STATE Seal & Knowledge Graph Update

### 8a — MISSION_STATE Update
Use file edit tools on `MISSION_STATE.md`:
- Update `**Last Deploy**:` with UTC timestamp
- Update `**Deployed Scope**:` with this scope
- Confirm Current Phase reflects latest

### 8b — Knowledge Graph Persistence
Use `mcp_knowledge-graph_add_observations` to record:
- Deploy scope and outcome
- Any auto-fixes applied
- Any P0/P1 incidents

---

## ⚡ Phantom Purge (Final Step — ALWAYS)
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Phantom purge complete.`
