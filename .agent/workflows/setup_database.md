---
description: Absolute Firestore rule bounding and full database structural mapping
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /setup_database
## Sovereign Firestore Architecture — Schema-Guard Enforced, Zero-Hallucination

> ⚡ **LAW 20 (Schema-Guard)**: NEVER write Firestore queries or document writes without first pulling live schema via Firebase MCP and generating TypeScript interfaces. Save to `types/firebase.d.ts`. All subsequent code uses ONLY these types.

> 🔑 **DATA HALLUCINATION PREVENTION**: Hallucinations occur when agents assume field names, types, or collection structures. Schema-Guard eliminates this by anchoring to live data.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest these skills** via `view_file` on each `SKILL.md` before proceeding:
1. `.agent/skills/data-model-architect/SKILL.md` — Firestore schema governance, indexing, migrations
2. `.agent/skills/database-schema-validator/SKILL.md` — Field type contracts, naming conventions, drift detection

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

## SSOT INGESTION (Before Touching ANY Firestore Code)

Use `view_file` on `MISSION_STATE.md`.
Use `view_file` on `KNOWLEDGE.md`.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists) — check "Zombie Code List" before any writes.
Use `view_file` on `firebase.json` — confirm `firestore` config.
Use `view_file` on `.firebaserc` — confirm project.
Use `view_file` on `firestore.rules` (if exists).

**Grounding Mandate**: NO Firestore code until Schema-Guard (Sector 2) is complete.

---

## SECTOR 1 — Live Database Environment (Two-Key MCP)

### 1a — Database Status (Key 1 — Firebase MCP)
Use `mcp_firebase-mcp-server_firestore_list_databases` with parent `"projects/gen-lang-client-0386732425"`.
Document: database ID, location, type (Native vs Datastore).

### 1b — Live Collection Discovery
Use `mcp_firebase-mcp-server_firestore_list_collections` with parent `"projects/gen-lang-client-0386732425/databases/(default)/documents"`.
List ALL root-level collections. This is the canonical collection registry.

```
Live Collections (from MCP — AUTHORITATIVE):
- [collection1]
- [collection2]
- ...
```

### 1c — Index Inventory (Key 2 — gcloud MCP)
Use `mcp_firebase-mcp-server_firestore_list_indexes` for each major collection.
Document ALL existing composite indexes. Any query without a matching index = runtime failure.

```
Existing Indexes:
- collection: [name] | fields: [f1 ASC, f2 DESC] | status: READY
```

---

## SECTOR 2 — SCHEMA-GUARD (Law 20 — Zero Hallucination)

> **This is the most critical step. NEVER write Firestore code before completing this.**

### 2a — Sample Document Pull (Per Collection)
For each collection discovered in Sector 1, fetch a representative document:
Use `mcp_firebase-mcp-server_firestore_list_documents` with the collection parent.
Pull 1-3 sample documents per collection.

### 2b — Field Type Analysis
For each document, analyze ALL fields:
- String vs Timestamp vs Number vs Boolean vs Reference vs Array vs Map
- Nullable vs required
- `createdAt`/`updatedAt` — are these Strings or Firestore `Timestamp` objects?
- Array fields — what type are the elements?
- Map fields — what is the nested structure?

### 2c — TypeScript Interface Generation (MANDATORY)
Generate TypeScript interfaces for EVERY document type discovered. Save to `types/firebase.d.ts`:

```typescript
// types/firebase.d.ts — AUTO-GENERATED from live MCP schema — DO NOT EDIT MANUALLY
import { Timestamp } from 'firebase/firestore';

export interface UserProfile {
  uid: string;
  email: string;
  displayName: string | null;
  role: 'admin' | 'user' | 'editor'; // verified from Claim-Check
  tier: 'premium' | 'free';
  createdAt: Timestamp; // CONFIRMED: Firestore Timestamp, NOT string
  updatedAt: Timestamp;
  // ... all fields with exact types
}

export interface [CollectionName]Document {
  id: string;
  // ... generated from MCP sample
}
```

**Law**: ALL subsequent Firestore code in this session MUST use ONLY these generated interfaces. Zero `any`. Zero `Record<string, any>`.

### 2d — Schema Mismatch Detection
Compare generated interfaces against any EXISTING TypeScript types in the codebase:
Use `grep_search` for `interface.*Document` or `type.*Schema` in `src/` and `functions/src/`.
Any field that differs between existing types and live MCP data = **SCHEMA MISMATCH**.
Flag and update all divergent type definitions.

---

## SECTOR 3 — Security Rules Architecture

### 3a — Current Rules Audit
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `"firestore"`.
Parse and evaluate every rule:

| Collection | Read Rule | Write Rule | Has Auth Check | Has UID Match | Risk Level |
|---|---|---|---|---|---|
| users | | | | | |
| [others] | | | | | |

Any `allow read, write: if true;` → **P0 CRITICAL**. Mark as BLOCKER.

### 3b — Rule Scaffolding (Based on Schema + Verified Claims from setup_auth)
Create sovereign rules anchored to Schema-Guard findings:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Schema-validated: user documents contain 'uid' field matching auth.uid
    match /users/{userId} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if request.auth != null && request.auth.uid == userId
        && request.resource.data.keys().hasAll(['uid', 'email', 'role', 'createdAt'])
        && request.resource.data.role is string;
    }
    // ... per-collection rules based on actual schema
  }
}
```

### 3c — Rules Validation
Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `"firestore"` and the complete rules source.
Zero errors required before proceeding.

---

## SECTOR 4 — Index Planning (No-Index-No-Query Law)

For every compound query in the codebase:
Use `grep_search` for `.where(` and `.orderBy(` in `src/` and `functions/src/`.
For each compound query found, verify a matching index exists in Sector 1 index inventory.

Missing indexes → create via `mcp_firebase-mcp-server_firestore_create_index`.

Rule: **Never ship a compound query without a pre-created index.** Runtime index errors are avoidable hallucination artifacts.

---

## SECTOR 5 — Transaction Safety Audit

Use `grep_search` for `.update(` in `functions/src/`.
For every `.update()` call on shared resources (counters, balances, order totals):
Verify it is wrapped in `runTransaction`. If not → auto-refactor to use transaction.

```typescript
// CORRECT — transaction safe
await runTransaction(db, async (transaction) => {
  const doc = await transaction.get(ref);
  const current = doc.data()!.count || 0;
  transaction.update(ref, { count: current + 1 });
});
```

---

## SECTOR 6 — Emulator Verification

// turbo
```bash
firebase emulators:start --only firestore --project gen-lang-client-0386732425 &
sleep 5 && echo "emulator started"
```

Run integration test against emulator to verify:
- Read/write operations succeed for authenticated users
- Reads/writes fail for unauthenticated users
- Compound queries work (indexes present)

Kill emulator after verification:
// turbo
```bash
pkill -f "firebase emulators" || true
```

---

## SECTOR 7 — Zombie Code Purge
Use `view_file` on `.agent/CODEBASE_MAP.md` → check Zombie Code List.
Use `grep_search` for any zombie collection names or deprecated fields in active code.
Remove references or add deprecation notices.

---

## Knowledge Base Persistence (R.A.P.S)
Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Live collection registry with document count estimates
- TypeScript interface schemas (key fields only)
- Composite index map
- Schema mismatches found and resolved
- Security rule risk assessment

---

## SECTOR 9 — CODEBASE_MAP.md Update
Update `.agent/CODEBASE_MAP.md` with:
- Updated Firestore schema diagram (Mermaid if possible)
- Confirmed live collections list
- Index registry
- Known zombie collections

---

## SECTOR 10 — MISSION_STATE.md Update
Update `MISSION_STATE.md`:
- Database: CONFIGURED
- Collections: [count] verified
- Schema-Guard: COMPLETE — types/firebase.d.ts generated
- Security Rules: VALIDATED
- Indexes: [count] configured

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Database sovereignty sealed. Schema-Guard active. No hallucinations shall pass.`
