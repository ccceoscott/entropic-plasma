---
description: Antigravity Agent Termination Diagnosis & Recovery — Phase 211.2 Sovereign Standard
alwaysApply: false
---

# INFINITY PROTOCOL v11.0 — /agent_termination
## Agent Hang / Termination Diagnosis & Recovery Protocol

> **Invoke when:** an agent turn hangs, a browser subagent fails to start, an MCP tool times out,
> a terminal `run_command` never returns, or the IDE stalls between turns.

> **Law:** NEVER use `kill -9` on MCP processes. The `mcp_watchdog.sh` cron (every 10 min) is the
> self-healing authority. Manual kills create zombie descriptors that cause worse hangs.

---

## §1 — Triage Decision Tree

```
Agent terminated or hung?
├── Did a browser_subagent call precede it?
│   └── → See §4: Browser Agent Recovery (MOST COMMON — check this first)
├── Is it a run_command that never returned?
│   └── → See §2: Terminal Hang Kill
├── Is it an MCP tool call that timed out?
│   └── → See §3: MCP Server Recovery
├── Is it a Firebase/Firestore operation?
│   └── → See §5: Firebase Context Drift
└── Unknown cause?
    └── → See §6: Nuclear Reset Sequence
```

---

## §2 — Terminal Hang Kill (run_command Sovereignty)

**Phase 57 / Phase 211.2 Law: run_command is BANNED for:**
- Any grep/search → use `grep_search` MCP (non-blocking)
- Any finalize/session op → use `write_to_file` / `multi_replace_file_content`
- Any network-touching call without explicit timeout
- `gcloud config get-value project` (blocks indefinitely in non-TTY)
- `npx playwright` (use `./node_modules/.bin/playwright`)
- `firebase emulators:exec` without `timeout 300`
- `session-proof.sh` or `tsc --noEmit` in drift_guard (belongs in session_start only)

**Recovery:** If `run_command` is hanging:
1. The user must manually kill it in the terminal with `Ctrl+C`.
2. Do NOT issue another `run_command` immediately — wait 2 turns.
3. Switch to the equivalent MCP tool or `grep_search` alternative.

**Safe alternatives table:**
| Banned | Sovereign |
|---|---|
| `run_command` grep | `grep_search` MCP |
| `gcloud config get-value project` | `.firebaserc` JSON parse (absolute path) |
| `npx playwright` | `./node_modules/.bin/playwright` |
| `npx tsc` | `./node_modules/.bin/tsc --noEmit` + `{ timeout: 60000 }` |
| `firebase firestore:rules > /tmp/...` | `mcp_firebase-mcp-server_firebase_get_security_rules` |
| `gcloud auth print-access-token` | `execSync('gcloud auth ...', { timeout: 8000 })` |
| drift_guard terminal commands | Read-only `view_file` on `MISSION_STATE.md` only |

---

## §3 — MCP Server Recovery

**Symptom patterns:**
- `calling "initialize": EOF` → server crashed on startup
- `Method not found` → protocol version mismatch or capability negotiation failure
- Tool call returns after 60s+ → server process hung on blocking I/O
- Tool not visible at all → config shadow issue (§3.4)

### §3.1 — Fallback Chain (Priority Order)

When a specific MCP server is dead, fall back in this order:

| Dead Server | Sovereign Fallback |
|---|---|
| `firebase-mcp-server` | `mcp_gcloud_run_gcloud_command` for GCS/IAM; `grep_search` for local state |
| `gcloud` | `mcp_firebase-mcp-server_*` tools; direct HTTPS via `read_url_content` |
| `knowledge-graph` | `view_file` on `/Users/teknojunkeee/.gemini/antigravity/knowledge-graph.jsonl` |
| `brave-search` | `mcp_firebase-mcp-server_developerknowledge_search_documents` or `read_url_content` |
| `chrome-devtools` | 5s wait then retry; fall back to `mcp_chrome-devtools_take_screenshot`; if dead → terminal curl |

### §3.2 — Self-Healing Wait Protocol

DO NOT restart MCP servers manually.
`mcp_watchdog.sh` runs every 10 minutes via cron and handles restarts.

**Protocol:**
1. Detect failure pattern (EOF, timeout, method not found)
2. Switch to fallback chain (§3.1) for current task
3. Wait for watchdog cycle (≤10 min) before retrying the failed server
4. Only escalate to user if: watchdog has run 2+ cycles and server still dead

### §3.3 — BRAVE_API_KEY Injection Fix

If `brave-search` crashes on startup (missing key):
```bash
# Add to ~/.zshrc (REQUIRED — NEVER hardcode in mcp_config.json)
export BRAVE_API_KEY="your_key_here"
```
Then restart the IDE. The `mcp_config.json` uses `${BRAVE_API_KEY}` which reads from the shell env.

### §3.4 — Config Shadow Detection

If MCP tools act on stale/wrong data:
1. Check: only ONE sovereign config must exist at `~/.gemini/antigravity/mcp_config.json`
2. Check: `~/.gemini/mcp_config.json` should NOT exist (or must be identical)
3. Resolution: `cp ~/.gemini/antigravity/mcp_config.json ~/.gemini/mcp_config.json` then full IDE restart

---

## §4 — Browser Agent Recovery (HIGHEST FREQUENCY TERMINATION VECTOR)

> **Phase 211.2 Law**: Before invoking ANY `browser_subagent`, you MUST load
> `.agent/rules/multiagent_laws.mdc` via `view_file` and verify Laws A1-A10 compliance.
> Skipping this check is the primary cause of recurring terminations.

**Root cause taxonomy (ordered by frequency):**

| # | Root Cause | Symptom | Fix |
|---|---|---|---|
| 1 | Task field > 400 words | Agent terminates immediately after subagent launch | Trim to ≤400 words, single objective |
| 2 | Missing `RecordingName` / `TaskSummary` / `TaskName` | Tool call rejected or silent fail | Add all 4 mandatory fields |
| 3 | Multi-objective task | Subagent enters infinite loop, parent waits forever | Decompose into sequential single-objective calls |
| 4 | Parallel browser_subagent calls | Page state corruption, both fail | Chain sequentially with `waitForPreviousTools: true` |
| 5 | Phantom purge inside Task field | No-op (subagent can't run rm -rf) | Move purge to separate `run_command` AFTER subagent returns |
| 6 | Subagent has no return condition | Runs forever | State explicit return condition in Task |
| 7 | No URL / no credentials in Task | Subagent can't start the flow | All task fields must be self-contained |

**Symptom:** `CORTEX_STEP_TYPE_OPEN_BROWSER_URL: action timed out, browser connection is reset`

**Recovery sequence:**
1. Wait 5s and retry `open_browser_url` once (slow boot race condition)
2. Try `about:blank` — if this also fails, the issue is internal to browser tooling
3. If internal: shift ALL browser verification to `chrome-devtools` MCP tools (Law A8):
   - `mcp_chrome-devtools_take_snapshot` → DOM state
   - `mcp_chrome-devtools_take_screenshot` → Visual verification
   - `mcp_chrome-devtools_navigate_page` → Navigation
   - `mcp_chrome-devtools_evaluate_script` → JS execution
4. After any successful browser session: **PHANTOM PURGE** (run immediately via `run_command`, `SafeToAutoRun: true`):
   ```bash
   rm -rf ~/.gemini/antigravity/browser_recordings
   ```

**Port conflict (Ghost Project):**
If browser navigates to wrong app on localhost:
1. Check document.title via `mcp_chrome-devtools_evaluate_script`
2. If wrong project: tell user to run:
   ```bash
   lsof -ti:5173,3000,4173,9099,8080,4400 2>/dev/null | xargs kill -9 2>/dev/null || true
   ```
3. Verify expected dev server starts on correct port before retrying

---

## §5 — Firebase Context Drift

**Symptom:** Firebase MCP returns data from the wrong project ("Ghost Project")

**Prevention:** Always run at workspace switch:
```
mcp_firebase-mcp-server_firebase_update_environment(
  project_dir: "/absolute/path/to/project",
  active_project: "correct-project-id"
)
```

**Recovery:**
1. `mcp_firebase-mcp-server_firebase_get_environment` → confirm current project
2. `mcp_firebase-mcp-server_firebase_update_environment` with correct `project_dir` + `active_project`
3. Verify with `mcp_firebase-mcp-server_firebase_get_project` → name should match expected

---

## §6 — Nuclear Reset Sequence

Use only when 3+ MCP servers are dead and watchdog has not healed after 20+ minutes.

**Steps (user executes manually):**
```bash
# 1. Kill all stray MCP node processes (safe — these are worker processes, not the IDE)
ps aux | grep 'mcp-deps' | grep -v grep | awk '{print $2}' | xargs kill 2>/dev/null || true

# 2. Kill dev server port squatters
lsof -ti:5173,3000,4173,9099,8080,4400 2>/dev/null | xargs kill -9 2>/dev/null || true

# 3. Phantom purge (safe — run_command SafeToAutoRun)
rm -rf ~/.gemini/antigravity/browser_recordings

# 4. Full IDE restart (Cmd+Shift+P → "Restart" or quit and reopen)
```

After restart: re-run `/session_start` before any work.

---

## §7 — Termination Audit Checklist

Run before declaring any session stable:

- [ ] All 5 MCP servers respond to a health ping
- [ ] Firebase MCP `active_project` matches current workspace `.firebaserc`
- [ ] No `run_command` blocking calls in any active workflow step
- [ ] No `session-proof.sh` or `tsc --noEmit` in `drift_guard.md` (Phase 211.2 FIXED)
- [ ] `multiagent_laws.mdc` has `alwaysApply: false` (Phase 211.2 FIXED)
- [ ] `browser_recordings` directory purged (if browser subagent was used)
- [ ] `BRAVE_API_KEY` injected via `~/.zshrc`, NOT hardcoded in `mcp_config.json`
- [ ] No duplicate `mcp_config.json` shadow at `~/.gemini/mcp_config.json`
- [ ] `mcp_watchdog.sh` cron is active: `crontab -l | grep mcp_watchdog`

---

## §8 — browser_subagent Pre-Invocation Checklist (Phase 211.2 — MANDATORY)

Before writing ANY `browser_subagent` call, verify ALL of the following:

```
[ ] TaskName     — ≤5 words, Title Case (e.g. "Verify Checkout Happy Path")
[ ] Task         — ≤400 words, ONE objective, self-contained URL + credentials + return condition
[ ] TaskSummary  — ≤2 sentences, user-facing goal description
[ ] RecordingName — ≤3 words, lowercase_underscores (e.g. "checkout_happy_path")
[ ] Sequential   — NOT running in parallel with another browser_subagent call
[ ] Single-obj   — Exactly ONE verifiable outcome, not a multi-step workflow chain
[ ] Return cond  — Explicit "return when you see X / screenshot Y / URL is Z" in Task
[ ] No code      — No bash commands or code blocks inside Task field
[ ] Phantom purge — Separate run_command AFTER subagent returns (NOT inside Task)
```

If ANY checkbox fails → **DO NOT invoke browser_subagent**. Fix the invocation first or use chrome-devtools MCP (Law A8).

---

> ⚡ Phase 211.2 Law: Three kills sealed. drift_guard terminal commands eradicated. multiagent_laws demoted. The fleet is sovereign. The wizard does not retry what was already wrong.
