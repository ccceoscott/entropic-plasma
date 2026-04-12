---
description: Full checkout, inventory, and Stripe webhook state auditing
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /ecommerce_audit
## Sovereign E-commerce State Audit — Zero-Loss, Idempotency Enforced

> ⚡ **LAW 21 (Financial Idempotency)**: NEVER process a payment or order fulfillment without verifying a unique `idempotency_key` (Stripe Event ID or Order ID) in the database. Duplicate transactions = P0 FAILURE.

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
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run.

---

## SECTOR 1 — Stripe Key Audit (Zero-Trust)

### 1a — Secret Manager Check
Use `mcp_gcloud_run_gcloud_command` with args:
`["secrets", "list", "--project=...", "--format=json", "--quiet"]`
Verify `STRIPE_SECRET_KEY` and `STRIPE_WEBHOOK_SECRET` are registered.

### 1b — Code Leak Scan
Use `grep_search` for `sk_live` or `sk_test` in the entire codebase.
Hardcoded keys found → **P0 HALT**. Move to Secret Manager immediately.

---

## SECTOR 2 — Inventory & Pricing Integrity (Schema-Guard)

### 2a — Product Schema Pull
Use `mcp_firebase-mcp-server_firestore_list_documents` on `products` collection.
Verify:
- `price` field type (must be Number/Integer)
- `stock` or `inventory` field presence
- `status` (active/draft)

### 2b — Pricing Logic Audit
Use `grep_search` for pricing calculation logic in `functions/src`.
Verify: No client-supplied prices are HONORED. All pricing MUST be pulled from Firestore in the backend during checkout creation.

---

## SECTOR 3 — Webhook Idempotency Audit

### 3a — Webhook Handler Discovery
Use `grep_search` for `stripe.webhooks.constructEvent` in `functions/src`.

### 3b — Event ID Check
Verify the handler checks `stripe_events/{eventId}` before processing.
If missing → **P1 RISK (Double Billing)**. Refactor to use idempotency collection.

---

## SECTOR 4 — Checkout Flow Verification

### 4a — Cloud Function Audit
Verify `createCheckoutSession` (or equivalent) pulls data ONLY from Firestore, not request body.

---

## SECTOR 5 — MISSION_STATE.md Update

Update `MISSION_STATE.md`:
- E-commerce Audit: COMPLETE
- Stripe Secrets: SECURE
- Pricing Integrity: VERIFIED
- Idempotency: ENFORCED

`🧹 E-commerce state verified. Financial integrity sealed.`
