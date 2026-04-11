---
description: Comprehensive unit testing across components, cloud functions, and emulator boundaries
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /unit_testing
## Sovereign Test Execution — Self-Healing, Zero-Tolerance Failure Protocol

> ⚡ **MANDATE**: Every test failure triggers immediate root-cause analysis and auto-fix attempt. Tests are truth. Never modify tests to make code pass — fix the code.

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

### Phase 0c — TypeScript Gate (Pre-Test)
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```
TS errors block testing. Fix first.

---

## PHASE 1 — Test Infrastructure Verification

### 1a — Test Framework Audit
Use `view_file` on `functions/package.json`:
- Confirm `jest` or `vitest` with version ≥ declared standard
- Confirm test script includes `NODE_OPTIONS=--max-old-space-size=4096`
- Confirm `--testTimeout` is set (recommended: 10000ms for emulator-backed tests)

### 1b — Test File Discovery
// turbo
```bash
find functions/src -name "*.test.ts" -o -name "*.spec.ts" | head -20
```
Count total test files. If 0 → this is a P1. Scaffold tests for core functions immediately (Phase 3).

### 1c — Emulator Detection
// turbo
```bash
lsof -ti:5001,9099,8080 2>/dev/null | head -5 || echo "emulators offline"
```
Record status. Some test suites (integration) require emulators. Unit tests must NOT require emulators.

### 1d — Testing KI Grounding (MCP)
Search standard KIs (`~/.gemini/antigravity/knowledge/`) or `KNOWLEDGE.md` for context.
Load any established testing patterns from previous sessions to avoid re-solving known patterns.

---

## PHASE 2 — Core Unit Test Execution

### 2a — Full Unit Test Suite
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm test -- --forceExit 2>&1
```

### 2b — Failure Analysis (MANDATORY for each FAIL)
For each `FAIL` in output:
1. **Read the full error** — full stack trace, not just summary
2. **Locate the test file** via `view_file`
3. **Locate the source file** it tests via `view_file`
4. **Root cause classification**:
   - Type A: Logic regression in source → fix source
   - Type B: Stale test expectations → only update if source behavior is intentionally different
   - Type C: Missing mock → add mock
   - Type D: Async timing issue → add `await` or fix promise chain
   - Type E: Import path changed → update import
5. **Apply fix** via file edit tools
6. Log: `🔧 [AUTO-FIX] [test-name]: Type [A-E] — [fix description]`

### 2c — Re-Run After Fixes
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm test -- --forceExit 2>&1 | tail -20
```
Repeat 2b-2c until 0 failures or a root cause is identified that requires user input.

---

## PHASE 3 — Test Coverage Analysis

### 3a — Coverage Report
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm test -- --coverage --forceExit 2>&1 | tail -30
```

### 3b — Coverage Gap Identification
For any file with < 60% coverage:
1. Use `view_file` on the source file
2. Identify untested critical paths (auth checks, error handlers, data transformations)
3. Scaffold missing test cases using THIS pattern:

```typescript
describe('[FunctionName]', () => {
  it('should [behavior] when [condition]', async () => {
    // Arrange
    const input = { /* minimal valid input */ }
    // Act
    const result = await functionUnderTest(input)
    // Assert
    expect(result).toMatchObject({ /* expected shape */ })
  })

  it('should throw [ErrorType] when [invalid condition]', async () => {
    await expect(functionUnderTest(invalidInput)).rejects.toThrow('[ErrorMessage]')
  })
})
```

4. Prioritize coverage for: auth validation, data validation, error paths, Firestore write operations

### 3c — Critical Functions Mandatory Coverage List
Confirm 100% coverage on these function categories:
- Authentication helpers
- Stripe webhook handlers
- Firestore security utility functions
- Rate limiting functions
- Any function with `admin.firestore().collection().doc().set()`

---

## PHASE 4 — Emulator Integration Tests (if applicable)

### 4a — Emulator Start (if needed)
If integration tests exist AND emulators offline:
// turbo
```bash
firebase emulators:start --only firestore,functions,auth --project gen-lang-client-0386732425 &
```
Wait 10 seconds for emulator initialization.

### 4b — Integration Test Execution
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 180 ./node_modules/.bin/jest --testPathPattern=integration --forceExit 2>&1 | tail -20
```

### 4c — Emulator Log Scan (MCP)
After integration tests, use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "WARNING"` and `page_size: 20`.
Emulator logs sometimes surface data validation issues not caught by assertions.
Any warning → investigate → fix source.

---

## PHASE 5 — Frontend Component Tests (if exist)

### 5a — Component Test Discovery
// turbo
```bash
find src -name "*.test.tsx" -o -name "*.spec.tsx" | head -20
```

### 5b — Component Test Execution
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm test -- --forceExit 2>&1 | tail -20
```
Same failure analysis protocol as Phase 2b.

---

## PHASE 6 — `any` Type Eradication in Tests

Use `grep_search` for `: any` and `as any` in test files (`*.test.ts,*.spec.ts`).
`any` in tests hides type bugs. Each match → replace with specific type or `unknown` with type guard.
Log: `🔧 [TEST HARDENED] [file]: replaced any with [type]`

---

## PHASE 7 — Unhandled Promise Rejection Audit

Use `grep_search` for `.catch(` and `process.on('unhandledRejection'` in `functions/src/**/*.ts`.
Any async function without error handling → wrap in try/catch.
Any function with `.catch(console.error)` → replace with proper error handling and telemetry.

---

## PHASE 8 — Final TypeScript & Knowledge Seal

### 8a — Final TS Check
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```

### Knowledge Base Persistence (R.A.P.S)
Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Test patterns established
- Coverage gaps found and filled
- Auto-fix types applied (A-E classification)
- Any emulator-specific behavior documented

### 8c — MISSION_STATE Update
Bump phase. Log: `Testing: [N] tests, [X]% coverage, [F] auto-fixed failures.`

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Test session sealed.`
