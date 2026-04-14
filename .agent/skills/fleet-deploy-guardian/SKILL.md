---
name: fleet-deploy-guardian
description: Fleet-wide deployment guardian — safe-deploy protocol, project ID verification, pre-commit hooks, rollback patterns, and multi-gate deploy execution.
phase: "209"
category: ops
tags: ["deploy", "firebase", "safe-deploy", "rollback", "pre-commit"]
  - deploy_receipt: target project ID, deploy scope, and timestamp
  - gate_pass_log: results of all pre-deploy checks (secrets, lint, rules)
  - rollback_instructions: exact command to revert if needed
success_criteria:
  - Project ID verified via .firebaserc before any firebase deploy
  - Zero hardcoded secrets detected in scan
  - Deploy scope explicitly declared (--only functions, --only hosting, etc.)
  on_security_block: security-auditor
  on_rules_block: auth-security-architect
  on_type_block: typescript-safety-enforcer
---

# Fleet Deploy Guardian (R.A.P.S.) — Phase 207.16

# Fleet Deploy Guardian Instructions (God Protocol Rule 25):

*   **The Vanguard Identity Lock:** Enforce mandatory `firebase use <EXPECTED_PROJECT>` script assertions before any deploy operation to prevent alias bleeding.
*   **Execution Blockade:** The guard MUST `process.exit(1)` immediately if the returned alias does not match the active target string exactly.
*   **Manual Transmission:** Support bypass mechanisms (`--skip-build`, `--skip-tests`) exclusively wrapped in dry-run checks and mandatory post-deploy live audits.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Affirm absolute directory proximity locks prior to any `safe-deploy` initialization.
- [ ] Parse dynamic `.firebaserc` files for exact project-ID safety matches.
- [ ] Scan for cross-project "Poison Strings" or legacy brand bleeds.

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
