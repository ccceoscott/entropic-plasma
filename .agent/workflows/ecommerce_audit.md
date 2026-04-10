---
description: Full checkout, inventory, and Stripe webhook state auditing
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /ecommerce_audit
## Sovereign E-Commerce State Audit — Payment, Inventory, Webhook Integrity

> ⚡ **MANDATE**: E-commerce hallucinations are financial hazards. Every audit requires live MCP verification of payment state, inventory documents, and webhook event logs. No assumptions about Stripe.

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

## SSOT INGESTION

Use `view_file` on `MISSION_STATE.md`.
Use `view_file` on `KNOWLEDGE.md`.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists).

---

## SECTOR 1 — Live Firestore E-Commerce Schema Audit (Schema-Guard — Law 20)

### 1a — Collection Discovery
Use `mcp_firebase-mcp-server_firestore_list_collections` for root and user-scoped collections.
Identify all e-commerce collections:
- `orders`, `products`, `carts`, `inventory`, `transactions`, `subscriptions`

### 1b — Sample Document Pull
For each e-commerce collection, pull 2-3 documents:
Use `mcp_firebase-mcp-server_firestore_list_documents` per collection.
Document exact field names and types for:
- `orders`: status enum values, payment fields, amount fields (cents vs dollars?)
- `products`: `price`, `stock`, `sku`, `stripeProductId`, `stripePriceId`
- `inventory`: quantity fields, reservation fields

### 1c — Schema Divergence Check
Compare live schema against any TypeScript interfaces in the codebase:
Use `grep_search` for `interface Order` or `interface Product` in `src/` and `functions/src/`.
Any field mismatch between live MCP data and code types → **SCHEMA MISMATCH** → auto-fix interfaces.

---

## SECTOR 2 — Stripe Integration Health

### 2a — Webhook Function Audit
Use `mcp_firebase-mcp-server_functions_list_functions` → identify Stripe webhook handler(s).
Use `grep_search` for `stripe.webhooks.constructEvent` in `functions/src/`.
Verify:
- Webhook signature verification is present (critical security check)
- `STRIPE_WEBHOOK_SECRET` is defined via Secret Manager (Law 10)
- Endpoint returns 200 immediately before async processing (Stripe retry prevention)

### 2b — Idempotency Check (Critical)
Use `grep_search` for `payment_intent` or `checkout.session` in `functions/src/`.
For every webhook event handler, verify idempotency guard:
```typescript
// REQUIRED — prevents double-processing
const existingOrder = await db.collection('orders').doc(paymentIntentId).get();
if (existingOrder.exists) {
  logger.info('Duplicate webhook — skipping');
  return;
}
```
Missing idempotency → **P0 FINANCIAL RISK**. Auto-add pattern.

### 2c — Webhook Events Coverage
Verify these critical Stripe events are handled:
- `checkout.session.completed` → fulfill order
- `payment_intent.payment_failed` → notify user, release inventory
- `invoice.payment_failed` (if subscriptions) → update subscription status
- `customer.subscription.deleted` → revoke access

Missing handlers → document as GAPS. Do NOT silently ignore unhandled events.

---

## SECTOR 3 — Checkout Flow Integrity

### 3a — Cart-to-Order Transaction Audit
Use `grep_search` for `runTransaction` in `functions/src/`.
Every checkout that converts cart → order and deducts inventory MUST use Firestore transaction.
Missing transactions on inventory deductions → **P0 RACE CONDITION**. Auto-add.

### 3b — Amount Calculation Audit
Use `grep_search` for `.price` or `amount` in `functions/src/`.
Verify: Are amounts stored in CENTS (integer, Stripe standard) or dollars (float, dangerous)?
Float amounts → auto-convert to cents. Document conversion in KNOWLEDGE.md.

### 3c — Order Status State Machine
Pull sample orders from Sector 1.
Verify valid status transitions exist and are enforced:
```
PENDING → PROCESSING → COMPLETED
PENDING → CANCELLED
PROCESSING → REFUNDED
```
No `if (status === 'done')` guessing — must match live enum values from MCP data.

---

## SECTOR 4 — Inventory Control Audit

Use `mcp_firebase-mcp-server_firestore_query_collection` on `products` with filter: `stock LESS_THAN 5`.
Document low-stock products.

Use `grep_search` for `stock` in `functions/src/`.
Verify stock reservation on checkout vs stock deduction on fulfillment are separate operations.
Negative stock values possible? → add floor guard: `Math.max(0, newStock)`.

---

## SECTOR 5 — Security Rules Audit (Payments)

Use `mcp_firebase-mcp-server_firebase_get_security_rules` with type `"firestore"`.
For payment/order collections:
- `orders` → `allow write: if false;` for CLIENT writes (only Functions write)
- `products` → readable by all, writable only by admin role
- `transactions` → readable by owning user only, writable only by Functions

Any collection where clients can write payment data directly → **P0 CRITICAL BLOCKER**.

---

## SECTOR 6 — Functions Error Log Triage (MCP)
Use `mcp_firebase-mcp-server_functions_get_logs` with:
- `function_names: ['stripeWebhook', 'createCheckout']` (adjust names)
- `min_severity: "ERROR"`
- Last 24 hours

Any uncaught errors in payment functions → investigate root cause → auto-fix.

---

## SECTOR 7 — E2E Checkout Browser Witness

Spawn browser subagent to:
1. Navigate to product listing page
2. Add product to cart
3. Proceed to checkout (test mode)
4. Complete purchase with Stripe test card `4242 4242 4242 4242`
5. Screenshot: order confirmation page
6. Verify order document appears in Firestore (via MCP query)
7. Screenshot: DevTools Network tab showing successful webhook response

**No E2E browser witness = checkout NOT verified.**

---

## SECTOR 8 — Multi-Item Cart & Persistence Audit

### 8a — Cart Storage Key Verification
Use `grep_search` for `epihab-cart-storage` in `src/` to confirm the canonical storage key.

### 8b — Multi-Item Subtotal Math Check
Verify that the cart subtotal computation is:
```
subtotal = sum(item.price for item in cart.items)
```
NOT `sum(item.price * item.quantity)` unless `item.price` is already the line total.
Use `grep_search` for `reduce` + `cart` in `src/store/` or `src/hooks/`.

### 8c — Cart Persistence Test
Confirm `persist: true` or equivalent is set on the Zustand cart store.
Use `grep_search` for `persist` in cart store files.

### 8d — Empty Cart Guard
Use `grep_search` for `items.length` combined with `/checkout` navigation to confirm the empty-cart redirect guard is implemented.

---

## SECTOR 9 — Promo / Coupon Code Pipeline Audit

### 9a — Backend Promo Function Check
Use `mcp_firebase-mcp-server_functions_list_functions` to identify any `applyPromo`, `validateCoupon`, or `redeemCode` functions.

### 9b — Promo Code Collection Audit
Use `mcp_firebase-mcp-server_firestore_list_collections` to identify `promoCodes`, `coupons`, or `discountCodes` collections.
If present: pull 2-3 sample documents via `firestore_list_documents`.

### 9c — PaymentIntent Discount Propagation
Use `grep_search` for `discount` or `coupon` in `functions/src/` to confirm promo codes are applied server-side before `createPaymentIntent`.

### 9d — Promo Error Handling Check
Use `grep_search` for `invalid.*promo\|promo.*invalid\|coupon.*not found` in `src/` to confirm UI-level error handling.

---

## SECTOR 10 — Tax Jurisdiction Verification

### 10a — TaxJar / Stripe Tax Integration Check
Use `grep_search` for `taxjar\|stripe.*tax\|automatic_tax\|tax_code` in `functions/src/`.
Confirm the `createPaymentIntent` call passes `automatic_tax: { enabled: true }` OR a TaxJar lookup is performed.

### 10b — Jurisdiction Baseline Verification
Pull 3 recent orders from the `orders` collection.
Check `taxAmount` field — confirm it is a number (not undefined/NaN).

### 10c — Tax NaN Guard
Use `grep_search` for `taxAmount` in `src/` to confirm all display paths handle `taxAmount ?? 0` (null-safe default).

---

## SECTOR 11 — Declined Payment & Error Recovery Audit

### 11a — Stripe Error Handler Coverage
Use `grep_search` for `card_declined\|payment_failed\|stripe.*error` in `src/` and `functions/src/`.
Confirm there is a catch path that surfaces a human-readable error message (NOT throws to console).

### 11b — createPaymentIntent Failure Mode
Use `grep_search` for `catch` blocks adjacent to `createPaymentIntent` in Cloud Functions.
Confirm function returns a structured error response (status 4xx with `{ error: string }`) rather than throwing 500.

### 11c — Frontend Error State UI
Use `grep_search` for `paymentError\|stripeError\|cardDeclined` in `src/` to confirm a React state variable drives the error display.

---

## SECTOR 12 — Seller Dashboard & Order Receipt Audit

### 12a — Seller Route Guard
Use `grep_search` for `seller\|admin` route definitions in `src/router\|src/App.tsx\|src/routes/`.
Confirm seller routes are protected by an `isAdmin\|isSeller\|role` check.

### 12b — Order Receipt Financial Fields
Use `grep_search` for `subtotal\|grandTotal\|orderTotal` in seller/portal order components.
Confirm all 4 financial fields render: `subtotal`, `shipping`, `tax`, `total`.

### 12c — Order Status Enum Audit
Pull sample documents from the `orders` collection.
Confirm `status` field uses canonical enum values: `pending`, `processing`, `shipped`, `delivered`, `cancelled`.

---

## SECTOR 13 — Audit Report Generation

Create audit summary:
| Area | Status | Issues Found | Auto-Fixed | Blockers |
|---|---|---|---|---|
| Schema Accuracy | ✅/⚠️/❌ | | | |
| Webhook Verification | ✅/⚠️/❌ | | | |
| Idempotency | ✅/⚠️/❌ | | | |
| Transaction Safety | ✅/⚠️/❌ | | | |
| Inventory Control | ✅/⚠️/❌ | | | |
| Security Rules | ✅/⚠️/❌ | | | |
| E2E Browser Witness | ✅/⚠️/❌ | | | |
| Multi-Cart Math | ✅/⚠️/❌ | | | |
| Cart Persistence | ✅/⚠️/❌ | | | |
| Promo/Coupon Pipeline | ✅/⚠️/❌ | | | |
| Tax Jurisdiction | ✅/⚠️/❌ | | | |
| Decline Recovery | ✅/⚠️/❌ | | | |
| Seller Dashboard | ✅/⚠️/❌ | | | |

**ALL GREEN** → `✅ E-commerce audit complete. Platform is financially sovereign.`
**ANY BLOCKER** → `❌ AUDIT BLOCKED: [list]. Do not go live until resolved.`

---

## SECTOR 14 — Knowledge Graph Persistence (MCP)
Use `mcp_knowledge-graph_add_observations` to record:
- E-commerce schema snapshot (live field types)
- Idempotency patterns applied
- Any financial risk gaps found and resolved
- Promo/coupon configuration status
- Tax jurisdiction integration status
- Declined payment error recovery patterns
- Checkout flow E2E result

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 E-commerce audit sealed. Every transaction protected.`
