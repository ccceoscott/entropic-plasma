---
description: Comprehensive Unit Testing — Self-Healing, Zero-Tolerance Failure Protocol.
alwaysApply: false
---

# 🧪 /unit_test — The Sovereign Forge (v12.0)

⚡ **MANDATE**: Every test failure triggers immediate root-cause analysis and auto-fix attempt. Tests are truth. Never modify tests to make code pass — fix the code.

## 🧠 Skill Ingestion
**Automatically ingest this Domain Bundle**:
1. `!hammer` — Sovereign Hammer (Ops, Testing, Execution)
2. `!arch` — Sovereign Architect Domain (Logic, Data, Type Safety)

---

## 🔍 THE TESTING PATH
1. **Test Discovery**: Locate test files (`.test.ts`, `.spec.tsx`). Identify untested critical paths (Auth, DB Writes, Monetary Math).
2. **Execution**: Run `npm test` under the terminal wrapper with memory caps (`NODE_OPTIONS=--max-old-space-size=4096`). 
3. **Failure Analysis**: For every `FAIL`:
   - Identify Root Cause (Logic, Stale Expectation, Missing Mock, Async Timing)
   - ⚡ Do NOT ask permission. Automatically deduce, patch the source code, and re-run.
4. **Type Eradication**: Scour test files for `: any` and `as any`. Eradicate them with strict types or `unknown` type guards.
5. **Coverage Seal**: Report final test count, coverage gaps, and auto-fixes applied.

Declare: `✅ [UNIT TESTING COMPLETE] | Tests executed. Failures healed. Zero 'any' types remain.`
