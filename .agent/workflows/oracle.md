---
description: Invoke the Sovereign Research Oracle — Pattern Recognition and Recursive Skill Improvement.
alwaysApply: false
---

# Workflow: Research Oracle (Summoned)

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/sovereign-research-oracle/SKILL.md` — Knowledge ingestion, pattern recognition, recursive skill improvement

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

*The knowledge of the ancients is reborn.*

## Arcane Objective
You have summoned the **Sovereign Research Oracle**. Use this workflow to perform deep data mining on the brain, identify architectural drift, or improve system rules.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `sovereign-research-oracle/SKILL.md`.
2.  **Oracle Scan**: Run `node scripts/research-oracle.cjs` to extract KI stats.
3.  **Deduction**: Update `RESEARCH_LOG.md` with new Wins and Losses.

*The pattern is seen; the protocol evolves.*
