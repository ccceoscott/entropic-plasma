---
description: GSD (Get Shit Done) end-to-end workflow — persistent memory, atomic git commits, and sovereign sprint execution for enterprise-scale projects
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /gsd
## Get Shit Done — End-to-End Sovereign Sprint Protocol

> ⚡ **GSD** is the enterprise task execution layer that sits on top of Antigravity. It provides persistent project memory, atomic git commits per sub-task, spec-driven development, and session handoff continuity. Version: `get-shit-done-cc@1.34.2`.
>
> **Trigger**: Any time a large sprint, feature build, or multi-session work block begins. Also triggered manually with `/gsd`.

---

## PRE-FLIGHT: Verify GSD Installation
// turbo
```bash
cat ~/.gsd/defaults.json 2>/dev/null && echo "GSD_OK" || echo "GSD_MISSING"
```

If `GSD_MISSING`:
```bash
npx -y get-shit-done-cc@latest --gemini --global 2>&1 | tail -10
```
Expected: 8 hooks installed, `Done!` message. If it fails → abort and investigate `~/.gsd/`.

---

## PHASE 0 — COGNITIVE TRAJECTORY SYNTHESIS (Sovereign Planning)

> Before any planning or spec-writing, you MUST synthesize the trajectory from the Remote Brain. This ensures the current sprint does not violate global architectural patterns.

### Step 0a — Trajectory Analysis:
Call `mcp_brain-mcp_search_knowledge` with:
- `query`: [Primary Goal from MISSION_STATE.md]
- `projectId`: [active project id]
- `mode`: `"hybrid"`
- `limit`: 10

### Step 0b — Synthesis Validation:
1.  **Directives**: Absorb the `synthesis` block. These are your "Unbreakable Laws" for this sprint.
2.  **Contradiction Check**: Scan the `contradictions` array. If any recent architectural decisions conflict with the Brain's memory → **STOP** and resolve with the user.
3.  **Meta-Context Alignment**: Verify that the proposed work aligns with the `metaContext` (architectural principle).

---

## PHASE 1 — GSD PROJECT INITIALIZATION

> Run ONCE per project. Skip if `~/.gsd/projects/[project-id].json` already exists.

### Step 1a — Map the Codebase
Open the target workspace in Antigravity. Run:

```
/gsd-map-codebase
```

GSD will analyze:
- Directory structure
- Key entry points (pages, functions, components)
- Framework detection (Next.js, Firebase, etc.)
- Build configuration (package.json scripts)
- Test configuration (jest, vitest)

Wait for GSD to output: `✓ Codebase mapped to ~/.gsd/projects/[project]/map.json`

### Step 1b — Initialize the GSD Project
```
/gsd-new-project
```

GSD prompts for:
- **Project Name**: Use the Firebase project ID from `.firebaserc` (e.g., `gen-lang-client-0386732425`)
- **Primary Goal**: Paste the "Next Session Entry Point" from `MISSION_STATE.md`
- **Stack**: `Next.js + Firebase + TypeScript + Tailwind`
- **Test Command**: `cd functions && npm test`
- **Build Command**: `NODE_OPTIONS=--max-old-space-size=4096 npm run build`

GSD creates:
- `~/.gsd/projects/[project-id].json` — persistent project state
- `~/.gsd/sessions/[session-id].json` — current session state
- `.gsd/` directory in workspace (if enabled) — local spec files

---

## PHASE 2 — SPRINT PLANNING (Spec-Driven)

### Step 2a — Load Brain Context & Synthesis
Before planning, pull Remote Brain Synthesis as the sprint's analytical anchor:

Use `mcp_brain-mcp_search_knowledge` with:
- `query`: [primary goal from MISSION_STATE.md]
- `projectId`: [project ID]
- `mode`: `"hybrid"`
- `globalSearch`: true
- `limit`: 10

Log the returned `synthesis`, `metaContext`, and any `contradictions`. These MUST inform the spec and be explicitly referenced in the "Context" section.

### Step 2b — Write the Sprint Spec

Create (or update) `.gsd/sprint-spec.md` in the workspace:

```markdown
# GSD Sprint Spec — [PROJECT_NAME] — Phase [N]

## Goal
[Single sentence: what does Done look like?]

## Context
[2-3 sentences from MISSION_STATE.md + Brain KIs]

## Constraints
- [ ] TypeScript strict — 0 errors at end of sprint
- [ ] No `Record<string,any>` (Law 20)
- [ ] NODE_OPTIONS=--max-old-space-size=4096 on all scripts
- [ ] No hardcoded API keys
- [ ] git push via paste command only (never run_command)

## Tasks (Atomic — 1 commit per task)
- [ ] [TASK-1]: [precise sub-task description] → `[commit message preview]`
- [ ] [TASK-2]: [precise sub-task description] → `[commit message preview]`
- [ ] [TASK-3]: [precise sub-task description] → `[commit message preview]`
...

## Definition of Done
- [ ] All tasks marked [x]
- [ ] TypeScript gate: 0 errors
- [ ] Tests: all suites passing
- [ ] Security: zero leaked secrets
- [ ] Brain memory committed (`save_session_memory`)
- [ ] MISSION_STATE.md sealed with new phase number
```

### Step 2c — Approval Gate
> **ABSOLUTE MANDATE**: Do NOT start Phase 3 execution until the user gives explicit thumbs up on the sprint spec. Reference: Artifact-Driven Review Gate (Law §7).

Display the spec as an artifact. Wait for: "proceed", "looks good", "execute", or a thumbs up.

---

## PHASE 3 — ATOMIC EXECUTION LOOP

> Each task executes as an atomic unit: read → implement → test → commit. No partial code blobs across multiple tasks.

### For Each Task in `.gsd/sprint-spec.md`:

#### Step 3a — Pre-Task Context & Trajectory Pull
Call `mcp_brain-mcp_search_knowledge` with:
- `query`: [this specific task description]
- `projectId`: [project ID]
- `mode`: `"hybrid"`
- `limit`: 5

**Execution Requirement**:
- Absorb the `synthesis` and `metaContext` from this result to guide the implementation.
- If `contradictions` are found for this specific task → **HEAL** the task description in `.gsd/sprint-spec.md` before coding.

#### Step 3b — Implement (5:1 Research/Write rule)
Research first:
1. If task involves external API/SDK → use `mcp_firebase-mcp-server_developerknowledge_search_documents` (2-3 keywords MAX)
2. If task modifies Firestore schema → use `mcp_firebase-mcp-server_firebase_get_security_rules` to confirm live rule state
3. If task modifies types → check `types/firebase.d.ts` and `SCHEMA_REFERENCE.json` first

Then write code. Apply predictive safeguards:
- Optional chaining `?.` on all external data access
- `|| ''` / `|| []` null-safe defaults
- `formatDateSafe()` on all timestamp fields
- `timeout` wraps on all `execSync` calls

#### Step 3c — Verify Task
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -5
```
AND
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -10
```

Zero tolerance: any error → fix before proceeding. Auto-heal up to 3 attempts. Log each heal action.

#### Step 3d — Atomic Commit
// turbo
```bash
git add -A && git commit -m "[task-type]: [task description] — Phase [N].[task-index]"
```

Commit types: `feat` / `fix` / `refactor` / `chore` / `test` / `seal`

Log: `✅ [TASK-N COMMITTED] [commit hash] — [task description]`

#### Step 3e — Mark Task Complete
Update `.gsd/sprint-spec.md`: change `- [ ] [TASK-N]` to `- [x] [TASK-N]`
Update `~/.gsd/sessions/[session-id].json` via GSD if applicable.

#### Step 3f — Brain Memory Micro-Commit (on significant tasks only)
For any task that discovers a non-obvious pattern, bug, or architectural constraint:

Call `mcp_brain-mcp_save_session_memory` immediately after the atomic commit with:
- `taxonomy`: `"BUG" | "ARCH" | "PERF" | "SECURITY"`
- `context`: [what component this was in]
- `problem`: [what the issue was]
- `solution`: [exact fix applied]
- `portfolioAlignment`: true if applies fleet-wide

> **Note**: If 429 quota hit → log warning and continue. P1 issue (Vertex AI ADC migration pending).

---

## PHASE 4 — SPRINT REVIEW GATE

After all tasks are marked `[x]`:

### Step 4a — Full TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1
```
Zero errors required.

### Step 4b — Full Test Suite
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -20
```
100% pass required.

### Step 4c — Build Gate (frontend, if applicable)
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 180 npm run build 2>&1 | tail -10
```

### Step 4d — Security Perimeter Final
Use `grep_search` on `src/`, `functions/src/`, `scripts/`:
- `AIza` → hardcoded Firebase API key
- `sk-` → OpenAI key bleed
- `apiKey:\s*['"][^$]` → any hardcoded key pattern

Zero tolerance.

### Step 4e — Browser Witness (UI changes only)
If any UI components were modified, dispatch browser subagent:
- Navigate to `localhost:3000` (or deployed URL)
- Screenshot key page(s) touched by this sprint
- Log: `📸 [BROWSER WITNESS] Visual verified by Zoltan's Eye`
- **Phantom purge after**:
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```

---

## PHASE 5 — SPRINT SEAL & HANDOFF

### Step 5a — Session Memory Final Write
Call `mcp_brain-mcp_save_session_memory` with full sprint summary:
- All completed tasks as `completedGoals`
- Any remaining items as `activeBlockers`
- Key learnings as `learningNodes` (use full schema from `/session_end`)
- Phase bumped from MISSION_STATE.md value

### Step 5b — Project State Update
Call `mcp_brain-mcp_upsert_project_state`:
- `status`: `"ACTIVE"` (sprint done, project continues) or `"PAUSED"` (handoff)
- `notes`: `"Sprint [N] sealed — [what's next]"`

### Step 5c — MISSION_STATE Seal
Bump phase number. Update:
- `Last Major Accomplishments` — this sprint's output
- `Next Session Entry Point` — precise next uncompleted task with `[ ]`
- `System Health` — TypeScript, tests, build status all

### Step 5d — Walkthrough
Generate `walkthrough.md` with:
- Sprint summary (2-3 sentences)
- Task-by-task changes (files modified → what changed)
- Test results
- Screenshots (if browser witness ran)
- Any known remaining issues

### Step 5e — Commit the Seal
// turbo
```bash
git add -A && git commit -m "seal: Sprint Phase [N] — [sprint goal] — [task count] tasks shipped"
```

### Step 5f — Push (PASTE COMMAND ONLY)
> **SOVEREIGN LAW**: git push via run_command = hang vector. ALWAYS provide paste command.

```
GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main
```

---

## PHASE 6 — GSD SESSION HANDOFF (Multi-Session Sprints)

If the sprint spans multiple sessions:

### On Session End
GSD saves session state automatically via hooks. Additionally:
1. Run `/session_end` (which includes Remote Brain memory commit)
2. Note in MISSION_STATE.md: `Next Session Must Resume At: [TASK-N]`
3. The `~/.gsd/sessions/[session-id].json` preserves exact task index

### On Session Resume
1. Run `/session_start` (which includes Brain Sprint Intelligence Preload)
2. Read `.gsd/sprint-spec.md` to find the first unchecked `[ ]` task
3. Call `mcp_brain-mcp_search_knowledge` with the unchecked task as query
4. Resume from Phase 3 Step 3a for that specific task

> **GSD HOOK**: The `session-state-orientation` hook (installed by `--gemini --global`) automatically reads `.gsd/sprint-spec.md` at session start and presents the next incomplete task. Zero manual navigation required.

---

## QUICK REFERENCE

| Command | Action |
|---|---|
| `/gsd` | Start this workflow |
| `/gsd-map-codebase` | Analyze workspace structure |
| `/gsd-new-project` | Initialize GSD project state |
| `[spec thumbs up]` | Release execution gate |
| `[task complete]` | Atomic commit + brain micro-save |
| `/session_end` | Seal + brain write + MISSION_STATE |
| `/session_start` (next session) | Brain preload + resume from spec |

---

## COMPATIBILITY

- **Antigravity IDE**: Full support (primary target — `--gemini --global` flag)
- **GSD Version**: `get-shit-done-cc@1.34.2`
- **Brain MCP**: Required (`mcp_brain-mcp_save_session_memory`, `mcp_brain-mcp_search_knowledge`)
- **Node**: 22 LTS (all commands use `NODE_OPTIONS=--max-old-space-size=4096`)

---

*The GSD layer is Zoltan's war room. Tasks enter as chaos. They leave as atomic commits. The Brain remembers everything. The fleet obeys.*
