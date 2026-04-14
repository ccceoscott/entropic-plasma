---
description: Advanced Firebase/Stripe e-commerce bootstrapping, zero-trust rules, idempotency engines, and storefront hardening.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /ecommerce_bootstrap
## Sovereign E-commerce Infrastructure — Zero-Trust, Zero-Loss Edition

> ⚡ **MANDATE**: This workflow scaffolds the entire financial core. Pre-requisites: `/setup_auth` and `/setup_database` must be COMPLETE.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest these skills** via `view_file` on each `SKILL.md` before proceeding:
1. `.agent/skills/ecommerce-reviewer/SKILL.md` — Order lifecycle, Stripe idempotency, inventory atomicity
2. `.agent/skills/fleet-deploy-guardian/SKILL.md` — Safe-deploy protocol, project ID verification, rollback

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
If stale → auto-upgrade (0b). If current → confirm (0c).

### Phase 0b — Auto-Upgrade
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 120 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run.

---

## SECTOR 1 — Stripe Secret Provisioning (GCloud)

### 1a — Create Secrets
Run `mcp_gcloud_run_gcloud_command`:
- `["secrets", "create", "STRIPE_SECRET_KEY", "--replication-policy=automatic"]`
- `["secrets", "create", "STRIPE_WEBHOOK_SECRET", "--replication-policy=automatic"]`

### 1b — Request Keys
Ask user for Stripe Secret Key and Webhook Secret (local testing).
Store via `["secrets", "versions", "add", "STRIPE_SECRET_KEY", "--data-file=-"]`.

---

## SECTOR 2 — Idempotency Engine Scaffolding

### 2a — Create `stripe_events` Collection
Use `mcp_firebase-mcp-server_firestore_add_document` to create a placeholder record in `stripe_events` to initialize the collection.

### 2b — Security Rules
Add to `firestore.rules`:
```
match /stripe_events/{eventId} {
  allow read: if false; // System only
  allow write: if false;
}
```

---

## SECTOR 3 — Backend Webhook Scaffold

Create `functions/src/stripe/webhook.ts`:
- Implementation MUST include signature verification.
- Implementation MUST include `stripe_events` idempotency check.
- Implementation MUST emit events to Internal Event Bus (if present).

---

## SECTOR 4 — Storefront Skeleton (Next.js)

### 4a — Cart State (Zustand)
Create `src/store/useCart.ts` with:
- Persisted state (localStorage)
- Action: `addItem`, `removeItem`, `clearCart`

### 4b — Product Query
Create `src/hooks/useProducts.ts` using `react-query` or standard `useEffect` mapping live Firestore data.

---

## SECTOR 5 — MISSION_STATE.md Update

Update `MISSION_STATE.md`:
- E-commerce: BOOTSTRAPPED
- Stripe Secrets: REGISTERED
- Webhook Handler: DEPLOYABLE

`🧹 E-commerce infrastructure provisioned. Ready for trade.`
