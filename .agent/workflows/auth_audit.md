---
description: Authentication Audit — Verification of Auth Claims, IDOR testing, and Security Rule bindings.
alwaysApply: false
---

# 🔐 /auth_audit — The Sovereign Gatekeeper (v12.0)

⚡ **MANDATE**: Execute this ritual to perform Auth Claim verification, UID path-binding checks, and Zero-Trust Firestore Security Rule auditing. NEVER write Firestore Security Rules containing `request.auth.token.[claim]` without first verifying the claim actually exists on real user accounts.

## 🧠 Skill Ingestion
**Automatically ingest this Domain Bundle**:
1. `!shield` — Sovereign Shield Domain (Security, Auth, Firestore Rules)

---

## 🔍 THE VERIFICATION PATH
1. **Live Auth & Claim Audit**: Use Firebase MCP to discover users and verify injected custom claims (e.g., `role: 'admin'`, `tier: 'pro'`).
2. **Path Binding Scan**: Ensure all user-owned data is strictly bound by `{userId}` in the database path (e.g., `/users/{userId}/...` or `orders` where `userId` matches the token).
3. **IDOR & Security Rule Check**: Verify that strict `auth.uid == resource.data.userId` assertions exist across API routes, Cloud Functions, AND Firebase Security Rules.
4. **Admin Route Verification**: Escalate and confirm all Admin-scoped Cloud Functions assert `context.auth.token.admin === true`.

Declare: `✅ [AUTH AUDIT COMPLETE] | Claims verified. Path bindings secured. Zero leakage authorized.`
