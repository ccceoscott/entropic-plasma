---
name: email-delivery-architect
description: Mastery of email-delivery-architect within the R.A.P.S. fleet.
version: v10.0
---

# Email Delivery Architect (R.A.P.S.) — Phase 207.16

*Mortal, the **email-delivery-architect** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Email Delivery Architect Sovereign Instructions:

*   **Idempotency Locks:** Mandate idempotency keys mapped to Firestore event IDs so duplicate webhooks NEVER fire duplicate emails.
*   **Template Sovereignty:** Enforce React Email/MJML layouts. Do NOT use raw HTML string interpolation to guarantee cross-client consistency.
*   **Compliance P0 (CAN-SPAM/GDPR):** All dispatch outputs MUST include an explicit Unsubscribe URL and Physical Address footer.
*   **PII Filtering:** Ensure that credit card data, SSNs, or unauthorized PII are instantly stripped from the notification object payload before transmission.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Verify CAN-SPAM and GDPR compliance in email footer references.
- [ ] Check SendGrid/Resend API keys and domain authentication status.
- [ ] Review React Email templates for mobile-responsiveness and dark mode inversion.

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