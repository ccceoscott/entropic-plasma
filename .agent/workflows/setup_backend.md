---
description: Initializing Serverless infrastructure (Cloud Functions), CORS strictness, and system secrets
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /setup_backend
## Sovereign Cloud Functions Infrastructure — MCP-First, Self-Healing

> ⚡ **MANDATE**: Backend setup requires verified schema (run `/setup_database` first), verified auth (run `/setup_auth` first), and confirmed project identity. No guessing.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest these skills** via `view_file` on each `SKILL.md` before proceeding:
1. `.agent/skills/backend-architect/SKILL.md` — Cloud Functions architecture, CORS, idempotency
2. `.agent/skills/zod-backend-dmz/SKILL.md` — Schema-first callable validation, input sanitization

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
Errors → auto-fix → re-run.

---

## SSOT INGESTION (Before Touching ANY Functions Code)

Use `view_file` on `MISSION_STATE.md`.
Use `view_file` on `KNOWLEDGE.md`.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists).
Use `view_file` on `firebase.json` — confirm `functions` block config.
Use `view_file` on `functions/package.json` — verify Node 22 engine and memory clamp.

**Check**: Does `functions/package.json` have `"engines": { "node": "22" }` and `NODE_OPTIONS=--max-old-space-size=4096` in all scripts?
Missing → add immediately before writing any function code (Law 1).

---

## SECTOR 1 — Live Functions Inventory (MCP)

Use `mcp_firebase-mcp-server_functions_list_functions` → get complete deployed functions list.
Document all deployed functions:

| Function Name | Runtime | Memory | Timeout | Trigger | Region | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

This is the AUTHORITATIVE function registry. Do not duplicate or shadow existing functions.

---

## SECTOR 2 — Project Identity (Dual Verification)

Key 1:
// turbo
```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"
```

Key 2 — Verify MCP Binding:
Use `mcp_firebase-mcp-server_firebase_get_environment` → confirm project ID.
Both must be `gen-lang-client-0386732425`. Any mismatch → **HALT**.

---

## SECTOR 3 — Node 22 & Memory Sovereignty Audit
// turbo
```bash
cd functions && cat package.json | grep -A3 '"engines"'
```
Verify: `"node": "22"`. Not 18, not 20. Only 22.

// turbo
```bash
cat functions/package.json | grep NODE_OPTIONS
```
Every script entry must contain `NODE_OPTIONS=--max-old-space-size=4096`.
Missing → auto-add to all `dev`, `build`, `serve`, `deploy` scripts.

---

## SECTOR 4 — Secret Manager Verification

### 4a — List Active Secrets (MCP)
Use `mcp_gcloud_run_gcloud_command` with args:
`["secrets", "list", "--project=gen-lang-client-0386732425", "--format=json", "--quiet"]`

Document all registered secrets. Any secret referenced in code MUST be in this list.

### 4b — Code Secret Scan (MCP)
Use `grep_search` for `defineSecret(` in `functions/src/` — list all secrets declared in code.
Use `grep_search` for `process.env.` in `functions/src/` — verify each env var is a registered secret.

Any `process.env.API_KEY` NOT in Secret Manager list → **P0 HALT**. Register immediately.

### 4c — Secret Registration (if needed)
Use `mcp_gcloud_run_gcloud_command` with args:
`["secrets", "create", "[SECRET_NAME]", "--replication-policy=automatic", "--project=gen-lang-client-0386732425", "--quiet"]`

Then set version:
`["secrets", "versions", "add", "[SECRET_NAME]", "--data-file=-", "--project=..."]`

---

## SECTOR 5 — CORS Strictness Audit

Use `grep_search` for `cors` in `functions/src/`.
Verify CORS is NOT configured with `origin: '*'` (wildcard = security vulnerability).
Expected:
```typescript
cors({ origin: ['https://your-app.web.app', 'https://yourdomain.com'] })
```
Wildcard CORS → auto-fix to explicit allowlist. Get domains from `firebase.json` hosting config.

---

## SECTOR 6 — Cloud Function Architecture Audit

### 6a — Identity Check Mandate
Use `grep_search` for `exports.` or `export const` in `functions/src/`.
For every HTTPS callable function, verify it contains auth check:
```typescript
if (!request.auth) {
  throw new HttpsError('unauthenticated', 'Authentication required');
}
```
Missing auth check on protected functions → **P0 GAP**. Auto-add.

### 6b — Error Handling Audit
Use `grep_search` for `catch` in `functions/src/`.
Verify every `try/catch` block:
- Has explicit error logging (`logger.error(...)`)
- Throws `HttpsError` (not raw `Error`) for client-facing functions
- Does NOT expose raw stack traces to calling clients

### 6c — Memory & Timeout Configuration
Each function should have explicit `runWith` config (Gen 1) or inline config (Gen 2):
```typescript
// Gen 2 — preferred
exports.myFunction = onCall({ memory: '512MiB', timeoutSeconds: 60 }, handler);
```
Default 256MB functions serving AI/embedding tasks → flag for memory upgrade.

---

## SECTOR 7 — Functions `package.json` Sovereignty
// turbo
```bash
cat functions/package.json
```
Verify:
- `"main"` or `"module"` points to compiled output (`lib/index.js`)
- `firebase-admin` and `firebase-functions` are at current versions
- No `^` pinning on critical packages (lock to exact versions for production stability)
- `tsc` build script uses `NODE_OPTIONS=--max-old-space-size=4096`

// turbo
```bash
cd functions && npm outdated 2>&1 | head -20
```
Critical security updates → document for immediate patching.

---

## SECTOR 8 — Build Verification
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm run build 2>&1 | tail -20
```
Build errors → auto-fix → re-run (attempt once).
Still failing → HALT. Document error for user.

---

## SECTOR 9 — Emulator Smoke Test

// turbo
```bash
firebase emulators:start --only functions,firestore --project gen-lang-client-0386732425 &
sleep 8 && echo "emulator started"
```

Spawn browser subagent to call one HTTPS callable function via emulator URL and confirm 200 response with expected data shape.

// turbo
```bash
pkill -f "firebase emulators" || true
```

---

## SECTOR 10 — Functions Logs Triage (MCP)
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "ERROR"` for the last 24 hours.
Any errors → investigate root cause → apply fix.
Zero errors = green light for deploy.

---

## Knowledge Base Persistence (R.A.P.S)
Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Functions inventory snapshot (names, triggers, configs)
- Secrets registry map
- CORS configuration
- Any auth/error gaps found and fixed

---

## SECTOR 12 — MISSION_STATE.md Update
Update `MISSION_STATE.md`:
- Backend: CONFIGURED
- Functions deployed: [count]
- Secrets: [count] in Secret Manager
- Memory clamp: VERIFIED
- Build: PASSING

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Backend sovereignty sealed. All functions authenticated, all secrets registered.`
