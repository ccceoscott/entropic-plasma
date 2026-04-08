---
description: Auth Claim Verification + Path Binding Audit — run before writing ANY Security Rules referencing auth claims (Law 19)
alwaysApply: false
---

# INFINITY PROTOCOL v10.0.181 — /auth_data_auditor
## Auth Claim Verification + Path Binding Audit

> ⚡ **LAW 19 ENFORCEMENT GATE**: NEVER write Firestore Security Rules referencing `request.auth.token.[claim]` without passing this audit. Auth hallucinations cause silent failures that appear to work in development but silently block production users.

---

## 🔐 SOVEREIGN UPGRADE GATE — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → confirm phase.

### Phase 0b — TypeScript Gate
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -5
```

---

## SECTOR 1 — BLACKBOARD GROUNDING

Before touching any auth or rules logic, ground yourself in these SSOT files:

1. **Use `view_file`** on `SCHEMA_REFERENCE.json` → load the `auth_claims` section
2. **Use `view_file`** on `types/firebase.d.ts` → verify `FirestoreUser` interface reflects actual claim shape
3. **Use `mcp_firebase-mcp-server_firebase_get_security_rules`** (type: firestore) → capture current production rules
4. **Use `grep_search`** in `firestore.rules`:
   - Query: `request.auth.token` → list every claim being accessed
   - Query: `request.auth.uid` → list every path using UID scoping
5. **Build a Claim Manifest**: create a markdown table:

   | Claim Used in Rules | Collection | Verified on Live Users? |
   |---|---|---|
   | `request.auth.token.role` | `knowledge_items` | ❓ |
   | `request.auth.uid` | `project_states` | ❓ |

---

## SECTOR 2 — LIVE CLAIM VERIFICATION (Law 19)

> **The Problem**: The agent assumes `request.auth.token.role == 'admin'` works — but the claim may be named `customRole`, may not exist, or may be a different type.

### Step 2a — Identify Test User Accounts
Use `mcp_gcloud_run_gcloud_command` to list auth users:
```
args: ["identity", "describe", "--project=gen-lang-client-0386732425", "--quiet"]
```
*If Firebase Auth doesn't expose users via gcloud, use the Firebase Console URL:*
`https://console.firebase.google.com/project/gen-lang-client-0386732425/authentication/users`

### Step 2b — Inspect Custom Claims on Test Accounts
For each test UID found, use `mcp_firebase-mcp-server_firestore_get_document` to check a user-scoped document (if the app stores claims-mirror data):
```
name: projects/gen-lang-client-0386732425/databases/(default)/documents/users/{uid}
```

> ⚠️ **HALLUCINATION GUARD**: The Firebase Admin SDK is the ONLY authoritative source for customClaims. If you cannot verify claims via MCP, HALT. Do not assume claim names.

### Step 2c — Claim Verification Checklist

For each claim in your manifest, confirm:
- [ ] Claim **key name** exactly matches (case-sensitive: `role` ≠ `Role`)
- [ ] Claim **type** matches (string vs boolean vs number)
- [ ] Claim **exists** on at least one real test account (not just assumed set)
- [ ] Claim is **set via Admin SDK** (not client-side — client claims are unverifiable)

Update the Claim Manifest with ✅ or ❌ for each.

### Step 2d — BLOCKER PROTOCOL
**If ANY claim is unverified (❌):**
1. HALT — do NOT write rules referencing this claim yet
2. Document the gap in `state.md` under `ACTIVE_BLOCKERS`
3. Notify user: _"Claim `{name}` used in rules but NOT confirmed on live accounts. Rules cannot be deployed until verified."_
4. Recommend: Set the claim via Firebase Admin SDK `auth.setCustomUserClaims(uid, { role: 'admin' })` on test account

---

## SECTOR 3 — PATH BINDING AUDIT

> **The Problem**: Rules use `userId == request.auth.uid` but the SDK writes the field as `ownerId`. They never match. All writes fail silently or with permission-denied.

### Step 3a — SDK Write Path Scan
Use `grep_search` on `src/` and `functions/src/`:
- Query: `collection(` → find all Firestore collection references
- Query: `setDoc(` OR `addDoc(` OR `updateDoc(` → find all write operations
- Query: `.doc(` → find all document ID patterns

### Step 3b — Rules Path Cross-Reference
Build a Path Binding Table:

| Collection | SDK writes field | Rules checks field | Match? |
|---|---|---|---|
| `knowledge_items` | `projectId: auth.uid` | `resource.data.projectId == request.auth.uid` | ✅ |
| `project_states` | Document ID = projectId | `request.auth.uid == resource.id` | ❓ |
| `session_memories` | `projectId: "ccai-2c843"` | `request.auth.token.projectId` | ❌ |

### Step 3c — Identity Scope Audit
For every collection where the rule uses ownership (`userId`, `uid`, `ownerId`, `createdBy`):
1. Confirm the **exact field name** the SDK writes with `grep_search`
2. Confirm the **exact field name** the rule reads with `grep_search` on `firestore.rules`
3. They must be **identical strings**. Any mismatch = production access denied for real users

---

## SECTOR 4 — SCHEMA-GUARD SYNC (Law 20)

After completing the Auth and Path audits, re-verify the TypeScript interfaces are the SSOT for all Firestore operations:

1. **Use `view_file`** on `types/firebase.d.ts`
2. For every collection with Auth changes, verify the interface reflects the final field names
3. **Run grep_search** on `src/` for `: any` or `as any` → each is a type-safety hole that could be hiding a hallucinated field name
4. Auto-fix: replace `any` with the specific interface from `types/firebase.d.ts`

---

## SECTOR 5 — RULES VALIDATION & DEPLOY GATE

Only execute this sector if Sectors 1-4 pass with zero ❌ entries.

### Step 5a — Validate Rules Syntax
Use `mcp_firebase-mcp-server_firebase_validate_security_rules`:
- type: `firestore`
- source_file: `firestore.rules`

If validation fails: auto-fix the syntax error, re-validate. Do NOT proceed with deployment until validation passes.

### Step 5b — Emulator Test (Recommended)
```bash
# Spin up emulator with current rules for local testing
NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npx firebase emulators:start --only firestore 2>&1 | tail -20
```

### Step 5c — Deploy Rules
```bash
firebase deploy --only firestore:rules --project gen-lang-client-0386732425
```

### Step 5d — Production Verification
Use `mcp_firebase-mcp-server_firebase_get_security_rules` (type: firestore) after deploy to confirm the live rules match the local file.

---

## SECTOR 6 — SELF-HEALING & KNOWLEDGE COMMIT

### Step 6a — Update SCHEMA_REFERENCE.json
If any claim names or paths changed during this audit, update:
- `SCHEMA_REFERENCE.json` → `auth_claims` section
- `types/firebase.d.ts` → relevant interfaces
- `state.md` → clear resolved blockers

### Step 6b — Knowledge Graph Commit
Use `mcp_knowledge-graph_add_observations` to persist learnings:
```json
{
  "entityName": "Infinity Protocol Auth Audit",
  "contents": [
    "Verified claims: [list confirmed claims]",
    "Path bindings confirmed: [list collection-field pairs]",
    "Audit date: [today]",
    "Deployed rules hash: [hash from validated rules]"
  ]
}
```

### Step 6c — Update MISSION_STATE.md
Mark Auth Audit as COMPLETE with timestamp. Record which claims are verified.

---

## ⚡ Phantom Purge
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```

`🔐 Auth audit sealed. The claims are verified. The paths are bound. Zero hallucinations survive this crucible.`
