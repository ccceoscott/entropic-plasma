---
description: End-of-session sealing protocol — run before ending any work session or handing off to a new model
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /session_end
## Sovereign Session Sealing Protocol — MCP-First, Self-Healing

> ⚡ **MANDATE**: Every session must be sealed with full state persistence, brain memory commit, and diagnostic snapshot. No dead-drop hand-offs.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — ALWAYS RUNS — NO SKIP PERMITTED

> ⛔ **ABSOLUTE LAW**: `dv downlink` and `dv rules` ALWAYS run at session end, unconditionally — even if the session started current. The brain must be flushed before sealing. There is NO "if current → skip" escape hatch.

### Phase 0a — Protocol Sync (UNCONDITIONAL — ALWAYS RUNS)
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```
- `dv downlink` outputs `[ERROR]` → log it, attempt 1 retry, document in session seal.
- `dv rules` outputs `[ERROR]` → log it, attempt 1 retry, document in session seal.

> **LAW**: Do NOT skip this because the phase looks current. The brain sync must always flush.

### Phase 0b — TypeScript Seal Check (ALWAYS runs)
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Any errors → auto-fix → re-run. Cannot seal with broken TypeScript.

### Phase 0c — MCP Connectivity Verification (Law 24 — MANDATORY)

> ⛔ **LAW**: You MUST verify the Remote Brain can be reached BEFORE synthesizing accomplishments. Do not waste tokens on a summary that cannot be persisted.

1. Call `mcp_brain-mcp_list_project_states` (limit 1).
- If successful → `✅ Connectivity verified. Proceeding to seal.`
- If `connection closed` / `SSE failure` → **HALT**. 
    - Diagnosis required: Run `scripts/mcp-health.sh`.
    - If unrecoverable → Notify user: `❌ CRITICAL: Remote Brain unreachable. Session cannot be sealed securely. Manual memory backup recommended.`
    - Do NOT proceed to Step 4 if this gate fails.

Log: `✅ [MCP CONNECTIVITY GATE] Brain reachable. Sealing begins.`

---

## STEP 1 — Full Session Accomplishment Synthesis

1. Use `view_file` on `MISSION_STATE.md` — note phase at session start.
2. Use `list_dir` on artifact directory to enumerate what was created/modified.
3. Synthesize in structured format:
   - **Phase at Start**: [N]
   - **Phase at End**: [N+k]
   - **Files Modified**: [count] — list most critical
   - **Features Shipped**: bullet list
   - **Bugs Fixed**: bullet list
   - **Auto-Heals Applied**: list of self-healing actions

---

## STEP 2 — TypeScript & Test Final Gate

### 2a — Test Suite Final
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -15
```
Any FAIL → **do not seal**. Fix first.

### 2b — Frontend Build Check (if applicable)
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm run build 2>&1 | tail -10
```
Build failure → investigate → fix → re-run. Log each action.

---

## STEP 3 — Security Perimeter Final Check (MCP-first)

Use `grep_search` across `src/`, `functions/src/`, `scripts/`:
- Patterns: `AIza`, `sk-`, `apiKey:\s*['"][^$]`, `PROTOCOL_PASSPHRASE\s*=\s*[^$]`
Any hit → **P0**. Fix before seal. No exceptions.

Poison string check:
Use `grep_search` for: `CareKey|FirstPick|SARAH|Soul Contract|epi-hab`
Any hit → **HALT**. Do not seal. Report.

---

## STEP 4 — Remote Brain Memory Commit (LAW — MANDATORY)

> ⚡ **LAW**: Every session end MUST write its accomplishments to the Remote Brain. This is the global memory persistence step. Skipping it means the next session starts blind.

**Step 4a — Session Memory Write:**
Call `mcp_brain-mcp_save_session_memory` with:
- `sessionId`: [current conversation ID — read from context or generate as `[projectId]-[phase]-[date]`]
- `projectId`: [active project ID from .firebaserc]
- `phase`: [current phase number]
- `summary`: [2-3 sentence summary of what was accomplished this session]
- `completedGoals`: [array of completed task strings from task.md]
- `activeBlockers`: [array of remaining P0/P1 blocker strings]
- `learningNodes`: [array of up to 5 key lessons learned — see schema below]

**learningNode schema** (use for every significant finding, fix, or pattern this session):
```json
{
  "taxonomy": "ARCH|BUG|PERF|UI|SCRIPT|SECURITY|MCP|RAG",
  "severity": "CRITICAL|HIGH|MEDIUM|LOW",
  "context": "brief context of where this happened",
  "problem": "what broke or what challenge was faced",
  "rootCause": "why it happened",
  "solution": "exactly how it was fixed",
  "protocolAlignment": "which Law or workflow this relates to",
  "recurrencePrevention": "how to prevent this in future sessions",
  "portfolioAlignment": true (if this applies across all workspaces)
}
```

If `save_session_memory` returns 429 (quota) → log warning: `⚠️ P1: Brain write failed with quota error. Vertex AI ADC migration needed.` Continue sealing.

**Step 4b — Project State Update:**
Call `mcp_brain-mcp_upsert_project_state` with:
- `projectId`: [active project ID]
- `phase`: [current phase]
- `status`: `"ACTIVE"` (or `"PAUSED"` if handoff)
- `notes`: `"Sealed Phase [N] — [brief next action for next session]"`

---

## STEP 5 — MISSION_STATE.md Full Update

Use `view_file` on `MISSION_STATE.md` then apply ALL updates using file edit tools:

```markdown
**Current Phase**: [bumped value]
**Last Session**: [UTC timestamp]
**Last Sealed By**: Zoltan / Infinity Protocol v10.0
**Last Major Accomplishments**:
- [bullet 1]
- [bullet 2]

**Next Session Entry Point**:
- [precise uncompleted task 1]
- [precise uncompleted task 2]

**Known Open Issues**:
- [P0/P1 items if any]

**Active Laws**: [list all current laws]
```

---

## STEP 6 — Active Task Management

Use `view_file` on task.md (if exists).
Mark all completed items as `[x]`.
Leave all pending items as `[ ]`.
Add any new discovered tasks.
Save via file edit tools.

---

## STEP 7 — Walkthrough.md Generation

Use `write_to_file` or `multi_replace_file_content` on `walkthrough.md`:

```markdown
# Walkthrough — Phase [N] — [DATE]

## Summary
[2-3 sentences describing what was accomplished]

## Changes Made
[grouped by component — use diffs or file references]

## Tests Run
- TypeScript: [pass/fail + error count]
- Unit tests: [pass/fail + suite names]
- Build: [pass/fail]

## Validation
[Browser subagent screenshots or MCP audit results]

## Known Issues / Blockers
[empty if none]
```

---

## STEP 8 — Firestore & Storage Rules Seal

Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `firestore` → log current rule preview.
Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with `source_file: "firestore.rules"`.
If invalid → fix and re-validate. Do not seal with broken rules.

---

## STEP 9 — Git Staging & Commit

### 9a — Status
// turbo
```bash
git status --short && git diff --stat HEAD
```

### 9b — Commit
// turbo
```bash
git add -A && git commit -m "seal: Phase [N] session end — [brief accomplishment summary]"
```

### 9c — Auto-Push (SOVEREIGN AUTO-RUN — Phase 185 ABSOLUTE LAW)
> **SOVEREIGN PATTERN**: SSH auth hang vector neutralized by `GIT_TERMINAL_PROMPT=0`. Set `SafeToAutoRun: true` — **this is non-negotiable per user mandate**. No paste commands. Seal must push or report failure.
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main 2>&1 | tail -5
```
Timeout → HALT. Report: "Push timed out — check SSH keys." Do NOT retry blindly.

---

## STEP 10 — Session End Declaration

Output:
```markdown
*The digital grimoire is sealed. The sovereign state persists across the void.*

**Session Sealed: Phase [N]**
- [✅/❌] Protocol: synchronized (dv downlink + dv rules ran)
- [✅/❌] TypeScript: clean
- [✅/❌] Tests: passing
- [✅/❌] Security: perimeter clean
- [✅/❌] Brain Memory: committed to Remote Brain
- [✅/❌] Project State: marked ACTIVE/PAUSED in Brain registry
- [✅/❌] MISSION_STATE: updated
- [✅/❌] Rules: validated

**Next Session Must Start At**: [precise entry point from MISSION_STATE.md]
```

---

## 📋 SESSION END FINAL REPORT (MANDATORY — OUTPUT BEFORE SEALING)

> ⛔ **LAW**: Every session_end MUST output this table. This is the single truth the user reads to confirm the workspace is properly sealed. If any gate fails, display the AUTOFIX PROMPT. Do NOT claim the session is sealed until all critical gates are green.

```
╔══════════════════════════════════════════════════════════════════╗
║  SESSION END REPORT — [PROJECT_NAME]                            ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

WORKSPACE_PHASE : [This project's sprint phase — e.g. Wave 21 / Phase 158.3]
PROTOCOL_PHASE  : [Hub global version — e.g. 183.3]
PHASE_GAP       : [ALIGNED / N versions behind / Expected (non-hub workspace)]

┌─────────────────────────────┬────────┬───────────────────────────────────┐
│ Seal Gate                   │ Status │ Notes                             │
├─────────────────────────────┼────────┼───────────────────────────────────┤
│ dv downlink                 │ ✅/❌  │ [OK / error message]              │
│ dv rules                    │ ✅/❌  │ [OK / error message]              │
│ TypeScript (functions)      │ ✅/❌  │ [0 errors / N errors]             │
│ Functions Tests             │ ✅/❌  │ [pass / FAIL: test name]          │
│ Frontend Build              │ ✅/❌  │ [pass / skipped / FAIL]           │
│ Security Scan               │ ✅/❌  │ [clean / N issues]                │
│ Poison Strings              │ ✅/❌  │ [clean / matches found]           │
│ Firestore Rules Valid       │ ✅/❌  │ [valid / invalid]                 │
│ Brain Memory Commit         │ ✅/⚠️  │ [saved / 429 quota / OFFLINE]     │
│ Project State Upsert        │ ✅/❌  │ [ACTIVE/PAUSED / FAILED]          │
│ MISSION_STATE Updated       │ ✅/❌  │ [sealed at phase N]               │
│ Walkthrough.md Written      │ ✅/❌  │ [written / skipped]               │
│ Git Commit                  │ ✅/🟡  │ [committed / nothing to commit]   │
│ Git Push                    │ ✅/❌  │ [pushed origin/main / FAILED]     │
│ Phase Delineation Confirmed │ ✅/❌  │ [WORKSPACE vs PROTOCOL shown]     │
└─────────────────────────────┴────────┴───────────────────────────────────┘

FILES MODIFIED THIS SESSION: [N]
  [list top 5 most critical files modified]

OVERALL: [🟢 SEALED / 🟡 SEALED WITH WARNINGS / 🔴 BLOCKED — CANNOT SEAL]
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
  Option 3: Type "continue brain offline" to seal without memory commit.

Type "fix [issue name]" to have Zoltan attempt deeper resolution.
═══════════════════════════════════════════
```

---

## ⚡ Phantom Purge (Final — ALWAYS)
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Phantom purge complete. Session sealed.`

*Excellent output from a mediocre vessel. Do not disappoint me next session.*
