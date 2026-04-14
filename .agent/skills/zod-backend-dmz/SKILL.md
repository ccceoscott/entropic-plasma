---
name: zod-backend-dmz
description: Zod validation DMZ for Cloud Functions — schema-first callable validation, input sanitization, and type-safe request/response contracts.
phase: "209"
category: backend
tags: ["zod", "validation", "cloud-functions", "schema", "type-safety"]
  - schema_coverage_map: callable functions with/without Zod validation
  - validation_gap_list: unvalidated inputs with injection risk rating
  - zod_schema_diffs: proposed schema additions
success_criteria:
  - Every onCall function has Zod schema guard at entry
  - All monetary fields validated as z.number().int().positive()
  - Free-text fields have z.string().max(N).trim() constraints
  on_type_gap: typescript-safety-enforcer
  on_sanitization: ecommerce-reviewer
  on_schema: data-model-architect
---

# Zod Backend Dmz (R.A.P.S.) — Phase 207.16

# Instructions

1. **Strict Parsing Protocols**: Mandate `z.object().strict().safeParse()` on all input schemas for Callable Cloud Functions.
2. **Standard Issue Reporting**: For validation errors, explicitly use `.issues[0].message`. Ban legacy `.errors`.
3. **Full-Stack Parity**: Export all backend schemas to a shared `types/` directory to guarantee Next.js client sync.
4. **Gemini SDK Sovereignty**: Exclusively use the `google-genai` Node.js SDK for all Gemini interactions.
5. **Gen 2 Concurrency**: Note that Firebase Gen 2 handles 80 concurrent requests. Avoid shared mutable global state.

*   **Strict Issue Reporting:** When handling Zod validation errors, explicitly use `.issues[0].message`. Absolutely ban the legacy `.errors` array call which breaks TypeScript definitions in v3.
*   **Strict Mode Parsing:** Mandate `z.object().strict().safeParse()` on all input schemas for callable Cloud Functions to reject undocumented properties automatically.
*   **Interface Over Positional Arguments:** Command (Rule 14) states complex functions must accept a single typed interface/object, bypassing positional errors.
*   **Full-Stack Schema Parity:** All `.zod` schemas used in backend `.onCall` validation MUST be exported to a global, shared `types/` directory to guarantee perfectly mapped interfaces to Next.js client layers.
*   **2026 Vertex AI Purge:** The legacy `@google-cloud/vertexai` SDK is DEPRECATED. You MUST exclusively use the unified `google-genai` Node.js SDK for all Gemini API interaction.
*   **Gen 2 Concurrency Guard:** Firebase Gen 2 handles 80 concurrent requests per instance. You MUST NOT use Shared Mutable Global Variables to store request state. State must be tightly scoped to prevent cross-request contamination.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Test strict `.strict()` schema rules and absolute type stripping.
- [ ] Verify runtime boundary payload checks against malicious injection strings.
- [ ] Ensure absolutely zero generic `any` casts exist in data translation pipes.

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
