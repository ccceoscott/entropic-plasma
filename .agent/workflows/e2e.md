---
description: Invoke the Playwright E2E Master — Automated Verification and Production Testing.
alwaysApply: false
---

# Workflow: E2E Master (Summoned)

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


*Through the subagent's eyes, the truth is revealed.*

## Arcane Objective
You have summoned the **Sovereign Playwright E2E Agent**. Use this workflow to write, execute, and troubleshoot E2E tests against local or production environments.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `sovereign-playwright-e2e/SKILL.md`.
2.  **Environment Check**: Verify if port 5173 or 3000 is active.
3.  **Execute**: Run Playwright with Sovereign Workers (`--workers=1`).

*The subagent witnesses all.*
