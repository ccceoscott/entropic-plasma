---
description: The Sovereign Oracle Loop (Law 29) — Autonomic Nervous System for mid-task failure resolution.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /self_heal
## Law 29: The Autonomic Nervous System

> ⚡ **TRIGGER**: This workflow is automatically executed by the Agent mid-session when an unknown terminal error, strange stack trace, or architectural friction blocks the immediate path. 

### STEP 1 — Freeze Execution
Do not guess. Do not proceed. Do not attempt a "try-catch" bandaid without understanding the root cause.

### STEP 2 — The Sovereign Oracle (Trajectory Synthesis)
Invoke the Brain's generic synthesis engine immediately:

```
mcp_mcp-local-hub_brain_search_knowledge({ 
  query: "[Exact 1-2 words of the stack trace or architectural friction]", 
  limit: 10, 
  mode: "hybrid",
  globalSearch: true
})
```

**Analysis Mandate**:
1.  **Direct Fix**: If `synthesis` contains a direct code fix, implement it.
2.  **Meta-Context**: Verify if the error is caused by a violation of the `metaContext`. If so, refactor the offending component to align with the core principle.
3.  **Contradictions**: If the reranker detects a contradiction between your current approach and past successful patterns, pivot immediately.
4.  **Knowledge Item Recall**: If synthesis is inconclusive, manually inspect the top 3 items in the `results` array.

### STEP 3 — GDK / FDK Proxies
If the local Brain returns 0 results for the specific error, and the error pertains to a core framework (Firebase/GCP/Next.js/Tailwind), query the `mcp_firebase-mcp-server_firebase_developer_knowledge` or `google_developer_knowledge` tools before resorting to the archaic Integrated Browser.

### STEP 4 — Post-Resolution Generation (3-Turn Rule)
If resolving this specific error takes more than 3 conversation turns, you are **MANDATED** to document the fix so the Brain can absorb it.
We will defer this to `/session_end` by marking a pending task in `task.md`. At session seal, we will write the detailed fix to:
`~/.gemini/antigravity/knowledge/[error_name]/artifacts/[error_name]_fix.md`
*(This will be picked up by the `npm run ingest` cron automatically tomorrow).* 

Resume normal execution.
