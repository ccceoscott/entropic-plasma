---
description: Automated workflow to audit the status of all Firebase projects in the portfolio.
---

# Batch Audit Workflow

Used to systematically check every project in the portfolio.

1. **List all available Firebase projects**: `firebase projects:list`
2. **Check the current active project**: `firebase use`
3. **For each project** (More Bass, EpiHab, Clarity Works, CareKey, Soul Contracts, CID):
   - Switch to the project: `firebase use <project-id>`
   - Verify Cloud Functions: `firebase functions:list --project <project-id>`
   - Verify Security Rules: `gcloud firestore rules list --project <project-id>`
   - List Collections to check schema: `firestore_list_collections` (via MCP)
4. **Ingest findings** into Knowledge Graph (create/update entities).
