---
name: sovereign-terminal-operator
description: Sovereign terminal operator — Phase 57 hang-eradication patterns, non-blocking grep, timeout-safe CLI invocations, and shell diagnostic protocols.
phase: "209"
category: ops
tags: ["terminal", "bash", "hang-eradication", "cli", "diagnostics"]
---

# Sovereign Terminal Operator (R.A.P.S.) — Phase 207.16

# Execution Paradigms (Phase 57 Hang Laws)

*   **Execution Paradigms:** Absolutely prohibit `run_command` tools from wrapping pure bash `cat`, `grep`, or `sed`—you MUST use native MCP `write_to_file` and `grep_search`.
*   **Target Binaries:** Ban bare `npx playwright` or `npx tsc`. Require direct bin paths (e.g. `./node_modules/.bin/playwright`).
*   **Identity Resolution:** Ban `gcloud config get-value`. Require `.firebaserc` file extraction instead (`node -e "console.log(require('./.firebaserc').projects.default)"`).
*   **Synchronous Locks:** Prohibit `execSync(cmd)` without a robust timeout structure (e.g. `execSync(cmd, { timeout: 8000 })`).
*   **Memory Sovereignty (Rule 8):** Ensure Apple Silicon compliance by enforcing `NODE_OPTIONS=--max-old-space-size=4096` in all execution prefixes.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Verify PATH exports map to native Node 22 (`/opt/homebrew/Cellar/node@22/...`).
- [ ] Check for non-blocking flags to prevent CLI hangs during background tasks.
- [ ] Confirm `grep_search` MCP tools are prioritized over raw bash `grep`/`cat`.

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
