---
description: Run an automated periodic scan of the project against Google and Firebase Developer Knowledge, and output improvement recommendations into Firebase Storage.
---

# 📖 KNOWLEDGE AUDIT WORKFLOW (Phase 55+ Sovereign)

This workflow is an **automated inspection routine** that mandates the agent to perform a global review of the active workspace's state and cross-reference its architecture against the official, native Google & Firebase Developer Knowledge mappings.

## ⚡ PREREQUISITES
- The agent must be active in a workspace featuring a valid `.firebaserc`.
- The `mcp_firebase-mcp-server_developerknowledge_search_documents` tool must be accessible.

---

## 🛑 STAGE 1: INGEST CURRENT WORKSPACE CONTEXT
The agent must read the current `MISSION_STATE.md` to determine the Active Project, Framework Type (e.g., Next.js, Cloud Functions), and overall architectural components.
1. Read `MISSION_STATE.md` via file path `view_file` tool.
2. Read `.firebaserc` via file path `view_file` to capture the Active Project ID.

---

## 🛑 STAGE 2: KNOWLEDGE BASE INTERROGATION
Based on the ingested components from STAGE 1, the agent must physically query the integrated Developer Knowledge MCP tool using 2-4 strict keywords (never semantic sentences) to fetch the 2025+ standardized methodologies.
1. Query example: `mcp_firebase-mcp-server_developerknowledge_search_documents(query="Firebase Gen2 Functions configuration")`
2. Query example: `mcp_firebase-mcp-server_developerknowledge_search_documents(query="Next.js App Router performance")`
3. Execute `mcp_firebase-mcp-server_developerknowledge_get_documents` on 1-3 highly relevant results.

---

## 🛑 STAGE 3: SYNTHESIS & REPORT GENERATION
The agent must analyze the difference between the queried documentation mandates and the current workspace codebase.
1. Create a markdown artifact named `[PROJECT_ID]_knowledge_audit_[DATE].md` in the `/tmp/` directory.
2. The report MUST include:
   - **Date & Active Project**
   - **Identified Drift**: Code or architecture that deviates from the official Google/Firebase documentation.
   - **Recommendations**: Specific actionable migrations, refactors, or security enhancements prioritized by severity.

---

## 🛑 STAGE 4: FIREBASE STORAGE ARCHIVAL (Automated)
To persist this intelligence without bloating the Git repository, the agent must upload the artifact to the specific project's default Firebase Storage Bucket.
1. Formulate the bucket URL: `gs://[PROJECT_ID].appspot.com/knowledge_audits/` (or `.firebasestorage.app` depending on the project spec).
2. Execute the upload via gcloud MCP or standard run_command:
// turbo
```bash
gcloud storage cp /tmp/[REPORT_NAME].md gs://$(node -e "console.log(require('./.firebaserc').projects.default)").appspot.com/knowledge_audits/
```
3. Update `MISSION_STATE.md` to log that a Knowledge Audit was successfully performed and uploaded.

---
**Completion:** The agent shall inform the user that the knowledge audit is finished, present the findings briefly in chat, and provide the GCS reference link.
