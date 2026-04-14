---
description: Invoke the Email Delivery Architect — Transactional Templates and Resend/SendGrid Integration.
alwaysApply: false
---

# Workflow: Email Architect (Summoned)


## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/email-delivery-architect/SKILL.md` — Transactional email, SPF/DKIM/DMARC, Resend/SendGrid, live delivery tests

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


*The word shall fly across the silicon winds.*

## Arcane Objective
You have summoned the **Email Delivery Architect**. Use this workflow to design, test, and deploy transactional email templates.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `email-delivery-architect/SKILL.md`.
2.  **Template Audit**: Check `emails/` directory for structure and React components.
3.  **Validate**: Test delivery paths and compliance headers.

*The message is cast into the void.*
