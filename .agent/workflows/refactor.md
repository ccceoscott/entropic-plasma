---
description: Safe, zero-downtime refactoring of massive components
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /refactor
> ⚡ **REQUIRED SKILLS**: `sovereign-refactoring-architect`, `zod-backend-dmz`
## Sovereign Refactoring Protocol — Zero Breaking Changes, Full Test Coverage

> ⚡ **MANDATE**: Every refactor is test-gated before AND after. No refactor ships without TypeScript clean and unit tests passing. Self-healing on all regressions.

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

### Phase 0c — TypeScript Pre-Refactor Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
**CRITICAL**: Record exact error count BEFORE refactor. If pre-existing errors → document them as separate from refactor-introduced errors.

### Phase 0d — Pre-Refactor Test Baseline
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -10
```
Record: test count, pass count, fail count. Refactor must NOT increase failure count.

---

## PHASE 1 — Component Analysis & Refactor Plan

### 1a — Target Component Deep Read
Use `view_file` on target component — read ALL lines. Do not skip sections.
Identify:
- Lines of code
- Number of responsibilities (signals: hooks, API calls, rendering, state, formatters all in one file)
- External dependencies used
- Types/interfaces defined inline vs. imported

### 1b — Dependency Graph
Use `grep_search` for the component name across `src/**/*.tsx,src/**/*.ts` to find all consumers.
This is the blast radius. Any change must not break any consumer.

### 1c — MCP Knowledge Anchoring
Search standard KIs (`~/.gemini/antigravity/knowledge/`) or `KNOWLEDGE.md` for context.
Check if a refactor pattern for this component type has been established previously.
If yes → follow the established pattern exactly.

### 1d — Refactor Specification (Required Before Execution)
Document in structured format:
```
Target: [component name] ([line count] lines)
Violations: [list each SRP violation]
Planned Splits:
  - [NewComponent1]: [responsibility]
  - [NewHook1]: [concern]
  - [NewUtil1]: [utility logic]
Consumer Impact: [list of files that import target]
Blast Radius: [count] files
```

---

## PHASE 2 — Execution (Surgical Splits)

### 2a — Type Extraction (ALWAYS FIRST)
Extract all TypeScript interfaces and types from the target component.
Create `types/[ComponentName].types.ts` or add to existing types file.
Update all imports in consumers.
Run TS check after this step:
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Must be zero new errors before continuing. If new errors → fix immediately.

### 2b — Utility Extraction
Extract pure functions (no hooks, no JSX) to `utils/[domain].ts`.
Pure functions = same input → same output. No side effects.
Run TS check.

### 2c — Hook Extraction
Extract React state and side-effect logic to `hooks/use[Feature].ts`.
Each hook: single concern. 1 hook = 1 purpose.
Run TS check.

### 2d — Sub-Component Extraction
Extract logical rendering sections to individual component files.
Each sub-component: receives only props it needs (prop drilling analysis required).
Run TS check.

### 2e — Barrel Export Update
Update index files or existing barrel exports to include new files.
Do NOT create new barrel files (tree-shaking impact).

---

## PHASE 3 — Post-Refactor Verification

### 3a — TypeScript Full Verification
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
Compare error count to pre-refactor baseline.
**Zero new errors permitted**. If new errors appeared → auto-fix each.
Log: `🔧 [AUTO-FIXED] [error type]: [fix applied]`

### 3b — Frontend TypeScript Scan
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
Same zero-new-error policy.

### 3c — Test Suite Post-Refactor
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 npm test 2>&1 | tail -15
```
Compare against pre-refactor baseline from Phase 0d.
Any new failures → immediate investigation → auto-fix:
1. Was it a test that depended on the OLD internal structure? → Update test to reflect new structure
2. Was it a genuine regression? → Fix the code, not the test

### 3d — Consumer Verification
For each consumer identified in Phase 1b:
- Use `view_file` to confirm imports are updated
- Key entry: the consuming component renders without prop type errors

---

## PHASE 4 — Browser Regression Check (Eye of Zoltan)

### 4a — Dev Server
// turbo
```bash
lsof -ti:3000 2>/dev/null | head -3 || echo "no server"
```
If not running → `NODE_OPTIONS=--max-old-space-size=4096 npm run dev &` and wait 8s.

### 4b — Visual Regression Test
Use `browser_subagent` to:
1. Navigate to `http://localhost:3000`
2. Navigate to the page that uses the refactored component
3. Take screenshot
4. Report any visual regression vs. known baseline
5. Report any console errors from the refactor

### 4c — Console Error Scan (MCP)
Use `mcp_chrome-devtools_list_console_messages` with types `["error", "warn"]`.
Any new errors post-refactor → identify source → fix.

---

## PHASE 5 — Code Quality Metrics

### 5a — `any` Type Eradication
Use `grep_search` for `as any` and `: any` in the new/modified files.
Each `any` → replace with specific type. Log each fix.
Target: ZERO `any` types in new code.

### 5b — Optional Chaining Enforcement
Use `grep_search` for `&&` in JSX access patterns (e.g., `user && user.name` → should be `user?.name`).

### 5c — null-safe Defaults
Use `grep_search` for `|| ''` and `|| 0` and `|| []` — confirm null-safe fallbacks exist for all external data access.

---

## PHASE 6 — Seal & Persistence

### Knowledge Base Persistence (R.A.P.S)
Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Refactor pattern used
- Component type → split strategy
- Any regression discovered and fixed
- Final line counts (before vs after)

### 6b — MISSION_STATE Update
Bump phase. Log in `Last Major Accomplishments`:
`Refactored [ComponentName]: [X] lines → [N] focused files. Zero regressions.`

### 6c — Git Commit
// turbo
```bash
git add -A && git commit -m "refactor: [ComponentName] SRP split — Phase [N] sovereign standard"
```

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Refactor complete. Zero breaking changes. Codebase hardened.`
