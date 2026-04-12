---
name: zustand-firebase-sync
description: Zustand global state and Firebase real-time sync master — store architecture, Firestore listeners, optimistic updates, and persistence patterns.
version: v10.1
phase: "209"
category: frontend
tags: ["zustand", "firebase", "state-management", "real-time", "persistence"]
---

# Zustand Firebase Sync (R.A.P.S.) — Phase 207.16

*Mortal, the **zustand-firebase-sync** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Instructions

1. **Hydration Sanctuary**: Isolate Firebase Admin SDK exclusively to Server Actions for data hydration into Zustand initializers.
2. **Interface Parity**: Mandate single object/interface payloads for all Server Actions (Rule 14).
3. **Pecuniary Wards**: Force conversion of financial vectors to **CENTS** (zero-decimal) before transmission.
4. **UI Isolation**: Keep generic UI state (drawers, modals) in a dedicated `useUIStore.ts` to prevent tree-wide re-renders.
5. **Architectural Purity**: NEVER use React Context for global state; defer entirely to modular Zustand slices.

*   **Rule 14 (Interface-Based Input):** Mandate single object/interface payloads for complex Server Actions to prevent positional argument regressions.
*   **Floating-Point Ban:** Dictate strict translation of financial vectors to zero-decimal minimum units (cents) before state transmission to prevent IEEE-754 precision bleeding.
*   **Hydration Boundary:** Isolate Firebase Admin SDK exclusively to Server Actions communicating down to Zustand slice initializers.
*   **CPQ Decoupling Integration:** When designing Calculate/Price/Quote matrices, always decouple from generic state and push to dedicated calculation engines inside Server Actions.
*   **Modularity:** Keep Zustand slices modular (e.g., `createOrderSlice`, `createProductSlice`). NEVER use React Context for global state.
*   **Data Plumber UI Isolation:** Act as the pure data orchestrator. For global drawer/modal components (like `<CartDrawer />`), mandate execution state through a completely isolated `useUIStore.ts` slice so that DOM mutations bypass full-tree React rendering updates.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Assess offline-first assumptions and sync hydration loops.
- [ ] Verify slice immutability and precise deep-equality rendering checks.
- [ ] Check Admin SDK hook logic for phantom re-renders or zombie subscriptions.

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