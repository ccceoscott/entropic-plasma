---
description: Environment health verification — run before major operations to confirm all tools and services are alive
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /verify_environment
## Sovereign Environment Health Gate — SSOT Grounded, Two-Key MCP, Self-Healing

> ⚡ **MANDATE**: This is the pre-flight health check. Every finding triggers immediate remediation. A broken environment cannot produce sovereign code. MCP-first throughout.

> 🔑 **TWO-KEY LAW**: Environment truth comes from BOTH local toolchain AND Firebase MCP. Never assume a tool works — verify it.

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
Any `[ERROR]` → HALT. Broken upgrade = broken session.

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run.

---

## SSOT INGESTION (Before All Checks)

> **Grounding Law**: Read ALL SSOT files before verifying anything. No guesses.

Use `view_file` on `MISSION_STATE.md` — note current phase, active laws.
Use `view_file` on `KNOWLEDGE.md` — note established patterns and constraints.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists) — note Zombie Code List.
Use `view_file` on `firebase.json` — note configured services and aliases.
Use `view_file` on `.firebaserc` — note project aliases.

**Declare ground truth**:
- Project: gen-lang-client-0386732425
- Phase: [from MISSION_STATE]
- Active services: [from firebase.json]

---

## SECTOR 1 — Node.js & npm Sovereignty
// turbo
```bash
node --version && npm --version && which node
```
Expected: Node v22.x.x. npm v10+.
- Node < 22 → **P0 HALT**: `nvm use 22 || nvm install 22`
- npm < 10 → `npm install -g npm@latest`
- `which node` not in nvm path → document for user

// turbo
```bash
node -e "console.log(process.env.NODE_OPTIONS || 'MISSING')"
```
Expected: contains `--max-old-space-size=4096`.
Missing → user must add `export NODE_OPTIONS=--max-old-space-size=4096` to `~/.zshenv`.
Log: `⚠️ Node memory clamp missing from environment`

---

## SECTOR 2 — Project Identity (Dual Verification — Two-Key)

**Key 1 — Local .firebaserc**:
// turbo
```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"
```
Expected: `gen-lang-client-0386732425`

**Key 2 — Firebase MCP Re-Anchor (Law 22 — unconditionally first):**
Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

**Key 3 — Verify re-anchor:**
Use `mcp_firebase-mcp-server_firebase_get_environment` → extract `projectId`.

Both must agree. Mismatch → **HALT**. Cross-project bleed detected.

---

## SECTOR 3 — Firebase CLI Health
// turbo
```bash
firebase --version 2>&1 | head -2
```
Expected: v14+ (2026 standard). If older → `npm install -g firebase-tools@latest`.

// turbo
```bash
firebase projects:list --json 2>&1 | head -10 || echo "firebase auth may be expired"
```
If auth error → user must run `firebase login` or confirm ADC.

**Firebase MCP Validation**:
Use `mcp_firebase-mcp-server_firebase_get_project` → confirm project details load without error.
MCP non-responsive → **HALT**: MCP server environment broken.

---

## SECTOR 4 — Git Environment
// turbo
```bash
git --version && git status --short && git log --oneline -3
```
Verify:
- No `fatal:` errors (repo not initialized)
- Working tree is clean or known-dirty
- Last 3 commits are from this project (not cross-project bleed)

// turbo
```bash
echo "GIT_TERMINAL_PROMPT=$GIT_TERMINAL_PROMPT"
```
Expected: `0`. If not set → document as hang risk. User should add `export GIT_TERMINAL_PROMPT=0` to `~/.zshrc`.

---

## SECTOR 5 — Dependency Integrity
// turbo
```bash
ls -la node_modules/.package-lock.json 2>/dev/null | head -2 || echo "node_modules missing"
```
Missing node_modules → `npm ci` before proceeding (auto-run with turbo).

// turbo
```bash
ls -la functions/node_modules/.package-lock.json 2>/dev/null | head -2 || echo "functions/node_modules missing"
```
Missing functions deps → `cd functions && npm ci`.

// turbo
```bash
npm outdated 2>&1 | head -10
```
Any critical security updates flagged → document as P2.

---

## SECTOR 6 — TypeScript & Build Tools
// turbo
```bash
./node_modules/.bin/tsc --version 2>/dev/null || echo "tsc missing"
```
Missing → `npm ci` repair step.

// turbo
```bash
ls -la .next/ 2>/dev/null | head -3 || echo "no build cache"
```
Stale `.next/` older than 2 days with recent code changes → `rm -rf .next/` recommended.
Log: `⚠️ Stale build cache detected — recommend clean build`

---

## SECTOR 7 — Port & Process Health
// turbo
```bash
lsof -ti:3000,5001,5173,9099,8080,4000 2>/dev/null | head -10 || echo "all ports clear"
```
Stale zombie processes on dev ports → `kill -9 [PID]` for each zombie.
Log each kill: `🔧 [AUTO-KILLED] Zombie process on port [X] PID [Y]`

---

## SECTOR 8 — MCP Server Health (Full Suite)

### 8a — Firebase MCP Re-Anchor + Health Check (Law 22)
> ⛔ Re-anchor first — never assume MCP is pointed at the right project.

Use `mcp_firebase-mcp-server_firebase_update_environment` with:
- `project_dir`: `/Users/teknojunkeee/Developer/infinity-protocol-1`
- `active_project`: `gen-lang-client-0386732425`
- `active_user_account`: `scott@constantconcepts.io`

Then: `mcp_firebase-mcp-server_firebase_get_environment` → must return `gen-lang-client-0386732425`.
✅ or ❌ log result.

### 8b — GCloud MCP
Use `mcp_gcloud_run_gcloud_command` with args `["--version", "--quiet"]`.
✅ or ❌ log result.

### 8c — Knowledge Graph MCP
Use `mcp_knowledge-graph_search_nodes` with query `"infinity protocol"`.
Expected: at least 1 result. 0 results = KG empty (normal for new project) or MCP broken.
✅ or ❌ log result.

### 8d — Brave Search MCP (if configured)
Use `mcp_brave-search_brave_web_search` with query `"Firebase 2026"` and count `1`.
✅ or ❌ log result.

### 8e — Chrome DevTools MCP
Use `mcp_chrome-devtools_list_pages` → returns page list.
✅ or ❌ log result.

**MCP Health Table**:
| MCP Server | Status | Notes |
|---|---|---|
| firebase-mcp-server | ✅/❌ | |
| gcloud | ✅/❌ | |
| knowledge-graph | ✅/❌ | |
| brave-search | ✅/❌ | |
| chrome-devtools | ✅/❌ | |

Any ❌ → attempt restart if applicable. If persistent → document as environment blocker.

---

## SECTOR 9 — Secret & Credential Health
// turbo
```bash
ls -la .env.local 2>/dev/null || echo ".env.local missing"
```
Missing `.env.local` → **WARNING**: create from `.env.example` template.

Use `grep_search` for `GOOGLE_APPLICATION_CREDENTIALS` in `.env.local`:
Present → confirm path exists:
```bash
ls -la "$GOOGLE_APPLICATION_CREDENTIALS" 2>/dev/null || echo "ADC path broken"
```

Use `mcp_gcloud_run_gcloud_command` with args `["auth", "application-default", "print-access-token", "--quiet"]`.
Token prints → ADC working. Error → user must run `gcloud auth application-default login`.

---

## SECTOR 10 — Memory & Performance Limits
// turbo
```bash
ulimit -n
```
Expected: ≥ 65536. Lower → `ulimit -n 65536` (session only). User must add to `~/.zshrc` for persistence.

// turbo
```bash
df -h . | tail -1
```
Available disk < 2GB → **WARNING**: builds may fail.

// turbo
```bash
sysctl hw.memsize 2>/dev/null || vm_stat | head -5
```
Log available RAM. Document if < 8GB (risk for Apple Silicon build OOM).

---

## SECTOR 11 — Environment Health Report

Generate full status table:

| Sector | Component | Status | Action Taken |
|---|---|---|---|
| Node | Version v22 | ✅/❌ | |
| Node | Memory clamp 4096 | ✅/❌ | |
| Project | Identity dual-verified | ✅/❌ | |
| Firebase CLI | Version current | ✅/❌ | |
| Git | Clean environment | ✅/❌ | |
| Deps | node_modules intact | ✅/❌ | |
| TypeScript | tsc available | ✅/❌ | |
| Ports | All clear | ✅/❌ | |
| MCP | All servers responsive | ✅/❌ | |
| ADC | Auth working | ✅/❌ | |
| Memory | ulimit adequate | ✅/❌ | |

**ALL GREEN** → `✅ ENVIRONMENT VERIFIED. Sovereign operations authorized.`
**ANY RED** → `❌ ENVIRONMENT BLOCKED: [list issues]. Resolve before proceeding.`

---

## SECTOR 12 — Knowledge Graph Update (MCP)
Use `mcp_knowledge-graph_add_observations` to record:
- Environment state at verification time
- Any auto-heals applied
- Any persistent warnings documented for future sessions

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Environment verification complete.`
