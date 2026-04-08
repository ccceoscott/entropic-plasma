---
description: Sovereign Brain Audit — Full effectiveness verification of the Remote Brain MCP system (workspace connectivity, data transfer, memory, security, self-heal, rule compliance, optimization, and all sub-systems)
---

# /brain_audit — Sovereign Brain Audit Protocol

**Triggers**: `/brain_audit`, or when the user says "audit the brain", "brain health check", "verify memory system"

**Purpose**: Guarantee full functional integrity of the Infinity Protocol Remote Brain MCP Architecture.
No gate is skippable. Each domain is independently verified. Flag all anomalies — auto-heal where possible, escalate when not.

---

## PRE-FLIGHT

// turbo
1. Read `MISSION_STATE.md` to confirm current phase and last sealed state.
// turbo
2. Confirm Firebase project ID: `node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"`
3. Record the project ID. Every step below MUST operate against this project only. NEVER cross-contaminate.

---

## DOMAIN 1 — WORKSPACE CONNECTIVITY

**Goal**: Verify every MCP server and remote endpoint is reachable and responding.

// turbo
4. Run `mcp_firebase-mcp-server_firebase_get_environment` — verify: authenticated user, active project ID, billing enabled.
5. Run `mcp_gcloud_run_gcloud_command` with args `["run", "services", "list", "--platform=managed", "--region=us-central1", "--format=json(status.address.url,metadata.name,status.conditions)", "--quiet"]` — locate `mcpserver-*` service, verify URL and status condition `Ready = True`.
6. Attempt a direct health check of the Brain MCP endpoint by running `mcp_brain-mcp_brave_web_search` with a trivial query (e.g. "test"). If it fails: diagnose Cloud Run logs immediately (see Domain 7).
7. Run `mcp_firebase-mcp-server_functions_list_functions` and compare result count against the known deployed count (currently 19). If fewer: log all missing function names as CRITICAL findings.
8. Run `mcp_gcloud_run_gcloud_command` with args `["functions", "list", "--gen2", "--format=json(name,state,updateTime)", "--project=<PROJECT_ID>", "--quiet"]` to enumerate function states. Any function NOT in `ACTIVE` state is a CRITICAL finding.

**Self-Heal**: If any Cloud Run service is `NOT_READY`, run `mcp_gcloud_run_gcloud_command` with args `["run", "revisions", "list", "--service=mcpserver-*", "--region=us-central1", "--quiet"]` to identify the failing revision and check recent deploy logs.

---

## DOMAIN 2 — REMOTE BRAIN MCP SERVER HEALTH

**Goal**: Verify per-session McpServer+transport architecture is operating without errors.

9. Run `mcp_firebase-mcp-server_functions_get_logs` with `function_names: ["brainMcpHandler"]`, `min_severity: "ERROR"`, `page_size: 20`. If ANY error contains "Server not initialized", "Internal MCP error", or "sessionStore" — this is a CRITICAL regression requiring immediate rollback to Phase 182.2.
10. Run `mcp_firebase-mcp-server_functions_get_logs` with `function_names: ["brainMcpHandler"]`, `min_severity: "INFO"`, `page_size: 10`. Confirm logs show: session initialization messages and tool invocations. If only warnings: flag as degraded.
11. **AUTOCONNECT SELF-HEAL GATE**: Before invoking tools, validate Brain MCP is alive:
    - Call `mcp_brain-mcp_upsert_project_state` with `projectId: "brain-audit-heartbeat", phase: 1, status: "ACTIVE"`.
    - **Success** → `✅ Brain MCP ONLINE — proceeding with tool verification.`
    - **Connection error / SSE closed** → **AUTOCONNECT PROTOCOL**:
      a. Check Cloud Run health: `curl -s --max-time 10 "https://mcpserver-g5pod66w5a-uc.a.run.app/health"` — if returns `{"healthy":true}` → transport stale, retry tool call immediately.
      b. If retry succeeds → `✅ Brain MCP RECONNECTED (autoconnect).` Continue.
      c. If retry fails → display **Brain MCP Repair Prompt** (do NOT skip Domain 2 silently):
      ```
      ══════════════════════════════════════════════
      🔴 BRAIN MCP OFFLINE — AUDIT CANNOT COMPLETE DOMAIN 2
      ══════════════════════════════════════════════
      The Remote Brain SSE transport is down.

      OPTION 1 — IDE Restart (recommended):
        Restart Gemini IDE → reconnect is automatic.

      OPTION 2 — Force Cloud Run redeploy:
        firebase deploy --only functions --project gen-lang-client-0386732425

      OPTION 3 — Mark Domain 2 CRITICAL and continue audit of other domains:
        Type "continue brain offline" to skip Domain 2 for now.
      ══════════════════════════════════════════════
      ```
      Log Domain 2 as CRITICAL in final report. Continue to Domain 3 if user says "continue brain offline".
12. Invoke each of the 6 Brain MCP tools individually and record pass/fail:
    - `mcp_brain-mcp_brave_web_search` with `query: "MCP protocol test"` → expect results array
    - `mcp_brain-mcp_save_session_memory` with minimal valid payload → expect `{ status: "OK" }`
    - `mcp_brain-mcp_search_knowledge` with `query: "test", projectId: "<PROJECT_ID>"` → expect results or empty array
    - `mcp_brain-mcp_upsert_project_state` with `projectId: "brain-audit-test", phase: 1` → expect success
    - `mcp_brain-mcp_firebase_developer_knowledge` with `query: "Firestore"` → expect doc results
    - `mcp_brain-mcp_google_developer_knowledge` with `query: "Cloud Run"` → expect doc results
    - Record latency for each call.

**Self-Heal**: If `save_session_memory` returns HTTP 429: flag P1 Gemini quota breach. Log recommendation to migrate to Vertex AI ADC billing.

---

## DOMAIN 3 — DATA TRANSFER & STORAGE INTEGRITY

**Goal**: Verify all Firestore collections are readable/writable with correct schema.

12. Run `mcp_firebase-mcp-server_firestore_list_collections` on `projects/<PROJECT_ID>/databases/(default)/documents` — list all top-level collections present.
13. Verify these REQUIRED collections are present: `knowledge_items`, `session_memories`, `project_states`, `activity`, `health`. If any is missing: flag as CRITICAL (data loss or schema regression).
14. Run `mcp_firebase-mcp-server_firestore_list_documents` on `session_memories` with `pageSize: 3` — verify documents exist and contain fields: `projectId`, `summary`, `phase`, `updatedAt`.
15. Run `mcp_firebase-mcp-server_firestore_list_documents` on `knowledge_items` with `pageSize: 3` — verify documents contain: `title`, `summary`, `taxonomy`, `embedding` (null or vector), `createdAt`.
16. Run `mcp_firebase-mcp-server_firestore_query_collection` on `project_states` with filter `field: "status", op: "EQUAL", string_value: "ACTIVE"` — verify at least 1 active project state exists.
17. Run `mcp_firebase-mcp-server_firestore_list_documents` on `health/knowledge` — verify last drift scan timestamp is within 7 days. If older: flag as STALE and recommend `/brain_audit` or manual `scanKnowledgeDrift` trigger.
18. Verify `knowledge_items` collection has at least 1 document with `embedding` that is NOT null — confirms the vector pipeline is writing embeddings.

**Self-Heal**: If `health` collection is missing: it will be auto-populated on next `scanKnowledgeDrift` trigger. Recommend manually invoking the health Cloud Function via MCP hub.

---

## DOMAIN 4 — VECTOR SEARCH & EMBEDDING PIPELINE

**Goal**: Confirm semantic search is functioning with live embedding generation.

19. Run `mcp_brain-mcp_search_knowledge` with `mode: "semantic"`, `query: "TypeScript error fix"`, `projectId: "<PROJECT_ID>"` — verify:
    - Response contains `results` array (not empty or error)
    - `mode` in response = `"semantic"` (not `"keyword"` fallback — fallback means embedding generation failed)
    - At least 1 result has `relevanceScore > 0.5`
20. If semantic mode fell back to keyword: check `mcp_firebase-mcp-server_functions_get_logs` for `generateVectorsBatch` errors. Likely cause: `GEMINI_API_KEY` not accessible or quota exceeded.
21. Run `mcp_brain-mcp_search_knowledge` with `mode: "hybrid"`, `globalSearch: true`, `query: "protocol compliance"` — verify linked resonance items are returned.
22. Verify temporal decay is working: check that knowledge items older than 90 days appear with lower `relevanceScore` than equivalent recent items in the same result set.

---

## DOMAIN 5 — SELF-HEAL & SELF-LEARNING VERIFICATION

**Goal**: Confirm the brain's autonomous learning, deduplication, and error recovery systems are functioning.

23. Run `mcp_firebase-mcp-server_functions_get_logs` with `function_names: ["saveSessionMemory"]`, `page_size: 10` — look for: `"Skipping duplicate KI"` messages (confirms deduplication is active), and `"summarizeSession"` calls (confirms LLM summarization is active).
24. Run `mcp_firebase-mcp-server_functions_get_logs` with `function_names: ["scanKnowledgeDrift"]`, `page_size: 5` — verify it ran recently and produced a `"Knowledge Drift Scan Complete"` info log.
25. Check `mcp_firebase-mcp-server_firestore_list_documents` on `activity` collection with `pageSize: 5` — verify recent activity entries with `type: "audit"` exist (confirms health loop is running).
26. Check `mcp_firebase-mcp-server_firestore_list_documents` on `health/knowledge/drift` path — verify drift records exist for recent KIs.
27. Simulate a deduplication test: call `mcp_brain-mcp_save_session_memory` twice with identical `learningNodes[0].problem` — second call must log `"Skipping duplicate KI"` in function logs.

---

## DOMAIN 6 — MEMORY ANALYSIS & COMPLETENESS

**Goal**: Full inventory and quality check of all brain memory structures.

28. Run `mcp_firebase-mcp-server_firestore_query_collection` on `knowledge_items` — count total documents (use `limit: 100` to get sample). Cross-reference with `health` doc `totalItems` field.
29. Run `mcp_brain-mcp_search_knowledge` for each taxonomy type: `["ARCH", "BUG", "PERF", "UI", "SCRIPT", "SECURITY", "MCP", "RAG"]`. Confirm at least 5 total taxonomy types have knowledge items stored (empty taxonomy = memory gap).
30. Check for ORPHANED KIs (no `artifactPaths`): Run `mcp_firebase-mcp-server_firestore_query_collection` on `knowledge_items` with filter `field: "artifactPaths", op: "EQUAL", string_array_value: []` — list count. Flag if > 20% of total.
31. Check for CORRUPT KIs (missing `title` or `summary`): query `knowledge_items` where `title` is empty — flag count.
32. Run `mcp_firebase-mcp-server_firestore_list_documents` on `session_memories` with `pageSize: 20` — verify sessions span multiple projects (global brain functioning). If all are single-project: flag portfolio resonance gap.
33. Token Budget Check: Load context for current project via `mcp_brain-mcp_search_knowledge` — verify response `tokenMetrics.isCapExceeded` is `false`. If cap exceeded: flag budget tuning required.

---

## DOMAIN 7 — CLOUD RUN & FUNCTION OBSERVABILITY

**Goal**: Verify production health metrics of all deployed Cloud Run functions.

34. Run `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "ERROR"`, `page_size: 50` for the past 24h — categorize all errors by function name. Functions with > 5 errors in 24h are CRITICAL.
35. Run `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "WARNING"`, `page_size: 30` — catalog warnings. Quota warnings (429) against `GEMINI_API_KEY` = P1 billing remediation needed.
36. Run `mcp_gcloud_run_gcloud_command` with args `["run", "services", "describe", "mcpserver-<SUFFIX>", "--region=us-central1", "--format=json(status.latestReadyRevisionName,status.observedGeneration,status.conditions)", "--quiet"]` — verify `latestReadyRevisionName` matches current deployment.
37. Check Cold Start behavior: review brainMcpHandler logs for any initialization time > 10s. If frequent: recommend `minInstances: 1` in Cloud Run config.

**Self-Heal**: If error rate > 10%: immediately run Domain 2 Step 11 tool verification and compare results to determine if transport layer or tool layer is failing.

---

## DOMAIN 8 — SECURITY PERIMETER AUDIT

**Goal**: Zero-trust validation of all security gates.

38. Run `mcp_firebase-mcp-server_firebase_get_security_rules` with `type: "firestore"` — verify rules gate all brain collections. Specifically check:
    - `knowledge_items`: MUST require `request.auth != null`
    - `session_memories`: MUST require `request.auth != null`
    - `project_states`: MUST require `request.auth != null`
    - `health/**`: MUST be admin-only or deny-all
39. Run `mcp_firebase-mcp-server_firebase_get_security_rules` with `type: "storage"` — verify storage rules deny unauthenticated access.
40. Secret Scan: Run `grep_search` on `functions/src` with `Query: "GEMINI_API_KEY"` — verify ONLY `defineSecret("GEMINI_API_KEY")` pattern appears, NEVER raw key strings.
41. Run `grep_search` on `functions/src` with `Query: "process.env.GEMINI"` — must return 0 results (banned pattern — all secrets must use `defineSecret`).
42. Run `grep_search` on `functions/src` with `Query: "hardcoded|sk-|AIza"` pattern — must return 0 exposed key strings.
43. Verify CORS: Run `grep_search` on `functions/src` with `Query: "cors:"` — confirm all Cloud Functions use domain-restricted CORS (no wildcard `"*"`).
44. Run `mcp_firebase-mcp-server_functions_get_logs` with `filter: "\"auth\"", min_severity: "WARNING"` — check for unauthorized access attempts.

---

## DOMAIN 9 — RULES & PROTOCOL COMPLIANCE

**Goal**: Verify every Law from the Infinity Protocol Governance doc is enforced in the current codebase.

45. Read `.agent/workflows/governance.md` — extract all Laws (currently 23).
46. For each Law, run a targeted verification:
    - **Law 1 (Node V8)**: `grep_search` in `functions/package.json` for `NODE_OPTIONS=--max-old-space-size=4096` — must appear in dev, build, and test scripts.
    - **Law 2 (Project ID)**: `grep_search` in `scripts/` for `gcloud config get-value project` — must return 0 results (banned pattern).
    - **Law 3 (E2E)**: `grep_search` in all workflow files for `npx playwright` — must return 0 results.
    - **Law 8 (git push ban)**: `grep_search` in `.agent/workflows/` for `git push` — verify only appears in paste instructions, never in auto-run turbo steps.
    - **Law 10 (Broadcast Scope)**: Read `broadcast.md` workflow — verify it NEVER touches `firebase.json`, `*.ts`, `*.js`, `src/`.
    - **Law 20 (no any)**: `grep_search` in `functions/src` for `Record<string, any>` — count instances. Target: 0. Flag any remaining instances.
    - **Law 22 (Cache)**: `grep_search` in `next.config.ts` for `productionBrowserSourceMaps: false` — must be present.
    - **Law 23 (Brain Audit)**: Verify this `brain_audit.md` workflow exists in `.agent/workflows/`.
47. Read `GEMINI.md` in project root — verify version stamp matches current phase.
48. Read `MISSION_STATE.md` — verify `updatedAt` field is within last 48 hours. If stale: flag as knowledge continuity risk.
49. Read `KNOWLEDGE.md` — verify it exists and is non-empty. If missing: flag as CRITICAL knowledge gap.
50. Verify `.cursorrules` exists and is non-empty. If missing: run `dv rules` immediately.

**Self-Heal**: For any missing workflow files, create them from the governance spec. For any stale MISSION_STATE: `/session_end` to reseal.

---

## DOMAIN 10 — SELF-OPTIMIZATION & PERFORMANCE

**Goal**: Confirm token budgeting, query expansion, reranking, and decay are all producing optimal results.

51. Call `mcp_brain-mcp_search_knowledge` with `mode: "hybrid"` and a complex multi-word query. Verify `expandedQueries` in response contains > 1 query (confirms LLM query expansion is active).
52. Verify temporal decay is differentiating results: search for a topic where you know old and new KIs exist. Confirm newer KIs appear with higher `relevanceScore`.
53. Run `mcp_firebase-mcp-server_functions_get_logs` searching for `[RERANK]` tag in `searchKnowledge` logs — confirms Gemini reranker is invoked for semantic searches.
54. Check token budget utilization: call `loadSessionContext` (via any project) and verify `tokenMetrics.total < tokenMetrics.budget`. Sustained cap-exceed requires increasing `DEFAULT_BUDGET.total` or pruning old sessions.
55. Check `mcp_firebase-mcp-server_functions_get_logs` for `[CONDENSE]` tags — confirms hierarchical summarization is running for large session histories.

---

## DOMAIN 11 — BACKUP & DISASTER RECOVERY

**Goal**: Verify brain data is backed up and recoverable.

56. Read `scripts/backup_brain.sh` — verify it exists and references the correct Firestore export path and GCS bucket.
57. Run `mcp_gcloud_run_gcloud_command` with args `["storage", "ls", "gs://<PROJECT_ID>-backups/brain/", "--quiet"]` (or similar bucket pattern) — verify recent backup files exist (within 7 days). If no backups: CRITICAL — run backup immediately.
58. Verify the backup cron is registered: `grep_search` in `scripts/` for `backup_brain` to confirm it's referenced in cron setup.
59. Run `mcp_firebase-mcp-server_functions_get_logs` with `function_names: ["backupBrain", "exportFirestore"]` if applicable — confirm no export errors.

---

## DOMAIN 12 — KNOWLEDGE DRIFT DETECTION

**Goal**: Flag stale, orphaned, or corrupt knowledge items.

60. Call the `scanKnowledgeDrift` agent tool via `mcp_firebase-mcp-server_functions_get_logs` with `function_names: ["runKnowledgeDriftScan"]` — review latest scan results.
61. Read `health/knowledge` Firestore document — parse: `stale`, `orphaned`, `corrupt`, `healthy` counts.
62. If `stale > 20%` of total: list top 5 stale KIs and recommend archival.
63. If `corrupt > 0`: list corrupt KI IDs for manual review and repair.
64. If `orphaned > 50%`: recommend adding artifact path indexing to `saveSessionMemory` pipeline.
65. Generate a drift score summary: `(corrupt * 3 + stale * 1 + orphaned * 0.5) / totalItems` — score > 0.5 = DEGRADED state.

---

## DOMAIN 13 — FLEET PROTOCOL SYNCHRONIZATION

**Goal**: Verify brain connectivity exists for all active workspaces, not just current project.

66. Read `~/.gemini/antigravity/mcp_config.json` — verify `brain-mcp` entry points to correct Cloud Run URL.
67. List the 5 most recent conversations from KIs — verify at least 3 different `projectId` values appear in `session_memories` (confirms multi-workspace brain usage).
68. Run `mcp_brain-mcp_search_knowledge` with `globalSearch: true`, `query: "deployment fix"` — verify KIs from multiple projects are returned in results.
69. Check MISSION_STATE.md for "Fleet Broadcast" status — if flagged as pending, note it as P2 action item.

---

## DOMAIN 14 — FINAL HEALTH SCORE & REPORT

**Goal**: Synthesize all findings into a single actionable audit report.

70. Aggregate all domain results. Score each domain PASS / WARN / FAIL / CRITICAL.
71. Create a structured audit report in the following format and write it as an artifact `brain_audit_report_<date>.md`:

```markdown
# Brain Audit Report — <DATE>
**Project**: <PROJECT_ID>
**Phase**: <CURRENT_PHASE>
**Auditor**: Zoltan (Infinity Protocol v10.0)

## Executive Summary
<3-sentence overall health assessment>

## Domain Scores
| Domain | Status | Key Findings |
|--------|--------|--------------|
| 1. Workspace Connectivity | PASS/WARN/FAIL/CRITICAL | ... |
| 2. Remote Brain MCP | ... | ... |
| 3. Data Transfer & Storage | ... | ... |
| 4. Vector Search & Embedding | ... | ... |
| 5. Self-Heal & Learning | ... | ... |
| 6. Memory Analysis | ... | ... |
| 7. Observability | ... | ... |
| 8. Security Perimeter | ... | ... |
| 9. Rules & Protocol | ... | ... |
| 10. Self-Optimization | ... | ... |
| 11. Backup & Recovery | ... | ... |
| 12. Knowledge Drift | ... | ... |
| 13. Fleet Synchronization | ... | ... |

## Critical Findings (MUST FIX NOW)
- ...

## P1 Findings (Fix This Session)
- ...

## P2 Findings (Fix Next Session)
- ...

## Drift Score
<formula result + interpretation>

## Recommended Next Actions
1. ...
2. ...
```

72. Update `MISSION_STATE.md` with brain audit completion timestamp and overall score.
73. If any CRITICAL findings were identified: halt and present findings to user immediately before proceeding with any other work.

---

## 📋 BRAIN AUDIT FINAL REPORT (MANDATORY — ALWAYS OUTPUT LAST)

> ⛔ **LAW**: Every `/brain_audit` run MUST conclude with this line-item table. All 13 domains must be scored. Phase delineation MUST appear. Autofix prompts MUST be shown for any ❌ or CRITICAL result.

```
╔══════════════════════════════════════════════════════════════════╗
║  BRAIN AUDIT REPORT — [PROJECT_NAME]                            ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

WORKSPACE_PHASE : [This project's sprint phase — not the hub version]
PROTOCOL_PHASE  : [Hub infrastructure version — e.g. 183.3]
PHASE_GAP       : [ALIGNED / N behind / Expected (non-hub workspace)]

BRAIN MCP       : [✅ ONLINE (latency: Xms) / ⚠️ OFFLINE (autoconnect: FAILED)]
BRAIN VERSION   : [phase from /health endpoint]

┌──────────────────────────────┬──────────┬──────────────────────────────┐
│ Domain                       │ Score    │ Key Finding                  │
├──────────────────────────────┼──────────┼──────────────────────────────┤
│ 1. Workspace Connectivity    │ PASS/... │ [summary]                    │
│ 2. Remote Brain MCP Health   │ PASS/... │ [autoconnect: OK/FAILED]     │
│ 3. Data Transfer & Storage   │ PASS/... │ [collections present/missing]│
│ 4. Vector Search & Embedding │ PASS/... │ [semantic/keyword fallback]  │
│ 5. Self-Heal & Learning      │ PASS/... │ [dedup active/inactive]      │
│ 6. Memory Analysis           │ PASS/... │ [N KIs / taxonomy gaps]      │
│ 7. Cloud Run Observability   │ PASS/... │ [error rate / cold starts]   │
│ 8. Security Perimeter        │ PASS/... │ [rules gated / wildcards?]   │
│ 9. Rules & Protocol          │ PASS/... │ [N law violations]           │
│ 10. Self-Optimization        │ PASS/... │ [rerank/expansion active]    │
│ 11. Backup & Recovery        │ PASS/... │ [last backup: X days ago]    │
│ 12. Knowledge Drift          │ PASS/... │ [drift score: X]             │
│ 13. Fleet Synchronization    │ PASS/... │ [N workspaces connected]     │
└──────────────────────────────┴──────────┴──────────────────────────────┘

CRITICAL: [N]   P1: [N]   P2: [N]
DRIFT SCORE: [formula result] — [HEALTHY / DEGRADED / CRITICAL]

OVERALL: [🟢 SOVEREIGN / 🟡 DEGRADED / 🔴 CRITICAL — See findings above]
```

**If any domain is FAIL or CRITICAL — display the AUTOFIX PROMPT:**

```
═══════════════════════════════════════════
🔧 AUTOFIX REQUIRED — [DOMAIN NAME]
═══════════════════════════════════════════
Issue: [what failed]
Auto-heal attempted: [yes/no — what was tried]
Result: [fixed / FAILED]

If failed — manual fix:
  [exact command or action for user to take]

For Brain MCP offline:
  Option 1: Restart IDE (recommended — 30 seconds)
  Option 2: firebase deploy --only functions --project [PROJECT_ID]
  Option 3: Type "continue brain offline" to proceed in degraded mode

For quota errors (429):
  Migrate saveSessionMemory to Vertex AI ADC (see P1 in next session)

Type "fix [domain name]" to have Zoltan attempt deeper resolution.
═══════════════════════════════════════════
```

---

## POST-AUDIT SELF-HEAL CHECKLIST
- [ ] All 6 brain-mcp tools: responding
- [ ] Firestore `knowledge_items`: exists + has embeddings
- [ ] Session memory deduplication: active
- [ ] Knowledge drift scan: run within 7 days
- [ ] Security rules: all brain collections gated
- [ ] No `Record<string,any>` in functions/src
- [ ] CORS: no wildcards
- [ ] Backup: within 7 days
- [ ] MISSION_STATE: within 48h
- [ ] Token budget: not exceeded
- [ ] WORKSPACE_PHASE and PROTOCOL_PHASE declared separately
- [ ] Brain MCP autoconnect: tested and documented

// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Phantom purge complete. Brain audit sealed.`

*Your brain has been audited. Tend to your failures before the void notices them, mortal.*
