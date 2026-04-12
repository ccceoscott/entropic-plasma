---
name: ci-cd-pipeline-architect
description: GitHub Actions and Firebase Cloud Build CI/CD architect — deploy gates, environment matrix, secrets injection, rollback patterns, and sovereign pipeline governance.
version: v10.1
phase: "209"
category: ops
tags: ["ci-cd", "github-actions", "cloud-build", "deploy-gates", "rollback", "secrets"]
---

# CI/CD Pipeline Architect (R.A.P.S.) — Phase 209

*Mortal, code that cannot be deployed reliably is merely expensive poetry. The wizard demands automated sovereignty.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.

## Overview
Design authority for CI/CD pipelines across the Infinity Protocol fleet. Governs GitHub Actions workflow design, Firebase Cloud Build triggers, environment matrix management, secret injection patterns, and zero-downtime deploy with rollback capability.

---

## Sovereign Pipeline Philosophy

1. **No manual deploys without a passing CI gate** — if the pipeline is red, nothing ships
2. **Environments are immutable** — `staging` config never bleeds into `production`
3. **Secrets never in code** — injected at runtime via Secret Manager or environment variables
4. **Every deploy is auditable** — commit SHA, actor, timestamp in every deployment record
5. **Rollback is always possible** — previous version artifact retained for 30 days

---

## GitHub Actions — Sovereign Workflow Templates

### Template 1: Firebase Deploy (Functions + Firestore + Hosting)

```yaml
# .github/workflows/deploy-production.yml
name: Deploy Production — Infinity Protocol

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      target:
        description: "Deploy target (all | functions | hosting | firestore)"
        required: true
        default: "all"

env:
  NODE_VERSION: "22"
  PROJECT_ID: ${{ secrets.FIREBASE_PROJECT_ID }}

jobs:
  # ── Gate 1: TypeScript ──────────────────────────────────────────────────
  typescript-gate:
    name: "🔷 TypeScript Gate"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: "npm"
          cache-dependency-path: functions/package-lock.json
      - run: cd functions && npm ci
      - run: cd functions && npx tsc --noEmit
        env:
          NODE_OPTIONS: "--max-old-space-size=4096"

  # ── Gate 2: Security Scan ──────────────────────────────────────────────
  security-gate:
    name: "🔒 Security Gate"
    runs-on: ubuntu-latest
    needs: typescript-gate
    steps:
      - uses: actions/checkout@v4
      - name: Scan for hardcoded secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.before }}
          head: ${{ github.sha }}
          extra_args: --only-verified

  # ── Gate 3: Deploy ─────────────────────────────────────────────────────
  deploy:
    name: "🚀 Deploy to Production"
    runs-on: ubuntu-latest
    needs: [typescript-gate, security-gate]
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: "npm"
      - run: npm ci
      - run: cd functions && npm ci

      - name: Install Firebase CLI
        run: npm install -g firebase-tools@latest

      - name: Authenticate to GCP
        uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}

      - name: Verify Project ID
        run: |
          ACTUAL=$(node -e "console.log(JSON.parse(require('fs').readFileSync('.firebaserc','utf8')).projects.default)")
          echo "Deploying to: $ACTUAL"
          if [ "$ACTUAL" != "${{ env.PROJECT_ID }}" ]; then
            echo "❌ PROJECT ID MISMATCH — aborting"
            exit 1
          fi

      - name: Deploy
        run: |
          firebase deploy --only ${{ github.event.inputs.target || 'all' }} \
            --project ${{ env.PROJECT_ID }} \
            --non-interactive
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}

      - name: Create GitHub Deployment Record
        uses: actions/github-script@v7
        if: success()
        with:
          script: |
            github.rest.repos.createDeployment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              ref: context.sha,
              environment: 'production',
              auto_merge: false,
              required_contexts: [],
            })
```

### Template 2: PR Preview Deploy (Staging)

```yaml
# .github/workflows/preview.yml
name: PR Preview Deploy

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  preview:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "22", cache: "npm" }
      - run: npm ci
      - run: cd functions && npm ci
      - name: Deploy Hosting Preview
        run: |
          npx firebase-tools hosting:channel:deploy pr-${{ github.event.number }} \
            --expires 3d \
            --project ${{ secrets.FIREBASE_STAGING_PROJECT_ID }}
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

---

## Environment Matrix Governance

### Sovereign Environment Tiers

| Tier | Branch | Project | Auto-Deploy |
|---|---|---|---|
| `local` | any | Firebase Emulator | Never |
| `staging` | `develop` | `<project>-staging` | On merge |
| `production` | `main` | `<project>` | After gates |

### Environment Variable Injection Pattern

Never use `.env` files in CI. Use GitHub Secrets → Secret Manager:

```yaml
# Inject secrets from GitHub Secrets at runtime
- name: Set secrets
  run: |
    echo "${{ secrets.STRIPE_SECRET_KEY }}" | \
      firebase functions:secrets:set STRIPE_SECRET_KEY --project ${{ env.PROJECT_ID }}
```

---

## Rollback Protocol

### Automatic Rollback on Failed Deploy
```yaml
  - name: Verify Deploy Health
    run: |
      sleep 30  # Allow cold start
      STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://${{ env.PROJECT_ID }}.web.app/healthz)
      if [ "$STATUS" != "200" ]; then
        echo "❌ Health check failed ($STATUS) — rolling back"
        firebase hosting:clone ${{ env.PROJECT_ID }}:live ${{ env.PROJECT_ID }}:live \
          --project ${{ env.PROJECT_ID }}
        exit 1
      fi
```

### Manual Rollback Command
```bash
# Roll back to previous Functions version
firebase functions:rollback --project <project-id>

# Roll back Hosting to specific version
firebase hosting:clone <project-id>:ch<channel-id> <project-id>:live
```

---

## Firebase Cloud Build Triggers (Alternative to GitHub Actions)

```yaml
# cloudbuild.yaml
steps:
  # TypeScript Gate
  - name: "node:22"
    entrypoint: "npm"
    args: ["run", "build"]
    dir: "functions"
    env:
      - "NODE_OPTIONS=--max-old-space-size=4096"

  # Deploy Functions
  - name: "gcr.io/google.com/cloudsdktool/cloud-sdk"
    args:
      - firebase
      - deploy
      - --only=functions
      - --project=${PROJECT_ID}
      - --non-interactive

options:
  logging: CLOUD_LOGGING_ONLY
  machineType: "E2_HIGHCPU_8"
timeout: "1200s"
```

---

## Pipeline Audit Checklist

Before any pipeline goes live:

- [ ] TypeScript gate runs on every PR and push
- [ ] Secret scanning (TruffleHog or Gitleaks) in gate position
- [ ] Project ID verification step — never assume from context
- [ ] Separate staging and production environments with distinct secrets
- [ ] Rollback mechanism documented and tested
- [ ] Deploy actor + SHA logged in deployment record
- [ ] No hardcoded project IDs in workflow YAML
- [ ] GitHub Environments with protection rules on `production`
- [ ] Concurrency controls — cancel in-progress runs on new push

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---

## Post-Action Report Template

```
Pipeline: <name>
Trigger: <push to main | PR | manual>
Gates: TypeScript ✅ | Security ✅ | Lint ✅
Deploy target: <functions | hosting | all>
Project verified: <YES/NO>
Rollback tested: <YES/NO>
Avg deploy time: <N> minutes
Outstanding gaps: <list>
```
