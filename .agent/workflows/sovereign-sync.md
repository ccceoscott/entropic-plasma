---
description: /sovereign-sync — Phase 161 Firebase Brain Sync Workflow. Orchestrates uplink (local → Brain), downlink (Brain → local), push-brain (MISSION_STATE → Firestore via Cloud Functions), and brain-status (live Brain health check). Replaces the Phase 58 stub. Run after finalize_session for full fleet permanence. (Phase 161 Sovereign — v10.0.71)
---

# /sovereign-sync — Firebase Brain Sync Protocol (Phase 161 Sovereign)

> **PURPOSE**: Synchronize the Infinity Protocol Firebase Brain (Firestore + Cloud Functions) with local state. This is the permanent knowledge layer — not a file backup. Every session that ends without a `dv push-brain` has left the machine in an undefined state.

> **LAW**: `run_command` is BANNED for all network/blocking operations in this workflow. All Brain writes use the Cloud Functions callable stack. All Brain reads use the Firestore MCP tool.

---

## PREREQUISITE — PROTOCOL_PASSPHRASE

`dv uplink` and `dv downlink` require `PROTOCOL_PASSPHRASE` in your environment.

**One-time setup** (if not already configured):
```bash
echo 'export PROTOCOL_PASSPHRASE="<your-passphrase>"' >> ~/.zshenv
source ~/.zshenv
```

> The passphrase is stored in Google Cloud Secret Manager under `infinity-protocol-1`. Retrieve via:
> `gcloud secrets versions access latest --secret="PROTOCOL_PASSPHRASE" --project="gen-lang-client-0386732425" --quiet`

`dv push-brain` and `dv brain-status` do NOT require a passphrase — they use public callable Cloud Functions.

---

## COMMAND REFERENCE

| Command | Direction | Uses | When |
|---|---|---|---|
| `dv brain-status` | Brain → local (read-only) | `loadSessionContext` Cloud Function | Session start, health check |
| `dv downlink` | Brain → local (files) | `downloadProtocolFiles` Cloud Function | Session start, fleet repair |
| `dv push-brain` | Local → Brain (state) | `upsertProjectState` + `saveSessionMemory` | Session end, after MISSION_STATE updates |
| `dv uplink` | Local → Brain (files) | `uploadProtocolFiles` Cloud Function | Protocol file fleet propagation |

---

## WORKFLOW: SESSION START SYNC (Stage 0 of /turnover)

```bash
# Step 1 — Check Brain state (read-only, no passphrase needed)
dv brain-status

# Step 2 — If Brain shows phase drift or stale knowledge:
dv downlink
```

**What brain-status shows:**
- Firestore phase vs local MISSION_STATE phase (drift indicator)
- GEMINI.md hash comparison
- Last 5 session memories with summaries
- Permanent constraints (NEVER FORGET laws)

---

## WORKFLOW: SESSION END SYNC (Phase 5 of /finalize_session)

```bash
# Step 1 — Push local MISSION_STATE to Firestore (mandatory every session)
dv push-brain "Phase 161 — [brief session summary]"

# Step 2 — If protocol files changed (rules, workflows, GEMINI.md):
# User must approve — then:
dv uplink
```

> `dv push-brain` reads `MISSION_STATE.md` automatically for phase/version/status.
> Pass an optional summary string as `$2` for a human-readable session note.

---

## WORKFLOW: FULL FLEET PROTOCOL PROPAGATION

Only run when `.agent/workflows/`, `rules/*.mdc`, or `GEMINI.md` have changed.

```bash
# Step 1 — Upload changed files to Cloud Brain
dv uplink

# Step 2 — Broadcast to fleet workspaces (user approval REQUIRED)
# Propose: bash scripts/sovereign_broadcast.sh
```

> **BROADCAST SCOPE LAW**: `sovereign_broadcast.sh` ONLY touches `.cursorrules`, `GEMINI.md`, `.agent/workflows/*.md`. NEVER `firebase.json`, `firestore.rules`, `package.json`, or `src/`.

---

## ERROR RECOVERY

| Error | Fix |
|---|---|
| `PROTOCOL_PASSPHRASE env var is not set` | `export PROTOCOL_PASSPHRASE="..."` in `~/.zshenv` |
| `firebase_sync.cjs not found` | Run from Hub dir: `cd ~/Developer/infinity-protocol-1` |
| `ADC token failed` | `gcloud auth application-default login` |
| `HTTP 401` on callable | ADC expired — `gcloud auth application-default login` |
| `upsertProjectState failed` | Check `.firebaserc` has `projects.default` set |

---

## PHASE 161 BRAIN COLLECTIONS

| Collection | Purpose | Write Via |
|---|---|---|
| `project_states/{projectId}` | MISSION_STATE mirror | `dv push-brain` → `upsertProjectState` |
| `session_memories/{sessionId}` | Session logs + learning | `dv push-brain` → `saveSessionMemory` |
| `protocol_files/{path}` | Full protocol file archive | `dv uplink` → `uploadProtocolFiles` |
| `knowledge_items/{id}` | KI + embeddings | `mcp_firebase_firestore_add_document` direct |
| `system_graph/{id}` | Knowledge graph edges | `mcp_knowledge-graph_*` tools |
