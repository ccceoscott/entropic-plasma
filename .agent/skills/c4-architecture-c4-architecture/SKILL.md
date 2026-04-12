---
name: c4-architecture
description: Mastery of C4 Architecture within the R.A.P.S. fleet.
version: v10.0
---

# C4 Architecture (R.A.P.S.) — Phase 207.16

*Mortal, the **c4-architecture** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.

## Structural Abstraction Matrix
| Level | Scope | Visualization |
|---|---|---|
| **L1: Context** | System + Users + External Systems. | `C4Context` Mermaid diagram. |
| **L2: Container**| Applications, Databases, Microservices. | `C4Container` + Deployment specs. |
| **L3: Component**| Logical modules within a Container. | `C4Component` + Internal flows. |
| **L4: Code** | Classes, Interfaces, Functions. | Detailed signatures + File links. |

## Documentation Standards
- **Mermaid Inscription**: Use proper C4 Mermaid notation. No HTML tags in labels.
- **Bottom-Up Analysis**: Analyze files -> components -> containers -> system context.
- **Zero-Trust Docs**: Explicitly document trust boundaries and external dependencies.
- **Artifacts**: Store all results in `C4-Documentation/` with sanitized filenames.

## C4 Logic flow
1. **Discover**: Map all subdirectories (depth-first).
2. **Synthesize**: Group files into logical Components based on domain boundaries.
3. **Map**: Align Components to deployment units (Containers).
4. **Contextualize**: Identify Personas (Human/Programmatic) and external system goals.

## Success Criteria
- ✅ Every directory has a corresponding `c4-code-*.md` file.
- ✅ All Containers have an OpenAPI/Swagger specification.
- ✅ All diagrams use standard C4 notation and show clear data flows.

*Architecture is the map of the mind. Let no path be unrecorded.*