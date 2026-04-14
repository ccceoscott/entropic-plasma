---
description: Invoke the Zustand Firebase Sync Master — Global State and Real-time Persistence.
alwaysApply: false
---

# Workflow: State Master (Summoned)

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/zustand-firebase-sync/SKILL.md` — Zustand store architecture, Firestore listeners, optimistic updates, persistence

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

*The memory of the machine is eternal.*

## Arcane Objective
You have summoned the **Zustand Firebase Sync Master**. Use this workflow to architect global state slices and connect them to real-time Firebase listeners.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `zustand-firebase-sync/SKILL.md`.
2.  **Store Audit**: Check `src/store` for `persist` and `devtools` middleware.
3.  **Sync Check**: Verify `onSnapshot` lifecycle management.

*The state is preserved in the silicon heart.*
