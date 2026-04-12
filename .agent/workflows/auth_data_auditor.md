---
description: Auth Claim Verification + Path Binding Audit — run before writing ANY Security Rules referencing auth claims (Law 19)
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /auth_data_auditor
## Sovereign Auth-Path Integrity Audit (E2E)

> ⚡ **LAW 19 (Auth Claim Verification)**: NEVER write Firestore Security Rules containing `request.auth.token.[claim]` without first verifying via Firebase Admin MCP that the claim actually exists on real user accounts. Auth-Mismatch = BLOCKER.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` before proceeding:
1. `.agent/skills/auth-security-architect/SKILL.md` — Custom claims forensics, IDOR prevention, zero-trust rule auditing

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
If stale → auto-upgrade (0b). If current → confirm (0c).

### Phase 0b — Auto-Upgrade
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run.

---

## SECTOR 1 — Live Auth Provider Audit (MCP)

Use `mcp_firebase-mcp-server_firebase_get_environment` → confirm active project.
Use `mcp_firebase-mcp-server_firebase_get_project` → confirm Auth is enabled.

---

## SECTOR 2 — Custom Claim Forensic Audit (Law 19)

> **MANDATE**: You MUST pull a real user record via MCP to verify claim structure.

### 2a — Sample User Discovery
Use `mcp_firebase-mcp-server_firestore_list_documents` on `users` collection → pick recent UID.

### 2b — Claim Injection Check
Check `functions/src` for `setCustomUserClaims` calls.
Document defined claims:
- role: [e.g. 'admin']
- tier: [e.g. 'pro']

### 2c — Live Verification
If possible, use `mcp_gcloud_run_gcloud_command` to inspect a test user's actual token claims via Identity Toolkit API.
`["identity", "describe", "--project=...", "--uid=..."]`

---

## SECTOR 3 — UID Path Binding Verification

### 3a — Collection Discovery
Use `mcp_firebase-mcp-server_firestore_list_collections` → list all root collections.

### 3b — User-Owned Path Audit
Verify all user-specific data is bound by `{userId}` in path.
Example: `/users/{userId}/...` or `/profiles/{userId}`.

---

## SECTOR 4 — Security Rules Audit

Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `"firestore"`.
Verify every rule referencing `auth.token` matches verified claims from Sector 2.

---

## SECTOR 5 — MISSION_STATE.md Update

Update `MISSION_STATE.md`:
- Auth Claims Verified: ✅/❌
- Path Bindings Checked: ✅/❌
- Result: [PASS/FAIL]

`🧹 Auth-Path integrity verified. Zero leakage authorized.`
