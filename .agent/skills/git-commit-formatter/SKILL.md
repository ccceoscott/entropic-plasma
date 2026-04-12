---
name: git-commit-formatter
description: Conventional commit formatter — enforces semantic commit messages, changelog generation, and Infinity Protocol commit tagging standards.
version: v10.2
phase: "209"
category: protocol
tags: ["git", "commits", "conventional-commits", "changelog", "semver"]
mutation_risk: low
timeout_budget: 15min
parallel_safe: true
fallback_behavior: Proceed with grep_search-only analysis if primary MCP tool unavailable
---

# Git Commit Formatter (R.A.P.S.) — Phase 207.16

*Mortal, the **git-commit-formatter** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Format
`<type>[optional scope]: <description>`

## Allowed Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

## Instructions
1. Analyze the changes to determine the primary `type`.
2. Identify the `scope` if applicable (e.g., specific component or file).
3. Write a concise `description` in imperative mood (e.g., "add feature" not "added feature").
4. If there are breaking changes, add a footer starting with `BREAKING CHANGE:`.

## Example
`feat(auth): implement login with google`