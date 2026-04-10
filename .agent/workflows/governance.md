---
description: Immutable Machine Laws — 29 sovereign laws governing all Infinity Protocol operations
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /governance
## The Immutable Machine Laws — Phase 185+

> ⚡ **READ-ONLY REFERENCE**: This workflow documents the laws. It does not execute them. Violations trigger automatic halt in any workflow that detects them.

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

## THE SOVEREIGN MACHINE LAWS

### Law 1 — Node V8 Memory Sovereignty
`NODE_OPTIONS=--max-old-space-size=4096` MUST prefix ALL `dev`, `build`, and `test` scripts in `package.json`. Never 8192. Never absent. Absolute on Apple Silicon.

### Law 2 — Project Identity Lock
The active Firebase project MUST be verified via `.firebaserc` before any deploy, write, or destructive operation. Command: `node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"`. NEVER use `gcloud config get-value project` — hangs in non-interactive shells.

### Law 3 — git push Sovereign Auto-Push (Phase 185 — ABSOLUTE)
`git push` MUST use sovereign hang guards: `GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main`. The hang vector is SSH/HTTPS **auth prompting** — neutralized by `GIT_TERMINAL_PROMPT=0`. With keys preconfigured, auto-run via `run_command` with **`SafeToAutoRun: true`** is **MANDATORY** — this is not optional. The user has explicitly mandated zero paste commands for git push. On timeout → HALT and report, do not retry blindly. See `/fix_push` for recovery.

### Law 4 — grep_search Over run_command
Secret scans, pattern searches, and file content searches MUST use `grep_search` MCP tool. `run_command grep` blocks, hangs on large directories, and is a terminal kill vector.

### Law 5 — Firestore Rules via MCP
Rules export and validation MUST use `mcp_firebase-mcp-server_firebase_get_security_rules` and `mcp_firebase-mcp-server_firebase_validate_security_rules`. NEVER `firebase firestore:rules > /tmp/...`.

### Law 6 — GCloud via MCP
Fleet audits, function status, and GCP resource queries MUST use `mcp_gcloud_run_gcloud_command`. Bare `gcloud` in `run_command` = potential hang. Always add `--quiet` flag.

### Law 7 — TypeScript Integrity Gate
`tsc --noEmit --skipLibCheck` runs before every code merge, deploy, and at the start of every session. ANY errors → auto-fix attempt (if < 5 identifiable errors). Still failing → HALT. No broken TypeScript ships.

### Law 8 — No Implicit Any
`noImplicitAny: true` and `strict: true` in `tsconfig.json`. ZERO `as any` or `: any` in any non-test file. Each `any` = a hiding place for a hallucinated type. Eradicate immediately.

### Law 9 — Phantom Purge
`rm -rf ~/.gemini/antigravity/browser_recordings` MUST run after every browser subagent session. Auto-run via `run_command` — local `rm -rf` is safe and instant. NEVER via blocking MCP.

### Law 10 — Secret Manager Registration
Newly introduced API keys or secrets MUST be stored in Google Cloud Secret Manager immediately. NEVER hardcoded. Use Secret Manager or `.env.local`. `.env.local` MUST be in `.gitignore`.

### Law 11 — ADC Over FIREBASE_TOKEN
Firebase headless auth uses Application Default Credentials (ADC). `gcloud auth print-identity-token` and raw `FIREBASE_TOKEN` are banned. Use `gcloud auth application-default login` once, then ADC flows everywhere.

### Law 12 — Timeout All Shell Commands
Every bash command in scripts uses timeouts:
- `git fetch`: `GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true`
- `tsc`: `timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck`
- `osascript`: `timeout 5 osascript -e "..." || true`
- `tmutil`: `timeout 10 tmutil deletelocalsnapshots / || true`

### Law 13 — Worker Clamp Ban
`experimental.memoryBasedWorkersCount` is ABSOLUTELY BANNED in `next.config.ts` on Apple Silicon. Causes OOM build crashes. Remove immediately if detected.

### Law 14 — Compiler Parity
`productionBrowserSourceMaps: false` and `removeConsole: { exclude: ['error', 'warn'] }` MUST be in `next.config.ts` for all production builds.

### Law 15 — TypeScript Performance
`"disableReferencedProjectLoad": true` and `"disableSolutionSearching": true` in `.vscode/settings.json`. `"typescript.tsserver.maxTsServerMemory": 2048` — never higher.

### Law 16 — Cross-Project Isolation
NEVER apply rules, credentials, API keys, or branding from one project to another. Poison strings (`CareKey`, `FirstPick`, `SARAH`, `Soul Contract`, `epi-hab`) trigger immediate HALT if detected.

### Law 17 — SSOT Files Mandatory
Every project MUST maintain `MISSION_STATE.md` (root), `KNOWLEDGE.md` (root), and `.agent/CODEBASE_MAP.md`. Every session starts by reading all three. Updated after every major file write or command.

### Law 18 — Two-Key Project Verification (Pre-Deploy)
Before ANY deploy or MCP-dependent operation:
1. **Re-anchor** the Firebase MCP server unconditionally: call `mcp_firebase-mcp-server_firebase_update_environment` with `project_dir=/Users/teknojunkeee/Developer/infinity-protocol-1`, `active_project=gen-lang-client-0386732425`.
2. **Verify** via `mcp_firebase-mcp-server_firebase_get_environment` — must show `gen-lang-client-0386732425`.
3. **Cross-verify** via `.firebaserc`: `node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"`.
All three must agree. If MCP still shows wrong project after re-anchor → MCP server failure → HALT.

### Law 19 — Auth Claim Verification Before Rules
NEVER write Firestore Security Rules referencing `request.auth.token.[claim]` without first verifying via Firebase Admin MCP that the claim actually exists on real user accounts. Auth-Mismatch = BLOCKER.

### Law 20 — Schema-Guard Before Data Code
NEVER write Firestore queries or document writes without first pulling live schema via Firebase MCP and generating TypeScript interfaces. Save to `types/firebase.d.ts`. All subsequent code uses only these types.

### Law 21 — Universal Upgrade Gate
Every workflow MUST begin with the Sovereign Upgrade Gate:
1. Check local Phase vs Hub Phase
2. Auto-upgrade if stale (`dv downlink` + `dv rules`)
3. TypeScript gate (zero errors required)
4. Self-heal any warnings discovered
Any workflow that skips this gate is in violation of the Protocol.

### Law 22 — MCP Ghost Context Sovereignty
The `firebase-mcp-server` is a GLOBAL process shared across all workspaces. It drifts to the last project that called `firebase_update_environment`. This is the **Ghost Context Problem**.

**ABSOLUTE MANDATE**: The `mcp_firebase-mcp-server_firebase_update_environment` call with `infinity-protocol-1` credentials MUST execute:
- At the start of EVERY session (Step 2 of `/session_start`)
- Before EVERY deploy (`/deploy` LOCK 1b)
- Before EVERY MCP-dependent operation

NEVER assume the MCP is correctly pointed. ALWAYS re-anchor first. Checking without re-anchoring is a protocol violation.

**The anchor values are immutable for this workspace:**
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

### Law 23 — Spot-Check Protocol Pre-Propagation Mandate
**ABSOLUTE LAW**: Before running ANY spot-check, compliance audit, or test on a non-Hub workspace, the Protocol MUST be propagated to that workspace FIRST.

**Pre-Propagation Checklist (MANDATORY for every target workspace):**
1. **GEMINI.md** — Copy Hub's `GEMINI.md` to target workspace root (overwrite)
2. **governance.md** — Copy Hub's `.agent/workflows/governance.md` to target workspace
3. **session_start.md** — Copy Hub's `.agent/workflows/session_start.md` to target workspace
4. **audit.md** — Copy Hub's `.agent/workflows/audit.md` to target workspace
5. **MISSION_STATE.md** — Update `Last Protocol Sync:` timestamp in target workspace

**Enforcement Commands:**
```bash
# For each TARGET_WORKSPACE (e.g., infinity-press, soul-contracts-charts):
cp ~/Developer/infinity-protocol-1/GEMINI.md ~/Developer/<TARGET_WORKSPACE>/GEMINI.md
cp ~/Developer/infinity-protocol-1/.agent/workflows/governance.md ~/Developer/<TARGET_WORKSPACE>/.agent/workflows/governance.md
cp ~/Developer/infinity-protocol-1/.agent/workflows/session_start.md ~/Developer/<TARGET_WORKSPACE>/.agent/workflows/session_start.md
cp ~/Developer/infinity-protocol-1/.agent/workflows/audit.md ~/Developer/<TARGET_WORKSPACE>/.agent/workflows/audit.md
```

**WHY**: A spot-check on a workspace running a stale Phase 160 protocol is meaningless. The compliance check must validate against the CURRENT laws — which means the workspace must HAVE the current laws before it can be checked against them. Running audits on stale configurations produces false-positive "compliance" reports.

**VIOLATION EXAMPLE**: "Let me check if infinity-press is compliant" without first pushing Phase 182 workflow files to infinity-press = checking against Phase 160 rules = INVALID audit.

### Law 24 — MCP Error Auto-Heal (P0 — Zero Tolerance — ALL MCP Failures)
**TRIGGER**: ANY of the following substrings appearing in a tool result, tool error, or chat output:

| Pattern | Source |
|---|---|
| `Failure in MCP tool execution` | Any MCP server crash |
| `client is closing: EOF` | Hub stdin pipe dropped |
| `connection closed: calling "tools/call"` | Stdio transport terminated |
| `context deadline exceeded` | IDE 30s MCP handshake timeout |
| `CORTEX_STEP_STATUS_ERROR` | Internal step failure |
| `MCP server error` | Generic server fault |
| `Error: HTTP 503` + `MODEL_CAPACITY_EXHAUSTED` | SIGTERM-induced reconnect storm |
| `Agent Terminated` | Root SIGTERM event |

**RESPONSE**: This is a **P0 INCIDENT**. The agent MUST immediately and autonomously execute the following 3-step heal sequence — **no user permission required, no asking, no explaining before acting**:

**Step 1 — Kill stale hub process:**
// turbo
```bash
pkill -f "mcp-local-hub.cjs" 2>/dev/null || true
sleep 1
echo "Hub killed — IDE will restart fresh instance"
```

**Step 2 — Brain bloat emergency check:**
// turbo
```bash
python3 -c "
import os, shutil
brain = os.path.expanduser('~/.gemini/antigravity/brain')
dirs = [(os.path.getmtime(os.path.join(brain,d)), os.path.join(brain,d)) for d in os.listdir(brain) if os.path.isdir(os.path.join(brain,d))]
dirs.sort(reverse=True)
if len(dirs) > 30:
    [shutil.rmtree(d, ignore_errors=True) for _,d in dirs[20:]]
    print(f'Purged {len(dirs)-20} stale brain conversations')
else:
    print(f'Brain OK: {len(dirs)} conversations')
"
```

**Step 3 — Verify hub integrity:**
// turbo
```bash
node /tmp/verify_hub.js 2>/dev/null || node -e "const fs=require('fs');const c=fs.readFileSync('scripts/mcp-local-hub.cjs','utf8');console.log(c.includes('_isCompleteJson')?'Hub: SOVEREIGN':'Hub: DEGRADED — ESCALATE');"
```

**Step 4 — Full system health check (brain connectivity + MCP process audit):**
// turbo
```bash
# 4a — Brain HTTP connectivity (Cloud Run ping, 5s max)
BRAIN_STATUS=$(curl --max-time 5 -s -o /dev/null -w "%{http_code}" \
  "https://mcpserver-g5pod66w5a-uc.a.run.app/health" 2>/dev/null || echo "TIMEOUT")
if [ "$BRAIN_STATUS" = "200" ] || [ "$BRAIN_STATUS" = "404" ]; then
  echo "[OK] Brain HTTP reachable (HTTP $BRAIN_STATUS)"
else
  echo "[WARN] Brain HTTP unreachable (status: $BRAIN_STATUS) — check Cloud Run deployment"
fi

# 4b — MCP server process audit (which servers are alive, flag multi-instance bloat)
echo ""
echo "=== MCP Server Process Audit ==="
for SERVER in "mcp-local-hub" "firebase experimental:mcp" "gcloud-mcp" "mcp-server-memory" "chrome-devtools-mcp"; do
  COUNT=$(pgrep -f "$SERVER" 2>/dev/null | wc -l | tr -d ' ')
  if [ "$COUNT" -gt "2" ]; then
    echo "[BLOAT]  $SERVER — ${COUNT} instances (multi-workspace RSS waste, ~$((COUNT * 50))MB est)"
  elif [ "$COUNT" -gt "0" ]; then
    echo "[ALIVE]  $SERVER ($COUNT instance(s))"
  else
    echo "[DOWN]   $SERVER — will be restarted by IDE on next tool call"
  fi
done

# 4c — knowledge-graph file lock check (double-spawn creates corrupt state)
KG_FILE="$HOME/.gemini/antigravity/knowledge-graph.jsonl"
KG_PROCS=$(pgrep -f "mcp-server-memory" 2>/dev/null | wc -l | tr -d ' ')
if [ "$KG_PROCS" -gt "1" ]; then
  echo "[WARN] DOUBLE-SPAWN: $KG_PROCS knowledge-graph processes sharing same JSONL — killing extras"
  # Keep only the most recent
  pgrep -f "mcp-server-memory" 2>/dev/null | sort -r | tail -n +2 | xargs kill -15 2>/dev/null || true
else
  echo "[OK] knowledge-graph: $KG_PROCS process(es) — no file-lock contention"
fi

# 4d — Brain local dir health
BRAIN_COUNT=$(ls -1 ~/.gemini/antigravity/brain/ 2>/dev/null | wc -l | tr -d ' ')
BRAIN_MB=$(du -sm ~/.gemini/antigravity/brain/ 2>/dev/null | cut -f1 || echo 0)
echo "[INFO] Brain local: ${BRAIN_COUNT} conversations / ${BRAIN_MB}MB"
echo "=== Heal Sequence Complete ==="
```

**After heal**: Report in one line: `🔧 MCP P0 HEALED — hub restarted, brain HTTP [STATUS], brain local [N]convos/[X]MB, KG procs [N], hub SOVEREIGN`. Then resume the task immediately.

**WHY**: All patterns in the trigger table are symptoms of the same root cascade: hub stalls on bare-JSON initialize (no `\n`) → context deadline → SIGTERM → rapid reconnects → Claude capacity exhausted → 503. Killing the stale hub forces the IDE to restart it with the Phase 185.6 fixed binary, breaking the loop in under 3 seconds. Brain bloat compounds the window by slowing IDE startup.

**ESCALATION**:
- Hub `DEGRADED` → halt + run `/audit_antigravity DOMAIN 2`
- Brain HTTP unreachable + not `TIMEOUT` (i.e. DNS failure) → check Cloud Run: `mcp_gcloud_run_gcloud_command ["run", "services", "list", "--region=us-central1", "--quiet"]`
- KG double-spawn persists after kill → check `mcp_config.json` for duplicate knowledge-graph entries



---
### Law 29 — The Autonomic Nervous System (Self-Heal Loop)
**TRIGGER**: Encountering an unknown stack trace, architectural blocker, or failure taking >1 turn to fix.
**RESPONSE**: The Integrated Browser is BANNED for error resolution. The Agent MUST immediately freeze execution and query `mcp_mcp-local-hub_brain_search_knowledge` with the EXACT error string. If no local KI exists, query GDK/FDK proxies. 
**LEARNING MANDATE**: If an error resolution takes >3 turns, the Agent MUST autonomously use `write_to_file` to create a new markdown KI in `~/.gemini/antigravity/knowledge/` documenting the fix. This expands the Brain continuously.

---
## GOVERNANCE AUDIT — Run This to Verify Compliance

### GA1 — package.json Script Compliance
Use `view_file` on `package.json` and `functions/package.json`.
Verify every `dev/build/test` script has `NODE_OPTIONS=--max-old-space-size=4096` (Law 1).
Auto-add any missing instances.

### GA2 — next.config.ts Compliance
Use `view_file` on `next.config.ts`.
Verify: `productionBrowserSourceMaps: false` (Law 14).
Verify: `removeConsole` present (Law 14).
Use `grep_search` for `memoryBasedWorkersCount` — must not exist (Law 13).

### GA3 — tsconfig.json Strictness
Use `view_file` on `tsconfig.json`.
Verify: `"strict": true` and `"noImplicitAny": true` (Law 8).

### GA4 — .gitignore Completeness
Use `view_file` on `.gitignore`.
Verify: `.env.local`, `serviceAccountKey*.json`, `*.pem` are excluded (Law 10).

### GA5 — SSOT File Existence
// turbo
```bash
ls -la MISSION_STATE.md KNOWLEDGE.md 2>&1
ls -la .agent/CODEBASE_MAP.md 2>/dev/null || echo "CODEBASE_MAP.md missing"
```
Missing files → auto-scaffold with minimal content.

### GA6 — Law Table Version Check
Confirm this governance.md contains 24 laws.
If any law is missing from the active GEMINI.md or `.cursorrules` → flag for sync via `dv broadcast`.

---

## VIOLATION RESPONSE PROTOCOL

When any Law is violated during a workflow:

1. **Immediate HALT** — stop current operation
2. **Classify**: which Law number was violated?
3. **Root cause**: why? (missing config, inherited pattern, model assumption?)
4. **Auto-fix** if possible (add NODE_OPTIONS, fix tsconfig, update .gitignore)
5. **Re-verify**: confirm fix removes the violation
6. **Document**: use `mcp_knowledge-graph_add_observations` to record the violation type for cross-session learning
7. **Resume**: only after all violations are resolved

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Governance audit sealed. The Laws endure.`
