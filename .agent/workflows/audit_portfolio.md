---
description: Automated workflow to audit the status of all Firebase projects in the portfolio. (Phase 160 Sovereign)
---

# /audit_portfolio — Sovereign Fleet Inspection

Systematically interrogates every Firebase project in the Constant Concepts portfolio. This is the **mandatory diagnostic gate** before any fleet-wide upgrade or migration.

> **⚠️ PHASE 57 SOVEREIGN LAW:**
> - `gcloud config get-value project` is **BANNED** — hangs in non-interactive shells
> - `gcloud config get-value account` is **BANNED** — same reason  
> - `firebase projects:list` is **SAFE** (Firebase CLI uses local token cache)
> - Use `mcp_gcloud_run_gcloud_command` MCP tool instead of `run_command` for gcloud

---

## 1. 🛡️ Identity Lock via MCP (NOT terminal)

Use the **gcloud MCP tool** — it is non-blocking:

Call: `mcp_gcloud_run_gcloud_command` with args `["config", "get-value", "project"]`
Call: `mcp_firebase-mcp-server_firebase_list_projects` (MCP tool — zero hang risk)

> **Project ID sovereign pattern:** Read from local file instead of network:
> `node -e "console.log(require('./.firebaserc').projects.default)"`
> via `run_command` with `WaitMsBeforeAsync: 2000` and `SafeToAutoRun: true`

---

## 2. 🔥 Per-Project Diagnostic Loop (MCP Tools Only)

For each active project, use MCP tools exclusively:

- `mcp_firebase-mcp-server_functions_list_functions` — list Cloud Functions
- `mcp_firebase-mcp-server_firestore_list_databases` with `parent: "projects/<id>"`
- `mcp_gcloud_run_gcloud_command` with args `["run", "services", "list", "--platform", "managed", "--project", "<id>"]`

**Known Fleet Projects:**
- `gen-lang-client-0386732425` (Infinity Protocol — ACTIVE)
- EpiHab, CID Seniors, Infinity Press, FirstPick, Soul Contracts, More Bass, Lspproductionservices, AZDJ Academy

---

## 3. 📊 Security Rules Audit (MCP Tool)

Use: `mcp_firebase-mcp-server_firebase_get_security_rules` with `type: "firestore"`

Scan result for `if true` — halt if found without auth guard. Escalate to `/security_scan`.

---

## 4. 🧠 Ingest Findings (File Tool)

Use `write_to_file` or `multi_replace_file_content` to update `MISSION_STATE.md`.
Use `mcp_knowledge-graph_add_observations` for cross-session intelligence.

*Status: Fleet Inspected. Sovereign Order Restored. No terminal hangs.*
