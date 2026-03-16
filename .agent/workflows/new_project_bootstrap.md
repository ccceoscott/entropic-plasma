---
description: Standard Protocol for initializing a NEW Firebase project with Governance Standards ("God Mode").
---

# New Project Bootstrap Protocol

This workflow is the **MANDATORY FIRST STEP** for any new Firebase project in the `infinite-juno` portfolio. It ensures the project starts "Safe by Default" with standardized Rules, Indexes, and Workflows.

## Step 1: Initialization

1.  Initialize the project directory.
    ```bash
    mkdir <project-name>
    cd <project-name>
    firebase init
    ```
    *(Select Firestore, Functions, Emulators)*

## Step 2: Governance Injection

1.  **Stop!** Do NOT write custom rules yet.
2.  **Copy Governance Artifacts** from `infinite-juno`:
    *   `templates/firestore_master.rules` -> `firestore.rules`
    *   `templates/firestore.indexes.json` -> `firestore.indexes.json`
    *   `.agent/workflows/` -> `.agent/workflows/` (Copy ALL standard workflows)

## Step 3: Configuration & Safety Check

1.  **Configure `firebase.json`**:
    Ensure it points to the standard files:
    ```json
    {
      "firestore": {
        "rules": "firestore.rules",
        "indexes": "firestore.indexes.json"
      }
    }
    ```

2.  **Verify Project ID**:
    Run `firebase projects:list` to ensure you are targeting the correct NEW project.

## Step 4: Initial Deployment

1.  Deploy the safeguards BEFORE adding any app logic.
    ```bash
    firebase deploy --only firestore:rules,firestore:indexes
    ```

## Step 5: Verification

1.  Run the **Security Scan Workflow**:
    ```bash
    # (Agent Instruction)
    # Run the .agent/workflows/security_scan.md workflow on this new project.
    ```
2.  Confirm that `ALLOW_WRITE` is `FALSE` (Default Deny) for the root `matched /{document=**}`.

---
**Outcome**: The project is now governed by the Portfolio Standard. You may proceed with development.
