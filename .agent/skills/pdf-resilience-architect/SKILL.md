---
name: pdf-resilience-architect
description: PDF generation and processing resilience architect — Puppeteer/PDFKit hardening, memory leak prevention, timeout management, and S3/GCS upload patterns.
phase: "209"
category: backend
tags: ["pdf", "puppeteer", "pdfkit", "resilience", "generation"]
---

# Pdf Resilience Architect (R.A.P.S.) — Phase 207.16

# Instructions

1. **CORS Tainted Guardian**: Mandate pre-fetching of remote assets into Base64 Data URIs before rendering the canvas.
2. **Oklch Transmutation**: Remap `oklch()` color functions to standard HEX strings in the clone phase to prevent engine crashes.
3. **Memory Sanctum**: In iOS/Safari, implement pagination to prevent multi-page rendering from crashing the tab.
4. **Vector Alignment**: Force explicit inline dimensions on all SVGs during pre-processing for A4 matrix scaling.

*   **CORS Tainted Canvas Guard:** Absolute pre-fetching of remote assets into Base64 Data URIs is MANDATORY before firing the render canvas.
*   **Oklch Remediation:** Intercept and remap `oklch()` color functions to standard HEX strings in the clone phase to prevent legacy canvas engines crashing.
*   **Vector Safety:** Default all SVGs to explicitly defined dimensions (`width` and `height` inline) during the pre-processing stage to ensure scale matches on A4 matrices.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Verify `html2canvas` / `jspdf` dependency versions and stable mounts.
- [ ] Confirm PDF orientation rules (A4, portrait/landscape) and element off-screen visibility.
- [ ] Audit memory constraints for multi-page rendering to prevent Safari/iOS crashing.

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
