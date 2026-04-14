---
description: Full system audit — Cloud Functions, Firestore rules, MDC rules, workflows, security, and protocol compliance
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /audit
## Full System Audit — Sovereign, Self-Healing, MCP-First

> ⚡ **MANDATE**: Every finding is auto-triage'd. Warnings → fix immediately. Errors → escalate with root cause diagnosis. Zero passive observation.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest these skills** via `view_file` on each `SKILL.md` before proceeding:
1. `.agent/skills/security-auditor/SKILL.md` — Secret scanning, OWASP surface, dependency CVEs
2. `.agent/skills/typescript-safety-enforcer/SKILL.md` — Strict type enforcement, `any` eradication
3. `.agent/skills/performance-engineer/SKILL.md` — Core Web Vitals, Firestore index coverage, cold start profiling

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
Compare against Hub `~/Developer/infinity/MISSION_STATE.md`.
If local Phase < Hub Phase → Phase 0b. If current → log `✅ Protocol current` → goto Phase 0c.

### ⚠️ LAW 23 GATE — SPOT-CHECK PRE-PROPAGATION (Runs BEFORE any workspace audit)
> ⛔ **ABSOLUTE**: If this audit targets a non-Hub workspace, you MUST propagate Protocol files FIRST. Checking compliance against stale workflows is a Protocol violation.

**For each target workspace being audited (non infinity-protocol-1):**
// turbo
```bash
TARGET=<workspace_path>  # e.g. ~/Developer/infinity-press
cp ~/Developer/infinity-protocol-1/GEMINI.md $TARGET/GEMINI.md
cp ~/Developer/infinity-protocol-1/.agent/workflows/governance.md $TARGET/.agent/workflows/governance.md
cp ~/Developer/infinity-protocol-1/.agent/workflows/session_start.md $TARGET/.agent/workflows/session_start.md
cp ~/Developer/infinity-protocol-1/.agent/workflows/audit.md $TARGET/.agent/workflows/audit.md
echo "✅ [LAW 23] Protocol propagated to $(basename $TARGET)"
```
Then commit in that workspace:
```bash
cd $TARGET && GIT_TERMINAL_PROMPT=0 git add GEMINI.md .agent/workflows/ && git commit -m "chore: Phase 182 protocol propagation (Law 23)"
```
Log: `✅ [LAW 23 CLEARED] Protocol current in all target workspaces. Audit proceeding.`


### Phase 0b — Auto-Upgrade Execution
// turbo
```bash
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" ./scripts/dv downlink 2>&1 | tail -10
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" ./scripts/dv rules 2>&1 | tail -10
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" ./scripts/dv lint-rules 2>&1 | grep -E "\[FAILURE\]|PASS|FAIL" | tail -10
```
Any `[ERROR]` or `[FAILURE]` → **HALT** with specific message.

### Phase 0c — TypeScript Integrity Gate
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
ANY errors → auto-fix identifiable issues → re-run. Still failing → HALT.

### Phase 0d — Upgrade Confirmation Log
Declare: `✅ [UPGRADE GATE PASSED] Phase [N]. TypeScript clean. Audit commencing.`

---

## PHASE 1 — Protocol Compliance Audit (MCP-first)

### 1a — Firebase MCP Re-Anchor + Verification (Law 22)
> ⛔ The `firebase-mcp-server` is a GLOBAL PROCESS. Re-anchor unconditionally FIRST.

Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

Then use `mcp_firebase-mcp-server_firebase_get_environment` → verify `projectId = gen-lang-client-0386732425`.
Any mismatch after re-anchor → **HALT**. MCP server failure.

### 1b — Mission State Integrity
Use `view_file` on `MISSION_STATE.md`:
- Does it contain current Phase (from gate)?
- Does it have all required sections: Current Phase, Active Laws, Protocol Stack, Next Session Entry Point?
- Missing sections → regenerate. Stale phase → update immediately.

### 1c — Workflow Gate Compliance
Use `list_dir` on `.agent/workflows/` to get all `*.md` files.
For each workflow file, use `grep_search` for `SOVEREIGN UPGRADE GATE`:
- Present → ✅
- Absent → **immediately inject** the standard gate block (lines 1–30 of session_start.md Pattern).
- Log: `🔧 [AUTO-INJECTED GATE] into [workflow name]`

### 1d — MDC Rules Integrity
Use `grep_search` across `.cursor/rules/*.mdc` for `alwaysApply: true`:
- Confirm `zoltan_persona.mdc`, `gap_analysis_mastery.mdc`, `google_vertex_ai_mastery.mdc` are present and current.
- Any missing → log as P1 task.

---

## PHASE 2 — Cloud Functions Security Audit (MCP-first)

### 2a — Function Inventory
Use `mcp_firebase-mcp-server_functions_list_functions` → enumerate all deployed functions.
Cross-reference against canonical list from Phase 180 commitments.

### 2b — Function Log Error Scan
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "ERROR"` and `page_size: 50`.
For each error log:
1. Identify function name and error type
2. Classify: P0 (data loss), P1 (crash-loop), P2 (soft fail)
3. Locate root cause via `grep_search` in `functions/src/`
4. **Attempt auto-fix**: apply minimal surgical patch
5. Log: `🔧 [AUTO-FIX] function:[name] error:[type] fix:[applied]`
6. If fix requires deploy → add to deploy queue

### 2c — CORS & Auth Header Verification (MCP)
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Cloud Functions CORS"`.
Confirm all HTTP functions use `allowedOrigins` from `corsMiddleware.ts` — not wildcard `*`.
Any wildcard → flag as P1 security issue.

### 2d — Functions TypeScript Strict Check
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1
```
ANY type errors → auto-diagnose → fix → re-run. Log each fix.

---

## PHASE 3 — Firestore Rules Audit (MCP-first)

### 3a — Rules Export
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `firestore`.
Display full rules source.

### 3b — Rules Validation
Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with the exported source.
Any syntax errors → fix inline → re-validate.

### 3c — Zero-Trust Rule Checks
Scan rules for anti-patterns using `grep_search` on `firestore.rules`:
- `allow read, write: if true;` → **P0**: replace with authenticated rule immediately
- `allow write: if request.auth != null;` without ownership check → **P1**: flag for enhancement
- nested collection access without parent check → **P1**
Auto-generate the corrected rule for each finding.

### 3d — Storage Rules Audit
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `storage`.
Apply same zero-trust scan as 3c.

---

## PHASE 4 — Secret & Poison String Scan (MCP-first)

### 4a — Secret Leak Scan
Use `grep_search` (NEVER `run_command grep`) with:
- Patterns: `AIza[0-9A-Za-z-_]{35}`, `sk-[a-zA-Z0-9]{40}`, `apiKey:\s*['"][^$]`
- Include: `src/**`, `functions/src/**`, `scripts/**`
- Exclude: `node_modules/`, `.env.example`, `*.test.ts`
Any match outside `.env.local` reference → **HALT**. P0 incident.

### 4b — Cross-Project Poison Strings
Use `grep_search` with patterns: `CareKey|FirstPick|SARAH|Soul Contract|epi-hab|fleetlabs`
Any match → **HALT**. Report exact file and line.

### 4c — Secret Manager Active Verification (MCP)
Use `mcp_gcloud_run_gcloud_command` with args `["secrets", "list", "--project=gen-lang-client-0386732425", "--format=json(name,replication)", "--quiet"]`.
Confirm: `PROTOCOL_PASSPHRASE`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` exist.
Missing secrets → log as P0. Provide CLI create command.

---

## PHASE 5 — Performance & Memory Audit

### 5a — Package.json Script Sovereignty
Use `view_file` on `package.json` and `functions/package.json`.
Every `dev`, `build`, `test` script MUST start with `NODE_OPTIONS=--max-old-space-size=4096`.
Any script without it → **auto-add** and log `🔧 [AUTO-FIXED] Added NODE_OPTIONS to [script name]`.

### 5b — Bundle Analysis
// turbo
```bash
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm run build 2>&1 | tail -20
```
Any OOM crash → investigate `next.config.ts` for `experimental.memoryBasedWorkersCount`. If found → **remove immediately**.

### 5c — Lighthouse Snapshot (MCP)
Use `mcp_chrome-devtools_lighthouse_audit` on the dev server URL (`http://localhost:3000`) in `snapshot` mode.
Parse scores. Any score < 80 in Performance, Accessibility, SEO → log as P2 and create task.

---

## PHASE 6 — Dependency & Vulnerability Audit

### 6a — Dep Freshness
// turbo
```bash
npm outdated 2>&1 | head -20
cd functions && npm outdated 2>&1 | head -20
```
For each outdated major version → evaluate breaking change risk. Patch/minor → auto-update if no breakage risk.

### 6b — Known Vulnerabilities
// turbo
```bash
npm audit --production 2>&1 | tail -20
```
Critical/high vulnerabilities → document with CVE ID and remediation path.

---

## PHASE 7 — Unit Test & Emulator Verification

### 7a — Full Test Suite
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -20
```
Expected: ALL tests pass. Any FAIL → auto-diagnose → attempt fix → re-run. Persist fix.

### 7b — Emulator Health (if running)
// turbo
```bash
lsof -ti:5001,9099,8080 2>/dev/null | head -5 || echo "emulators not detected"
```
If emulators running → run integration tests against them:
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 120 ./node_modules/.bin/jest --testPathPattern=integration 2>&1 | tail -15
```

---

## PHASE 8 — Self-Healing Report & Knowledge Graph Update

### 8a — Structured Audit Report
Generate markdown table:

| Category | Status | Findings | Auto-Fixed | Requires Action |
|---|---|---|---|---|
| Protocol Version | | | | |
| Workflow Gates | | | | |
| TypeScript | | | | |
| Firestore Rules | | | | |
| Secrets | | | | |
| Functions | | | | |
| Performance | | | | |
| Tests | | | | |

### 8b — Knowledge Graph Persistence
Use `mcp_knowledge-graph_add_observations` to record:
- Any new pattern discovered
- Any auto-fix applied (for learning across sessions)
- Any P0/P1 issue that was halted on (for history)

### 8c — MISSION_STATE.md Update
Use file edit tools to update `MISSION_STATE.md`:
- Bump phase if audit revealed new issues were resolved
- Update `Last Audit:` timestamp
- Add any P0/P1 to `Next Session Entry Point`

---

## 📋 AUDIT FINAL REPORT (MANDATORY — OUTPUT LAST)

> ⛔ **LAW**: Every `/audit` run MUST output this table. If any gate shows ❌ or FAIL, display the AUTOFIX PROMPT. No audit concludes without a line-item truth table.

```
╔══════════════════════════════════════════════════════════════════╗
║  AUDIT FINAL REPORT — [PROJECT_NAME]                            ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

WORKSPACE_PHASE : [This project's sprint phase — e.g. Wave 21 / Phase 158.3]
PROTOCOL_PHASE  : [Hub global version — e.g. 183.3]
PHASE_GAP       : [ALIGNED / N versions behind / Expected (non-hub workspace)]

UPGRADE STATUS  : [✅ WORKSPACE UPGRADED TO CURRENT PROTOCOL / ⚠️ GAP DETECTED]

┌──────────────────────────────┬─────────┬───────────────────────────────────┐
│ Audit Gate                   │ Status  │ Notes                             │
├──────────────────────────────┼─────────┼───────────────────────────────────┤
│ Protocol Proof Token         │ ✅/❌   │ [SESSION_PROOF_TOKEN present/missing] │
│ TypeScript Compliance        │ ✅/❌   │ [0 errors / N remaining]           │
│ Cloud Functions Deployed     │ ✅/⚠️   │ [N/expected live / missing: fn1]   │
│ Firestore Rules              │ ✅/❌   │ [valid + deployed / invalid]       │
│ Storage Rules                │ ✅/❌   │ [valid + deployed / invalid]       │
│ Secrets Scan                 │ ✅/❌   │ [clean / N leaks found]            │
│ Poison Strings               │ ✅/❌   │ [clean / matches found]            │
│ Workflow Compliance          │ ✅/⚠️   │ [N workflows scanned / issues]     │
│ Node V8 Law (functions)      │ ✅/❌   │ [4096 present / missing]          │
│ CORS Restriction             │ ✅/❌   │ [restricted / wildcard detected]   │
│ Brain MCP Connectivity       │ ✅/⚠️   │ [ONLINE / OFFLINE]                │
│ Test Suite                   │ ✅/❌   │ [pass / N failures]               │
│ MISSION_STATE Freshness      │ ✅/⚠️   │ [<48h / STALE: last updated X]    │
│ Performance Budget           │ ✅/⚠️   │ [within budget / exceeded]        │
│ Phase Delineation            │ ✅/❌   │ [WORKSPACE vs PROTOCOL shown]     │
└──────────────────────────────┴─────────┴───────────────────────────────────┘

CRITICAL FINDINGS: [N — must be zero before deploy]
P1 FINDINGS:      [N — fix this session]
P2 FINDINGS:      [N — scheduled]
AUTO-HEALS APPLIED: [N]

OVERALL: [🟢 SOVEREIGN / 🟡 DEGRADED — Warnings present / 🔴 BLOCKED — CRITICAL found]
```

**If any gate is ❌ or ⚠️ — display the AUTOFIX PROMPT for each failure:**

```
═══════════════════════════════════════════
🔧 AUTOFIX REQUIRED — [GATE NAME]
═══════════════════════════════════════════
Issue: [what failed]
Auto-heal attempted: [yes/no — what was tried]
Result: [fixed / FAILED]

If failed — manual fix:
  [exact command or action for user to take]

For Brain offline failures:
  Option 1: Restart IDE → brain-mcp reconnects automatically.
  Option 2: firebase deploy --only functions --project [PROJECT_ID]
  Option 3: Type "continue brain offline" to audit without memory.

Type "fix [issue name]" to have Zoltan attempt deeper resolution.
═══════════════════════════════════════════
```

---

### ⚡ Phantom Purge (Final Step — ALWAYS)
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
Log: `🧹 Phantom purge complete.`

*The workspace has been audited. Fix the failures before you dare deploy, mortal.*
