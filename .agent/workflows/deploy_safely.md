---
description: Safe Atomic Deployment Workflow
---
# Safe Atomic Deployment

Follow this workflow for EVERY deployment to ensure stability and prevent zero-downtime failures.

## 1. 🔒 Environment Verification
- [ ] **Check Project ID:**
    ```bash
    # Run in terminal
    echo $GCLOUD_PROJECT && echo $FIREBASE_PROJECT
    ```
    - Verify matches expected production ID.

## 2. 🧪 Pre-Deploy Validation
- [ ] **Lint Check:**
    ```bash
    npm run lint
    ```
- [ ] **Type Check:**
    ```bash
    npm run type-check # or tsc --noEmit
    ```
- [ ] **Regression Tests (E2E):**
    ```bash
    # MANDATORY: Verify core flows
    npx playwright test --project=chromium --grep "@critical"
    ```
- [ ] **Build Check:**
    ```bash
    npm run build
    ```
    - **IF** build fails, **STOP**. Do not proceed to deploy.

## 3. 🚀 Atomic Deployment
- [ ] **Deploy:**
    ```bash
    firebase deploy --only hosting,functions # or specific service
    ```
- [ ] **Verify:**
    - Visit the production URL immediately.
    - Check for "White Screen of Death" (Console errors).

## 4. ↩️ Rollback Plan
- [ ] **If Failed:**
    ```bash
    firebase hosting:rollback
    ```
