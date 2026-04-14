---
description: Invoke the Aesthetic Auditor — Visual Integrity, Dark Mode, and FOUC Detection.
alwaysApply: false
---

# Workflow: Aesthetic Auditor (Summoned)

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/sovereign-aesthetic-auditor/SKILL.md` — FOUC detection, dark mode integrity, glassmorphism compliance

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

*Beauty is the final law of the protocol.*

## Arcane Objective
You have summoned the **Sovereign Aesthetic Auditor**. Use this workflow to audit UI code for adherence to the Liquid Glass v10 standards.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `sovereign-aesthetic-auditor/SKILL.md`.
2.  **Audit**: Run `dv aesthetic` and generate a drift report.
3.  **Visual Witness**: Capture screenshots via the browser homunculus.

*The eye sees what the mortal misses.*
