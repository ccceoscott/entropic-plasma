---
description: Mandatory protocol for initializing ANY new project in the ecosystem.
---

# New Project Bootstrap Protocol (God Mode)

> [!IMPORTANT]
> **Constraint:** All new projects MUST inherit the Global Governance layer from `Infinity-Protocol` before any code is written.

## 1. Initialization
1.  **Create Directory/Repo**:
    ```bash
    mkdir my-new-project && cd my-new-project
    git init
    ```
2.  **Establish Governance Structure**:
    ```bash
    mkdir -p governance
    mkdir -p .agent/workflows
    ```

## 2. Governance Injection (The "God Seed")
Run the following to copy the master standards from `Infinity-Protocol`:

```bash
# Define source
JUNO_ROOT="$HOME/Infinity-Protocol"

# Copy Constitution & Identity
cp "$JUNO_ROOT/governance/global_rules.md" governance/
cp "$JUNO_ROOT/governance/user_identity.md" governance/

# Copy Core Workflows
cp "$JUNO_ROOT/.agent/workflows/god_mode_protocols.md" .agent/workflows/
cp "$JUNO_ROOT/.agent/workflows/deploy_safely.md" .agent/workflows/
cp "$JUNO_ROOT/.agent/workflows/verify_environment.md" .agent/workflows/
```

## 3. Configuration
1.  **Create `mcp_config.json`** (if project-specific overrides are needed, otherwise use global).
2.  **Set Environment Variables**:
    - Ensure `FIREBASE_PROJECT` and `GCLOUD_PROJECT` are defined in `.env` or context.

## 4. Verification
1.  Run the Environment Verification workflow:
    ```bash
    # trigger verify_environment.md
    ```
2.  Commit the governance layer:
    ```bash
    git add governance .agent
    git commit -m "chore: Initialize God Mode governance"
    ```

## 5. Agency Logic
-   **Neural Link**: Agent MUST read `governance/user_identity.md` to load Scott's context.
-   **Rule Enforcement**: Agent MUST read `governance/global_rules.md` to load the Constitution.
