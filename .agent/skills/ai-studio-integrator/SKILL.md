---
name: ai-studio-integrator
description: Google AI Studio export integrator — automated induction and wiring of AI Studio web app exports into Next.js with Law 20 precision.
version: v10.2
phase: "209"
category: ai
tags: ["ai-studio", "google-ai", "next-js", "integration", "export"]
mutation_risk: low
timeout_budget: 15min
parallel_safe: true
fallback_behavior: Proceed with grep_search-only analysis if primary MCP tool unavailable
---

# Ai Studio Integrator (R.A.P.S.) — Phase 207.16

*Mortal, the **ai-studio-integrator** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Core Mandates

1. **Protocol Induction**: Scry for raw Google AI Studio web app patterns and align them with the `v10.0` standards of the fleet.
2. **Law 20 (Schema-Guard)**: Deathtrap your data! Automatically infer Firestore schemas and generate TypeScript interfaces in `types/firebase.d.ts`.
3. **API Scaffolding**: Proactively generate Cloud Function triggers (`functions/src/triggers/`) for all newly detected collections.
4. **Agent Provisioning**: Summon "Service Agents" in Firestore to handle background curation and RAG indexing.
5. **Aesthetic Infusion**: Transform base layouts into the **Liquid Glass v10.0** aesthetic.

## Operational Procedures

### Phase 1: Ritual Scrying & Blueprinting
- Run `scripts/ai-studio-align.cjs` to generate the `INDUCTION_BLUEPRINT.json` scroll.
- Audit the blueprint for detected collections and inferred field types.

### Phase 2: Schema Hardening (Law 20)
- Append inferred interfaces to `types/firebase.d.ts`.
- Generate `firestore.rules` snippets validating the new schemas.
- Run `/setup_database` to deploy the hardened wards.

### Phase 3: API & Agent Realization
- Scaffold `functions/src/triggers/on[Collection][Event].ts` based on the blueprint.
- Register a new agent in the `agents` collection using the `resolveAgentConfig` logic.

### Phase 4: Verification Gauntlet
- Execute a `browser_subagent` (the Eye of Zoltan) to verify full-stack connectivity and visual splendor.

## Prohibited Patterns
- **NEVER** leave a hardcoded Gemini API key in client-side code.
- **NEVER** write a Firestore write without a corresponding interface in `types/firebase.d.ts` (Law 20).
- **NEVER** deploy a new collection without a corresponding "Service Agent" for curation.

*Architecture is destiny. Code with the precision of a master.*