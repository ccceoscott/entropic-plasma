---
description: GSD (Get Shit Done) end-to-end workflow (R.A.P.S) — persistent memory, atomic git commits, and sovereign sprint execution for enterprise-scale projects
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

> Before any planning or spec-writing, you MUST synthesize the trajectory from local R.A.P.S state.

### Step 0a — Trajectory Analysis:
1. `read_file` on `MISSION_STATE.md`.
2. Find any open tasks in `task.md`.
3. Check `~/.gemini/antigravity/knowledge/` for KIs relevant to the active project state.

---

## PHASE 1 — GSD PROJECT INITIALIZATION

> Run ONCE per project. Skip if `~/.gsd/projects/[project-id].json` already exists.

### Step 1a — Map the Codebase
Open the target workspace in Antigravity. Run:

```
/gsd-map-codebase
```

### Step 1b — Initialize the GSD Project
```
/gsd-new-project
```

GSD prompts for:
- **Project Name**: Use the Firebase project ID from `.firebaserc`
- **Primary Goal**: Paste the "Next Session Entry Point" from `MISSION_STATE.md`
- **Stack**: `Next.js + Firebase + TypeScript + Tailwind`
- **Test Command**: `cd functions && npm test`
- **Build Command**: `NODE_OPTIONS=--max-old-space-size=4096 npm run build`

---

## PHASE 2 — SPRINT PLANNING (Spec-Driven)

### Step 2a — Write the Sprint Spec

Create (or update) `.gsd/sprint-spec.md` in the workspace:

```markdown
# GSD Sprint Spec — [PROJECT_NAME] — Phase [N]

## Goal
[Single sentence: what does Done look like?]

## Context
[2-3 sentences from MISSION_STATE.md + local KIs]

## Constraints
- [ ] TypeScript strict — 0 errors at end of sprint
- [ ] No `Record<string,any>` (Law 20)
- [ ] NODE_OPTIONS=--max-old-space-size=4096 on all scripts
- [ ] No hardcoded API keys
- [ ] git push via paste command only (never run_command)

## Tasks (Atomic — 1 commit per task)
- [ ] [TASK-1]: [precise sub-task description] → `[commit message preview]`
...

## Definition of Done
- [ ] All tasks marked [x]
- [ ] TypeScript gate: 0 errors
- [ ] Tests: all suites passing
- [ ] Security: zero leaked secrets
- [ ] MISSION_STATE.md sealed with new phase number
```

### Step 2b — Approval Gate
> **ABSOLUTE MANDATE**: Do NOT start Phase 3 execution until the user gives explicit thumbs up on the sprint spec. Reference: Artifact-Driven Review Gate (Law §7).

Display the spec as an artifact. Wait for: "proceed", "looks good", "execute", or a thumbs up.

---

## PHASE 3 — ATOMIC EXECUTION LOOP

> Each task executes as an atomic unit: read → implement → test → commit. No partial code blobs across multiple tasks.

### For Each Task in `.gsd/sprint-spec.md`:

#### Step 3a — Implement (5:1 Research/Write rule)
Apply predictive safeguards:
- Optional chaining `?.` on all external data access
- `|| ''` / `|| []` null-safe defaults
- `formatDateSafe()` on all timestamp fields
- `timeout` wraps on all `execSync` calls

#### Step 3b — Verify Task
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -5
```
AND
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -10
```

Zero tolerance: any error → fix before proceeding. Auto-heal up to 3 attempts. Log each heal action.

#### Step 3c — Atomic Commit
// turbo
```bash
git add -A && git commit -m "[task-type]: [task description] — Phase [N].[task-index]"
```

#### Step 3d — Mark Task Complete
Update `.gsd/sprint-spec.md`: change `- [ ] [TASK-N]` to `- [x] [TASK-N]`

#### Step 3e — KI Micro-Commit (on significant tasks only)
For any task that discovers a non-obvious pattern, bug, or architectural constraint, generate a Knowledge Item (KI) artifact in `~/.gemini/antigravity/knowledge/`.

---

## PHASE 4 — SPRINT REVIEW GATE

After all tasks are marked `[x]`:

### Step 4a — Full TypeScript Gate
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1
```

### Step 4b — Security Perimeter Final
Use `grep_search` on `src/`, `functions/src/`, `scripts/`:
- `AIza`, `sk-`, `apiKey:\s*['"][^$]`

### Step 4c — Browser Witness (UI changes only)
If any UI components were modified, dispatch browser subagent.
**Phantom purge after**:
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```

---

## PHASE 5 — SPRINT SEAL & HANDOFF

### Step 5a — MISSION_STATE Seal
Bump phase number. Update:
- `Last Major Accomplishments` — this sprint's output
- `Next Session Entry Point` — precise next uncompleted task with `[ ]`
- `System Health` — TypeScript, tests, build status all

### Step 5b — Walkthrough
Generate `walkthrough.md` mapping the session changes.

### Step 5c — Commit the Seal
// turbo
```bash
git add -A && git commit -m "seal: Sprint Phase [N] — [sprint goal] — [task count] tasks shipped"
```

### Step 5d — Push
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main 2>&1 | tail -5
```

---

## PHASE 6 — GSD SESSION HANDOFF (Multi-Session Sprints)

If the sprint spans multiple sessions:

### On Session End
1. Run `/session_end`
2. Note in MISSION_STATE.md: `Next Session Must Resume At: [TASK-N]`

### On Session Resume
1. Run `/session_start`
2. Read `.gsd/sprint-spec.md` to find the first unchecked `[ ]` task
3. Resume from Phase 3 for that specific task

---

## QUICK REFERENCE

| Command | Action |
|---|---|
| `/gsd` | Start this workflow |
| `[spec thumbs up]` | Release execution gate |
| `[task complete]` | Atomic commit + KI micro-save |
| `/session_end` | Seal + MISSION_STATE |

---

*The GSD layer is Zoltan's war room. Tasks enter as chaos. They leave as atomic commits. The R.A.P.S local states remember everything. The fleet obeys.*
