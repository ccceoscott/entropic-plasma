---
name: liquid-glass-ui
description: Liquid Glass UI scaffolder — premium dark-mode component architecture with translucency, glassmorphism, Framer Motion animations, and fluid typography.
version: v10.2
phase: "209"
category: frontend
tags: ["liquid-glass", "dark-mode", "glassmorphism", "framer-motion", "ui"]
mutation_risk: low
timeout_budget: 20min
parallel_safe: true
outputs:
  - component_manifest: list of scaffolded components with class names
  - token_map: design token assignments (colors, glass opacity, border-radius)
  - animation_spec: Framer Motion variant definitions
success_criteria:
  - No FOUC on page load (theme class applied before paint)
  - All glassmorphism elements use backdrop-filter
  - Framer Motion wrapped in LazyMotion
handoff_map:
  on_fouc_detected: sovereign-aesthetic-auditor
  on_perf_regression: performance-engineer
fallback_behavior: Proceed with design review via screenshot comparison if browser subagent unavailable
---

# Liquid Glass Ui (R.A.P.S.) — Phase 207.16

*Mortal, the **liquid-glass-ui** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Liquid Glass UI Scaffolder Sovereign Instructions:

*   **Rule 16 (Entrance Animation Hardening):** Prohibit `initial="hidden"` on top-level pages and containers to prevent "Ghost Renders"; require default DOM visibility.
*   **LazyMotion Enforcement:** Mandate `LazyMotion` with synchronous `domAnimation` feature flag instead of standard Framer Motion imports (`<motion.div>`) to prevent synchronous rendering bloat.
*   **Zero-Sized Container Resilience (Rule 20):** Prohibit Tailwind `contents` or unheighted wrappers for top-level pages; mandate `min-h-[400px]` fallback rendering.
*   **Hydration Sync:** Always append `"use client"` to the top. To prevent hydration mismatches, ensure dynamic SVG displacement maps or heavy animations are wrapped in a `useEffect` that only renders after the component has mounted on the client.
*   **FOUC Elimination:** Ban visual flashes by applying critical CSS transition logic directly to the container logic without reliance on delayed hydration.
*   **CPQ Typography & Rendering Bounds:** Ban all solid colors (`bg-red-500` etc.) in favor of `bg-white/5` and structural translucency. Data tables must be locked inside `overflow-hidden rounded-2xl border border-white/10`. Quantitative prices and sizes must utilize `text-white font-mono` high-contrast styling. Always enforce "Skeleton First" rendering utilizing `animate-pulse` masks initially.
*   **Next.js 15+ Caching Laws:** Route handlers and fetches are uncached by default in 2026. Mandate explicit `next: { revalidate: X }` tags or `unstable_cache` for DB hits.
*   **Suspense Streaming Boundaries:** Mandate that all `<Suspense fallback={...}>` Loading Skeletons are dimensionally identical to the rendered content to prevent Cumulative Layout Shift (CLS) when streaming.

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Audit Tailwind configuration for sovereign aesthetic tokens.
- [ ] Check `framer-motion` for `LazyMotion` enforcement over synchronous bloat.
- [ ] Verify translucency performance and repaint-costs on hardware-accelerated layers.

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