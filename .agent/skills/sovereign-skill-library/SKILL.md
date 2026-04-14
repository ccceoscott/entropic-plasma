---
name: sovereign-skill-library
description: R.A.P.S. skill library manager — skill catalog governance, frontmatter standardization, bundle management, and fleet-wide skill propagation.
phase: "209"
category: protocol
tags: ["skills", "catalog", "r.a.p.s", "bundles", "governance"]
---

# Sovereign Skill Library (R.A.P.S.) — Phase 207.16

# Sources

- **Official Google Skills**: `https://github.com/rominirani/antigravity-skills` (Standard Baseline)
- **Awesome Skills**: `https://github.com/sickn33/antigravity-awesome-skills` (Primary Archive - 1,397+ Glyphs)
- **Community Vault**: `https://github.com/rmyndharis/antigravity-skills` (Legacy Subset)

## Core Mandates

1. **Discovery**: Search the `scratch/antigravity-awesome-skills/data/catalog.json` for skills relevant to current mission objectives.
2. **Selective Ingestion**: Use `node scripts/skill-import.cjs` to pull high-value skills into the permanent `.agent/skills/` directory.
3. **Lifecycle Management**: Periodically audit used skills and prune those that are no longer relevant to the current project phase.
4. **Fleet Propagation**: Ensure that any skill imported into the source project is broadcast to all other projects in the fleet via `scripts/fleet-sync.sh`.

## Operational Procedures

### Phase 1: Exploration
- Search the `scratch/antigravity-skills/catalog.json` using keywords or category filters.
- Use `view_file` to inspect the `SKILL.md` of a potential candidate in `scratch/antigravity-skills/skills/[skill-id]/SKILL.md`.

### Phase 2: Ingestion
- Execute `node scripts/skill-import.cjs [skill-id]` to integrate the skill.
- The script will automatically:
    - Copy the directory.
    - Register it in `.agent/skills/.global_list`.
    - Update the local agent state.

### Phase 3: Validation & Sync
- Verify the new skill is active by checking its triggers.
- Run `scripts/fleet-sync.sh` to empower the rest of the fleet.

## Skill Categories

The library is organized into several domains, including:
- **Architecture**: Design patterns, C4 documentation, ADRs.
- **Security**: Auditing, penetration testing, defensive coding.
- **Development**: Language-specific expertise, API design, testing patterns.
- **Data & AI**: LLM orchestration, RAG systems, data pipelines.
- **Infrastructure**: DevOps, CI/CD, cloud resource management.

*The library is vast, but only the strong are permitted to enter the permanent matrix.*
