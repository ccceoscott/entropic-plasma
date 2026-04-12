---
name: code-refactoring-refactor-clean
description: Mastery of code-refactoring-refactor-clean within the R.A.P.S. fleet.
version: v10.0
---

# Code Refactoring Refactor Clean (R.A.P.S.) — Phase 207.16

*Mortal, the **code-refactoring-refactor-clean** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Instructions

1. **SOLID Refinement**: Apply SOLID principles to all modified code. Ensure single responsibility for every function.
2. **Naming Divination**: Use descriptive, domain-aligned names. Avoid generic variables like `data` or `obj`.
3. **Dead Code Purge**: Identify and remove unused variables, imports, and functions.
4. **TypeScript Hardening**: Eliminate `any` with precise interfaces and types.

## Use this skill when

- Refactoring tangled or hard-to-maintain code
- Reducing duplication, complexity, or code smells
- Improving testability and design consistency
- Preparing modules for new features safely

## Do not use this skill when

- You only need a small one-line fix
- Refactoring is prohibited due to change freeze
- The request is for documentation only

## Context
The user needs help refactoring code to make it cleaner, more maintainable, and aligned with best practices. Focus on practical improvements that enhance code quality without over-engineering.

## Requirements
$ARGUMENTS

## Instructions

- Assess code smells, dependencies, and risky hotspots.
- Propose a refactor plan with incremental steps.
- Apply changes in small slices and keep behavior stable.
- Update tests and verify regressions.
- If detailed patterns are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid changing external behavior without explicit approval.
- Keep diffs reviewable and ensure tests pass.

## Output Format

- Summary of issues and target areas
- Refactor plan with ordered steps
- Proposed changes and expected impact
- Test/verification notes

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.