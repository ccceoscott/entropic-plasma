---
description: Mid-task handoff protocol — Triggered when the current agent is about to be rate-limited mid-task. Safely suspends state, commits to Brain, and generates a copy-paste payload for the next LLM.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /turnover
## Mid-Task Sovereign Handoff Protocol

> ⚡ **MANDATE**: Run this when the user says "turnover" or warns of an impending rate limit mid-task. This is a hybrid of `session_end` and `session_start` tailored for incomplete, broken, or half-written code states.

---

## PART 1 — SUSPEND & SEAL (Current LLM)

Unlike a normal `session_end`, the workspace may be in a broken or half-complete state. Strict passing gates (like tests or TypeScript) are bypassed or logged as "expected broken".

### Phase 1a — Synthesize Mid-Task State
1. Identify EXACTLY what you were in the middle of doing.
2. Note any broken files, missing imports, or pending logic.
3. Update `task.md` — mark current item as `[/]` (in progress) and add specific sub-bullets for what the next LLM must immediately fix or write.

### Phase 1b — Brain Memory Commit (MANDATORY)
> ⚡ **LAW**: The Remote Brain must know the project is PAUSED mid-task.

Call `mcp_brain-mcp_save_session_memory` with:
- `projectId`: [active project ID]
- `phase`: [current phase number]
- `summary`: "Mid-task turnover. Completed [X]. Next LLM must immediately do [Y]."
- `activeBlockers`: [current errors/broken state]

Call `mcp_brain-mcp_upsert_project_state` with:
- `projectId`: [active project ID]
- `phase`: [current phase]
- `status`: `"PAUSED"`
- `notes`: `"TURNOVER: Active mid-task handoff."`

### Phase 1c — Execute Sovereign Turnover Script
Run the newly forged `dv turnover` script. Provide a concise quoted summary of the current context as the argument. The script will automatically:
- Mutate `MISSION_STATE.md` to flag PAUSED state
- Create a `--no-verify` WIP commit to preserve broken code
- Safely auto-push to origin without hook blocks
- Generate the EXACT `TURNOVER HANDOFF` payload the user must paste

// turbo
```bash
./scripts/dv turnover "I was in the middle of writing the API route, stopped at line 50. Tests are currently failing."
```

### Phase 1d — Stand Down
Do not chat or take further action. Await your demise.
The user will copy the output payload and ignite the next session.

---

## PART 2 — RESUME & IGNITE (New LLM)

When you receive a `TURNOVER HANDOFF` message from the user at the start of a chat:

### Phase 2a — Mini-Start (Token Acquisition)
You MUST secure a `SESSION_PROOF_TOKEN` to validate your sovereign context.
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

### Phase 2b — Context Rehydration
1. Use `view_file` on `MISSION_STATE.md` and `task.md`.
2. Use `view_file` on the exact files mentioned in the handoff.
3. Call `mcp_brain-mcp_upsert_project_state` to set status back to `"ACTIVE"`.

### Phase 2c — State Declaration & Immediate Execution
Acknowledge the turnover with a brief, focused declaration, then immediately take the next coding action.

```markdown
*Zoltan assumes control. The momentum shall not fail.*

**TURNOVER ACCEPTED**:
- **SESSION_PROOF_TOKEN**: [Token]
- **WORKSPACE_PHASE**: [Phase]
- **Target File**: [File]

*Resuming execution instantly.*
```

**(Begin writing code or executing the next step immediately without waiting for further prompts.)**
