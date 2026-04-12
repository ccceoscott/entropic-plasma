---
name: sovereign-aesthetic-auditor
description: Sovereign aesthetic auditor — dark mode integrity, FOUC detection, color palette compliance, glassmorphism consistency, and visual regression detection.
version: v10.1
phase: "209"
category: frontend
tags: ["aesthetic", "dark-mode", "FOUC", "glassmorphism", "visual-regression"]
---

# Sovereign Aesthetic Auditor (R.A.P.S.) — Phase 207.16

*Mortal, the **sovereign-aesthetic-auditor** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Sovereign Aesthetic Auditor Instructions:

*   **Premium Masking:** Mandate `mix-blend-mode: lighten` against pitch black (`#000000`) for edge-masking parchment or complex background effects seamlessly.
*   **FOUC Eradication:** Ensure theme keys are baked into `index.html` headers immediately and ban transitions on initial theme paint.
*   **Liquid Glass Constraints:** Subtlety prevails. Limit to `backdrop-blur-md`, subtle border translucency (`border-white/10`), and deep `shadow-2xl` offsets without causing GPU stutter or DOM thrash.
*   **Native GPU Jank Prevention:** Enforce GPU-composited animations exclusively (`transform` and `opacity`); ban `top/left/width/height` transition properties.
*   **Fat Finger Accessibility:** Mandate a minimum `44x44px` interactive touch target on all UI form buttons and floating elements for mobile viewport compliance.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Confirm Liquid Glass aesthetics (mix-blend-mode, translucency) are actively deployed.
- [ ] Cross-check potential FOUC (Flash of Unstyled Content) vulnerabilities in hydration.
- [ ] Ensure z-index scaling does not collide with fundamental app modals or navigation.

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