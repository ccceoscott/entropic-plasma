---
description: Knowledge drift detection — audit active project against official docs and backup findings to Firebase Storage
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /knowledge_audit
## Knowledge Drift Detection & Firebase Brain Sync — MCP-First

> ⚡ **MANDATE**: Architecture decisions must be grounded in current official documentation, not memory. This workflow compares implementation against live docs and persists findings.

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

---

## PHASE 1 — Current Implementation Snapshot

### 1a — Technology Stack Inventory
Use `view_file` on `package.json` to extract all dependencies and versions.
Use `view_file` on `functions/package.json` for server-side stack.
Record:
- Firebase SDK version (client)
- firebase-admin version (server)
- firebase-functions version
- Next.js version
- Framer Motion version
- TypeScript version

### 1b — Knowledge Graph Current State (MCP)
Use `mcp_knowledge-graph_read_graph` — full entity dump.
Identify all KIs currently stored. Note timestamps and freshness.

### 1c — KNOWLEDGE.md State
Use `view_file` on `KNOWLEDGE.md` — read architectural decisions section.
Note any decisions that reference external APIs or library behavior.

---

## PHASE 2 — Official Documentation Cross-Reference (MCP)

> ⚠️ **LAW**: Max 2-3 keyword tokens per search. Long queries hang the MCP.

### 2a — Firebase SDK Drift Check
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Firebase Web SDK v10"`.
Compare documented API surface against current `import` patterns in `src/**/*.ts`.

### 2b — Cloud Functions Node 22 Check
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Cloud Functions Node 22"`.
Confirm: `"engines": { "node": "22" }` in functions/package.json.
Verify no deprecated v1 `functions.https.onRequest` patterns still in use (v2 `onRequest` preferred).

### 2c — Firestore Rules Best Practices
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Firestore security rules"`.
Compare with current `firestore.rules` — identify any deprecated rule syntax.

### 2d — Next.js App Router Check
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Next.js App Router"`.
Confirm: no Pages Router patterns (`/pages/api/`) in `src/`.
Confirm: `'use client'` directives are appropriately scoped.

### 2e — Framer Motion LazyMotion
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Framer Motion LazyMotion"`.
Confirm: all animation components use `LazyMotion + domAnimation + m.` pattern.

### 2f — GCP Secret Manager
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Secret Manager"`.
Confirm secret access pattern in functions matches `defineSecret()` v2 pattern.

---

## PHASE 3 — Drift Analysis

For each area audited in Phase 2:

| Area | Current Pattern | Official Recommended | Drift Level | Action |
|---|---|---|---|---|
| Firebase SDK | | | None/Minor/Major | |
| CF Node Version | | | | |
| CF API Version | | | | |
| Firestore Rules | | | | |
| Next.js Patterns | | | | |
| Framer Motion | | | | |
| Secret Manager | | | | |

**Drift Severity Classification:**
- **None**: Implementation matches current docs
- **Minor**: Compatible but not latest pattern (P3 — schedule for next major upgrade)
- **Major**: Deprecated or breaking pattern detected (P1 — fix in this session)

---

## PHASE 4 — Auto-Remediation of Major Drift

For each **Major** drift item:
1. Use `grep_search` to find all instances in the codebase
2. Apply fix using file edit tools
3. Run TypeScript check after each fix:
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
4. Log: `🔧 [DRIFT-FIX] [area]: [old pattern] → [new pattern]`

For each **Minor** drift → document in `KNOWLEDGE.md` under "Deferred Upgrades".

---

## PHASE 5 — Firebase Brain Backup

### 5a — Audit Report Generation
Create structured audit report as markdown content.

### 5b — Firebase Storage Backup (MCP)
Use `mcp_gcloud_run_gcloud_command` with args to upload to Storage:
```
["storage", "cp", "/tmp/knowledge_audit.md", 
 "gs://gen-lang-client-0386732425.firebasestorage.app/knowledge_audits/[YYYY-MM-DD].md",
 "--quiet"]
```

### 5c — Firestore Record (MCP)
Use `mcp_firebase-mcp-server_firestore_add_document` to record the audit run:
```json
{
  "parent": "projects/gen-lang-client-0386732425/databases/(default)/documents",
  "collectionId": "knowledge_audits",
  "document": {
    "fields": {
      "runDate": { "stringValue": "[ISO timestamp]" },
      "phase": { "stringValue": "[current phase]" },
      "driftItems": { "integerValue": "[count]" },
      "majorDrift": { "integerValue": "[count]" },
      "autoFixed": { "integerValue": "[count]" }
    }
  }
}
```

---

## PHASE 6 — Knowledge Graph Update (MCP)

### 6a — New Entity Creation
For any new pattern discovered → use `mcp_knowledge-graph_create_entities`:
- Entity name: `"[Technology] Pattern [Year]"`
- Entity type: `"ArchitecturalPattern"`
- Observations: documented pattern, source URL, date confirmed

### 6b — Existing Entity Update
For each existing KI with drift detected → use `mcp_knowledge-graph_add_observations`:
- Record: drift found, version difference, fix applied

### 6c — Deprecation Records
For each deprecated pattern found and fixed → add as observation to warn future sessions.

---

## PHASE 7 — KNOWLEDGE.md Update

Use `view_file` on `KNOWLEDGE.md`, then apply updates:
- Update `Last Knowledge Audit:` timestamp
- Add new confirmed patterns under "Established Patterns"
- Add deferred minor drift under "Deferred Upgrades"
- Remove any entries that are now resolved

---

## PHASE 8 — Final Verification

### 8a — TypeScript Final Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```

### 8b — MISSION_STATE Update
Bump phase. Log: `Knowledge audit: [N] areas checked, [X] major drift fixed, [Y] minor deferred.`

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Knowledge audit complete. Brain backed up.`
