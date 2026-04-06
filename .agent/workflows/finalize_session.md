---
description: 🏁 SESSION END PROTOCOL v5.0 — Sovereign Close-of-Session Engine. 9 execution phases, 24 stages. Forensics, Security Clearance, Knowledge Permanence, State Reconciliation, Cloud Synchronization, Version Control + CI/CD Verification, Process Hygiene + Dependency Audit, Intelligence Synthesis, and Receipt Emission. Firebase rules validation, dev server error log harvest, aesthetic compliance scan, environment key parity, CI/CD status post-push, dependency drift audit, Node version sovereignty, and codebase snapshot metrics. Paired with /turnover (SESSION START). Every session ends with omniscient clarity, zero security debt, and a pre-staged next-session entry point. (Phase 161 Sovereign — v10.0.71)
---

# /finalize_session — 🏁 SESSION END — Sovereign Close-of-Session Engine v5.0 (Phase 161 / v10.0.71)

> **ROLE DECLARATION**: This is the **SESSION END** protocol. Run this at the *end* of every working session. Its counterpart is `/turnover`, which is the **SESSION START** protocol. These two are a sovereign pair — begin with `/turnover`, end with `/finalize_session`.

> **PURPOSE**: Converts a live session's ephemeral working memory into permanent, structured, verifiable artifacts across disk, the knowledge graph, and Firestore — then closes all process debt, validates the security posture, verifies CI/CD landed, scores the session, and emits a binding finalization receipt with a pre-generated next-session entry prompt.

> **MANDATE**: Run at the end of every session. No exceptions. A session that ends without finalization leaves the machine in an undefined state. Undefined machines cause drift, phantom bugs, and compounding context debt across model switches.

> **TIMING LAW**: Full sovereign execution takes 12-18 minutes. Do not rush. The cost of shortcutting this protocol is paid at 10x at the start of the next session.

> **PHASE STRUCTURE**: v5.0 organizes 24 stages into 9 execution phases. Each phase has a clear boundary and can be executed independently in speed-mode variants. See Annexe A.

---

## ⚠️ ABSOLUTE SOVEREIGN LAWS (INVIOLABLE — READ BEFORE EXECUTING)

| Operation | Status | Sovereign Alternative |
|---|---|---|
| `gcloud auth print-identity-token` | ❌ BANNED | ADC / Firebase MCP tool |
| `gcloud config get-value project` | ❌ BANNED (hangs) | `view_file` on `.firebaserc` |
| `git fetch` without guards | ❌ BANNED | `GIT_TERMINAL_PROMPT=0 timeout 30 git fetch` |
| `npx playwright` or bare `tsc` | ❌ BANNED | `./node_modules/.bin/playwright` / `./node_modules/.bin/tsc` |
| `curl` to `onCall` Firebase endpoints | ❌ BANNED | Firestore MCP write or `test_all_connectivity.sh` |
| `run_command` for secret scanning | ❌ BANNED | `grep_search` MCP — non-blocking |
| `// turbo-all` annotation | ❌ BANNED | Per-step `// turbo` only on confirmed local-only ops |
| `kill -9` on MCP processes | ❌ BANNED | `scripts/phantom_purge.sh` handles cleanly |
| Overwriting full `MISSION_STATE.md` | ❌ BANNED | Surgical `multi_replace_file_content` field edits only |
| Writing MISSION_STATE with `echo >>` | ❌ BANNED | `multi_replace_file_content` MCP tool |
| Generic commit message (`chore: auto-sync`) | ❌ BANNED | Phase 6 context-aware message generation |
| `curl --max-time 0` (no timeout) | ❌ BANNED | Always `--max-time 12 --connect-timeout 4` |
| `osascript` bare in scripts | ❌ BANNED | `timeout 5 osascript ... \|\| true` |
| `tmutil` bare in scripts | ❌ BANNED | `timeout 10 tmutil ... \|\| true` |
| `execSync` without timeout | ❌ BANNED | `execSync(cmd, { timeout: 8000 })` |
| Skipping knowledge graph write after KI disk write | ❌ BANNED | Both disk AND graph — dual-write is sovereign law |
| Proposing broadcast without user approval | ❌ BANNED | Phase 5 explicitly proposes — never auto-runs |
| Inflated quality score > actual session quality | ❌ BANNED | Score the session as it actually was |

> `// turbo` ONLY applies to steps explicitly marked. Those are confirmed instant, local-only, zero hang risk operations.

---

# PHASE 1 — FORENSICS & PRE-FLIGHT

*Purpose: Read before writing. Establish ground truth before any artifact is touched.*

---

## 🔭 STAGE 1 — Conversation Log Tail Forensics (ALWAYS FIRST)

**Read the last 100 lines of the raw conversation log before touching a single file. Catch unresolved promises before they escape.**

```
view_file:
  path: ~/.gemini/antigravity/brain/<CONVERSATION_ID>/.system_generated/logs/overview.txt
  StartLine: <TotalLines - 100>
  EndLine: <TotalLines>
```

**Pattern scan the tail (look for these signals):**

| Signal | Risk | Action |
|---|---|---|
| `"I'll do X next"` / `"Let me fix Y"` | Forgotten promise trapped in model output | Add to task.md immediately |
| `run_command` with `WaitMsBeforeAsync` → no `command_status` follow-up | Background command possibly still running | Call `command_status` before anything else |
| `browser_subagent` call → no screenshot verification | UI changes unverified in production | Note in walkthrough as ⚠️ UNVERIFIED |
| Mid-deploy signal: `"firebase deploy"` → no receipt | Deploy may be in flight or failed | Check Firebase Hosting status via MCP |
| User frustration signals (short replies, repeats) | Session quality was degraded | Honest quality score < 60 in Phase 8 |
| `"TODO"` / `"placeholder"` in last 20 lines of model output | Work disguised as done | Downgrade `[x]` → `[ ]` in task.md |
| Outstanding `[/]` items never resolved | State corruption | Reconcile before writing anything |
| `"greatly enhance"` repeated 3+ times | Model wasn't delivering what user needed | Score on Promise Fulfillment dimension < 6 |

**Pre-Flight Checklist (all must pass before Stage 2):**
- [ ] No `Active CommandId` currently running (call `command_status` to confirm done/error)
- [ ] No `Status: BLOCKED` without documented resolution
- [ ] At least ONE `[x]` completed item in task.md this session
- [ ] No `browser_subagent` calls left without screenshot verification
- [ ] No mid-sentence model outputs cut by context truncation

**Session Type Classification (drives all downstream artifact depth):**

| Session Type | Signal | Downstream Impact |
|---|---|---|
| Feature / UI | Source changes, `[x]` items | Full KI + graph + walkthrough |
| Protocol evolution | `.agent/workflows/` or `rules/` changed | KI + graph + broadcast warranted |
| Infrastructure | `functions/`, `scripts/`, `storage.rules` | KI + connectivity probe + rules validation |
| Bug fix / hotfix | < 5 files, no new features | Concise KI |
| Research / planning | No source changes | Planning KI + task.md |
| Hybrid | Source AND protocol changes | Full KI + broadcast |
| Failed | No completions, user stopped early | Minimal KI + quality score < 40 |

---

## 🔥 STAGE 2 — Dev Server Error Log Harvest (NEW IN v4.0)

**A dev server that's been running 12+ hours has accumulated runtime errors. Harvest them before closing the session. These are your silent failures.**

> This stage is particularly critical when ADDITIONAL_METADATA shows a `next dev` server running for > 4 hours, as in this session (11h58m+).

// turbo
```bash
# Get the PID of the long-running dev server
DEV_PID=$(pgrep -f "next-server" 2>/dev/null | head -1 || pgrep -f "node.*dev" 2>/dev/null | head -1)
echo "Dev server PID: ${DEV_PID:-NOT_FOUND}"
```

// turbo
```bash
# Check if Next.js logs to a file (common in long-running background sessions)
ls -la .next/*.log 2>/dev/null || echo "No .next/*.log files"
ls -la /tmp/next-*.log 2>/dev/null || echo "No /tmp/next-*.log files"
```

// turbo
```bash
# Runtime error scan — check for FATAL/ERROR patterns in any accessible logs
timeout 5 find .next -name "*.log" -newer package.json 2>/dev/null \
  | head -3 \
  | xargs -I{} tail -20 {} 2>/dev/null \
  || echo "No accessible Next.js runtime logs found"
```

**What to do with harvest results:**

| Finding | Action |
|---|---|
| `FATAL: SIGSEGV` or `Killed` | OOM — note in KI, add `NODE_OPTIONS=--max-old-space-size=4096` to all scripts |
| `ENOENT: no such file or directory` | Missing file — check if it was deleted this session |
| `EADDRINUSE: port 3000` | Zombie process from prior session — kill in Stage 19 |
| `UnhandledPromiseRejection` | Bug introduced this session — add to task.md as P1 fix |
| `Hydration failed` | React SSR mismatch — note in walkthrough as UNVERIFIED |
| No errors / logs inaccessible | Note "clean runtime or logs inaccessible" in receipt |

> Write non-trivial findings to the walkthrough `Known Issues Deferred` section. These are bugs that existed during the session and should be fixed next session.

---

# PHASE 2 — SECURITY CLEARANCE

*Purpose: Nothing leaves the workspace without a clean security posture.*

---

## 🔒 STAGE 3 — Credential & Poison String Scan

**The last line of defense before any bit goes to git.**

**Scan 1 — Credential Exposure** (use `grep_search`, NOT `run_command`):
- `AIza` → `src/` — Google API keys
- `sk-proj-` → `src/` — OpenAI project keys
- `sk-ant-api` → `src/` — Anthropic keys
- `ghp_` → `src/` — GitHub PATs
- `private_key` → `src/` — embedded private keys
- `firebase_token` (exact match) → `src/` — identity token leak
- `BSAmN` → `src/` — Brave Search API key (already in mcp_config.json — flagging if it bleeds into source)

> **CRITICAL**: Any credential hit in `src/` → STOP. Do NOT commit. Alert user. Rotate credential immediately.

**Scan 2 — Cross-Project Poison Strings** (use `grep_search`):
- `Soul Contract` → SearchPath `src/`
- `CareKey` → SearchPath `src/`
- `SARAH` → SearchPath `src/` (only flag in non-SARAH projects)
- `FirstPick` → SearchPath `src/`
- `infinity-press` → SearchPath `src/` (flag if in non-press project)

**Scan 3 — .env Commit Guard:**

// turbo
```bash
git diff --cached --name-only 2>/dev/null | grep -E "^\.env" \
  && echo "🔴 .env FILE STAGED — ABORT" || echo "✅ No .env files staged"
```

**Scan 4 — Type Regression Check** (use `grep_search`):
- `as any` → `src/` — new instances introduced this session
- `@ts-ignore` → `src/` — new suppressions added
- `@ts-nocheck` → `src/` — always a red flag
- `turbo-all` → `.agent/` — no turbo-all annotations in workflows (BANNED)

---

## 🛡️ STAGE 4 — Firebase Security Rules Validation (NEW IN v4.0)

**Security rules are code. Unvalidated rules deployed to production are a live vulnerability. Given `storage.rules` is open — validate before committing.**

**Storage Rules Validation** (use `mcp_firebase-mcp-server_firebase_validate_security_rules`):
```json
{
  "type": "storage",
  "source_file": "storage.rules"
}
```

**Firestore Rules Validation** (use `mcp_firebase-mcp-server_firebase_validate_security_rules`):
```json
{
  "type": "firestore",
  "source_file": "firestore.rules"
}
```

**Gate rules:**

| Validation Result | Action |
|---|---|
| ✅ Valid — no errors | Clear to commit rules |
| ⚠️ Warning only | Document warning in KI, proceed with caution |
| 🔴 Error found | DO NOT COMMIT rules file. Fix the error first. |
| File not found | Note which rules file is missing — create if required |

**Current storage.rules posture (from open file analysis):**
> `storage.rules` is currently a complete client deny-all (`allow read, write: if false`). This is the sovereign Phase 60 secure default. Validation will confirm no syntax errors were introduced if the file was opened for editing.

**RTDB Rules** (if Realtime Database is used):
```json
{
  "type": "rtdb",
  "source_file": "database.rules.json"
}
```

> Firebase rules validation uses the MCP server — no `firebase` CLI required, no terminal hang risk.

---

## 🎨 STAGE 5 — Aesthetic Compliance Scan (NEW IN v4.0)

**The Liquid Glass v10.0 aesthetic is the law. Banned color tokens introduced this session contaminate the visual sovereign standard. Mirror turnover Stage 13.**

> Only scan files modified this session — not the entire codebase. Use `git diff HEAD --name-only` to identify touched TSX/CSS files, then scan only those.

**Get changed files first:**

// turbo
```bash
git diff HEAD --name-only 2>/dev/null | grep -E "\.(tsx|css|ts)$" | head -20
```

**Then use `grep_search` on only the changed files** (not the whole `src/` — targeted precision):

For each modified `.tsx` or `.css` file, check for:
- `slate-[0-9]` — banned slate tokens
- `zinc-[0-9]` — banned zinc tokens
- `gray-[0-9]` — banned generic gray tokens (use `neutral-` only if needed)
- `bg-white` — banned flat white backgrounds
- `border-white` — banned flat white borders
- `text-white` — audit (may be valid, but flag for review)
- `backdrop-blur` inside a child element (recursive blur = performance death on iOS)

**Liquid Glass Approved Alternatives:**

| Banned | Sovereign Alternative |
|---|---|
| `bg-white` | `bg-white/5` or `bg-indigo-950/40` |
| `border-white` | `border-white/10` |
| `slate-*` | `indigo-*`, `violet-*`, or `cyan-*` (theme-dependent) |
| `gray-*` | `neutral-*` only as a last resort |
| `backdrop-blur` on child | Move to container only |

**Gate rule:** If > 3 banned tokens introduced this session → do NOT commit until fixed. If 1-2 → warn in receipt and add to task.md as P2 cleanup.

---

## 🔑 STAGE 6 — Environment Key Parity (NEW IN v4.0)

**A new environment variable referenced in source but absent from `.env.example` breaks every future agent session and every developer setup. Catch it here.**

**Step 1 — Extract all env variable references from changed source files:**

Use `grep_search`:
- Query: `process.env.NEXT_PUBLIC_` → SearchPath `src/` — client-side env vars
- Query: `process.env.` → SearchPath `src/` — all env references
- Query: `functions.config()` → SearchPath `functions/src/` — Cloud Functions env
- Query: `defineSecret` → SearchPath `functions/src/` — Secret Manager refs

**Step 2 — Extract all keys defined in `.env.example`:**

// turbo
```bash
timeout 5 grep -E "^[A-Z_]+=.*" .env.example 2>/dev/null | cut -d= -f1 \
  | sort > /tmp/_finalize_env_example_keys.txt \
  && wc -l /tmp/_finalize_env_example_keys.txt \
  || echo ".env.example not found or empty"
```

**Step 3 — Cross-reference:**

For every `process.env.X` found in Step 1, verify `X` appears in `.env.example`. If it doesn't:
1. Add it to `.env.example` with a placeholder value and a comment explaining where to find it
2. Note it in the walkthrough `Known Issues Deferred` if it requires Secret Manager setup
3. If it's a new secret → add to the Secret Manager registration checklist

**Common drift pattern in this project:**
- `NEXT_PUBLIC_FIREBASE_*` — Firebase client config (all should be in `.env.example`)
- `GEMINI_API_KEY` — Vertex AI / Gemini key (should NOT be in `.env.example` — in Secret Manager only)
- `BRAVE_API_KEY` — currently in `mcp_config.json` as plaintext — note this in security receipt

---

## 🧬 STAGE 7 — TypeScript Integrity Gate

**The last thing pushed to origin is never broken TypeScript.**

// turbo
```bash
timeout 90 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -20
```

**Gate rules:**

| TSC Result | Action |
|---|---|
| 0 errors | ✅ Clear to commit |
| 1-3 NEW errors (this session) | 🟠 Fix now — do NOT defer |
| 1-3 PRE-EXISTING (untouched files) | 🟡 Document in KI — proceed |
| 4+ errors of any kind | 🔴 STOP — fix before commit |

> **New vs. pre-existing**: `git stash` → run TSC → note count → `git stash pop` → run TSC → delta = this session's regressions.

**Build manifest signal (non-blocking):**

// turbo
```bash
stat -f "%Sm — %N" -t "%Y-%m-%dT%H:%M" .next/build-manifest.json 2>/dev/null \
  || echo "No .next/ build present — recommend build before next deploy"
```

---

# PHASE 3 — KNOWLEDGE PERMANENCE

*Purpose: All understanding produced this session becomes retrievable, indexed, and permanent.*

---

## ✍️ STAGE 8 — Walkthrough Synthesis

**The walkthrough is a living ledger. Every session appends. Never overwrites. This is the machine's engineering journal.**

Read current walkthrough with `view_file`:
```
~/.gemini/antigravity/brain/<CONVERSATION_ID>/walkthrough.md
```

**Append a new session entry (use `multi_replace_file_content` at end of file):**

```markdown
---

## Session: Phase [N] — [ISO DATE] — [SESSION_TYPE]

### Completed This Session
- **[Deliverable]**: [File/component with one-line technical summary]

### Key Technical Decisions
- **[Decision]**: [Why X over Y — the reason matters more than the choice]

### Quantitative Change Summary
| Metric | Value |
|--------|-------|
| Files modified | [N] (+[lines] / -[lines]) |
| New components/services | [N] |
| TSC errors | [0 / N pre-existing / N new] |
| Stages completed | [N/22] |
| Quality score | [N/100] |

### Files Changed
| File | Change | Summary |
|------|--------|---------|
| [filename] | ADDED / MODIFIED / DELETED | [one-line] |

### Runtime Errors Detected (Stage 2 Harvest)
- [Error type]: [File/line if known] | [Action taken]
- None found / Logs inaccessible

### Aesthetic Compliance
- Banned tokens introduced: [None / List with file:line]
- Rules validation: [✅ Storage + Firestore valid / ⚠️ warnings / 🔴 errors found]

### Known Issues Deferred
- **[Issue]**: [WHY deferred, WHEN to address, priority]

### Verification Status
| Gate | Status |
|------|--------|
| TSC | ✅ 0 errors / 🟡 N pre-existing / 🔴 N new |
| Firebase rules | ✅ Valid / 🔴 Error |
| Aesthetic | ✅ Clean / ⚠️ N violations |
| Env parity | ✅ In sync / ⚠️ N missing keys |
| Build | ✅ Current / ⚠️ Stale |
| Deploy | ✅ Hash [XXXX] / ⏸️ Pending |
| CI/CD | ✅ Passing / ⚠️ Unknown / 🔴 Failing |
```

---

## 🧠 STAGE 9 — KI Disk Write

**Knowledge written to disk outlasts any conversation, session, or model switch.**

**KI Path:**
```
~/.gemini/antigravity/knowledge/<project>_phase<N>_<topic>/artifacts/session_<YYYY-MM-DD>.md
```

**KI Template (adapt depth to session type from Stage 1):**

```markdown
# [PROJECT] — Phase [N]: [Session Topic]

## Summary
[2-3 sentence executive description of what was accomplished and its lasting impact]

## What Was Built / Changed
- **[File/Service]**: [Purpose, pattern, and why built this way]

## Infrastructure Context
[For infrastructure sessions: what endpoints were tested, what rules were modified, what MCP server was changed]

## Key Patterns Established
[Any new implementation pattern established this session]
```typescript
// Pattern signature
```

## Sovereign Laws Discovered / Added
| Law | Rule | Enforced In |
|-----|------|-------------|
| [Name] | [Exact rule text] | [File] |

## Blockers Resolved
| Blocker | Root Cause | Fix Applied |
|---------|------------|-------------|

## Runtime Errors Found (Stage 2 Harvest)
| Error | File/Location | Fix Status |
|-------|---------------|------------|

## Security Posture
| Gate | Status |
|------|--------|
| Firebase rules | [Valid / Error] |
| Env parity | [In sync / N missing] |
| Credentials | [Clean / Violation list] |

## Known Debt Deferred
| Item | Priority | Target Phase |
|------|----------|--------------|
| [CrashBoundary.tsx] | P1 | Next session |

## Codebase Metrics Snapshot
| Metric | Value |
|--------|-------|
| TS source files | [N] |
| Total lines (rough) | [N] |
| Components | [N] |
| Cloud Functions | [N] |
| Node version | [x.x.x] |

## Next Session Entry Point
[Exact file to open. Exact first tool call. Exact task.]
```

---

## 🧬 STAGE 10 — Knowledge Graph Entity Write

**The graph is the AI-queryable index. The disk KI is the archive. Both must be written — they serve different purposes.**

Use `mcp_knowledge-graph_create_entities`:

```json
{
  "entities": [{
    "name": "[PROJECT]_Phase[N]_[SHORT_TOPIC]",
    "entityType": "SessionKnowledge",
    "observations": [
      "Session date: [ISO DATE]",
      "Session type: [type from Stage 1]",
      "Files changed: [file1.tsx, BrainService.ts, storage.rules, braveSearch.ts]",
      "Key decision: [most important architectural decision]",
      "New laws: [any new sovereign laws]",
      "Blockers resolved: [what was fixed]",
      "Runtime errors: [what was harvested in Stage 2]",
      "Security posture: [rules valid/invalid, env parity status]",
      "TSC status: [0 errors / N pre-existing]",
      "Quality score: [N/100]",
      "Next entry: [exact next session starting point]"
    ]
  }]
}
```

**Update BrainService graph node if BrainService.ts was modified this session:**

Use `mcp_knowledge-graph_add_observations` if `BrainService.ts` was changed:
```json
{
  "observations": [{
    "entityName": "[PROJECT]_BrainService",
    "contents": [
      "Modified [ISO DATE] — [what changed]",
      "Current interfaces: KnowledgeItem, GraphNode, GraphLink",
      "Key query: getDocs via onSnapshot for real-time KI sync"
    ]
  }]
}
```

**Relations to create:**
```json
{
  "relations": [{
    "from": "[PROJECT]_Phase[N]_[TOPIC]",
    "to": "[PROJECT]_Phase[N-1]_[PRIOR]",
    "relationType": "buildsOn"
  }]
}
```

---

## 🔧 STAGE 11 — Stale KI Remediation

**Stale KIs are active misinformation in the graph. Fix wrong assertions now. A stale KI corrupts the next turnover's context ingest.**

**Fast verification of KIs cited this session** (spot-check 1 claim per KI):

| KI | Claim to Verify | Verify Via |
|---|---|---|
| `fleet_hang_eradication_phase57` | `grep_search` is non-blocking replacement | It still is ✅ |
| `antigravity_ide_architecture` | Chat hydration race condition workaround | Known behavior ✅ |
| `infinity_protocol_firebase_ascension` | `gen-lang-client-0386732425` as prod target | `view_file .firebaserc` |
| `model_context_protocol_servers` | playwright purged, vitest purged | `view_file mcp_config.json` ✅ confirmed |
| Any KI referencing `context7` or `figma-dev-mode` | Listed as purged | ✅ confirmed purged in mcp_config.json |

**If stale KI found** → `multi_replace_file_content` on the specific wrongasssertion:
```
~/.gemini/antigravity/knowledge/<ki_name>/artifacts/<file>.md
```

**Do NOT delete KIs.** Update them. The history of what was true at a time has forensic value.

---

# PHASE 4 — STATE RECONCILIATION

*Purpose: Every artifact that tracks current state must agree with reality.*

---

## 📋 STAGE 12 — Task.md Reconciliation

**The task list must reflect observable reality, not aspirational memory.**

Use `view_file` → `multi_replace_file_content`:
```
~/.gemini/antigravity/brain/<CONVERSATION_ID>/task.md
```

**Reconciliation rules:**
1. `[/]` at session end → `[ ]` with explanation. No in-progress items survive session close.
2. Completed items not originally listed → add as `[x]` retroactively (ledger accuracy).
3. Items from Stage 1 forensics (forgotten promises) → add as `[ ]` with priority.
4. Planned but not started → `[ ]` with P0/P1/P2 annotation.
5. If `"greatly enhance finalize session"` repeated 3+ times → it was a signal the current version was insufficient at that moment. Note what was missing in the KI.

---

## 🔖 STAGE 13 — MISSION_STATE Seal

**Surgical edits only. Never overwrite the full file.**

Use `view_file` (full) → `multi_replace_file_content` for targeted field updates only:

```markdown
Required updates:
- Version: bump patch (v10.0.46 → v10.0.47)
- Phase: current designation
- Status: SOVEREIGN | DEGRADED | BLOCKED
- Last Updated: [current ISO timestamp]
- Active CommandId: NONE
- Suspend Point: "Session ended cleanly Phase [N]. Resume at [specific_file]."
- Next Action: [EXACT first action — must be specific enough to execute in < 10 seconds]
- Last Deploy Hash: [actual git hash if deployed]
```

**Phase advancement:** If ≥ 80% of current phase objectives completed → increment phase number. Document transition in `## Historical Operations (Sealed)`.

**MISSION_STATE health verification (post-update):**
- [ ] No duplicate section headers
- [ ] `Status` is one of exactly three valid values
- [ ] `Active CommandId: NONE` definitively
- [ ] `Next Action` is specific and actionable (not "resume work")

---

## ⚖️ STAGE 14 — Protocol Law Registry

**New laws discovered this session must be formally registered in all three enforcement locations. Undocumented laws are forgotten laws.**

**Required registration locations for every new law:**
1. `GEMINI.md` Phase 9 Laws table
2. `rules/governance.md` (or relevant `.mdc` for domain-specific laws)
3. `turnover.md` Stage 1 Banned Patterns (so it's audited every session start)

**Format for GEMINI.md Phase 9 table:**
```markdown
| [Law Name] | [Banned action] | [Sovereign alternative] |
```

**Laws from this session chain to verify registration:**
- `osascript bare` → `timeout 5 osascript ... || true`
- `tmutil bare` → `timeout 10 tmutil ... || true`
- `crontab via pipe` → tmp file + `timeout 5 crontab file`
- `git fetch in scripts without guards` → `GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true`
- `TypeScript in pre-commit bare` → `timeout 60 tsc --noEmit --skipLibCheck`
- `Bash -e flag in cron` → remove `-e`; use `-uo pipefail`

---

# PHASE 5 — CLOUD SYNCHRONIZATION

*Purpose: Permanent knowledge and protocol changes reach the cloud brain and the fleet.*

---

## 📡 STAGE 15 — Firebase Brain Sync + Fleet Broadcast Evaluation

### 15A — Firebase Brain Mandatory Push (Phase 161 Law)

**MANDATORY every session.** `dv push-brain` auto-reads `MISSION_STATE.md` for phase/version/status.

```bash
dv push-brain "Phase [N] — [2-sentence session summary]"
```

This calls two Cloud Functions in sequence:
1. **`upsertProjectState`** → writes to `project_states/{projectId}` with phase, version, status, goals, constraints
2. **`saveSessionMemory`** → writes to `session_memories/{sessionId}` with summary and learning nodes

> **Phase 161 Law**: `dv push-brain` is the CANONICAL path — not manual `mcp_firebase-mcp-server_firestore_add_document` to `session_memories`. The Cloud Function handles embedding generation, schema validation, and collection routing automatically.

> **On failure**: A push-brain failure **NEVER** blocks finalization. Log the error. The disk KI (Stage 9) is still the authoritative record.

> **BANNED**: Writing directly to `sessionMemory` collection (wrong name). Use `dv push-brain` → Cloud Function → `session_memories` (correct collection name).

**Verify sync after push:**
```bash
dv brain-status
```
Confirm: `✓ In sync` for both phase and GEMINI.md hash.

### 15B — Fleet Broadcast Decision Matrix

| Change Made This Session | Broadcast? | Risk of Not Broadcasting |
|---|---|---|
| Modified `.agent/workflows/finalize_session.md` | ✅ YES | All other projects use stale finalize_session |
| Modified `.agent/workflows/turnover.md` | ✅ YES | All other projects use stale turnover |
| Added rows to `GEMINI.md` Phase 9 laws | ✅ YES | Other projects don't enforce new law |
| Modified `rules/*.mdc` | ✅ YES | Other projects unprotected |
| Modified `src/components/*.tsx` | ❌ NO | Project-local UI change |
| Modified `functions/src/mcp/braveSearch.ts` | ❌ NO | Project-local function |
| Modified `storage.rules` | ❌ NO | Project-local security rules |
| MCP config sync performed (Stage [8]) | ✅ YES | Other projects have ghost MCP servers |

**If broadcast is warranted** → propose to user (NEVER auto-run):
```bash
bash scripts/sovereign_broadcast.sh
```
> This rewrites `.cursor/rules/`, `GEMINI.md`, and `.agent/workflows/` across ALL `~/Developer/` git repos. User must explicitly approve before execution.

---

# PHASE 6 — VERSION CONTROL + CI/CD VERIFICATION

*Purpose: Changes reach git with context, and their deployment is verified to have actually landed.*

---

## 🐙 STAGE 16 — Sovereign Git Commit & Push

**A commit without context is archaeology homework. Write a real message every time.**

**Step 1 — Review scope:**

// turbo
```bash
git status --short && echo "---" && git diff --stat HEAD 2>/dev/null | tail -10
```

**Step 2 — Stage ALL changes (only if Phases 1-2 security gates cleared):**

// turbo
```bash
git add .
```

**Step 3 — Context-aware commit message (reads from MISSION_STATE, not hardcoded):**

// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 bash -c '
  PHASE=$(grep "^\*\*Phase:" MISSION_STATE.md 2>/dev/null | head -1 | awk "{print \$2}" | tr -d "." || echo "N")
  VERSION=$(grep "^# MISSION STATE" MISSION_STATE.md 2>/dev/null | head -1 | sed "s/.*— //" | sed "s/[[:space:]]*$//" || echo "v10.0")
  FILES=$(git diff --cached --name-only 2>/dev/null | wc -l | tr -d " ")
  TYPE=$(git diff --cached --name-only 2>/dev/null | grep -qE "\.agent/workflows" && echo "protocol" || echo "feat")
  MSG="${TYPE}(phase${PHASE}): ${VERSION} — ${FILES} files — $(date +%Y-%m-%dT%H:%M:%SZ)"
  git diff --cached --quiet && echo "[INFO] Nothing staged" && exit 0
  git commit --no-verify -m "${MSG}" && echo "[✅ COMMITTED] ${MSG}"
'
```

**Step 4 — Push with hang guard:**

// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main 2>&1 \
  || echo "[⚠️ PUSH FAILED] KI on disk is authoritative — document push failure in receipt"
```

**Step 5 — Quantitative diff summary (feed into Stage 22 receipt):**

// turbo
```bash
git diff HEAD~1 --stat 2>/dev/null | tail -5 \
  || echo "(No prior commit to diff — first commit or detached HEAD)"
```

---

## 🚀 STAGE 17 — CI/CD Status Verification (NEW IN v4.0)

**We push to origin. We do NOT assume the push landed cleanly in production. Verify the CI/CD pipeline.**

> This stage closes a critical gap in all prior finalization protocols: we wrote code, we committed, we pushed — but did the deploy workflow actually pass?

**Step 1 — Get the current commit hash:**

// turbo
```bash
git log --oneline -1 2>/dev/null
```

**Step 2 — Check GitHub Actions status** (use `mcp_gcloud_run_gcloud_command` for GCP-native CI, OR note that GitHub requires the GitHub MCP server which is currently purged):

> **Known Gap**: `github-mcp-server` is permanently purged (requires Docker daemon). GitHub Actions status cannot be verified via MCP. Use the fallback below.

**Fallback — Firebase Hosting Live Probe:**

// turbo
```bash
# Verify the production URL responds (non-blocking, bounded)
timeout 10 curl -s -o /dev/null -w "%{http_code}" \
  --connect-timeout 4 --max-time 8 \
  "https://gen-lang-client-0386732425.web.app/" 2>/dev/null \
  && echo " (Firebase Hosting live check)" \
  || echo "⚠️ Firebase Hosting probe timed out or failed"
```

**Fallback — Cloud Functions Health Probe:**

> If `test_all_connectivity.sh` was open this session (it is), consider whether to run it as a post-deploy verification. However, per Phase 57 laws: network calls in finalization must be bounded. `test_all_connectivity.sh` already has a 120s hard kill. Propose to user rather than auto-run.

**CI/CD Status in Receipt:**

| Result | Receipt Entry |
|---|---|
| HTTP 200 from Hosting | ✅ Production live |
| HTTP 50x | 🔴 Deployment failed — check Firebase console |
| Timeout | ⚠️ Hosting probe timed out — check manually |
| GitHub Actions unknown | ⚠️ GitHub MCP purged — verify at github.com/[user]/[repo]/actions |

---

# PHASE 7 — PROCESS HYGIENE + DEPENDENCY AUDIT

*Purpose: Clean machine, clean dependencies, clean disk.*

---

## 🔬 STAGE 18 — Dependency Drift Audit (NEW IN v4.0)

**`package-lock.json` drift is a silent security and stability killer. Detect it here before it surfaces as a production error.**

**Step 1 — Lock file drift detection:**

// turbo
```bash
# Check if package-lock.json is in sync with package.json
timeout 15 npm ls --depth=0 --json 2>&1 | grep -E "(WARN|ERR|invalid|missing)" | head -10 \
  || echo "✅ No npm dependency warnings"
```

// turbo
```bash
# Check for deduplication opportunities and security notes
timeout 10 npm outdated --json 2>/dev/null | head -20 \
  || echo "✅ All packages current or npm outdated timed out"
```

**Step 2 — New dependencies added this session (vs. what was in package.json before):**

// turbo
```bash
git diff HEAD~1 package.json 2>/dev/null | grep "^+" | grep -v "^+++" | head -20 \
  || echo "(No package.json changes this session)"
```

> If new packages were added → verify they are:
> 1. In the correct section (`dependencies` vs `devDependencies`)
> 2. Not known security vulnerabilities (run `npm audit --audit-level=high` if time permits)
> 3. Compatible with Node 22 LTS

**Step 3 — Functions dependency parity:**

// turbo
```bash
# Check if functions/package.json has drifted from root requirements
timeout 5 diff \
  <(grep '"node":' package.json 2>/dev/null || echo "none") \
  <(grep '"node":' functions/package.json 2>/dev/null || echo "none") \
  && echo "✅ Node version parity" || echo "⚠️ Node version drift between root and functions"
```

---

## 🟢 STAGE 19 — Node Version Sovereignty (NEW IN v4.0)

**The sovereign standard is Node 22 LTS. A drift here causes silent CI/CD failures and Apple Silicon memory pressure.**

// turbo
```bash
node --version && echo "Expected: v22.x.x — if mismatch: nvm use 22"
```

// turbo
```bash
# Verify .nvmrc or .node-version is present and set correctly
cat .nvmrc 2>/dev/null || cat .node-version 2>/dev/null || echo "⚠️ No .nvmrc or .node-version file — drift risk"
```

// turbo
```bash
# Verify package.json engines field
grep -A3 '"engines"' package.json 2>/dev/null || echo "⚠️ No engines field in package.json — add: \"engines\": { \"node\": \">=22.0.0\" }"
```

**If Node is not v22.x.x:**
1. Run `nvm use 22` in the dev terminal
2. Add `"engines": { "node": ">=22.0.0" }` to `package.json` if missing
3. Verify `.nvmrc` contains `22` and commit it
4. Note in KI: "Node version drift detected — corrected to v22"

---

## 🔌 STAGE 20 — MCP Config Parity

**The live MCP config is the machine's nervous system. Ghost servers corrupt every future session.**

Compare canonical vs live using `view_file` on both:
- Canonical: `config/antigravity_mcp_config.json`
- Live: `~/.gemini/antigravity/mcp_config.json`

**Parity checklist:**

| Check | Expected State |
|---|---|
| Server count | 5 servers (firebase, gcloud, brave-search, chrome-devtools, knowledge-graph) |
| All have `NODE_OPTIONS=--max-old-space-size=4096` | ✅ Required for all |
| All have `timeout` defined | ✅ Required |
| Purged servers absent | playwright, vitest-sovereign, context7, figma-dev-mode, github-mcp-server, cloudrun, google-maps |
| `MEMORY_FILE_PATH` correct | `/Users/teknojunkeee/.gemini/antigravity/knowledge-graph.jsonl` |
| All `retryOnFailure: false` | ✅ — auto-retry hangs on connection failure |

If drift found → `multi_replace_file_content` to sync live config to canonical. Do NOT modify canonical unless this session explicitly upgraded the stack.

---

## 💀 STAGE 21 — Stale Process Termination + Phantom Purge

**Every orphaned process is RAM debt, port debt, and confusion debt. Every stale recording is disk debt.**

// turbo
```bash
pkill -f "next-router-worker" 2>/dev/null || true
pkill -f "next-render-worker" 2>/dev/null || true
pkill -f "next-swc-worker" 2>/dev/null || true
```

// turbo
```bash
# Dev server age audit
ps aux | grep -E "(next-server|node.*dev)" | grep -v grep \
  | awk '{print "PID:", $2, "| Runtime:", $10, "| Cmd:", $11, $12}' | head -5 \
  || echo "✅ No Next.js dev server running"
```

> **THIS SESSION CRITICAL**: Dev server at ~12h runtime. Propose termination:
> ```bash
> lsof -ti:3000 | xargs kill -SIGTERM 2>/dev/null; sleep 2; lsof -ti:3000 | xargs kill -9 2>/dev/null || true
> ```

// turbo
```bash
ps aux | grep -E "(playwright|chromium-node)" | grep -v grep | head -5 \
  || echo "✅ No Playwright zombies"
```

// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings/
rm -rf ~/.npm/_npx/
rm -rf ~/.gemini/antigravity-browser-profile/ 2>/dev/null || true
```

// turbo
```bash
timeout 10 tmutil deletelocalsnapshots / 2>/dev/null && echo "✅ APFS snapshots released" \
  || echo "(tmutil skipped)"
```

// turbo
```bash
df -h / | awk 'NR==2 { printf "[DISK] Free: %s / %s (%s used)\n", $4, $2, $5 }'
du -sh .next/cache 2>/dev/null || echo "No .next/cache"
```

---

# PHASE 8 — INTELLIGENCE SYNTHESIS

*Purpose: Self-assessment creates accountability. Future preparation eliminates cold-start overhead.*

---

## 🏆 STAGE 22 — Session Quality Score

**A machine that cannot score its own performance cannot improve. Score honestly.**

**10 Dimensions (0-10 each, 100 max):**

| Dimension | 10 Points | 0 Points |
|---|---|---|
| **Objective Clarity** | Completed what we set out to do | Nothing completed |
| **Protocol Adherence** | Zero Phase 57/70 violations | Multiple violations |
| **Security Hygiene** | All scans clean, rules validated, env parity verified | Credential exposed or rules unvalidated |
| **Knowledge Capture** | KI on disk AND in graph, walkthrough updated | No knowledge written |
| **Communication Quality** | Clear, no user confusion, no repeated requests | User had to repeat request 3+ times |
| **Commit Quality** | Informative commit message, context-rich | Generic `chore: auto-sync` |
| **Task Accuracy** | Task.md reflects reality, no phantom `[/]` | `[/]` items left at close |
| **Type Safety** | TSC 0 new errors | 4+ new errors introduced |
| **Process Hygiene** | Clean disk, no zombies, Node v22, deps current | EMFILE risk, zombies, drift |
| **Promise Fulfillment** | All requests completed without dropping context | Requests repeated due to drops |

**Total: /100**

**Quality Grade:**

| Score | Grade | Required Action |
|---|---|---|
| 90-100 | 🟢 SOVEREIGN | Elite session. No action required. |
| 75-89 | 🔵 COMPLIANT | Minor gaps. Note in KI. |
| 60-74 | 🟡 DEGRADED | Meaningful gaps. Document causes in KI. |
| 40-59 | 🟠 AT RISK | Post-mortem required in KI Stage 9. |
| 0-39 | 🔴 FAILED | Full post-mortem. Next session starts with root cause review. |

**Post-mortem format (score < 60):**
```markdown
## Post-Mortem (Sub-Sovereign Session)
- Root cause of failure: [Not symptoms — actual cause]
- What signal was ignored: [In retrospect, what should have triggered a pivot?]
- Protocol change recommended: [What new law or stage would have prevented this?]
- Dimensional breakdown: [Which of the 10 dimensions failed and why]
```

---

## 🔮 STAGE 23 — Codebase Metrics Snapshot + Predictive Next-Session Prompt

**Capture a quantitative snapshot of the codebase before closing. Then generate the optimal next-session entry prompt while context is at peak.**

**Codebase snapshot:**

// turbo
```bash
echo "=== CODEBASE METRICS ==="
echo "TS Source Files: $(find src -name '*.ts' -o -name '*.tsx' 2>/dev/null | wc -l | tr -d ' ')"
echo "Cloud Functions: $(find functions/src -name '*.ts' 2>/dev/null | grep -v test | grep -v spec | wc -l | tr -d ' ')"
echo "Test Files: $(find . -name '*.test.ts' -o -name '*.spec.ts' 2>/dev/null | grep -v node_modules | wc -l | tr -d ' ')"
echo "Scripts: $(find scripts -name '*.sh' 2>/dev/null | wc -l | tr -d ' ')"
echo "Workflow Files: $(find .agent/workflows -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"
echo "Node: $(node --version 2>/dev/null)"
echo "Last commit: $(git log --oneline -1 2>/dev/null)"
```

**Predictive next-session prompt (write to MISSION_STATE `Next Action` AND to walkthrough):**

```
═══════════════════════════════════════════════════════════════
PREDICTIVE NEXT SESSION ENTRY POINT — Generated [ISO DATE]
═══════════════════════════════════════════════════════════════

/turnover

After turnover's 20-stage handshake completes, resume Phase [N+1]:

PRIORITY 0 (P0 — execute first, no exceptions):
→ [Exact task: file, function, and what to do]

PRIORITY 1 (P1 — after P0):
→ [Exact task]

PRIORITY 2 (P2 — if time allows):
→ [Exact task]

MACHINE STATE NOTES FOR NEXT SESSION:
• Node version: [v22.x.x ✅ / ⚠️ drift detected]
• Pre-existing TSC errors: [N — do NOT count as new regressions]
• Dev server: [was terminated at close / was still running at close]  
• Dep drift: [✅ clean / ⚠️ N warnings]
• Last git hash: $(git log --oneline -1)
• Firebase rules: [✅ validated / ⚠️ unvalidated]
• Connectivity: [✅ test_all_connectivity.sh last run [DATE] / ⏸️ not run]
• Open files at close: [braveSearch.ts, BrainService.ts, storage.rules...]

Persona check: Zoltan online. Infinity Protocol v10.0 Active.
═══════════════════════════════════════════════════════════════
```

---

# PHASE 9 — RECEIPT EMISSION

*Purpose: The machine's binding contract. Always emit. Never skip.*

---

## ✅ STAGE 24 — Finalization Receipt

```
╔══════════════════════════════════════════════════════════════════╗
║  ✅ SESSION FINALIZED v5.0 — [ISO TIMESTAMP]                     ║
║  Infinity Protocol v10.0 | Phase [N]→[N+1] | [VERSION]          ║
╚══════════════════════════════════════════════════════════════════╝

🔭 FORENSICS (Phase 1)
  Tail scan     : [N lines — N signals / clean]
  Promises found: [None / List]
  Dead commands : [None / CommandId XXXX resolved]
  Runtime errors: [None / harvest result summary]

🔒 SECURITY (Phase 2)
  Credentials   : [✅ CLEAN / 🔴 VIOLATION: file:line]
  Poison strings: [✅ CLEAN / 🟡 flagged]
  .env guard    : [✅ No .env staged]
  Storage rules : [✅ VALID / 🔴 ERROR / ⟳ Not validated]
  Firestore rules: [✅ VALID / 🔴 ERROR / ⟳ Not validated]
  Aesthetic     : [✅ No banned tokens / ⚠️ N violations: file:line]
  Env parity    : [✅ In sync / ⚠️ N missing keys added to .env.example]
  TSC           : [✅ 0 errors / 🟡 N pre-existing / 🔴 N NEW]

📝 KNOWLEDGE (Phase 3)
  KI (disk)     : [~/.gemini/.../artifacts/<date>.md]
  Graph entity  : [[PROJECT]_Phase[N]_[TOPIC] — created/updated]
  Stale KIs     : [N fixed / None found]
  Walkthrough   : [Appended — session entry with [N] items]
  Task.md       : [N completed, N deferred, N added]
  MISSION_STATE : [v10.0.XX → v10.0.XY | Phase N | SOVEREIGN]

⚖️ STATE + PROTOCOL (Phase 4)
  New laws      : [N registered → GEMINI.md + governance.md + turnover.md]
  MCP parity    : [✅ In sync / ⚠️ N diffs synced]

📡 CLOUD (Phase 5)
  Firestore     : [✅ Written / Skipped / ⚠️ Failed (non-blocking)]
  Broadcast     : [✅ Warranted — proposed to user / Not required]

🔄 VERSION CONTROL (Phase 6)
  Diff          : [+N lines / -N lines / N files]
  Committed     : [HASH: "type(phaseN): ... message"] / [Nothing]
  Pushed        : [✅ origin/main @ HASH / ⚠️ Push failed]
  CI/CD         : [✅ Hosting 200 / 🔴 50x / ⚠️ Probe timed out]
  Build cache   : [✅ Current / ⚠️ Stale]

🔬 HYGIENE (Phase 7)
  Node version  : [v22.x.x ✅ / ⚠️ v[XX] — drift]
  Dep drift     : [✅ Clean / ⚠️ N warnings]
  Dev server    : [Terminated (was [N]h) / Running PID:XXXX / Not running]
  Playwright    : [✅ Clean / Killed via phantom_purge.sh]
  Disk free     : [XGB]
  APFS          : [✅ Released / Skipped]

🏆 QUALITY (Phase 8)
  Score         : [N/100]
  Grade         : [🟢 SOVEREIGN / 🔵 COMPLIANT / 🟡 DEGRADED / 🟠 AT RISK / 🔴 FAILED]
  Gap           : [Biggest gap this session, or "Clean session — no gaps"]
  Codebase      : [N TS files | N functions | N tests | Node v22]

🔮 NEXT SESSION (Phase 8)
  Open file     : [Exact path]
  First call    : [Exact tool or command]
  P0 task       : [Exact description]
  Prompt        : [See MISSION_STATE.md → Next Action]

╔══════════════════════════════════════════════════════════════════╗
║  PHANTOM PURGE: Already executed in Stage 21.                    ║
║  Confirm: rm -rf ~/.gemini/antigravity/browser_recordings        ║
╚══════════════════════════════════════════════════════════════════╝
```

> After emitting receipt → STOP. No further actions. Session is sealed. If user sends new request before next `/session_start`, run mini handshake first.

---

## 🧬 ANNEXE A — Speed Mode Reference

| Mode | When | Phases to Execute |
|------|------|-------------------|
| **Full Sovereign** | Normal end-of-session | All 9 phases, all 24 stages |
| **Rapid Seal** | Short session < 30 min, no source changes | Phase 1 (Stage 1), Phase 3 (Stage 9 brief + 10), Phase 4 (Stage 13), Phase 6 (Stage 16), Phase 7 (Stage 21), Phase 9 (Stage 24) |
| **Emergency Exit** | Session terminates unexpectedly | Stage 1 (tail only), Stage 9 (brief notes), Stage 13 (BLOCKED status), Stage 24 (partial receipt) |
| **Protocol-Only** | Workflows/rules changed only (no source) | Phases 1, 2, 3, 4 (Stage 14 — law registry), 5, 6, 7 (Stage 21 only), 8, 9 |
| **Infrastructure** | Functions/scripts/rules changed only | Phases 1, 2 (all — rules validation critical), 3, 4, 5, 6 (with CI/CD probe), 7, 8, 9 |
| **Post-Failure** | Quality score < 40 this session | Full + mandatory post-mortem in Stage 9 before KI write |

---

## 🧬 ANNEXE B — Hard Banned Anti-Patterns (Complete Registry)

| Anti-Pattern | Why Banned | Sovereign Alternative |
|---|---|---|
| Overwriting full `MISSION_STATE.md` | Destroys sealed phase history | Surgical field replacement |
| Generic commit `chore: auto-sync` | Zero information density | Stage 16 context-aware message |
| Skipping TypeScript gate | Broken types pushed to origin | Stage 7 mandatory on all full finalizations |
| `curl` to onCall Firebase functions | Always fails — no ID token | Firestore MCP tool |
| Skipping walkthrough update | Context lost for next session | Stage 8 mandatory |
| `kill -9` on dev server | Corrupts `.next/` state | SIGTERM → wait 2s → SIGKILL |
| Auto-run fleet broadcast | Modifies ALL workspaces destructively | Stage 15B proposes — user approves |
| Skipping receipts | Machine state unknown | Stage 24 is the contract |
| Leaving `[/]` items open | Ambiguous state | Downgrade to `[ ]` with note |
| Skipping knowledge graph write | KI on disk unindexed | Stage 10 mandatory after Stage 9 |
| Inflated quality score | Corrupts calibration | Score the session as it actually was |
| Skipping conversation tail forensics | Promises escape | Stage 1 is always FIRST |
| Skipping Firebase rules validation | Unvalidated rules to production | Stage 4 mandatory when rules are open |
| Skipping aesthetic compliance scan | Liquid Glass tokens drift | Stage 5 mandatory after UI work |
| Skipping env key parity | Silent runtime failures next session | Stage 6 mandatory when source changed |
| Skipping CI/CD probe | False confidence in deploy | Stage 17 bounded curl probe |
| Skipping dependency drift audit | Security and stability risk | Stage 18 mandatory |
| Skipping Node version check | Apple Silicon OOM, CI failures | Stage 19 mandatory |
| Generating next-session prompt from memory | Recency bias corrupts priorities | Stage 23 generates from Stages 12-13 data |

---

## 🧬 ANNEXE C — Emergency: Session Terminated Without Finalization

**Recovery at NEXT session start** (within `/turnover` Stage forensics):
1. Read last 100 lines of `overview.txt` — identify unresolved promises
2. `git log --oneline -3` — if no commit from this session → data still on disk
3. Run `tsc --noEmit` — delta vs. expected reveals what this session broke
4. Write emergency KI: `Session [DATE] terminated unexpectedly. State: [observed].`
5. Set MISSION_STATE `Status: DEGRADED` — document what's unknown
6. Do NOT start new work until full `/turnover` completes (20 stages minimum)

**Core principle**: Data is never truly lost if KI was written incrementally during the session. Stage 9 (KI write) should happen mid-session for critical decisions — not only at finalization.

---

*Status: Sovereign Finalization Protocol v5.0 — SESSION END PROTOCOL — 9 execution phases, 24 stages, 22 unique capabilities. Paired with `/turnover` (SESSION START). Seven additions over v3.0: Firebase rules validation, dev server error log harvest, aesthetic compliance scan, environment key parity, CI/CD status verification, dependency drift audit, Node version sovereignty, and codebase metrics snapshot. Zero promises escape. Zero processes linger. Zero knowledge lost. Zero security debt. Every session ends with omniscient clarity.*
