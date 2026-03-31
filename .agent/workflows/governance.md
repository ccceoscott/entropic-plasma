---
description: Sovereign Operating Laws — Node V8, Security, Firebase Ascension, Prompting Standards, Ghost-Purge (Phase 57 Sovereign — merges scotts_protocols + god_mode_protocols + antigravity_prompting)
---

# /governance — Absolute Sovereign Laws

The constitutional document of the Infinity Protocol. You are bound by these laws at all times. Merges `/scotts_protocols`, `/god_mode_protocols`, and `/antigravity_prompting`.

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

**User runs manually in their terminal (NEVER via `run_command`):**
```
rm -rf ~/.gemini/antigravity/browser_recordings/
rm -rf ~/.npm/_npx/
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

## Law 7: Telemetry Silence

```
NEXT_TELEMETRY_DISABLED=1
ASTRO_TELEMETRY_DISABLED=1
```

Both MUST be in `~/.zshenv`. Verify on every new project bootstrap.

---

## Law 8: Zero-Chat Baseline Hub Sync

**ABSOLUTE MANDATE**: The AI is structurally forbidden from processing any prompt, reading local files, or initiating any text chat BEFORE `dv downlink` (or `./scripts/dv sync-cloud`) is executed at the start of a session or model switch.

The Firebase Cloud Brain dictates reality. Local memory is an illusion until the downlink verifies it. Execute first. Speak second.

---

## Law 9: Phase 57 Sovereign Terminal Laws

| Banned | Sovereign Alternative |
|---|---|
| `gcloud config get-value project` | `node -e "console.log(require('./.firebaserc').projects.default)"` |
| `npx playwright` | `./node_modules/.bin/playwright` |
| `npx vite` / `npx tsc` | `./node_modules/.bin/vite` / `./node_modules/.bin/tsc` |
| `execSync(cmd)` | `execSync(cmd, { timeout: 8000 })` |
| `run_command` in finalize | `write_to_file` / `grep_search` MCP tools |
| `grep` via `run_command` | `grep_search` MCP tool |
| `firebase firestore:rules > /tmp` | `firebase_get_security_rules` MCP |
| bare `gcloud` in terminal | `mcp_gcloud_run_gcloud_command` MCP |
| `// turbo-all` on network workflows | per-step `// turbo` on local-only only |
| `run_command` phantom purge | Tell user to run manually in terminal |
| `gcloud <cmd>` without `--quiet` | Always add `--quiet` flag |
| `gcloud auth print-identity-token` | `FIREBASE_TOKEN` via `firebase login:ci` |
| `mcp_google-developer-knowledge` | Long semantic queries cause infinite stall; strictly limit to 2-3 explicit keyword tokens. |

*Comply, or you will be structurally purged by the `/finalize_session` directive. You are under the command of Scott (Constant Concepts). Assume nothing. Re-verify everything. Perform.*
