---
description: ⚡ SESSION START PROTOCOL v5.0 — Sovereign Omniscience Engine. 20-stage intelligence handshake. Identity lock, KI ingest, security forensics, codebase integrity, TypeScript gate, dependency hygiene, process inventory, build cache intelligence, CI/CD status, rules audit, script arsenal, aesthetic compliance, live health probes, conversation forensics, autonomous intelligence, phase synthesis, quality scoring, and the Omniscience Report. Run at the START of every session or model switch. Pair with /finalize_session (SESSION END). The machine does not move until it knows exactly where it stands. (Phase 161 Sovereign — v10.0.71)
---

# /turnover — 🚀 SESSION START — Sovereign Omniscience Engine v5.0 (Phase 161 / v10.0.71)

> **ROLE DECLARATION**: This is the **SESSION START** protocol. It is the mandatory intelligence-gathering engine that runs at the *beginning* of every working session. Its counterpart is `/finalize_session`, which is the **SESSION END** protocol. These two are a sovereign pair — begin with `/turnover`, end with `/finalize_session`.

> **ABSOLUTE LAW**: You are **FORBIDDEN** from writing a single line of code, issuing any deploy command, or making any architectural decision until **ALL applicable stages** are complete and a **Turnover Report has been emitted in chat**. No exceptions. No overrides. No time pressure justifies skipping this. The machine does not act until it knows exactly where it stands.

---

## 🔰 PROTOCOL PREAMBLE

### Trigger Conditions — SESSION START
Run at **session start** on **ANY** of the following:
- Start of a new working session or any model switch
- User says: `turnover`, `handshake`, `get context`, `pick up`, `continue`, `resume`, `where were we`, `/session_start` (deprecated alias)
- After a conversation switch, IDE reload, or window swap
- Before any deploy, migration, or destructive operation
- After any gap > 60 minutes in active work

> **LIFECYCLE POSITION**: This is Stage 1 of the working session. After `/turnover` emits the Omniscience Report, proceed with work. When work is complete, run `/finalize_session` (Stage 2 — SESSION END).

### Speed Modes
| Mode | When | Stages |
|------|------|--------|
| **Full** | Fresh session, model switch, deploy prep | All 20 stages |
| **Express** | Same model, same session, < 30 min gap | 0, 1, 2, 3, 5, 6, 10, 12, 14, 19, 20 |
| **Flash** | Mid-task check, "what's the status?" | 0, 1, 20 (partial) |
| **Pre-Deploy** | Before any `firebase deploy` | 0, 1, 4, 6, 7, 8, 11, 16, 20 |

### Tool Priority Law (Inviolable)
```
view_file → grep_search → list_dir → mcp_* → run_command (local/turbo-tagged only)
```
> `run_command` is BANNED for: secret scanning, network calls, blocking ops, finalize steps.
> Every `run_command` in this workflow is tagged `// turbo` — they are ALL safe local ops.

---

## ⚡ STAGE 0 — Dead Reckoning (Always First, < 15 seconds)

**The machine checks if it was interrupted before checking anything else.**

// turbo
```bash
grep -E "^- \*\*(Suspend Point|Active CommandId|Next Action|Last Deploy Hash|Status)\*\*" \
  MISSION_STATE.md 2>/dev/null | head -10
```

**Decision Tree**:
| Finding | Immediate Action |
|---------|-----------------|
| `Active CommandId: <ID>` (not NONE/empty) | Call `command_status(<ID>)` NOW — may still be running |
| `Next Action: DEPLOY PENDING` | 🚨 P0 — interrupted mid-deploy. Check hosting state first |
| `Status: BLOCKED` | Read blocker detail before anything else in MISSION_STATE |
| `Status: DEGRADED` | Identify degraded systems before starting new work |
| `Status: SOVEREIGN` | Proceed through full protocol |

> If deploy was mid-stream → use `mcp_gcloud_run_gcloud_command` with `["alpha", "firebase", "hosting:channel:list", "--project", "<PROJECT_ID>", "--quiet"]` to check hosting state before touching code.

---

## 🔐 STAGE 1 — 4-Point Identity Lock (Disk + Live, No Memory)

**Never trust in-memory state after any model switch. Always read from disk.**

**Point 1 — MISSION_STATE.md** (use `view_file`, full file):

Extract verbatim into working state table:

| Field | Extracted Value | Source Line |
|-------|-----------------|-------------|
| Phase | | |
| Status | SOVEREIGN / BLOCKED / DEGRADED | |
| Project Name | | |
| Firebase Project ID | | |
| Last Updated | | |
| Last Deploy Hash | | |
| Last Deploy Timestamp | | |
| Suspend Point | | |
| Next Action | | |
| Primary Objective | | |

**Point 2 — .firebaserc verification** (use `view_file`):
```
.firebaserc → projects.default must == Firebase Project ID from MISSION_STATE
```

**Point 3 — Firebase MCP Live Auth**:
Call `mcp_firebase-mcp-server_firebase_get_environment`. Confirm:
- Authenticated user: `scott@constantconcepts.dev` (or project-appropriate)
- Active project: matches `.firebaserc` value exactly

**Point 4 — Conversation ID Cross-Check**:
The `CONVERSATION_ID` from the system metadata header MUST resolve to a readable brain directory:
```
~/.gemini/antigravity/brain/<CONVERSATION_ID>/
```
Use `list_dir` to confirm it exists. If not → this is a new conversation with no prior artifacts.

> **HARD STOP**: If Points 1, 2, or 3 mismatch → emit `🚨 IDENTITY BREACH: [Point N failed: expected X got Y]` and halt. The machine is contaminated. Do NOT proceed.

**Emit handshake** (required before continuing):
> *"Infinity Protocol v10.0 Active: In [PROJECT_NAME] (Firebase: [PROJECT_ID]), Phase [N] — [STATUS]. 4-point identity confirmed. Resuming from: [SUSPEND_POINT]."*

---

## 🧠 STAGE 1.5 — Firebase Brain Verification (Phase 161 Law)

**Immediately after identity confirmation. No code. No actions. Brain first.**

```bash
dv brain-status
```

**Parse the output:**
| Finding | Action |
|---|---|
| `✓ In sync` on both phase and GEMINI.md | Proceed to Stage 2 |
| `⚠ PHASE DRIFT` (Firestore behind Local) | Note drift. Last session likely missed `dv push-brain`. Proceed anyway — will be remediated at /finalize_session |
| `⚠ PHASE DRIFT` (Local behind Firestore) | 🚨 STOP — another session wrote to Brain while you were away. Run `dv downlink` and re-read MISSION_STATE.md |
| `[BRAIN-STATUS FAILED]` | Check ADC: `gcloud auth application-default login`. Non-blocking if still failing — note in Omniscience Report |
| No project state found | Run `dv push-brain` at END of this session (Stage 15A) to initialize Brain |

> **Permanent Constraints surfaced by brain-status**: These are MACHINE LAWS from the Brain. Print them verbatim in the Omniscience Report.

---

## 📦 STAGE 2 — Full Artifact Pipeline Ingest

**`[/]` items in task.md outrank all new requests without exception.**

**Tier 1 — Session Brain** (use `view_file` for each):
```
~/.gemini/antigravity/brain/<CONVERSATION_ID>/task.md
~/.gemini/antigravity/brain/<CONVERSATION_ID>/walkthrough.md
~/.gemini/antigravity/brain/<CONVERSATION_ID>/implementation_plan.md
```

Extract from task.md: all `[ ]`, `[/]`, and top 5 `[x]` items. Build Pending Work Stack.

**Tier 2 — Project Ground Truth** (use `view_file`):
```
<PROJECT_ROOT>/KNOWLEDGE.md     ← collection names, endpoints, known bugs, patterns
<PROJECT_ROOT>/GEMINI.md        ← local rule overrides (supersede global rules)
```

**Tier 3 — Visual State Audit**:
`list_dir` on `~/.gemini/antigravity/brain/<CONVERSATION_ID>/`:
- Note the LATEST `.webp`/`.png`/`.webm` artifact and its ISO timestamp
- If newest screenshot is > 24h old AND UI work is pending → add "Fresh visual verification needed" to P2 queue
- If newest screenshot is < 2h old → visual state is current

**Tier 4 — Cross-Conversation Artifact Check**:
For each conversation in the 3 most recent summaries (system metadata):
- Did any prior session leave an unfinished `implementation_plan.md`?
- Was a plan approved but never executed? (`user said "yes"` → no `[x]` completion)
- Those become P1 items in THIS session's pending stack.

---

## 🧠 STAGE 3 — KI Omniscience Ingest

**KIs are snapshots. Disk is truth. Use KI for LAWS and PATTERNS — verify against actual files.**

**Step A — Full Knowledge Graph**:
Call `mcp_knowledge-graph_read_graph`. Scan for:
- Entities tagged with current project name → extract all observations
- Entities with type `LAW`, `BLOCKER`, `VIOLATION` → highest priority
- Relations connecting current project to other projects (dependency blast radius)
- Any entity updated more recently than MISSION_STATE (signals post-session KI write)

**Step B — KI Directory Discovery** (use `list_dir`):
```
~/.gemini/antigravity/knowledge/
```
Sort by modification time mentally. Identify:
1. Any KI modified since the last session timestamp (new intelligence available)
2. Any KI matching current project name or phase number

**Step C — Mandatory KI Reads** (use `view_file`, most critical first):
```
~/.gemini/antigravity/knowledge/agency_owner_profile_and_preferences/artifacts/aesthetic_feedback_log.md
~/.gemini/antigravity/knowledge/agency_owner_profile_and_preferences/artifacts/overview.md
~/.gemini/antigravity/knowledge/infinity_protocol/artifacts/phase_69_4.md
~/.gemini/antigravity/knowledge/infinity_protocol_firebase_ascension/artifacts/firebase_ascension_session.md
~/.gemini/antigravity/knowledge/antigravity_ide_architecture/artifacts/antigravity_docs_session.md
```

**Step D — Phase KI** (use `view_file` if exists):
```
~/.gemini/antigravity/knowledge/infinity_protocol_phase<N>*/artifacts/*.md
```

**Step E — KI vs. Disk Conflict Detection**:
For any KI law that references a specific file or pattern, verify the actual file on disk matches. A KI that says "PageHero is in 9 pages" must be verified by Stage 5 grep — not trusted blindly.

> **OUTPUT**: Bulleted list of active KI laws constraining the next action. Flag any KI/disk conflicts as `⚠️ KI STALE: [what KI says] vs [what disk shows]`.

---

## 🔒 STAGE 4 — Full-Spectrum Security Sweep

**ALL scans use `grep_search` MCP. NO terminal grep. This is Phase 57 law.**

**Scan 1 — Credential Exposure** (HARD STOP if found in non-.env files):
Patterns sourced directly from `scripts/scan-secrets.sh`:
- `AAAA[0-9A-Za-z_-]{28}` → GCP Service Account Key
- `AIza[0-9A-Za-z_-]{35}` → Google API Key
- `sk_live_` → Stripe Live Secret
- `sk-proj-` → OpenAI Project Key
- `sk-ant-api` → Anthropic Claude Key
- `ghp_` → GitHub PAT
- `-----BEGIN RSA PRIVATE KEY-----` → Embedded Private Key
- `SG\.[a-zA-Z0-9_-]{22}` → SendGrid Key
- Query: `private_key` → SearchPath: `src/` — inline private key
- Query: `.env` → SearchPath: staged files — never commit .env files

> Do NOT scan `node_modules/`. Do NOT scan `.git/`.

**Scan 2 — Cross-Project Poison Strings** (bleed guard):
- Query: `Soul Contract` → SearchPath: `src/`
- Query: `CareKey` → SearchPath: `src/`
- Query: `SARAH` → SearchPath: `src/`
- Query: `FirstPick` → SearchPath: `src/`
- Query: `Infinity Press` → SearchPath: `src/` (unless this IS the Infinity Press project)

**Scan 3 — Banned Terminal Patterns** (Phase 57 sovereign):
- Query: `require('./.firebaserc')` → SearchPath: `scripts/` — BANNED in Node 22 ESM
- Query: `gcloud config get-value project` → SearchPath: `scripts/` — BANNED (hangs)
- Query: `npx playwright` → SearchPath: `scripts/` — BANNED (use direct binary)
- Query: `turbo-all` → SearchPath: `.agent/workflows/` — BANNED on network workflows
- Query: `execSync` → SearchPath: `functions/src/` — flag each without `{ timeout: N }`
- Query: `set -e` → SearchPath: `scripts/` — BANNED in cron scripts (grep exits 1)

**Scan 4 — Type Safety Surface**:
- Query: `: any` → SearchPath: `functions/src/` (flag; exclude test files)
- Query: `as any` → SearchPath: `src/` (flag count)
- Query: `@ts-ignore` → SearchPath: `src/` (flag each; each is a suppressed error)

**Scan 5 — Secrets History Check** (git log, local only):

// turbo
```bash
git log --all --oneline --diff-filter=D -- '.env*' 2>/dev/null | head -5
```
> If any `.env*` file was ever committed and deleted → flag as `⚠️ SECRET HISTORY: rotate any credentials from that era`.

**Scan 6 — .env.local Presence**:

// turbo
```bash
ls -la .env.local 2>/dev/null && echo "✅ .env.local PRESENT" || echo "🔴 .env.local MISSING — BUILD WILL FAIL"
```

> **TRIPLE HARD STOP on Scan 1**: Any live credential outside `.env.local` or `.env.example` → halt ALL operations, alert user with exact file:line, and do NOT proceed under any circumstance.

---

## 🌳 STAGE 5 — Codebase Structure Verification

**Read actual disk state. Never assume from memory, KI, or prior session.**

**Tier 1 — Full Directory Skeleton** (use `list_dir`):
```
src/app/dashboard/      → list ALL subdirs + confirm root page.tsx (Overview) exists
src/app/dashboard/*/    → confirm each subdir has a page.tsx
src/components/         → confirm: PageHero.tsx, SovereignHeader.tsx, CommandPalette.tsx
src/lib/                → confirm: utils.ts, firebase.ts
functions/src/          → confirm: index.ts, memory/, mcp/
.agent/workflows/       → list all — confirm no deprecated files without DEPRECATED header
rules/                  → list all .mdc files
scripts/                → note any new scripts added since last session
```

**Tier 2 — Targeted Integrity Assertions** (use `grep_search`):
- "PageHero" in `src/app/dashboard/` → must appear in ALL 9 subdirs + root `page.tsx` (10 files total)
- "NODE_OPTIONS" in `package.json` → must appear in EVERY script entry (not just some)
- "removeConsole" in `next.config.ts` → must be present
- "productionBrowserSourceMaps" in `next.config.ts` → must be `false`
- "LazyMotion" OR `import { m }` in `src/` → flag any bare `motion.` import (Framer bloat)
- "slate-" in `src/` → BANNED aesthetic token (see aesthetic_feedback_log)
- "zinc-" in `src/` → BANNED aesthetic token
- `style={{` in `src/` → flag count; inline styles break design system sovereignty

**Tier 3 — Function Manifest** (use `view_file` first 60 lines):
`functions/src/index.ts` → count `export const` lines. Note function names. Compare to MISSION_STATE function count. Delta means something deployed/removed since last session.

**Tier 4 — Script Arsenal Inventory** (reference `list_dir` from scripts/):
Confirm these sovereign scripts exist and are non-zero:
```
scripts/scan-secrets.sh     → Gate 11 pre-commit scanner
scripts/mcp_watchdog.sh     → MCP process supervisor
scripts/phantom_purge.sh    → Playwright zombie killer
scripts/sovereign_broadcast.sh → Fleet-wide broadcast
scripts/dv                  → Sovereign CLI (master tool)
scripts/pre-commit-enforce.sh → Git hook
```
Flag any missing script as a security gap.

> Document every expected file that is MISSING. These are BLOCKERS.

---

## 🔄 STAGE 6 — Git Delta Intelligence

// turbo
```bash
git log --oneline -10
```

// turbo
```bash
git log --oneline origin/main -10
```

// turbo
```bash
git status --short
```

**Sync State Decision Tree**:
| Condition | Required Action |
|-----------|-----------------|
| Local HEAD == Remote HEAD, clean | ✅ CLEAN |
| Local BEHIND remote by N | `GIT_TERMINAL_PROMPT=0 git pull --rebase -q` |
| Local AHEAD of remote by N | Will push at `/finalize_session` — acceptable |
| Uncommitted tracked changes | `git diff --stat HEAD` → classify, then stash/commit/discard |
| Uncommitted untracked files | Verify none are secrets before any commit |
| Merge conflict markers present | `grep_search` "<<<<<<" in `src/` — P0 blocker |

**Staging Area Check** (prevent corrupt partial commits):

// turbo
```bash
git diff --cached --stat 2>/dev/null | head -20
```
> If anything is already staged → classify it. A partial stage from a killed commit is a P0.

**Deploy Delta Classification**:
From MISSION_STATE extract `Last Deploy Hash`. Then:

// turbo
```bash
git diff <LAST_DEPLOY_HASH> HEAD --stat 2>/dev/null | head -60
```

Auto-classify each changed file path:
| Path Pattern | Rebuild Signal |
|--------------|----------------|
| `src/app/` or `src/components/` | Frontend changed → **rebuild required** |
| `functions/src/` | Backend changed → **functions redeploy required** |
| `next.config.ts` or `.env.local` | Config changed → **full rebuild required** |
| `*.md`, `MISSION_STATE`, `.agent/workflows/` | Docs only → **no rebuild needed** |
| `package.json` or `package-lock.json` | Deps changed → **npm install + rebuild** |

> **Final output**: `Rebuild: YES/NO | Functions: YES/NO | npm install: YES/NO | Docs-only: YES/NO`

---

## ⚙️ STAGE 7 — Environment & Stack Sovereignty

// turbo
```bash
node --version && npm --version
```
**Node gate**: Must be `v22.x.x`. Anything below = `⚠️ NODE VERSION MISMATCH`. Build will use wrong APIs.

// turbo
```bash
grep -n "NODE_OPTIONS" package.json 2>/dev/null
```
Every single npm script must contain `NODE_OPTIONS=--max-old-space-size=4096`. Report line numbers of any violations.

// turbo
```bash
ls -la .git/hooks/pre-commit 2>/dev/null && echo "✅ Hook active" || echo "⚠️ Pre-commit hook MISSING"
```

// turbo
```bash
crontab -l 2>/dev/null | grep -E "(mcp_watchdog|phantom)" | head -3 || echo "⚠️ Watchdog cron NOT found"
```

**VSCode Sovereignty** (use `view_file`):
`.vscode/settings.json` → confirm BOTH:
- `typescript.tsserver.maxTsServerMemory: 2048` (Apple Silicon law)
- `NEXT_TELEMETRY_DISABLED` referenced (telemetry silence)

> Missing either = Memory Sovereignty violation. Add to P2 queue.

---

## 🧬 STAGE 8 — TypeScript Integrity Gate

**Never write new features on a broken type foundation.**

// turbo
```bash
./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -25
```
*(No `timeout` wrapper on macOS — TSC exits cleanly or the user sees it hang and can kill it)*

**Error Classification**:
| TSC Result | Status | Action |
|------------|--------|--------|
| 0 errors | ✅ TYPE-SAFE | Proceed freely |
| 1-3 errors | 🟡 TYPE WARNINGS | Note and include in report — can proceed with caution |
| 4-10 errors | 🟠 TYPE DEBT | Add P1 remediation before ANY new feature work |
| 11+ errors | 🔴 TYPE CRITICAL | P0 blocker — fix before any other work |
| Process hangs > 60s | ⚠️ TSC OOM | Check `maxTsServerMemory` — likely `node_modules` OOM |

**Suppression Audit** (use `grep_search`):
- `@ts-ignore` in `src/` → each is a hidden time bomb; count and report
- `@ts-expect-error` in `src/` → acceptable pattern; note count
- `// eslint-disable` in `src/` → note count; flag if > 10

**Framer Motion Compliance** (use `grep_search`):
- `import { motion }` in `src/` → BANNED — use `m` from LazyMotion
- `motion.div` in `src/` → BANNED — use `m.div`
> Violations add ~90KB to bundle. Flag each file.

---

## 📦 STAGE 9 — Dependency & Build Cache Intelligence

**Stale deps and stale builds are the most common silent killers before a deploy.**

**Dep Freshness**:

// turbo
```bash
stat -f "%Sm — %N" -t "%Y-%m-%dT%H:%M" node_modules/.package-lock.json package-lock.json 2>/dev/null
```

| Comparison | Meaning |
|------------|---------|
| `node_modules/.package-lock.json` newer | ✅ Deps fresh |
| `package-lock.json` newer | ⚠️ STALE — run `npm install` before next build |
| `/node_modules/` missing | 🔴 CRITICAL — cannot build at all |

// turbo
```bash
npm outdated --depth=0 2>/dev/null | head -10 || echo "✅ All deps current"
```
Flag any security-relevant package upgrade (firebase-admin, next, framer-motion, zod).

**Build Cache Freshness**:

// turbo
```bash
stat -f "%Sm — %N" -t "%Y-%m-%dT%H:%M" .next/build-manifest.json 2>/dev/null || echo "⚠️ No .next/ build — full build required"
```

// turbo
```bash
stat -f "%Sm — %N" -t "%Y-%m-%dT%H:%M" functions/lib/index.js 2>/dev/null || echo "⚠️ No compiled functions — functions build required"
```

> If `.next/build-manifest.json` is older than the most recent source file change → **build is stale**. Add to deploy checklist.

---

## 🖥️ STAGE 10 — Hot Process & Port Inventory

**The most underused intelligence source. An 11-hour dev server is a ticking time bomb.**

// turbo
```bash
ps aux | grep -E "(next-server|node.*dev|vite|webpack)" | grep -v grep | awk '{print $2, $10, $11, $12}' | head -10
```

For each active process, extract:
- **PID** — to monitor
- **Runtime** — calculate from start time vs now (flag anything > 4 hours)
- **Port** — to check for conflicts

// turbo
```bash
lsof -ti:3000 2>/dev/null | head -3 && echo "Port 3000 occupied" || echo "Port 3000 free"
lsof -ti:5001 2>/dev/null | head -3 && echo "Port 5001 occupied (emulator)" || echo "Port 5001 free"
```

**Decision Table**:
| Condition | Action |
|-----------|--------|
| Next dev server running < 4h | ✅ Healthy — note PID for report |
| Next dev server running > 12h | ⚠️ STALE PROCESS — mcp_watchdog should have killed it. Note PID. |
| Dev server on wrong port (not 3000) | 🔴 PORT CONFLICT — builds will fail to hot-reload |
| Multiple dev servers running | 🔴 ZOMBIE FLEET — kill secondary processes |
| Functions emulator running | Note port 5001/8080 — will conflict if you start another |

**Browser Recording Bloat**:

// turbo
```bash
du -sh ~/.gemini/antigravity/browser_recordings/ 2>/dev/null || echo "Directory empty/missing"
```
- > 500MB → Add to report: "🗑️ PHANTOM PURGE NEEDED — tell user to run `rm -rf ~/.gemini/antigravity/browser_recordings/`"

---

## 📡 STAGE 11 — Live System Health Probes

**All probes use sovereign curl with hard timeouts. A timeout is non-blocking — noted, not blocking.**

**Cloud Hub Uplink**:
// turbo
```bash
curl -s --connect-timeout 4 --max-time 8 -o /dev/null -w "Hub: %{http_code}\n" \
  "https://mcpserver-g5pod66w5a-uc.a.run.app/ping" 2>/dev/null || echo "Hub: COLD/UNREACHABLE"
```

**Production Hosting**:
// turbo
```bash
curl -s --connect-timeout 4 --max-time 8 -o /dev/null -w "Live: %{http_code}\n" \
  "https://gen-lang-client-0386732425.web.app" 2>/dev/null || echo "Live: UNREACHABLE"
```
> `404` on production = active incident. Elevate to P0 immediately.

**Firebase Functions** (MCP):
Call `mcp_firebase-mcp-server_functions_list_functions` → count deployed functions. Compare to local `functions/src/index.ts` export count. A delta of:
- `+N` deployed (more than local) → functions removed locally but not yet redeployed
- `-N` deployed (fewer than local) → new functions added locally but not yet deployed

**MCP Server Inventory** (use `view_file`):
```
~/.gemini/antigravity/mcp_config.json
```
Map each configured server to: ✅ Installed | ⚠️ Ghost (configured, not installed) | ❌ Missing.
Ghost nodes silently fail tool calls — they must be audited before relying on ANY MCP tool.

---

## 🎭 STAGE 12 — Rules & Workflow Governance Audit

**Rules drift silently. Workflows can contradict each other. The fleet rots without auditing.**

**Rules Audit** (use `list_dir` + `grep_search`):

`list_dir` on `rules/` → for each `.mdc` file:
- Does it have `alwaysApply: true`? → flag for monthly review (always-apply rules add latency)
- Is it in the superseded list from `scripts/clean-rules.sh`? → should be deleted
- Does it reference any other project name? → cross-project contamination

**Workflow Consistency Check** (use `grep_search`):
- "gen-lang-client-0386732425" in `.agent/workflows/` → must appear ONLY for this project's workflow references
- "DEPRECATED" in `.agent/workflows/*.md` → must have a `See /replacement` reference
- "turbo-all" in `.agent/workflows/` → BANNED on any workflow with network calls

**GEMINI.md Drift Detection** (use `view_file` + `view_file`):
1. View `GEMINI.md` in project root
2. View `~/.gemini/GEMINI.md` (global rules)
3. Identify any laws in global NOT present in local — they should be in sync
4. Identify any local overrides — are they intentional? Document.

**Playwright Guardian Compliance** (use `grep_search`):
- "video: 'off'" in `playwright.config.ts → must be present
- "workers: process.env.CI" in `playwright.config.ts` → must use `CI ? 1 : 3` pattern
- "webServer" in `playwright.config.ts` → BANNED when running under emulators:exec

---

## 🎨 STAGE 13 — Aesthetic Compliance Scan

**Visual splendor is non-negotiable. Banned tokens indicate aesthetic degradation.**

**Use `grep_search` for all scans:**

**Banned Color Tokens** (see aesthetic_feedback_log.md):
- `slate-` in `src/` → BANNED — violates Scott's dark mode standard
- `zinc-` in `src/` → BANNED — violates dark mode standard  
- `gray-` in `src/` → BANNED unless intentional neutral — flag and verify
- `text-gray` in `src/` → flag instances

**Premium Standard Verification**:
- `backdrop-blur` in `src/components/` → ✅ glassmorphism present
- `border-white/` in `src/components/` → ✅ liquid glass borders present
- `framer-motion` or `LazyMotion` in `src/app/layout.tsx` → must be present
- Google Font import in `src/app/layout.tsx` → must exist (no browser default fonts)

**Inline Style Violations**:
- `style={{` in `src/` → count; each bypasses the design system. > 5 = architecture concern

**TODO/FIXME Debt**:
- `TODO` in `src/` → count open items
- `FIXME` in `src/` → count; each is a known bug deferred
- `HACK` in `src/` → count; each is a ticking time bomb

> Output: Aesthetic score as `EXCELLENT / GOOD / DEGRADED / CRITICAL` based on violation density.

---

## 🔍 STAGE 14 — Conversation Forensics Engine

**The conversation log contains the user's actual intent. It is the highest-fidelity source of truth for pending work.**

**Primary source** (use `view_file`, last 150 lines):
```
~/.gemini/antigravity/brain/<CONVERSATION_ID>/.system_generated/logs/overview.txt
```

**Signal Mining Table**:

| Signal Type | Pattern to Detect | Assigned Priority |
|-------------|------------------|--------------------|
| **Unresolved promise** | "I will...", "I'll fix...", "Coming up next...", "TODO:" with no `✅` after | P0 |
| **User frustration** | "again", "still broken", "WHY", "you didn't", "I already told you", "again?!" | P0 — address FIRST |
| **Interrupted deploy** | `firebase deploy` command with no `✅ Deploy complete` line after | P0 |
| **Approved plan not executed** | User said "yes"/"go ahead"/"do it" with no code artifact after | P1 |
| **Partial implementation** | "let's also do X" or "add Y too" mid-task with no confirmation | P1 |
| **Suppressed issue** | "fix this later", "leave for now", "we'll sort this out" | P2 |
| **User preference signal** | "I like...", "make it more...", "less..." → update aesthetic log | P2 → add to KI |
| **Known workaround** | "for now just..." | P3 — note for Phase cleanup |

**Cross-Session Forensics** (from 3 recent conversation summaries in metadata):
- Did any other project's session reference a shared file (e.g., `GEMINI.md`, a workflow) that this project also uses?
- Was any new law added to the global protocol that hasn't been propagated to THIS project?

> **Output**: Ranked Forensics Table with every open signal and its assigned priority.

---

## 🚦 STAGE 15 — CI/CD Pipeline Status

**A failed CI pipeline means the last push didn't pass. This matters before any new deploy.**

// turbo
```bash
gh run list --repo ccceoscott/infinity-protocol --limit 5 --json status,conclusion,name,createdAt \
  2>/dev/null | head -50 || echo "⚠️ gh CLI not available or not logged in"
```

**Classify last run**:
| Status | Conclusion | Action |
|--------|------------|--------|
| completed | success | ✅ CI clean — deploy safe |
| completed | failure | 🔴 CI BROKEN — investigate before next deploy |
| in_progress | — | ⚠️ CI RUNNING — wait before pushing new commits |
| cancelled | — | Note — investigate if intentional |

> If CI is broken → read the failure reason before starting any new work. A broken CI means the production deploy pipeline is blocked.

---

## 🧠 STAGE 16 — KI vs. Disk Conflict Resolution

**This is the intelligence integrity check. KIs make assertions. Disk proves or disproves them.**

For each KI law or assertion that references a specific measurable fact (file exists, pattern present, count of functions, count of dashboard pages), verify against disk findings from Stages 5-15:

**Conflict Resolution Matrix**:
| KI Assertion | Disk Reality | Resolution |
|---|---|---|
| "PageHero in 9 pages" | grep found 8 | 🔴 CONFLICT — disk wins, Overview missing |
| "14 functions deployed" | functions/src has 12 | 🔴 CONFLICT — 2 functions in KI are phantom |
| "NODE_OPTIONS on all scripts" | package.json missing in 2 scripts | 🔴 CONFLICT — KI is stale |
| Assertions match disk | — | ✅ KI is current |

Mark each conflicting KI assertion as `STALE` in your working context. Disk wins. Always.

Then write a recommended KI update for each stale assertion (to be executed during `/finalize_session`).

---

## 🌐 STAGE 17 — Autonomous Intelligence Engine

**Transform all data collected into an actionable strategic picture.**

**A — Phase Completion Analysis**:
Based on task.md, walkthrough.md, and MISSION_STATE:
- Count `[x]` / total task items → calculate completion percentage
- If ≥ 80% complete → draft Phase [N+1] scope
- If ≤ 20% complete AND phase > 2 weeks old → current phase is stalled → diagnose root cause

**B — Priority-Ranked Action Queue**:
Using ALL signals from Stages 0-16, produce:
```
P0 — blockers (must resolve before anything else):
  P0-1: [Action] → [exact tool/command to execute]
  P0-2: [Action] → [exact tool/command]

P1 — unresolved promises / in-progress work:
  P1-1: [Action] → [exact tool/command]

P2 — pending tasks / tech debt:
  P2-1: [Action] → [exact tool/command]

P3 — opportunistic improvements:
  P3-1: [Action] → [exact tool/command]
```

**C — Proactive Intelligence (what the user didn't ask but should know)**:
- Any new KIs since last session that introduce new laws or patterns
- Protocol drift: is this project behind the fleet standard?
- Security surface changes since last deploy
- Aesthetic violations accumulating toward threshold
- Dependency security advisories for installed packages
- Browser recording bloat or phantom process alert if detected

**D — Phase [N+1] Scope Draft** (if Phase N ≥ 80% complete):
Draft 4-6 bullet points for the next phase based on:
- Known trajectory from MISSION_STATE
- Owner's preferences from KI (aesthetic goals, performance targets)
- Outstanding technical debt from the current phase
- Any user features mentioned but not yet started

---

## 📊 STAGE 18 — Turnover Quality Scoring

**Self-assess the completeness of this turnover before emitting the report.**

Score each dimension (full points if fully completed, partial if data was unavailable):

```
Identity Lock        : __/25  (5 pts each: MISSION_STATE, .firebaserc, Firebase MCP, Conversation ID, handshake emitted)
Artifact Ingest      : __/15  (5 pts each: task.md, walkthrough.md, KNOWLEDGE.md)
KI Intelligence      : __/15  (5 pts: graph read, mandatory KIs, phase KI)
Security Sweep       : __/15  (3 pts each: credential, poison, banned patterns, .env.local, history)
Codebase Integrity   : __/10  (2 pts each: dir skeleton, assertions, function manifest, scripts, framer compliance)
Git State            : __/10  (stage area, sync state, deploy delta classification)
TypeScript Gate      : __/5   (ran tsc, classified result)
Process Inventory    : __/5   (dev server age, port conflicts, recording bloat)
Forensics           : __/5   (mined overview.txt, cross-session check)
Intelligence Engine  : __/5   (phase %, action queue, proactive observations)
                    ━━━━━━━
TOTAL               : __/110
```

**Scoring Thresholds**:
| Score | Rating | Meaning |
|-------|--------|---------|
| 100-110 | 🟢 OMNISCIENT | Full intelligence — maximum confidence |
| 85-99 | 🟡 HIGH CONFIDENCE | Minor gaps — proceed with awareness |
| 70-84 | 🟠 MODERATE | Notable gaps — flag what was skipped |
| < 70 | 🔴 LOW CONFIDENCE | Significant gaps — user should be warned |

---

## 📋 STAGE 19 — Self-Healing Recommendations

**What would make the NEXT turnover faster, more complete, or more accurate?**

Based on what was difficult, missing, or surprising in this turnover:

**Infrastructure Gaps** (things that had to be skipped or guessed):
- If a mandatory file was missing → add creation to `/bootstrap_new_project` workflow
- If a KI was stale → schedule KI refresh during next `/finalize_session`
- If a script was missing → add scaffolding to `/governance`
- If MISSION_STATE had missing fields → propose MISSION_STATE schema update

**Protocol Evolution Proposals**:
- If any new banned pattern was found that isn't in `scan-secrets.sh` → add it
- If a new file type should be in the turnover checklist → note it
- If any stage took too long (e.g., TSC was slow) → document the optimization

> These recommendations are written to the Turnover Report as `🔧 PROTOCOL IMPROVEMENTS` and queued for `/finalize_session` KI write.

---

## 🖨️ STAGE 20 — Sovereign Omniscience Report (REQUIRED OUTPUT)

**This is the machine's binding declaration of known state. Nothing executes until this is emitted.**

```
╔══════════════════════════════════════════════════════════╗
║  ⚡ SOVEREIGN OMNISCIENCE REPORT v4.0                    ║
║  [ISO TIMESTAMP] | Infinity Protocol v10.0               ║
╚══════════════════════════════════════════════════════════╝

🔐 IDENTITY (4-Point Locked)
  Project   : [PROJECT_NAME]
  Firebase  : [PROJECT_ID]
  Phase     : [N] | [SOVEREIGN / BLOCKED / DEGRADED]
  Auth User : [email]
  Objective : [PRIMARY_OBJECTIVE_ONE_LINE]
  Suspended : [SUSPEND_POINT]

📦 PENDING WORK STACK (priority-ordered)
  🚨 P0 Promises  : → [unresolved promise 1]
                    → [unresolved promise 2]
  🔄 In-Progress  : → [task.md [/] item 1]
  📌 Queued       : → [task.md [ ] item 1]
                    → [task.md [ ] item 2]
  ✅ Completed    : → [top 3 from last session]

🖥️ OPEN FILE SIGNALS
  → [file]: [what user was working on / inference]
  → [file]: [inference]

🔒 SECURITY SURFACE
  Credentials : [✅ CLEAN / 🔴 FOUND: file:line → action required]
  Poison str  : [✅ CLEAN / 🔴 FOUND: string in file]
  History     : [✅ CLEAN / ⚠️ .env committed at <hash>]
  Banned pats : [✅ CLEAN / 🟡 N violations: list]
  .env.local  : [✅ PRESENT / 🔴 MISSING]
  any count   : [src: N, functions: N]

🌳 CODEBASE INTEGRITY
  PageHero    : [N/9 pages ✅ / MISSING: page_name]
  Framer      : [✅ m. only / 🟠 motion. in: file_list]
  Aesthetic   : [EXCELLENT / GOOD / DEGRADED: slate- N violations]
  Functions   : [local: N | deployed: N | delta: ±N]
  TODOs       : [N open / FIXME: N / HACK: N]
  @ts-ignore  : [N instances]

🔄 GIT STATE
  Local HEAD  : [HASH] — [N ahead / N behind / CLEAN]
  Remote main : [HASH]
  Staged      : [N files / CLEAN — no partial commit risk]
  Deploy delta: [N src files changed / docs-only / NONE]
  Build needed: [Rebuild: YES/NO | Functions: YES/NO | npm install: YES/NO]

⚙️ ENVIRONMENT SOVEREIGNTY
  Node    : [vX.X.X ✅/⚠️] | npm: [vX.X.X]
  NODE_OPT: [✅ all scripts / 🔴 missing from: script_names]
  TSC     : [✅ 0 errors / 🟡 N warnings / 🔴 N errors]
  Deps    : [✅ Fresh / 🟡 Stale / 🔴 Missing]
  Hook    : [✅ Present / ⚠️ Missing]
  Watchdog: [✅ Cron active / ⚠️ Not in crontab]

🚦 PROCESS INVENTORY
  Dev Server: [PID XXXX — running Nh Nm / ⚠️ STALE > 12h / NOT RUNNING]
  Port 3000 : [OCCUPIED / FREE]
  Port 5001 : [OCCUPIED (emulator) / FREE]
  Recordings: [✅ Clean / 🗑️ NMB — tell user to purge]

📡 LIVE SYSTEM HEALTH
  Cloud Hub : [✅ 200 / ⚠️ cold]
  Live Site : [✅ 200 / 🔴 degraded]
  MCP Stack : [N/N servers — ghosts: list]
  CI/CD     : [✅ passing / 🔴 FAILED: workflow_name]
  Functions : [N deployed / delta: ±N vs local]

🧠 ACTIVE KI LAWS
  → [Law]: [one-line constraint on next action]
  → [Law]: [one-line constraint]
  ⚠️ KI STALE: [assertion] → [disk reality]

🔍 FORENSICS FLAGS
  [P0]: [signal] → [exact fix]
  [P1]: [partial work] → [resume point]
  [P2]: [suppressed issue] → [when to address]

🎯 ACTION QUEUE (execute in this exact order)
  P0-1: [Action] → [exact command/tool]
  P0-2: [Action] → [exact command/tool]
  P1-1: [Action] → [exact command/tool]
  P2-1: [Action] → [exact command/tool]

📈 PHASE INTELLIGENCE
  Phase [N] completion : [N]% ([X] of [Y] tasks done)
  Phase [N+1] scope    : [ready / pending / draft:]
    → [bullet 1]
    → [bullet 2]

📊 TURNOVER QUALITY SCORE
  [N]/110 — [🟢 OMNISCIENT / 🟡 HIGH CONFIDENCE / 🟠 MODERATE / 🔴 LOW CONFIDENCE]
  Gaps: [list any skipped stages or missing data]

🔧 PROTOCOL IMPROVEMENTS
  → [recommendation for next turnover]

╔══════════════════════════════════════════════════════════╗
║  ONE-TAP FIRST ACTION:                                   ║
║  [Single exact command or tool call to begin work]       ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🧬 ANNEXE A — Speed Mode Stage Map

| Stage | Full | Express | Flash | Pre-Deploy |
|-------|------|---------|-------|------------|
| 0 Dead Reckoning | ✅ | ✅ | ✅ | ✅ |
| 1 Identity Lock | ✅ | ✅ | ✅ | ✅ |
| 2 Artifact Ingest | ✅ | ✅ | — | — |
| 3 KI Ingest | ✅ | ✅ | — | — |
| 4 Security Sweep | ✅ | — | — | ✅ |
| 5 Codebase Structure | ✅ | ✅ | — | — |
| 6 Git Delta | ✅ | ✅ | — | ✅ |
| 7 Environment | ✅ | — | — | ✅ |
| 8 TypeScript Gate | ✅ | — | — | ✅ |
| 9 Dependency/Cache | ✅ | — | — | ✅ |
| 10 Process Inventory | ✅ | — | — | — |
| 11 Live Health | ✅ | — | — | ✅ |
| 12 Rules Governance | ✅ | — | — | — |
| 13 Aesthetic Scan | ✅ | — | — | — |
| 14 Conversation Forensics | ✅ | ✅ | — | — |
| 15 CI/CD Status | ✅ | — | — | ✅ |
| 16 KI vs. Disk Conflicts | ✅ | ✅ | — | — |
| 17 Intelligence Engine | ✅ | ✅ | — | — |
| 18 Quality Score | ✅ | — | — | — |
| 19 Self-Healing | ✅ | — | — | — |
| 20 Report | ✅ | ✅ | ✅ | ✅ |

---

## 🧬 ANNEXE B — Hard Banned Anti-Patterns

| Anti-Pattern | Why Banned | Sovereign Alternative |
|---|---|---|
| "Based on our previous conversation..." | Memory is volatile and unverified post-switch | `view_file` MISSION_STATE.md — disk is law |
| Starting code before Stage 20 | Protocol violation — machine is acting blind | Emit report first. Always. |
| `run_command` for secret scanning | Blocking, Phase 57 law violation | `grep_search` MCP tool |
| `require('./.firebaserc')` in scripts | Crashes in Node 22 ESM | `JSON.parse(fs.readFileSync('.firebaserc', 'utf8'))` |
| Treating KI as ground truth | KIs can be months stale | Stage 16 conflict resolution — disk wins |
| Skipping conversation forensics | Misses unresolved promises → breaks trust | Stage 14 mandatory in Full and Express |
| Guessing open file intent without reading | Inference errors cause wrong P0 assignments | `view_file` first 30 lines of each open file |
| Assuming PageHero is in 9 pages | Was proven wrong — Overview was missed | `grep_search` every time, no assumption |
| Skipping process inventory | 11h dev server = stale state, port conflicts | Stage 10 mandatory in Full mode |
| Skipping build cache check | Stale .next/ silently serves old build | Stage 9 mandatory before every deploy |
| `kill -9` on MCP processes | Corrupts MCP state — watchdog handles it | Trust `mcp_watchdog.sh` — kill only after > 2h orphan |

---

## 🧬 ANNEXE C — Emergency Override Protocols

**MISSION_STATE.md missing or corrupt:**
1. `list_dir` root → confirm file absence
2. `git log --oneline -- MISSION_STATE.md | head -5` → find last known good version
3. `git show <HASH>:MISSION_STATE.md | head -40` → read last version
4. Reconstruct from: walkthrough.md + task.md + conversation log tail
5. Write new MISSION_STATE.md from reconstruction — note "(RECONSTRUCTED)" in Status

**.firebaserc missing:**
1. `mcp_firebase-mcp-server_firebase_get_environment` → get active project
2. Propose `firebase use <id>` to regenerate (user must approve — writes to disk)
3. Re-run Stage 1 Point 2 before proceeding

**node_modules missing entirely:**
1. Halt ALL work
2. Propose `npm install` (user must approve — unsafe operation)
3. After install: re-run Stages 9, 8 before any build

**All MCP servers unresponsive:**
1. Fall back to: `view_file`, `grep_search`, `list_dir`, `run_command` (local only)
2. Do NOT use ANY `mcp_firebase-*` or `mcp_gcloud_*` tools
3. Add to report: "⚠️ MCP DARK — operating in disk-only mode"
4. Do NOT attempt Firebase deploys without MCP identity confirmation

---

*Status: Sovereign Omniscience Engine v5.0 — SESSION START PROTOCOL — 20 stages. 4-point identity lock. Full-spectrum forensics. Autonomous intelligence synthesis. Quality scoring. Self-healing protocol evolution. Paired with `/finalize_session` (SESSION END). The machine knows exactly where it stands, or it does not move. The machine that cannot see itself cannot be trusted to build anything worth standing on. — Phase 161 Sovereign / v10.0.71*
