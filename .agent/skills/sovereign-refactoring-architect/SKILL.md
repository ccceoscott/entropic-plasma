---
name: sovereign-refactoring-architect
description: Sovereign refactoring architect — safe, systemic code evolution with side-effect analysis, module extraction, and zero-regression enforcement.
phase: "209"
category: backend
tags: ["refactoring", "architecture", "side-effects", "modules", "evolution"]
---

# Sovereign Refactoring Architect (R.A.P.S.) — Phase 207.16

# Instructions

1. **Structural Scrutiny**: Perform Deep Architectural Analysis (DAA) of the target files.
2. **Component Decomposition**: Target bloated files for splitting into modular Next.js components.
3. **Extraction Priority**: Must resolve extractions in strict order: 1) Types & Interfaces, 2) Pure Utils, 3) Hooks, 4) JSX Sub-components.
4. **Refactor Chain**: Delegate surgical cleanup to `code-refactoring-refactor-clean`.
5. **Safety Wards**: Mandatory regression testing via unit tests or E2E suites before completion.

*   **Phase 2 Extraction Priority:** Must resolve extractions in strict order: 1) Types & Interfaces, 2) Pure Utils, 3) Hooks, 4) JSX Sub-components.
*   **TypeScript Integrity:** Zero tolerance for new `any` types in outputs. Convert all blind `as any` casting to defined interfaces.
*   **Defensive Syntax:** Enforce mandatory optional chaining (`?.`) on nested props and null-safe defaults (`|| ''` or `??`) when reading external configuration.
*   **Next.js 15+ RSC Supremacy:** Enforce Server Components by default. Push "use client" directives to the leaves of the render tree and pass structural HTML shells as React children.
*   **Partial Prerendering (PPR):** Design components to support PPR by wrapping dynamic data fetches in `<Suspense>` boundaries while keeping the static shell instant.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Map explicit inter-component dependencies before isolating variables.
- [ ] Secure pre-refactor Git checkpoint for immediate rollback capability.
- [ ] Establish sequence of atomic, non-breaking modifications.

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
