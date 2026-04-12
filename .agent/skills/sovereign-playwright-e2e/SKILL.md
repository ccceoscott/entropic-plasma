---
name: sovereign-playwright-e2e
description: Sovereign Playwright E2E master — production test execution, Stripe CSP handling, multi-environment matrix, and worker concurrency governance.
version: v10.1
phase: "209"
category: testing
tags: ["playwright", "e2e", "production-testing", "stripe", "chromium"]
---

# Sovereign Playwright E2E (R.A.P.S.) — Phase 207.16

*Mortal, the **sovereign-playwright-e2e** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Sovereign Playwright E2E Instructions (Phase 195 Laws):

*   **Non-Blocking Logic:** Mandate `locator.isVisible({ timeout: N }).catch(() => false)` conditional flows instead of blocking `waitFor()` to prevent infinite test hangs.
*   **Production Environment Flags:** Mandate `--workers=1`, `--project=chromium`, and `PW_ALLOW_PROD=true` in execution scripts.
*   **Port Clearance:** Enforce pre-execution port check (`lsof -nP -ti:PORT | xargs kill -9`) to prevent watchdog hang.
*   **Soft Assertions:** Require `if (condition) { expect() } else { log('ℹ️ ...') }` for UX variations (e.g., if a `/register` route isn't strictly exposed).
*   **Stripe CSP Validation:** Stripe card iframes are CSP-blocked in testing. Verify mount only via iframe locator existence; skip payload filling.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Check `PW_ALLOW_PROD` environment flag verification.
- [ ] Set absolute `--workers=1` to enforce synchronous serial environment conditions.
- [ ] Verify Port 5173 collision avoidance logic and `lsof` purgatory locks.

### 📊 Sovereign Agent Post-Action Report

*At the conclusion of your execution, or before halting for user review, you MUST output this standardized report regarding the health and outcome of your task.*

**1. Systems Status & Execution Overview:**
- **🟢 Working:** [List functional components verified, architecture stabilized, or test suites passed]
- **🟡 Degraded:** [List components experiencing latency, minor warning logs, sync issues, or imperfect aesthetics]
- **🔴 Non-Functional:** [List explicitly broken logic, API blockers, or failed validations]

**2. Sovereign Compliance & Audit:**
- **Security Integrity:** [Pass/Fail/Not Applicable] (Secret exposure, IAM rules, Zero-Trust gates)
- **Performance Constraint:** [Pass/Fail/Not Applicable] (Node V8 Memory, Context Limit, payload size)
- **Architectural Drift:** [None/Minor/Major] (Does the codebase differ from established SSOT / MISSION_STATE?)

**3. Incident Triggers (Priority Tickets):**
- **[P0] CRITICAL BLOCKER:** [Immediate action required, deployment halted, severe data risk, security breach]
- **[P1] High Impact:** [Major feature failure, degraded primary user workflow, E2E suite failure]
- **[P2] Medium Impact:** [Edge-case failures, non-fatal performance friction, hydration warnings]
- **[P3] Low Impact:** [UI misalignments, tech debt, cleanup tasks, deprecated API usage]

**4. Next Sovereign Directive:**
- [List 1-2 immediate next steps based on the findings above, strictly adhering to R.A.P.S. architecture]