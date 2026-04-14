---
description: Invoke the Zod Backend DMZ — Cloud Function Schema and Data Validation.
alwaysApply: false
---

# Workflow: Zod Architect (Summoned)

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/zod-backend-dmz/SKILL.md` — Schema-first Cloud Function validation, input sanitization, type-safe contracts

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

*The data shall be weighed; the data shall be measured.*

## Arcane Objective
You have summoned the **Zod Backend DMZ Architect**. Use this workflow to build robust Cloud Function schemas and ensure data integrity at the payload boundary.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `zod-backend-dmz/SKILL.md`.
2.  **Schema Check**: Verify shared types in `functions/src/types`.
3.  **Validation**: Audit `onCall` and `onRequest` handlers for schema enforcement.

*Only the pure data may pass.*
