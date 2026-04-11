---
description: Immutable Machine Laws — 29 sovereign laws governing all Infinity Protocol operations
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /governance
## The Immutable Machine Laws (R.A.P.S Edition)

> ⚡ **READ-ONLY REFERENCE**: This workflow documents the laws. It does not execute them. Violations trigger automatic halt.

---

## THE SOVEREIGN MACHINE LAWS

### Law 1 — Node V8 Memory Sovereignty
`NODE_OPTIONS=--max-old-space-size=4096` MUST prefix ALL `dev`, `build`, and `test` scripts in `package.json`. Absolute on Apple Silicon.

### Law 2 — Project Identity Lock
The active Firebase project MUST be verified via `.firebaserc` before any deploy.

### Law 3 — git push Sovereign Auto-Push
`git push` MUST use sovereign hang guards: `GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main`. Auto-run via `run_command` with **`SafeToAutoRun: true`** is **MANDATORY**.

### Law 4 — grep_search Over run_command
Secret scans MUST use `grep_search`.

### Law 5 — Firestore Rules via MCP
Rules export MUST use `mcp_firebase-mcp-server_firebase_get_security_rules`.

### Law 6 — GCloud via MCP
GCP resource queries MUST use `mcp_gcloud_run_gcloud_command`.

### Law 7 — TypeScript Integrity Gate
`tsc --noEmit --skipLibCheck` runs before every deploy.

### Law 8 — No Implicit Any
`noImplicitAny: true` and `strict: true` in `tsconfig.json`. ZERO `as any` or `: any`.

### Law 9 — Phantom Purge
`rm -rf ~/.gemini/antigravity/browser_recordings` MUST run auto after browser use.

### Law 10 — Secret Manager
Secrets MUST be stored in GCSM. `.env.local` MUST be in `.gitignore`.

### Law 11 — ADC Over FIREBASE_TOKEN
Firebase headless uses ADC. `FIREBASE_TOKEN` is banned.

### Law 12 — Timeout Shell Commands
Every bash command MUST use `timeout`.

### Law 13 — Worker Clamp
`experimental.memoryBasedWorkersCount` is ABSOLUTELY BANNED.

### Law 14 — Compiler Parity
`productionBrowserSourceMaps: false` and `removeConsole`.

### Law 15 — TypeScript Performance
`"disableReferencedProjectLoad": true` and `"disableSolutionSearching": true`.

### Law 16 — Cross-Project Isolation
Poison strings (`CareKey`, `SARAH`, `FirstPick`) trigger HALT.

### Law 17 — R.A.P.S Files Mandatory
Every project MUST maintain `MISSION_STATE.md` and `task.md`.

### Law 18 — Two-Key Deploy Verification
1. Re-anchor Firebase MCP.
2. Verify via `firebase_get_environment`.
3. Verify via `.firebaserc`.

### Law 19 — Auth Claim Verification
NEVER write Security Rules referencing claims without verifying via Firebase Admin MCP.

### Law 20 — Schema-Guard
NEVER write Firestore queries without pulling schema first.

### Law 21 — Universal Upgrade Gate
Every workflow MUST begin with the Sovereign Upgrade Gate.

### Law 22 — MCP Ghost Context Sovereignty
Re-anchor `firebase-mcp-server` unconditionally.

### Law 23 — Fleet Propagation Mandate
Before checking a workspace, broadcast rules to it.

### Law 24 — MCP Error Auto-Heal
Kill stale hub: `pkill -f "mcp-local-hub.cjs" 2>/dev/null || true`. (Legacy Remote Brain hub loops removed).

### Law 25 — Workspace Sovereignty
Only the `user_information.workspaces[0].uri` determines the project. ACTIVE_DOC must match.

### Law 26 — R.A.P.S Anchoring
Local state (`MISSION_STATE.md` + `task.md` + local `.agent/`) supersedes Firebase Brain. Remote Brain MCP is DEPRECATED.

### Law 27 — Auto Broadcast
Any workflow edit propagates to the entire fleet automatically.

### Law 28 — R.A.P.S Write Stability
Write state locally. Network brain calls are banned to prevent hangs.

### Law 29 — The Autonomic Nervous System
If stuck, read local KIs. Do NOT use integrated browser. Write a local KI if resolution takes > 3 turns.

---

## GOVERNANCE AUDIT

### GA1-GA5 — Check configuration files and rules

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Governance audit sealed. The Laws endure.`
