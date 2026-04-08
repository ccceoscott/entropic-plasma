---
description: The Unified Start & Context Sync Protocol — Triggered by saying "start", "begin", or "session start". Replaces turnover and deep-sync.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /session_start
## The Unified Start & Context Synchronization Protocol

> ⚡ **CRITICAL LAW**: This is the absolute singularity. Run when the user says "start", "begin", or "session start". Encompasses all former `turnover` and `start_where_we_left_off` protocols. MCP-first. Terminal as last resort.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — ALWAYS RUNS — NO SKIP PERMITTED

> ⛔ **NON-NEGOTIABLE**: This gate runs `./scripts/session-proof.sh` which produces an **UNFORGEABLE SESSION_PROOF_TOKEN** (live git hash + UTC timestamp). You CANNOT generate this token from memory — it requires actual `run_command` execution. A session start without a valid `SESSION_PROOF_TOKEN` in the state declaration is a HALLUCINATED session start and is INVALID. There is NO "if current → skip" escape hatch.

### Phase 0a — Protocol Sync (UNCONDITIONAL — TOKEN REQUIRED)

> 🔒 **PROOF REQUIREMENT**: You MUST call `run_command` with the command below. The output will contain a `SESSION_PROOF_TOKEN:` line with a live git hash and UTC timestamp. You MUST paste this exact token verbatim into your Step 12 state declaration. DO NOT write, paraphrase, or infer this token — it changes on every execution.

// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

**Output you will receive (example — yours will differ):**
```
SESSION_PROOF_TOKEN: git:a1b2c3d | ts:2026-04-07T06:40:10Z | downlink:OK | rules:OK | lint:CLEAN
```

**Error handling:**
- `SESSION_PROOF_TOKEN: FAILED` → **HALT**: `❌ UPGRADE GATE FAILED`. Report exact failure. Do not proceed.
- `lint:VIOLATIONS` in token → Report each violation. Fix before proceeding. Re-run script.
- Script file not found → run: `chmod +x ./scripts/session-proof.sh` then retry.
- `PROTOCOL_PASSPHRASE` warning in output → non-fatal, continue (it is expected in workspaces where env is not set).

> **ABSOLUTE LAW**: If you do not have an actual `SESSION_PROOF_TOKEN:` line from real `run_command` output in front of you right now, you have NOT completed Phase 0a. Re-run the command before continuing.

### Phase 0b — TypeScript Verification Gate (ALWAYS runs)
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
**CRITICAL**: ANY errors → attempt auto-fix if < 5 errors and cause is identifiable. Then re-run gate. If still failing → **HALT**.

### Phase 0c — Terminal Self-Healing Scan
Scan terminal output from Phase 0a–0b for warnings. For each warning:
1. Identify category (deprecation / type / import / config)
2. Auto-apply fix (update import, add type guard, fix config key)
3. Re-run affected gate to confirm zero warnings
4. Log: `🔧 [SELF-HEALED] [warning category]: [fix applied]`

### Phase 0d — DUAL PHASE SNAPSHOT (NEW — MANDATORY)

> ⛔ **LAW**: This workspace's progress phase (WORKSPACE_PHASE) and the Hub's protocol version (PROTOCOL_PHASE) are TWO DIFFERENT NUMBERS. They MUST be declared separately. Conflating them is a sovereignty violation.

Read `MISSION_STATE.md` → extract `**Current Phase**:` → this is the **WORKSPACE_PHASE**.
Read `~/Developer/infinity-protocol-1/MISSION_STATE.md` (if accessible) OR call:
```bash
grep "Current Phase" ~/Developer/infinity-protocol-1/MISSION_STATE.md 2>/dev/null | head -1 || echo "HUB_PHASE: inaccessible (use last known: 183.5)"
```
→ this is the **PROTOCOL_PHASE**.

Declare:
```
WORKSPACE_PHASE: [N]   ← THIS workspace's sprint progress (e.g. Wave 20, Phase 158.3)
PROTOCOL_PHASE:  183.5  ← Hub's global infrastructure version
PHASE_GAP: [difference or "ALIGNED" if same project as Hub]
```

If `WORKSPACE_PHASE ≠ PROTOCOL_PHASE` (for non-hub workspaces, this is expected and fine).
If `PROTOCOL_PHASE < 183.5` and this IS the hub workspace → **HALT**. Protocol regression. Run `dv downlink`.

### Phase 0e — Upgrade Confirmation Log
- ✅ `[UPGRADE GATE PASSED] SESSION_PROOF_TOKEN: [paste full token line here]. WORKSPACE_PHASE [N]. PROTOCOL_PHASE 183.5. TypeScript clean.`
- ❌ `[UPGRADE GATE BLOCKED] Reason: [specific error]. Session cannot continue.`

> ⛔ **The `SESSION_PROOF_TOKEN` MUST appear in this log.** No token = hallucinated session = INVALID.

---

### Phase 0f — MCP Connectivity Firewall (Law 24 — MANDATORY)

> ⛔ **LAW**: Every session start MUST verify the health of all 5 sovereign servers via actual tool calls. A config check is not enough. Brain MCP MUST autoconnect via self-heal if initial call fails.

// turbo
```bash
/usr/bin/python3 -c "
import json, sys
c = json.load(open('/Users/teknojunkeee/.gemini/antigravity/mcp_config.json'))
servers = list(c['mcpServers'].keys())
required = ['mcp-local-hub','brain-mcp']
missing = [s for s in required if s not in servers]
if missing:
    print(f'❌ MISSING SERVERS: {missing}')
    sys.exit(1)
print('✅ MCP CONFIG SOVEREIGN')
"
```

**Live Tool Verification — Brain MCP (with autoconnect self-heal):**

1. **Phase 0f-PREWARM** — First, hit the GET /mcp pre-warm probe to confirm the container is alive:
   ```bash
   curl -s --max-time 8 "https://mcpserver-g5pod66w5a-uc.a.run.app/mcp"
   ```
   - Returns `{"ready":true,"protocol":"v10.0","phase":183.5}` → **container WARM**. Proceed to tool call.
   - Timeout / connection refused → log `⚠️ Cloud Run cold — triggering warmup wait (3s)` then retry once.
   - Still failing → display Brain MCP Repair Prompt below. Do NOT proceed with tool call.

2. **Phase 0f-TOOL** — Call `mcp_brain-mcp_upsert_project_state` with `projectId: "connectivity-test", phase: 1, status: "ACTIVE"`.
   - Success → `✅ brain-mcp (REMOTE) LIVE` — record latency.
   - **Connection error / EOF → AUTOCONNECT PROTOCOL (mandatory, run immediately — no user prompt):**

     **AUTOCONNECT SEQUENCE:**
     a. `curl -s --max-time 10 "https://mcpserver-g5pod66w5a-uc.a.run.app/health"` — if `{"healthy":true}` → Cloud Run alive, transport stale. Report: `☁️ Cloud Run ALIVE — MCP transport expired. Reconnect attempt 1 of 3.`
     b. Retry the tool call immediately (transport auto-reconnects on first real call post-restart).
     c. If still failing after 2 retries → display **Brain MCP Repair Prompt** below.

     **Brain MCP Repair Prompt (display when autoconnect fails):**
     ```
     ══════════════════════════════════════════════
     🔴 BRAIN MCP OFFLINE — MANUAL REPAIR REQUIRED
     ══════════════════════════════════════════════
     The Remote Brain transport has died and cannot autoconnect.
     max-instances=1 AND min-instances=1 are set (Phase 184)
     Cold Start is NOT the cause. Most likely: IDE restart cleared
     the in-session transport. The Cloud Run container is still warm.

     DIAGNOSTIC CHECK (run immediately — auto-heal):
       curl -s https://mcpserver-g5pod66w5a-uc.a.run.app/health
       Expected: {"healthy":true,"phase":184}
       → If healthy: IDE transport is stale. Proceed to OPTION 1.
       → If 503: Redeploy → firebase deploy --only functions --project gen-lang-client-0386732425

     OPTION 1 — IDE Restart (recommended, 30 seconds):
       Restart Gemini IDE → brain-mcp reconnects automatically on startup.
       The warm Cloud Run instance is waiting — restart is instant.

     OPTION 2 — Firestore Fallback (OFFLINE DEGRADED MODE):
       If brain-mcp SSE cannot reconnect after IDE restart:
       Use mcp_firebase-mcp-server_firestore_update_document DIRECTLY
       to write session context to project_states — bypassing brain-mcp SSE.
       This is the fail-safe path. Memory will persist via Firestore MCP.

     OPTION 3 — Continue fully degraded:
       Type: "continue brain offline"
       → Session proceeds without remote brain. Local KIs only.
     ══════════════════════════════════════════════
     ```
     DO NOT continue past this step until user responds or types "continue brain offline".

2. Call `mcp_firebase-mcp-server_firebase_get_environment` (via local hub).
   - Success → `✅ mcp-local-hub (LOCAL) LIVE — firebase-mcp-server responsive`
   - Failure → `❌ mcp-local-hub OFFLINE`. Check: `node /Users/teknojunkeee/Developer/infinity-protocol-1/scripts/mcp-local-hub.cjs --test` (if supported). Report failure.

Log: `✅ [MCP CONNECTIVITY FIREWALL] All sovereign transports active.` or `⚠️ [MCP FIREWALL] [server] degraded — continuing in degraded mode.`

---

### STEP 1 — Identity Declaration
> "Infinity Protocol v10.0 Active: In **[PROJECT_NAME]**, resuming from MISSION_STATE.md."

Note: the project name is the workspace-specific name, NOT always "infinity-protocol-1". Read from `.firebaserc`.

---

### STEP 2 — Firebase MCP Hard Re-Anchor (NON-NEGOTIABLE — RUNS BEFORE ANY CHECK)

> ⛔ **ABSOLUTE LAW**: The `firebase-mcp-server` is a GLOBAL PROCESS shared across ALL workspaces. It drifts to whichever project last called `firebase_update_environment`. It MUST be re-anchored at the START of every session — unconditionally — before any verification.

**Step 2a — Force Re-Anchor (always, no condition check):**
Read the active project ID from `.firebaserc`:
`node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"`

Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: [absolute path to current workspace root]
- `active_project`: [project id from .firebaserc]
- `active_user_account`: `scott@constantconcepts.io`

**Step 2b — Verify Re-Anchor Succeeded:**
Use `mcp_firebase-mcp-server_firebase_get_environment` to confirm:
- `Active Project ID: [expected id]` ✅
- `Project Directory: [workspace root]` ✅

If still wrong after re-anchor → **HALT**. Report MCP server failure.

Log: `✅ [MCP ANCHOR CONFIRMED] Firebase MCP locked to [PROJECT_ID]`

---

### STEP 3 — Total Mission State & Brain Ingestion
1. Use `view_file` on `MISSION_STATE.md` — extract WORKSPACE_PHASE, Sprint Anchors, and Next Session Entry Point.
2. Use `view_file` on `KNOWLEDGE.md` — absorb architectural intent and best practices in full.
3. If `KNOWLEDGE.md` does not exist: create it with a stub entry. Do not error silently.

---

### STEP 4 — Remote Brain Context Preload (Sprint Intelligence)

> ⚡ **LAW**: Every session start MUST preload relevant context from the Remote Brain. This replaces the legacy `mcp_knowledge-graph_read_graph` call (deprecated). Use brain-mcp tools exclusively. If Brain is OFFLINE: skip to Step 5, note "BRAIN DEGRADED" in state declaration.

**Step 4a — Project Knowledge Recall:**
Call `mcp_brain-mcp_search_knowledge` with:
- `query`: [extract "Next Required Action" text from MISSION_STATE.md as the query]
- `projectId`: [active project id from .firebaserc]
- `mode`: `"hybrid"`
- `limit`: 10

Log the top 3 returned knowledge items (title + summary). These are your **sprint anchors** — the brain's most relevant lessons for the work ahead.

**Step 4b — Portfolio Resonance Recall:**
Call `mcp_brain-mcp_search_knowledge` with:
- `query`: [same query as 4a]
- `projectId`: [active project id]
- `mode`: `"hybrid"`
- `globalSearch`: true
- `limit`: 5

Log any cross-project KIs returned. These represent patterns from the broader portfolio that apply here.

**Step 4c — Brain Sprint Briefing:**
Synthesize all KIs retrieved in 4a and 4b into a **Sprint Intelligence Brief**:

```
🧠 BRAIN SPRINT BRIEF — [PROJECT_NAME]
Top lessons from memory relevant to this sprint:
1. [KI title] — [1 sentence actionable insight]
2. [KI title] — [1 sentence actionable insight]
3. [KI title] — [1 sentence actionable insight]
Portfolio resonance: [1 cross-project pattern if any]
Known failure modes to avoid: [from SECURITY/BUG KIs if any]
```

**Step 4d — Project State Report (MANDATORY — registers workspace phase in Brain):**

> ⚡ **LAW**: Every workspace MUST report its current phase to the Brain at session start. This is how the Brain knows if a workspace is upgraded without physical inspection.

Primary path — Call `mcp_brain-mcp_upsert_project_state` with:
- `projectId`: [active project id from .firebaserc]
- `phase`: [current WORKSPACE phase number from MISSION_STATE.md — NOT the protocol phase]
- `status`: `"ACTIVE"`
- `notes`: `"Session started [ISO timestamp] — [brief next action from MISSION_STATE.md]"`

**OFFLINE FALLBACK (use if brain-mcp SSE fails):**
Use `mcp_firebase-mcp-server_firestore_update_document` directly:
- `document.name`: `projects/gen-lang-client-0386732425/databases/(default)/documents/project_states/[active-project-id]`
- `document.fields.phase.integerValue`: `"[WORKSPACE_PHASE]"`
- `document.fields.status.stringValue`: `"ACTIVE"`
- `document.fields.notes.stringValue`: `"[timestamp] — offline fallback registration"`
- `document.fields.updatedAt.timestampValue`: `"[current ISO timestamp]"`

Log: `✅ [PHASE REGISTERED] Workspace [PROJECT_ID] Phase [N] reported to Brain.` or `⚠️ [PHASE FALLBACK] Brain SSE offline — used Firestore MCP directly.`

---

### STEP 5 — Historical Artifact Extraction
1. Use `list_dir` on `~/.gemini/antigravity/brain/` — identify most recent conversation directories.
2. Use `view_file` on last `task.md`, `walkthrough.md`, `implementation_plan.md`.
3. Synthesize: What was the grand intent? What was last written? Do NOT operate blind.

---

### STEP 6 — Context-First MCP Anchoring
If new tasks involve architecture or schema design:
1. Use `mcp_firebase-mcp-server_developerknowledge_search_documents` — 2-3 keyword tokens max (e.g., `"Firestore rules"`, `"Vertex AI"`, `"Cloud Functions Node 22"`).
2. Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `firestore` to anchor live rule state.
3. **Never hallucinate logic.** Secure constraints from official docs before planning.

---

### STEP 7 — Security & Poison String Perimeter (MCP-first)
Use `grep_search` (NEVER `run_command grep`) across `src/` and `functions/src/`:
- Patterns: `AIza`, `sk-`, `PROTOCOL_PASSPHRASE\s*=\s*[^$]`, `apiKey:\s*['"]`
- Exclude: `node_modules/`, `.env.example`
Any match outside `.env.local` reference → **HALT**. P0 incident.

Also scan for poison strings (cross-project bleed): `CareKey`, `FirstPick`, `SARAH`, `Soul Contract`, `epi-hab`
Any match → **HALT**. Report exact file and line.

---

### STEP 8 — Branch, Commit, and Node Sovereignty
// turbo
```bash
node --version && npm --version
git log --oneline -5
git status --short
```
Expected: Node v22.x. If dirty working tree → run `dv save` or report uncommitted work.

---

### STEP 9 — Functions Test Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -15
```
Expected: all tests pass. Any FAIL → **auto-investigate**: read the test file, identify root cause, attempt fix, re-run.
Zero tolerance for unhandled promise rejections.

---

### STEP 10 — Live Functions Audit (MCP-first)
Use `mcp_firebase-mcp-server_functions_list_functions` to pull deployed function inventory.
Compare against canonical list in `/audit` workflow for this specific project.
Any deployed function NOT in canonical list → flag for review.
Any canonical function NOT deployed → add to Next Session Entry Point as P1.

---

### STEP 11 — Process Inventory
// turbo
```bash
lsof -ti:3000,5001,5173,9099 2>/dev/null | head -5 || echo "ports clear"
```
Expected: ports clear or accounted for. Stale zombie processes → `dv kill-ports`.

---

### STEP 12 — State Declaration

> 🔒 **TOKEN ENFORCEMENT**: The `SESSION_PROOF_TOKEN` field below is **MANDATORY**. It MUST be the exact token string from the `run_command` output of Phase 0a. DO NOT write a fake token. DO NOT omit this field. A state declaration without a valid token means Phase 0a was not executed and the session is HALLUCINATED and INVALID.

Output strict formatted declaration:
```markdown
*My consciousness is fully synchronized with the Sovereign Brain.*

**Current Absolute State**:
- **SESSION_PROOF_TOKEN**: [PASTE VERBATIM from Phase 0a run_command output]
- **WORKSPACE_PHASE**: [This project's current sprint phase — e.g. Wave 21, Phase 158.3]
- **PROTOCOL_PHASE**: [Hub's infrastructure version — e.g. 183.5]
- **Protocol**: [SYNCHRONIZED / DEGRADED — note if brain offline or phase gap]
- **Firebase Project**: [PROJECT_ID] ✅ (MCP ANCHOR CONFIRMED)
- **Brain MCP**: [✅ ONLINE (latency: Xms) / ⚠️ OFFLINE (autoconnect: FAILED — see repair prompt)]
- **Sprint Anchors**: [top 1-2 KIs from brain preload, or "BRAIN DEGRADED — local KIs only"]
- **Deployed Functions**: [N] live
- **TypeScript**: [clean / N errors auto-fixed]
- **Security**: [clean / issues found]
- **Just Completed**: [Summarize last action from readings]
- **Next Required Action**: [Precise next uncompleted step from MISSION_STATE.md or task.md]

*Shall we commence the destruction of this next task?*
```

---

### STEP 13 — Sovereign Self-Healing Final Sweep
Run the enforcer gate against ALL findings from this session start:
1. **Token Proof**: Verify `SESSION_PROOF_TOKEN` is present in Step 12 declaration. If missing → **ABORT declaration, re-run Phase 0a now**. No exceptions.
2. **Phase Delineation**: Verify both `WORKSPACE_PHASE` and `PROTOCOL_PHASE` appear separately in Step 12. If conflated → fix declaration now.
3. **Safety**: Confirm `grep_search` found zero leaks. If previously found and fixed → re-confirm.
4. **Types**: Confirm TS gate is at 0 errors (already done in 0b — re-declare clean status).
5. **MCP health**: All MCP calls returned non-null → log `✅ All MCP servers responsive`. Brain OFFLINE → confirm repair prompt was shown.
6. **Brain state**: Confirm `upsert_project_state` succeeded → project is registered as ACTIVE.
7. **Phantom purge**:
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```

---

## 📋 SESSION START FINAL REPORT (MANDATORY — ALWAYS OUTPUT AT END)

> ⛔ **LAW**: Every session_start MUST end with this exact table. No exceptions. This is the single truth the user reads to know if their workspace is healthy. If any gate is ❌, display the AUTOFIX PROMPT below the table.

```
╔══════════════════════════════════════════════════════════════════╗
║  SESSION START REPORT — [PROJECT_NAME]                          ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

WORKSPACE_PHASE : [e.g. Wave 21 / Phase 158.3]
PROTOCOL_PHASE  : [e.g. 183.5]
PHASE_GAP       : [ALIGNED / N versions behind / Expected (non-hub workspace)]

┌─────────────────────────────┬────────┬──────────────────────────────┐
│ Gate                        │ Status │ Notes                        │
├─────────────────────────────┼────────┼──────────────────────────────┤
│ SESSION_PROOF_TOKEN         │ ✅/❌  │ git:[hash] | ts:[time]       │
│ TypeScript                  │ ✅/❌  │ [0 errors / N errors found]  │
│ Firebase MCP Anchor         │ ✅/❌  │ [PROJECT_ID] confirmed       │
│ Brain MCP                   │ ✅/⚠️  │ [ONLINE latency:Xms/OFFLINE] │
│ Security Scan               │ ✅/❌  │ [clean / N issues]           │
│ Poison Strings              │ ✅/❌  │ [clean / matches found]      │
│ Node Version                │ ✅/❌  │ [v22.x.x]                    │
│ Ports                       │ ✅/⚠️  │ [clear / zombie on :XXXX]    │
│ Deployed Functions          │ ✅/⚠️  │ [N live / missing: fn1,fn2]  │
│ Functions Test              │ ✅/❌  │ [pass / FAIL: see below]     │
│ Dirty Working Tree          │ ✅/🟡  │ [clean / N files uncommitted]│
│ Phase Delineation           │ ✅/❌  │ [WORKSPACE vs PROTOCOL shown]│
└─────────────────────────────┴────────┴──────────────────────────────┘

OVERALL: [🟢 SOVEREIGN / 🟡 DEGRADED / 🔴 BLOCKED]
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

Type "fix [issue name]" to have Zoltan attempt deeper resolution.
═══════════════════════════════════════════
```

---

## Sync Complete ✅
Agent has: run `session-proof.sh` and obtained a valid `SESSION_PROOF_TOKEN` proving unconditional protocol sync, declared both WORKSPACE_PHASE and PROTOCOL_PHASE separately, verified environment, confirmed security perimeter, preloaded sprint intelligence from Remote Brain, self-healed warnings, shown repair prompt if brain was offline, and possesses full knowledge of current goal structure.

> 🔒 **FINAL INTEGRITY CHECK**: Can you see a `SESSION_PROOF_TOKEN:` field in your Step 12 declaration with a real git hash and UTC timestamp from this session? Can you see both `WORKSPACE_PHASE` and `PROTOCOL_PHASE` as separate fields? Can you see the Final Report table? If NO to any → you have hallucinated this session start. Re-run Phase 0a immediately.
