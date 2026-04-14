---
name: e2e-testing-patterns
description: Playwright E2E testing pattern library — sovereign test patterns, fixture management, network mocking, and multi-environment test matrix design.
phase: "209"
category: testing
tags: ["playwright", "e2e", "testing", "fixtures", "patterns"]
---

# E2E Testing Patterns (R.A.P.S.) — Phase 207.16

# Instructions

1. **Law 13 Compliance**: Adhere strictly to Phase 195 E2E Playwright Sovereign Laws (Workers=1, Timeout=150000, PW_ALLOW_PROD=true).
2. **Conflict Resolution**: Always purge active ports (5173/3000) before invocation using `lsof` and `kill`.
3. **Soft Assertions**: Never hard-fail on UX variations or optional steps. Use `isVisible` conditional logic.
4. **Stripe Ward**: Card iframes are CSP-blocked in tests. Verify mount only; skip fill.

Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do.

## Use this skill when

- Implementing end-to-end test automation
- Debugging flaky or unreliable tests
- Testing critical user workflows
- Setting up CI/CD test pipelines
- Testing across multiple browsers
- Validating accessibility requirements
- Testing responsive designs
- Establishing E2E testing standards

## Do not use this skill when

- You only need unit or integration tests
- The environment cannot support stable UI automation
- You cannot provision safe test accounts or data

## Instructions

1. Identify critical user journeys and success criteria.
2. Build stable selectors and test data strategies.
3. Implement tests with retries, tracing, and isolation.
4. Run in CI with parallelization and artifact capture.

## Safety

- Avoid running destructive tests against production.
- Use dedicated test data and scrub sensitive output.

## Resources

- `resources/implementation-playbook.md` for detailed E2E patterns and templates.
