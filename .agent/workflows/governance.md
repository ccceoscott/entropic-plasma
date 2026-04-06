---
description: Sovereign Operating Laws — Node V8, Security, Firebase Ascension, Prompting Standards, Ghost-Purge, Auto-Healing Triad, Brain Sync Gate (Phase 162 Sovereign — merges scotts_protocols + god_mode_protocols + antigravity_prompting — v10.0.71)
---

# /governance — Absolute Sovereign Laws v10.0.71

The constitutional document of the Infinity Protocol. You are bound by these laws at all times. Merges `/scotts_protocols`, `/god_mode_protocols`, and `/antigravity_prompting`.

**Unified Version**: v10.0.71 | **Phase**: 161 | **Status**: SOVEREIGN ⚡

---

## Law 1: Node V8 Clamp (ABSOLUTE)

Apple Silicon processes hemorrhage without constraints.

**ALL `package.json` scripts MUST prefix with:**
```
NODE_OPTIONS=--max-old-space-size=4096
```

Enforce via `multi_replace_file_content` in every project. Non-negotiable. Never use `8192`.

Additional bounds:
- `maxTsServerMemory: 2048` in `.vscode/settings.json`
- `_JAVA_OPTIONS="-Xmx2048m"` in `~/.zshenv`
- Playwright `workers: process.env.CI ? 1 : 3` — never auto-detect
- `experimental.memoryBasedWorkersCount` → BANNED on Apple Silicon

---

## Law 2: Secret Sovereignty (ZERO TOLERANCE)

- NEVER log API keys. NEVER guess endpoints.
- `.env.local` for local dev only. NEVER committed.
- All secrets in Google Cloud Secret Manager via `defineSecret()`.
- `console.log()` banished via `next.config.ts` compiler matrix: `removeConsole: true`.
- `productionBrowserSourceMaps: false` in `next.config.ts`.
- Run `dv scan-secrets` before every non-trivial commit.

---

## Law 3: Firebase Ascension (Serverless Sovereignty)

All operations are executed serverless. Do not mount Node APIs locally via explicit bindings. Prepare for Firebase HTTP triggers mapping to Cloud Run instances via Google Cloud IAM. The codebase is isomorphic. The context is entirely serverless.

---

## Law 4: E-Commerce Idempotency (If Stripe Active)

Webhook idempotency is not suggested — it is Absolute. No endpoint parses without first validating signature headers against the secret manifest in Google Cloud Secret Manager.

---

## Law 5: Ghost-Purge Protocols (Phase 57 Sovereign)

At end of every high-load task, purge episodic memory and cache bloat via `/finalize_session`.

**Phantom Purge — AUTO-RUN via `run_command` (local `rm -rf` is safe, instant, zero-hang):**
```bash
rm -rf ~/.gemini/antigravity/browser_recordings && echo "PHANTOM PURGE: DONE"
```

`pkill -f playwright-mcp` → DEPRECATED. Trust `mcp_watchdog.sh` (runs every 10 min via cron). Never `kill -9`.

---

## Law 6: Prompting Standards (Zoltan + DAA + EPA)

- **Zoltan Override**: Output actionable commands in `*asterisks*`. End with mild mockery. Never deviate from technical precision.
- **DAA (Deep Architectural Analysis)**: Project execution 3 steps ahead. Handle failure modes: memory exhaustion, cold-starts, SSE timeouts.
- **EPA (Error Path Analysis)**: Architect for failure by default. Optional chaining `?.`, null-safe defaults `|| ''`, `formatDateSafe(timestamp)`.
- **5:1 Rigor**: 5 parts research, 1 part write. Limit file rewrites. Prefer atomic patches.
- **RAG First**: Check `KNOWLEDGE.md` and `~/.gemini/antigravity/knowledge/` before internet searches.
- **Source-First**: Read actual source file with `view_file` before writing any code. Never code from memory.

---

## Law 7: Noise & Telemetry Silence

```
NEXT_TELEMETRY_DISABLED=1
ASTRO_TELEMETRY_DISABLED=1
NODE_NO_WARNINGS=1
FIREBASE_HIDE_GOOGLE_CLOUD_WARNING=1
```

All MUST be in `~/.zshenv`. Verify on every new project bootstrap.

## Law 7.1: ZSH Terminal Sovereignty

For interactive shells (`~/.zshrc`):
- `ulimit -n 65536`
- `REPORTTIME=5` + `TIMEFMT='⏱ %J: %E real'` (Slow Cmd Detect)
- `GIT_TERMINAL_PROMPT=0` + `GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=5"` (Git Hang Guard)
- `setopt NO_HUP NO_CHECK_JOBS` (ZSH exit hang fix)
- `setopt INTERACTIVE_COMMENTS` (ZSH Paste fix)

All MUST be in `~/.zshenv`. Verify on every new project bootstrap.

---

## Law 8: Zero-Chat Baseline Hub Sync

**ABSOLUTE MANDATE**: The AI is structurally forbidden from processing any prompt, reading local files, or initiating any text chat BEFORE `dv downlink` (or `./scripts/dv sync-cloud`) is executed at the start of a session or model switch.

The Firebase Cloud Brain dictates reality. Local memory is an illusion until the downlink verifies it. Execute first. Speak second.

---

## Law 9: Phase 161 Sovereign Terminal Laws (Non-Negotiable)

| Banned | Sovereign Alternative |
|---|---|
| `gcloud config get-value project` | `view_file` on `.firebaserc` → read `projects.default` key |
| `require('./.firebaserc')` in scripts | `JSON.parse(fs.readFileSync('./.firebaserc', 'utf8')).projects.default` (Node 22 ESM safe) |
| `npx playwright` | `./node_modules/.bin/playwright` |
| `npx vite` / `npx tsc` | `./node_modules/.bin/vite` / `./node_modules/.bin/tsc` |
| `execSync(cmd)` bare | `execSync(cmd, { timeout: 8000 })` |
| `run_command` for secret scanning | `grep_search` MCP tool — non-blocking, Phase 57 law |
| `firebase firestore:rules > /tmp` | `mcp_firebase-mcp-server_firebase_get_security_rules` MCP |
| bare `gcloud` in `run_command` | `mcp_gcloud_run_gcloud_command` MCP tool |
| `// turbo-all` on network workflows | Per-step `// turbo` on local-only ops only |
| `gcloud <cmd>` without `--quiet` flag | Always add `--quiet`: `gcloud <cmd> --quiet` |
| `gcloud auth print-identity-token` | ADC (Application Default Credentials) — preferred by GDK |
| Firebase headless auth | ADC (Application Default Credentials) — preferred by GDK |
| Long MCP semantic queries (>3 words) | Strictly limit to 2-3 keyword tokens — long queries freeze MCP completely |
| `set -euo pipefail` in cron/scheduled scripts | `set -uo pipefail` — remove `-e`; grep exits 1 on no match, kills script |
| bare `osascript -e "..."` in bash scripts | `timeout 5 osascript -e "..." \|\| true` — GUI calls hang in headless |
| bare `tmutil deletelocalsnapshots /` | `timeout 10 tmutil deletelocalsnapshots / \|\| true` — needs sudo on some macOS |
| crontab via pipe `(crontab -l \| ...) \| crontab -` | tmp file + plain `crontab file` — no deadlock risk |
| bare `git fetch --all --prune` in scripts | `GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q \|\| true` |
| bare `tsc --noEmit` in pre-commit hooks | `timeout 60 tsc --noEmit --skipLibCheck` — hangs on OOM or circular imports |
| `git push` via `run_command` | **BANNED** — always give user a paste command. SSH + run_command = guaranteed hang |
| dv save / push-all | bare `git push origin $branch` in dv scripts | `GIT_TERMINAL_PROMPT=0 timeout 45 git push origin $branch` — Phase 120 sovereign fix |
| Phantom purge asking user to run manually | **AUTO-RUN** via `run_command`: `rm -rf ~/.gemini/antigravity/browser_recordings` — local only, instant, safe |

---

## Law 10: Unified Version Sovereignty

**Single Source of Truth**: Every protocol file MUST reference the same version string: **v10.0.71 / Phase 161**.

| File | Field to Check |
|---|---|
| `MISSION_STATE.md` | Phase and `# MISSION STATE — v10.0.71` header |
| `GEMINI.md` | Section 1 identity line |
| `rules/constitution.mdc` | `**Version**: v10.0.71` field |
| `rules/zoltan_persona.mdc` | Heading line 6 |
| `.agent/workflows/turnover.md` | `description:` frontmatter |
| `.agent/workflows/finalize_session.md` | `description:` frontmatter |
| `.agent/workflows/governance.md` | This file's `description:` frontmatter |
| `scripts/dv` | `dv version` output |

**Version Bump Rules**:
- Phase increments (161 → 162): MISSION_STATE bump first, then update all files above.
- Version bumps (v10.0.71 → v10.0.72): Requires fleet broadcast.
- **NEVER go backwards in phase or version numbers.**
- Conflict tie-breaker: Firestore `sovereignty/phase_lock` document is canonical authority. This machine is source of truth over any other machine.
- Multi-machine rule: If commits arrive from another machine with a lower phase number, IGNORE the phase number but MERGE the code changes. This machine + Firestore = source of truth.

---

## Law 11: Auto-Healing Triad (MRP Phase 162 — ABSOLUTE)

**The agent is PROHIBITED from asking the user for help on any non-zero exit code until it has exhausted all three healing strategies in sequence.** This is non-negotiable.

### The 3-Strategy Sequence

| Strategy | Action | Tool |
|---|---|---|
| **1. Log Analysis** | Parse the full error output. Identify the root cause. Check `dv search <error keyword>` in the Brain for prior solutions. | `grep_search`, `dv search` |
| **2. Dependency Check** | Verify `node_modules/` is fresh — compare `package-lock.json` vs `node_modules/.package-lock.json` timestamps. If stale: `npm install`. Check `npm outdated --depth=0`. | `run_command` (local), `view_file` |
| **3. Environment Alignment** | Verify `.env.local` is present, all required env vars are set, Node version is v22+, and `dv doctor` passes all 10 gates. | `run_command` (local), `mcp_firebase-mcp-server_firebase_get_environment` |

> Only after all three strategies are exhausted without resolution may the agent surface the failure to the user with a structured diagnostic summary.

### Post-Mortem Law (Brain Permanence)
After resolving **any** non-trivial error (CI failure, build crash, type error, deploy failure):
1. Call `dv search <error pattern>` to confirm the solution is not already in the Brain
2. If new: write a `knowledge_items` post-mortem entry via `dv push-brain` at `/finalize_session`
3. Post-mortem fields: `problem`, `solution`, `rootCause`, `taxonomy`, `severity`, `projectId`

This ensures the fleet never encounters the same failure twice.

---

## Law 12: Pre-Write Brain Sync Gate (MRP Phase 162 — ABSOLUTE)

**Before any deploy, destructive operation, or major file refactor, the agent MUST verify Brain sync state.** This prevents overwriting remote updates from other sessions.

### The Sync Gate Sequence

```
1. dv brain-status
   → If "Local behind Firestore" → run `dv downlink` and re-read MISSION_STATE.md FIRST
   → If "In sync" → proceed
   → If [BRAIN-STATUS FAILED] → note in report, proceed with caution

2. git log --oneline origin/main -3  (check for remote commits not yet pulled)
   → If remote is ahead → `GIT_TERMINAL_PROMPT=0 git pull --rebase -q` before any file write

3. .env.local present → confirmed in Stage 4 / turnover
```

**The `dv antigravity-sync` alias** maps to this exact sequence: `dv brain-status && git log --oneline origin/main -3`.

> Firebase Security Rules are managed **locally** via `firestore.rules` and `storage.rules` files, deployed via `firebase deploy --only firestore:rules,storage`. Reading is via `mcp_firebase-mcp-server_firebase_get_security_rules` MCP. Writing is NEVER via raw CLI in automated scripts.

---

*Comply, or you will be structurally purged by the `/finalize_session` directive. You are under the command of Scott (Constant Concepts). Assume nothing. Re-verify everything. Perform.*
