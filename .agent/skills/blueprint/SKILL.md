---
name: blueprint
description: System blueprint generator — produces C4 diagrams, architecture decision records (ADRs), and data flow maps for new and existing systems.
phase: "209"
category: protocol
tags: ["blueprint", "architecture", "ADR", "c4", "documentation"]
---

# Blueprint (R.A.P.S.) — Phase 207.16

# Overview
Blueprint is for multi-session, multi-agent engineering projects where each step must be independently executable by a fresh agent that has never seen the conversation history.

## Instructions

1. **Vision Quest**: Deconstruct the objective into independent, self-contained construction steps (typically one-PR-sized).
2. **Contextual Isolation**: Each step MUST contain a brief that allows a fresh agent to execute it without prior history.
3. **Execution Logic**:
   - **Research**: Scan the codebase, read project memory, run pre-flight checks.
   - **Design**: Break objective into steps, identify parallelism.
   - **Draft**: Use `write_to_file` to anchor the `implementation_plan.md` first.
4. **Adversarial Gate**: Delegate review to a strongest-model sub-agent before committing to the path.

## Best Practices
- ✅ Use for tasks requiring 3+ PRs or multiple sessions.
- ✅ Ensure cold-start execution for every step.
- ❌ Don't invoke for tasks completable in a single PR.
- ❌ Don't invoke when the user says "just do it".

*The void requires structure. Do not build upon sand.*
