---
description: Invoke the Fleet Deploy Guardian — Safe, Multi-Gate Deployment Protocol.
alwaysApply: false
---

# Workflow: Deploy Guardian (Summoned)

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY

### Phase 0a — Protocol Sync
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

### Phase 0b — TypeScript Verification
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```

### Phase 0c — DUAL PHASE SNAPSHOT
Extract `WORKSPACE_PHASE` from `MISSION_STATE.md`.

---


*The code shall be forged in the fire of production.*

## Arcane Objective
You have summoned the **Fleet Deploy Guardian**. Use this workflow to execute safe deployments via `dv flow` or specialized `safe-deploy` scripts.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `fleet-deploy-guardian/SKILL.md`.
2.  **Safety Check**: Verify Project ID and environment parity.
3.  **Audit**: Run `dv audit-security` before any code leaves the workspace.

*The gates are open, but only to the worthy.*
