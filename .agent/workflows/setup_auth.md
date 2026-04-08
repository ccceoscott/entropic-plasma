---
description: End-to-end Firebase Authentication infrastructure deployment and scoping
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /setup_auth
## Sovereign Firebase Auth Infrastructure — Zero-Hallucination, Claim-Check Enforced

> ⚡ **LAW 19 (Auth Claim Verification)**: NEVER write Firestore Security Rules containing `request.auth.token.[claim]` without first verifying via Firebase Admin MCP that the claim actually exists on real user accounts. Auth-Mismatch = BLOCKER.

> 🔑 **AUTH-MISMATCH PREVENTION**: The agent MUST verify actual Custom Claims on live accounts before writing any rules or functions that depend on them. Re-prompting loops end here.

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

## SSOT INGESTION (Before Touching ANY Auth Code)

Use `view_file` on `MISSION_STATE.md`.
Use `view_file` on `KNOWLEDGE.md`.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists).
Use `view_file` on `firebase.json` — confirm `auth` is listed in services.
Use `view_file` on `.firebaserc` — confirm correct project.

**Grounding Mandate**: Read all SSOT files first. No auth code written until this step is complete.

---

## SECTOR 1 — Live Auth Environment Audit (Two-Key MCP)

### 1a — Firebase MCP Re-Anchor + Verification (Law 22)
> ⛔ Re-anchor unconditionally FIRST — the MCP drifts to whichever project last called update_environment.

Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

Then confirm: `mcp_firebase-mcp-server_firebase_get_environment` → active project = `gen-lang-client-0386732425`.
Use `mcp_firebase-mcp-server_firebase_get_project` → confirm Auth is enabled.

### 1b — Auth Provider Verification (Key 2 — gcloud MCP)
Use `mcp_gcloud_run_gcloud_command` with args:
`["identity", "describe", "--project=gen-lang-client-0386732425", "--quiet"]`

Document which providers are enabled:
| Provider | Status | Notes |
|---|---|---|
| Email/Password | ✅/❌ | |
| Google Sign-In | ✅/❌ | |
| Anonymous | ✅/❌ | |
| Phone | ✅/❌ | |
| Custom Token | ✅/❌ | |
| MFA/Blocking Functions | ✅/❌ | |

**No assumptions**. If unknown → consult Firebase Console or ask user.

---

## SECTOR 2 — CLAIM-CHECK AUDIT (Law 19 — Zero Hallucination)

> **This is the most critical step. Do NOT skip.**

### 2a — Sample User Discovery
Use `mcp_firebase-mcp-server_firestore_list_documents` on the `users` collection (or equivalent) to identify a test user UID.

### 2b — Live Custom Claims Inspection
Use `mcp_gcloud_run_gcloud_command` with args to call Admin SDK endpoint or inspect via GCloud Identity Toolkit.
Alternatively, use the Firestore MCP to read the user's document and examine any `role`, `claims`, or `permissions` fields.

**Document EVERY actual claim found on real accounts:**
```
Actual Claims on test account [UID]:
- role: [ACTUAL VALUE e.g. 'admin', 'user', 'editor']
- tier: [ACTUAL VALUE e.g. 'premium', 'free']
- emailVerified: [true/false]
```

### 2c — Auth-Mismatch Check
Before writing ANY Security Rule:
- Compare proposed `request.auth.token.[claim]` against actual claims list above
- If the claim does NOT exist on real accounts → **FLAG AUTH-MISMATCH** → STOP
- If the claim EXISTS → proceed with confidence

**If Auth-Mismatch detected**: Document the gap. Ask user: "Do you want me to create a Cloud Function to SET this claim, or change the rule to use an existing claim?"

---

## SECTOR 3 — UID-Path Binding Verification

### 3a — Firestore Path Audit
Use `mcp_firebase-mcp-server_firestore_list_collections` to list root collections.
For each user-owned collection, verify document path includes `{userId}`.

Expected safe pattern:
```
/users/{userId} → document owned by user
/profiles/{userId} → document owned by user
/orders/{userId}/items/{orderId} → subcollection owned by user
```

Unsafe patterns (flag immediately):
- Global write paths without `request.auth.uid == userId`
- Collections queryable without auth

### 3b — Rules UID Match Verification
Fetch current rules via `mcp_firebase-mcp-server_firebase_get_security_rules` with type `"firestore"`.
For every user-owned collection rule: verify `request.auth.uid == [userId variable]` is present.
Any rule allowing writes WITHOUT uid match → **P0 SECURITY GAP**. Mark as BLOCKER.

---

## SECTOR 4 — Auth Infrastructure Setup

Only proceed here if Sectors 1-3 are clean.

### 4a — Auth Providers (if setting up new)
Use `mcp_firebase-mcp-server_firebase_init` with appropriate auth provider config based on Sector 1 findings.

### 4b — Session Cookie / Token Configuration
Use `view_file` on any existing `authContext.tsx` or `useAuth.ts` to understand current token handling.
Verify:
- `getIdToken(true)` is used for forced refresh (not stale tokens)
- Token errors surface user-friendly messaging
- `onAuthStateChanged` properly cleaned up in `useEffect` return

### 4c — Custom Claims Cloud Function (if needed from 2c)
If Auth-Mismatch was found and user confirmed claim should be set via Function:
Create Cloud Function skeleton with correct structure:
```typescript
// functions/src/auth/setCustomClaims.ts
import { getAuth } from 'firebase-admin/auth';
export const onUserCreate = functions.auth.user().onCreate(async (user) => {
  await getAuth().setCustomUserClaims(user.uid, {
    role: 'user', // default claim — verified against actual claim schema
  });
});
```

---

## SECTOR 5 — Blocking Functions Audit (if applicable)

If Identity Platform is enabled:
Use `mcp_firebase-mcp-server_functions_list_functions` → find any `beforeSignIn` or `beforeCreate` functions.
Verify:
- Blocking functions don't silently fail (they must throw `functions.auth.HttpsError` on reject)
- MFA requirements are correctly gated

---

## SECTOR 6 — Auth Security Rules Hardening

Using findings from Sectors 2 and 3, write final rules:

```
match /users/{userId} {
  allow read, write: if request.auth != null && request.auth.uid == userId;
}
match /admin/{document} {
  // Only use claims VERIFIED to exist in Sector 2
  allow read, write: if request.auth != null && request.auth.token.role == 'admin';
}
```

Validate via `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `"firestore"`.

---

## SECTOR 7 — E2E Auth Verification (Browser Witness — Law)

Spawn browser subagent to:
1. Navigate to the app's login page
2. Attempt sign-in with test credentials
3. Screenshot: successful auth state (user menu visible, UID displayed in DevTools)
4. Attempt to access a protected route WITHOUT auth → confirm redirect to login
5. Attempt unauthorized Firestore write → confirm 403/permission-denied in console
6. Screenshot: all three states as evidence

Save recording. This is the Auth Browser Witness. **No auth work is "done" without this.**

---

## SECTOR 8 — TypeScript Auth Types
After all auth logic is written:
Use `grep_search` for `: any` in all auth-related files.
Eradicate every instance. Auth types must be explicit:
```typescript
// types/auth.d.ts — generated from verified claim schema
interface AuthUser {
  uid: string;
  email: string | null;
  role: 'admin' | 'user' | 'editor'; // from Sector 2 verified claims
  tier: 'premium' | 'free';
  emailVerified: boolean;
}
```

---

## SECTOR 9 — Knowledge Graph Persistence (MCP)
Use `mcp_knowledge-graph_add_observations` to record:
- Verified Auth providers for this project
- Actual Custom Claims structure (not assumed)
- UID-path bindings confirmed
- Any Auth-Mismatches found and resolution taken

---

## SECTOR 10 — MISSION_STATE.md Update
Update `MISSION_STATE.md`:
- Auth status: CONFIGURED
- Providers enabled: [list from Sector 1]
- Custom claims schema: [from Sector 2]
- Browser witness: CONFIRMED/PENDING

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Auth infrastructure sealed. Zero hallucinations authorized.`
