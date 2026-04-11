---
description: Ironclad Pre-Launch Audit — Two-Key MCP grounding, Schema Mismatch, Security Gap analysis, and Browser witness verification
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /preflight
## Ironclad Pre-Launch Audit — Deterministic Grounding, Zero Hallucination

> ⚡ **MANDATE**: This workflow NEVER writes code. It produces `pre_flight_audit.md` and awaits explicit user approval before any fix executes. The browser is the witness. Live MCP data is the truth.

> ⚠️ **TWO-KEY LAW**: Every verification pulls from two independent sources — Firebase MCP (raw infra) AND Remote Logic MCP (business schema). If they disagree, CIRCUIT BREAKER fires. Never guess.

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

## GROUNDING STEP — SSOT Ingestion (Before ALL Else)

> **LAW**: The agent MUST complete all of these reads before any analysis. No shortcuts.

### G1 — Local SSOT Files
Use `view_file` on `MISSION_STATE.md` — absorb fully.
Use `view_file` on `KNOWLEDGE.md` — absorb fully.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists) — note Zombie Code List.
Use `view_file` on `firestore.rules` — full rules source.
Use `view_file` on `firestore.indexes.json` — full index definitions.
Use `view_file` on `firebase.json` — deployment configuration.

### G2 — Infrastructure Grounding
Use `mcp_firebase-mcp-server_firebase_get_environment` → project ID must be `gen-lang-client-0386732425`.
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `firestore` → live production rules.
Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `storage` → live storage rules.
Use `mcp_firebase-mcp-server_functions_list_functions` → ALL deployed functions, regions, triggers.
Use `mcp_firebase-mcp-server_firestore_list_collections` with parent `projects/gen-lang-client-0386732425/databases/(default)/documents` → live collection list.

### G3 — Remote Logic MCP Key 2 (Business Schema)
Use `mcp_firebase-mcp-server_developerknowledge_search_documents` with query `"Firestore schema"` → 2-3 keyword tokens max.
Use `mcp_gcloud_run_gcloud_command` with args `["functions", "list", "--project=gen-lang-client-0386732425", "--format=json(name,status,runtime)", "--quiet"]` → confirm deployed function runtime is Node 22.

### G4 — Two-Key Reconciliation
Compare G2 (live Firebase) vs G3 (expected schema):
- Function list mismatch → flag as CIRCUIT BREAKER
- Collection mismatch → flag as CIRCUIT BREAKER
- Runtime not Node 22 → flag as BLOCKER

---

## STEP 1 — Schema Mismatch Analysis

### 1a — Code vs Live Firestore Schema
Use `grep_search` for `.set(` and `.update(` and `.add(` in `functions/src/**/*.ts` and `src/**/*.ts`.
For each Firestore write operation, extract the field names being written.
Cross-reference against `G2 collection list` and live documents.

**Schema Mismatch Table** (populate in audit artifact):

| File:Line | Collection | Fields Written in Code | Live Schema Has Field? | Severity |
|---|---|---|---|---|
| | | | Yes/No | BLOCKER/WARNING |

Any `No` → **BLOCKER**: field written in code does not exist in production schema.

### 1b — TypeScript Interface vs Live Schema
Use `grep_search` for `interface` and `type` declarations in `src/types/**/*.ts,functions/src/types/**/*.ts`.
For each interface that maps to a Firestore collection → verify every field exists in the live schema from G2.
Mismatched fields → **BLOCKER**.

---

## STEP 2 — Security Gap Analysis

### 2a — Cloud Functions Auth Check
Use `grep_search` for `export const` in `functions/src/**/*.ts`.
For each exported HTTP function:
- Does it check `request.auth` or validate a token? 
- Use `grep_search` for the function name to find its auth check
- No auth check → **BLOCKER**: "Function [name] has no auth validation"

### 2b — Firestore Rules Security Gaps
Analyze live rules from G2:

| Pattern Found in Rules | Severity | Notes |
|---|---|---|
| `allow read, write: if true` | BLOCKER | Open write access |
| `allow write: if request.auth != null` without uid check | BLOCKER | Missing ownership |
| `allow read: if request.auth != null` | WARNING | Missing ownership (read) |
| Missing `request.time` TTL guard on writes | WARNING | No time-bounded access |

Use `grep_search` on `firestore.rules` for each pattern:
- `if true` → BLOCKER
- `allow write: if request.auth != null` without subsequent uid comparison → BLOCKER

### 2c — Storage Rules Security Gaps
Same analysis for storage rules.

### 2d — Secret Exposure Check (MCP-first)
Use `grep_search` for `AIza` and `sk-` and `apiKey:\s*['"]` across `src/**,functions/src/**`.
Any match → **BLOCKER**.

---

## STEP 3 — Composite Index Audit

### 3a — Query vs Index Cross-Reference
Use `grep_search` for `.where(` in `src/**/*.ts,functions/src/**/*.ts`.
For each query with 2+ `.where()` clauses → extract field names and order-by field.
Cross-reference against `firestore.indexes.json` (G1) and live indexes from:
Use `mcp_firebase-mcp-server_firestore_list_indexes` for each relevant collection.

**Index Audit Table**:

| File:Line | Collection | Fields Queried | Composite Index Exists? | Status |
|---|---|---|---|---|
| | | | Yes/No | BLOCKER/OK |

Any `No` → **BLOCKER**: "Query at [file:line] will fail in production — missing composite index for [fields]"

---

## STEP 4 — Function Runtime & Deployment Health

### 4a — Runtime Verification
From G3, confirm ALL functions use `"runtime": "nodejs22"`.
Any function on `nodejs18` or older → **BLOCKER**: must migrate.

### 4b — Error Rate Check (MCP)
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "ERROR"` and `page_size: 50`.
For each error:
- Classify: auth failure / crash / timeout / schema mismatch
- Error rate > 5% on any function → **BLOCKER**
- Error rate 1-5% → **WARNING**

---

## STEP 5 — Live Browser Verification (The Witness)

### 5a — Dev Server Start
// turbo
```bash
lsof -ti:3000 2>/dev/null | head -3 || echo "no server"
```
If not running → `NODE_OPTIONS=--max-old-space-size=4096 npm run dev &` wait 8 seconds.

### 5b — Unauthenticated Protected Route Test
Use `browser_subagent` to:
1. Open `http://localhost:3000` in a fresh incognito context
2. Navigate directly to `/dashboard` (or equivalent protected route)
3. Record what happens:
   - Redirected to login → ✅ PASS
   - 401/403 response → ✅ PASS
   - Content loads without auth → ❌ **BLOCKER: unauthenticated access to protected route**
4. Screenshot the result
5. Report console output

### 5c — Auth Flow Smoke Test
Use `browser_subagent` to:
1. Navigate to login page
2. Attempt login with invalid credentials
3. Verify: error message displays (not blank screen, not crash)
4. Screenshot evidence

### 5d — Console Error Scan Post-Load (MCP)
Use `mcp_chrome-devtools_list_console_messages` with types `["error", "warn"]` after page load.
Any uncaught errors → **BLOCKER** unless known/acceptable.

---

## STEP 6 — Pre-Flight Audit Report Assembly

### 6a — Generate `pre_flight_audit.md`
Create comprehensive audit artifact with ALL findings organized as:

```markdown
# Pre-Flight Audit — [Project Name] — Phase [N]
## Audit Date: [ISO timestamp]
## Auditor: Zoltan / Infinity Protocol v10.0

---

## ⛔ BLOCKERS (Must Resolve Before Launch)
| ID | Category | File:Line | Description | Recommended Fix |
|---|---|---|---|---|

---

## ⚠️ WARNINGS (Technical Debt — Resolve Before Next Major Release)
| ID | Category | File:Line | Description | Recommended Fix |
|---|---|---|---|---|

---

## ✅ PASSING CHECKS
| Category | Status | Evidence |
|---|---|---|

---

## 📊 Summary
- Total Blockers: [N]
- Total Warnings: [N]
- Browser Verification: PASS/FAIL
- Schema Mismatches: [N]
- Security Gaps: [N]
- Index Gaps: [N]

## Next Step
Awaiting THUMBS_UP on this artifact before executing ANY fixes.
```

### 6b — Store in Firestore (MCP)
Use `mcp_firebase-mcp-server_firestore_add_document` to save audit record:
```json
{
  "parent": "projects/gen-lang-client-0386732425/databases/(default)/documents",
  "collectionId": "preflight_audits",
  "document": {
    "fields": {
      "auditDate": { "stringValue": "[ISO timestamp]" },
      "phase": { "stringValue": "[N]" },
      "blockers": { "integerValue": "[count]" },
      "warnings": { "integerValue": "[count]" },
      "browserVerification": { "stringValue": "PASS|FAIL" }
    }
  }
}
```

---

## STEP 7 — Await Approval

> **⛔ HARD STOP**: Do NOT proceed with any fixes until user provides explicit approval of `pre_flight_audit.md`.

Output:
```
*The grimoire has spoken. [N] blockers, [N] warnings discovered through the Two-Key oracle.*

📋 **`pre_flight_audit.md` is ready for your review.**

I am awaiting your THUMBS_UP before touching a single line of code.

**BLOCKER Summary**:
[list each blocker ID + one-line description]

**WARNING Summary**:
[list each warning ID + one-line description]

*Review carefully, mortal. Your launch fate rests on this document.*
```

---

## POST-APPROVAL: Atomic Fix Protocol

> **Only run this section after user provides explicit approval.**

For each BLOCKER (Warnings deferred):

**For each fix cycle** (repeat per blocker):
1. Apply minimal surgical fix to the identified file
2. Verify fix via TypeScript check:
   ```bash
   cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -5
   ```
3. If security rule fix → validate via MCP:
   Use `mcp_firebase-mcp-server_firebase_validate_security_rules`
4. If index fix → deploy index:
   ```bash
   firebase deploy --only firestore:indexes --project gen-lang-client-0386732425 --quiet 2>&1 | tail -5
   ```
5. Re-test the specific vulnerability via `browser_subagent`
6. Update `pre_flight_audit.md`: mark blocker as RESOLVED
7. Update `state.md` if blackboard exists: mark RESOLVED

After all blockers resolved:
// turbo
```bash
git add -A && git commit -m "fix: preflight blockers resolved — Phase [N] launch hardening"
```

---

## Knowledge Base Persistence (R.A.P.S)

Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Blocker patterns found (for cross-session learning)
- Schema mismatches discovered (to build CODEBASE_MAP.md)
- Security gaps eradicated
- Audit outcome

Update `MISSION_STATE.md`: Add "Last Pre-Flight Audit: [date] — [N] blockers resolved".

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Pre-flight audit sealed. The runway is clear — or it isn't. You've been warned.`
