---
description: Mid-task handoff protocol (R.A.P.S.) — Safely suspends state locally and generates a payload.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 (R.A.P.S.) — /turnover

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY

### Phase 0a — Protocol Sync
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

### Phase 0b — TypeScript Verification
// turbo
```bash
cd functions && NODE22_PATH NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```

### Phase 0c — DUAL PHASE SNAPSHOT
Extract `WORKSPACE_PHASE` from `MISSION_STATE.md`.

---

## Mid-Task Sovereign Handoff Protocol

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` before proceeding:
1. `.agent/skills/sovereign-terminal-operator/SKILL.md` — Hang-eradication, non-blocking CLI, timeout-safe invocations

> ⚡ **MANDATE**: Run this when the user says "turnover" or warns of an impending rate limit mid-task. The Remote Brain is DEPRECATED. All handover data must be written to `.agent/` and `MISSION_STATE.md`.

---

## PART 1 — SUSPEND & SEAL (Current LLM)

### Phase 1a — Synthesize Mid-Task State
1. Update `task.md` — mark current item as `[/]` (in progress) and add specific sub-bullets for what the next LLM must immediately fix or write.
2. Update `MISSION_STATE.md` using file edit tools to flag a `PAUSED` state along with precise instructions for the incoming Agent in the "Next Session Entry Point" section.

### Phase 1b — Execute Sovereign Turnover Script
Run the `dv turnover` script. Provide a concise quoted summary of the current context as the argument. The script will automatically:
- Create a `--no-verify` WIP commit to preserve broken code
- Generate the EXACT `TURNOVER HANDOFF` payload the user must paste

// turbo
```bash
./scripts/dv turnover "I was in the middle of writing the API route. task.md updated."
```

### Phase 1c — Stand Down
Do not chat or take further action. Await your demise.

---

## PART 2 — RESUME & IGNITE (New LLM)

When you receive a `TURNOVER HANDOFF` message:

### Phase 2a — Mini-Start (Token Acquisition)
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

### Phase 2b — Context Rehydration (R.A.P.S)
1. Use `read_file` on `MISSION_STATE.md` and `task.md`.
2. Use `view_file` on the exact files mentioned in the handoff.
3. Use file edit tools to remove the `PAUSED` state from `MISSION_STATE.md`.

### Phase 2c — State Declaration & Immediate Execution
Acknowledge the turnover with a brief, focused declaration, then immediately take the next coding action.

```markdown
*Zoltan assumes control. The momentum shall not fail.*

**TURNOVER ACCEPTED (R.A.P.S.)**:
- **SESSION_PROOF_TOKEN**: [Token]
- **WORKSPACE_PHASE**: [Phase]
- **Target File**: [File]

*Resuming execution instantly.*
```
