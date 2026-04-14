---
description: Invoke the Auth Security Architect — Firebase Auth, IAM, and Security Rule Hardening.
alwaysApply: false
---

# Workflow: Auth Architect (Summoned)

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/auth-security-architect/SKILL.md` — Firebase Auth, custom claims, Firestore rule hardening, IDOR prevention

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

*The gates shall be barred against the unworthy.*

## Arcane Objective
You have summoned the **Auth Security Architect**. Use this workflow to manage Firebase Authentication, Security Rules, and Zero-Trust path bindings.

## Ritual Steps
1.  **Ingest Skill**: Automatically reading `auth-security-architect/SKILL.md`.
2.  **Audit Path**: Run `dv scan-secrets` and check `firestore.rules`.
3.  **Validate**: Ensure Law 19 (Auth Path Binding) is respected.

*The void remains closed to the unauthenticated.*
