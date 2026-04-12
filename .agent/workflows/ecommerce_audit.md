---
description: Full order lifecycle, product validation, payment processing, database integrity, email delivery, and E2E checkout auditing
alwaysApply: false
skills:
  - ecommerce-reviewer
  - security-auditor
  - auth-security-architect
  - sovereign-playwright-e2e
  - email-delivery-architect
  - performance-engineer
  - typescript-safety-enforcer
bundles:
  - security
  - testing
  - ops
---

# INFINITY PROTOCOL v10.0 — /ecommerce_audit
## Sovereign E-Commerce Full-Spectrum Audit — Zero-Loss, Zero-Float, Zero-Doubt

> ⚡ **LAW 21 (Financial Idempotency)**: NEVER process a payment or order fulfillment without verifying a unique `idempotency_key` in the database. Duplicate transactions = **P0 FAILURE**.
> 💰 **ALL-CENTS LAW**: All monetary values are integers in CENTS. Floats = **P0 HALT**.
> 🔐 **SERVER-AUTHORITY LAW**: Price is NEVER accepted from client request body. Firestore is the source of truth.

---

## 🧙 SKILL ROSTER — Skills Invoked by this Workflow

This workflow activates the following R.A.P.S. skills. Read each skill's SKILL.md before executing its corresponding sector.

| Skill | Invoked At | Purpose |
|---|---|---|
| `ecommerce-reviewer` | ALL sectors | Master commerce laws, schema validators, audit domains |
| `typescript-safety-enforcer` | Phase 0c | TypeScript gate — `tsc --noEmit` must pass before audit begins |
| `security-auditor` | Sector 1 | Secret scanning, hardcoded key detection, surface area hardening |
| `auth-security-architect` | Sector 1c + Domain 8/11 | Firestore rules audit, IDOR verification, admin guard review |
| `email-delivery-architect` | Sector 6 | Email trigger mapping, SPF/DKIM/DMARC, provider audit, live delivery test |
| `sovereign-playwright-e2e` | Sector 7 | E2E browser checkout flows — all 5 test card scenarios |
| `performance-engineer` | Sector 8 | Cold start profiling, Firestore index coverage, rate limiting |

> **IMPORTANT**: Load skill SKILL.md at sector entry. Do not re-read if already loaded this session.

---

## 🔐 PHASE 0 — SOVEREIGN UPGRADE GATE (MANDATORY — RUNS FIRST)

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
> 🧠 **INVOKE SKILL**: Read `.agent/skills/typescript-safety-enforcer/SKILL.md` now.

// turbo
```bash
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" \
NODE_OPTIONS=--max-old-space-size=4096 \
cd functions && timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -20
```
Errors → auto-fix using `typescript-safety-enforcer` skill patterns → re-run. Do NOT proceed with TypeScript errors present.

### Phase 0d — Project Discovery
Before assuming collection names, use Firestore MCP to discover reality:
```
mcp_firebase-mcp-server_firestore_list_collections → parent: projects/{projectId}/databases/(default)/documents
```
Map discovered collections to expected: `orders`, `products`, `carts`, `stripe_events`, `webhook_events`, `users`.
Note any naming deviations and adjust all subsequent queries accordingly.

---

## 🔐 SECTOR 1 — Security & Credentials Audit (Zero-Trust Gate)

> 🧠 **INVOKE SKILLS**: `security-auditor` + `auth-security-architect`
> Read `.agent/skills/security-auditor/SKILL.md` and `.agent/skills/auth-security-architect/SKILL.md` before proceeding.

### 1a — Secret Manager Verification
Use `mcp_gcloud_run_gcloud_command`:
```
args: ["secrets", "list", "--project=PROJECT_ID", "--format=json", "--quiet"]
```
Verify presence of:
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- Email provider API key (Resend, SendGrid, etc.)

If any missing → **P0 HALT**. Move to Secret Manager before proceeding.

### 1b — Hardcoded Key Scan
> **`security-auditor` pattern**: Run these grep checks per skill's `Secret Detection` protocol.

Use `grep_search` for each pattern in the entire codebase root:
- `sk_live` → hardcoded Stripe live key
- `sk_test` → hardcoded Stripe test key
- `whsec_` → hardcoded webhook secret
- `SG.` → hardcoded SendGrid key
- `re_` → hardcoded Resend key
- `AIza` → hardcoded Firebase/GCP API key

Any found → **P0 HALT**. Rotate key immediately, move to Secret Manager.

### 1c — Firestore Rules Commerce Audit
> **`auth-security-architect` pattern**: Apply IDOR and Zero-Trust rule verification from skill.

Use `mcp_firebase-mcp-server_firebase_get_security_rules` (type: firestore).
Verify:
- `orders` → read: `auth.uid == resource.data.userId`. Write: admin SDK only (`false` for client).
- `products` → read: `true`. Write: `request.auth.token.admin == true`.
- `carts` → read/write: `auth.uid == resource.data.userId`.
- `stripe_events` → `read/write: false` (no client access ever).
- `webhook_events` → `read/write: false` (no client access ever).
- `users` → read: own document only. Write: own document, restricted fields.

### 1d — Admin Route Guard Check
Use `grep_search` for `token.admin` or `customClaims.admin` in Cloud Functions source.
Verify all admin-scoped Cloud Functions assert `context.auth.token.admin === true`.
Missing check → **P1 ESCALATION**.

### 1e — IDOR Vulnerability Test
> **`auth-security-architect` IDOR protocol**: Cross-user order access verification.

Use `grep_search` for `orders/{orderId}` fetch patterns in API routes and Cloud Functions.
Verify every fetch asserts `order.userId === request.auth.uid` BEFORE returning data.
**Manual test required**: If test users exist — attempt to read UserA's orderId as UserB. Must return permission denied.
Any path returning order data without UID check = **P0 IDOR breach**.

---

## 🧲 SECTOR 2 — Product Catalog Integrity
> 🧠 **INVOKE SKILL**: `ecommerce-reviewer` Domain 1 — Product Catalog Integrity

### 2a — Product Schema Pull
Use `mcp_firebase-mcp-server_firestore_list_documents` on `products` collection (limit: 20).
For each document verify:
- `price` → integer (CENTS). Float present = **P0**.
- `stock` / `inventory` → integer ≥ 0. Negative = **P1**.
- `status` → `active | draft | archived`. Missing = **P2**.
- `sku` → string, non-empty. Missing = **P2**.
- `variants` → `Record<string, { price, stock, sku }>` if multi-variant. Flat array = violation.
- `images` → array of https:// URLs. Base64 blobs = **P2** (storage cost).
- `metadata.createdAt` / `metadata.updatedAt` → Firestore Timestamps. Missing = **P3**.

### 2b — SKU Uniqueness Check
Use `mcp_firebase-mcp-server_firestore_query_collection` to group by `sku`.
Any duplicate SKUs = **P1** (fulfillment routing failure risk).

### 2c — Pricing Server-Authority Audit
Use `grep_search` for `req.body.price`, `req.body.amount`, `body.total` in `functions/src/`.
Any match that passes to Stripe = **P0 HALT**. All pricing MUST come from Firestore.

### 2d — Out-of-Stock Enforcement Audit
Use `grep_search` for checkout/order-creation functions.
Verify the function checks `product.stock >= requestedQty` before proceeding.
Missing stock gate = **P1** (overselling risk).

### 2e — Product Deletion Safety
Verify deleted products are ARCHIVED (status: `archived`), NOT hard-deleted.
Check Firestore rules block hard deletes on products that have active order references.

---

## 📦 SECTOR 3 — Order Lifecycle & State Machine
> 🧠 **INVOKE SKILL**: `ecommerce-reviewer` Domain 2 — Order Lifecycle & State Machine

### 3a — Order Schema Validation
Use `mcp_firebase-mcp-server_firestore_list_documents` on `orders` collection (limit: 10).
For each document verify:
- `orderId` → string (UUID or Stripe PI ID). Required.
- `userId` → string. Required.
- `status` → canonical enum: `PENDING | PROCESSING | AWAITING_FULFILLMENT | SHIPPED | DELIVERED | CANCELLED | REFUNDED`.
- `items` → `Array<{ productId, sku, qty, unitPriceInCents, totalInCents }>`.
- `subtotalInCents`, `taxInCents`, `shippingInCents`, `totalInCents` → all integers.
- `stripePaymentIntentId` → populated on PROCESSING+.
- `fulfillmentStatus` → `unfulfilled | partial | fulfilled`.
- `shippingAddress` → full address object.
- `createdAt`, `updatedAt` → Firestore Timestamps.

### 3b — Financial Math Verification
For sampled orders, verify:
- `items[n].totalInCents === items[n].unitPriceInCents * items[n].qty` (line item math)
- `subtotalInCents === sum(items[].totalInCents)` (subtotal aggregation)
- `totalInCents === subtotalInCents + taxInCents + shippingInCents` (grand total balance)

Any mismatch = **P0 Financial Integrity Failure**.

### 3c — State Transition Audit
Use `grep_search` for all locations writing `status` to `orders` collection in functions.
Map every transition and verify trigger source:
- `PENDING → PROCESSING` : triggered by `payment_intent.succeeded` webhook only.
- `PROCESSING → SHIPPED` : triggered by shipping webhook or admin action.
- `SHIPPED → DELIVERED` : triggered by delivery webhook or admin action.
- `* → CANCELLED` : triggered by `payment_intent.canceled` or admin action.
- `* → REFUNDED` : triggered by `charge.refunded` webhook only.

Orphaned transitions (PENDING → SHIPPED skipping PROCESSING) = **P1**.
`updatedAt` not set on transition = **P2**.

### 3d — Orphaned Order Detection
Use `mcp_firebase-mcp-server_firestore_query_collection`:
- Query `orders` where `status == PENDING` and `createdAt < [30 minutes ago]` → zombie carts risk.
- Query `orders` where `status == PROCESSING` and `stripePaymentIntentId == null` → orphaned order.
- List findings for remediation.

---

## 💳 SECTOR 4 — Payment Processing (Stripe)
> 🧠 **INVOKE SKILL**: `ecommerce-reviewer` Domain 3 — Payment Processing

### 4a — Stripe SDK Version Check
Use `grep_search` for `"stripe"` in `functions/package.json`.
Confirm SDK version. If < 12.x → flag for upgrade. Verify `apiVersion` is pinned (not dynamic).

### 4b — Webhook Handler Discovery
Use `grep_search` for `stripe.webhooks.constructEvent` in `functions/src/`.
Verify it's the ONLY method used to parse incoming webhook payloads.
Any `JSON.parse(req.body)` used instead = **P0** (signature verification bypass).

### 4c — Webhook Event Coverage Matrix
Use `grep_search` for each event type string in webhooks handler:

| Event String | Required Handler |
|---|---|
| `payment_intent.succeeded` | Create order, decrement inventory, send confirmation email |
| `payment_intent.payment_failed` | Log failure, send failure notification, no order created |
| `payment_intent.canceled` | Cleanup, restore reserved inventory |
| `payment_intent.requires_action` | Frontend must handle 3DS prompt |
| `charge.refunded` | Set order REFUNDED, send refund email |
| `charge.dispute.created` | Alert admin, freeze if possible |
| `checkout.session.completed` | (if using Checkout Sessions) Order create flow |

Any missing handler on `payment_intent.succeeded` or `charge.refunded` = **P0**.
Other missing handlers = **P1**.

### 4d — Idempotency Deduplication Architecture
Use `grep_search` for `stripe_events` or `webhook_events` collection writes in functions.
Required pattern:
```
1. Read webhook_events/{event.id} — if exists, return 200 immediately.
2. runTransaction: write stub to webhook_events/{event.id}.
3. Outside transaction: execute business logic.
4. Update webhook_events/{event.id} with { processedAt, result }.
```
Missing dedup = **P0 HALT (double billing risk)**.

### 4e — PaymentIntent Metadata Audit
Use `grep_search` for `stripe.paymentIntents.create` or `stripe.checkout.sessions.create`.
Verify `metadata` contains: `orderId`, `userId` for webhook correlation.
Missing metadata = **P1** (webhook can't correlate to Firestore order).

### 4f — 3DS / SCA Compliance Audit
Use `grep_search` for `requires_action` or `confirmCardPayment` in frontend source.
Verify frontend handles `{ status: 'requires_action', client_secret }` from backend.
Verify `stripe.confirmCardPayment(clientSecret)` is called client-side.
Missing 3DS handling = **P1** (SCA-regulated cards will silently fail in EU markets).

### 4g — Discount & Tax Server-Authority
> **`ecommerce-reviewer` Laws 13 + 14**: Discount and Tax must be server-enforced.

Use `grep_search` for `req.body.discountAmount`, `req.body.taxAmount`, `req.body.couponCode` in functions.
Any of these accepted from client and passed to Stripe = **P0 HALT**.
Verify coupon redemption uses Firestore transaction to atomically consume one-time codes.

### 4h — Webhook Retry Resilience
Use `grep_search` for `try/catch` wrapping all webhook handlers.
Verify catch blocks always return HTTP 200 (never 5xx on processing failure — prevents Stripe retry storm).
Verify failed events are logged to `webhook_errors` collection with `{ eventId, error, retryCount, timestamp }`.

---

## 🗃️ SECTOR 5 — Database Integrity & Coherence
> 🧠 **INVOKE SKILL**: `ecommerce-reviewer` Domain 4 — Database Integrity Tests

### 5a — Inventory Coherence Check
Use `mcp_firebase-mcp-server_firestore_query_collection` to:
1. Sum `qty` of all non-cancelled order items per product.
2. Compare against `initialStock - currentStock` for each product.
Mismatch > 0 = inventory leak (**P1**).
Mismatch < 0 = overselling occurred (**P0**, immediate investigation).

### 5b — Atomic Inventory Operation Audit
Use `grep_search` for inventory decrement patterns in functions source:
- `FieldValue.increment(-` → CORRECT atomic pattern.
- Direct assignment like `stock - qty` or `product.stock = newStock` → **P1** (race condition risk).

### 5c — Cart TTL Sweeper Verification
Use `grep_search` for scheduled function or Cloud Scheduler config targeting `carts` collection.
Use `mcp_firebase-mcp-server_firestore_query_collection` to find carts older than 24h with `status: active`.
Missing sweeper + stale carts found = **P1** (ghost inventory reservation).

### 5d — Financial Reconciliation
Use `mcp_firebase-mcp-server_firestore_query_collection` to:
- Sum `totalInCents` of all orders where `status NOT IN [CANCELLED, REFUNDED]`.
- Report total to user for Stripe dashboard comparison.
Note any discrepancy for manual investigation.

### 5e — User-Order Integrity
Query `orders` collection for `userId` values.
Spot-check 3 UserIDs exist in `users` collection.
Missing user document for an order = orphaned order (**P2**).

---

## 📧 SECTOR 6 — Email Delivery Verification
> 🧠 **INVOKE SKILL**: `email-delivery-architect`
> Read `.agent/skills/email-delivery-architect/SKILL.md` before proceeding.

### 6a — Email Provider & API Key Audit
Use `grep_search` for email provider import (`resend`, `@sendgrid`, `nodemailer`) in functions source.
Verify API key is loaded from `process.env` or Secret Manager, never hardcoded.

### 6b — Trigger Mapping Audit
Apply `email-delivery-architect` trigger-mapping protocol. For each order state transition, verify an email function is triggered:

| Trigger | Expected Email |
|---|---|
| `payment_intent.succeeded` | Order Confirmation (order #, items, total, shipping) |
| Order status → SHIPPED | Shipping Notification (tracking #, carrier) |
| Order status → DELIVERED | Delivery Confirmation (review CTA) |
| Order status → CANCELLED | Cancellation Notice (refund timeline) |
| Order status → REFUNDED | Refund Confirmation (amount, 3-5 days notice) |
| Partial refund issued | Partial Refund Confirmation (amount refunded) |
| User registration | Welcome Email |

Use `grep_search` for email send calls adjacent to each status write.
Any state transition without an email send = **P1**.

### 6c — Template Content Quality Check
Use `grep_search` for email template content in functions or templates directory.
Apply `email-delivery-architect` template quality checklist:
- Order ID / reference number ✓
- Itemized list (name, qty, price) ✓
- Subtotal, tax, shipping, total breakdown ✓
- Shipping address ✓
- Support contact / link ✓
- Mobile-responsive HTML (not plain text) ✓
- Branded sender domain (`orders@yourdomain.com`) ✓

### 6d — DNS / Deliverability Audit
Per `email-delivery-architect` skill: verify SPF, DKIM, DMARC exist for sending domain.
Verify sender domain is branded — not generic (e.g., not `noreply@gmail.com`).
Verify transactional emails do NOT contain unsubscribe link (they bypass opt-out by law).
Verify any marketing emails DO contain unsubscribe link (CAN-SPAM compliance).

### 6e — Email Delivery Live Test
1. Trigger test order via Stripe test card `4242 4242 4242 4242`.
2. Monitor function execution logs:
   `mcp_firebase-mcp-server_functions_get_logs` (filter: email function name, last 5 mins).
3. Verify no `4xx` / `5xx` errors in delivery logs.
4. Confirm email function execution time is < 10 seconds.
If email function fails silently → **P1** (customers receive no confirmation).

---

## 🧪 SECTOR 7 — E2E Checkout Flow Testing
> 🧠 **INVOKE SKILL**: `sovereign-playwright-e2e`
> Read `.agent/skills/sovereign-playwright-e2e/SKILL.md` before launching browser_subagent.
> Apply all sovereign-playwright-e2e helper function laws (non-blocking isVisible, 18s shipping API wait, etc.)

### Test Card Reference Matrix
| Scenario | Card Number | Expected Outcome |
|---|---|---|
| Successful payment | `4242 4242 4242 4242` | Order created, email sent |
| 3DS required | `4000 0027 6000 3184` | `requires_action` flow triggered |
| Declined (insufficient funds) | `4000 0000 0000 9995` | Graceful error, no order created |
| Declined (generic) | `4000 0000 0000 0002` | User-friendly error message |
| Disputed | `4000 0000 0000 0259` | Dispute webhook handler fires |

**Playwright Environment (MANDATORY)**:
```bash
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" \
NODE_OPTIONS=--max-old-space-size=4096 \
PROD_URL=https://<project>.web.app \
PW_ALLOW_PROD=true \
./node_modules/.bin/playwright test <spec> --project=chromium --workers=1 --timeout=150000
```

### 7a — Full Happy Path (browser_subagent)
Invoke `browser_subagent` (Zoltan's Eye). Apply sovereign-playwright-e2e non-blocking patterns:
1. Navigate to product page — verify price displays correctly (CENTS/100 = dollars).
2. Add to cart — verify cart count increments, cart total correct.
3. Proceed to checkout — verify shipping form validation (required fields enforced).
4. Enter test card `4242 4242 4242 4242`, expiry `12/34`, CVC `123`.
5. Submit payment — verify redirect to order confirmation/success page.
6. Immediately after: query `mcp_firebase-mcp-server_firestore_query_collection` on `orders` (filter: most recent) — verify `status: PROCESSING`, `stripePaymentIntentId` populated.
7. Query `stripe_events` — verify deduplication record created.
8. Query `products/{productId}` — verify `stock` decremented by ordered qty.
9. Check function logs — verify confirmation email function executed successfully.

### 7b — Declined Payment Path
1. Use card `4000 0000 0000 0002` (generic decline).
2. Verify human-readable error message shown on checkout (not a raw Stripe error dump).
3. Query `orders` — verify NO new order document created.
4. Query `products/{productId}` — verify stock was NOT decremented.

### 7c — Out-of-Stock Enforcement
1. Temporarily set `products/testProduct.stock = 0` via Firestore MCP.
2. Navigate to product page — verify "Out of Stock" UI state (button disabled).
3. Attempt direct API call to checkout function with `productId` — verify `OUT_OF_STOCK` error returned.
4. Restore `stock` after test.

### 7d — 3DS Authentication Flow
1. Use card `4000 0027 6000 3184` (3DS required).
2. Verify 3DS modal/iframe appears after payment submission.
3. Complete 3DS challenge — verify order created successfully after authentication.
4. Verify error state if 3DS is declined.

### 7e — Refund Flow
1. Identify a recent test order with `status: DELIVERED`.
2. Trigger refund via admin panel or direct Cloud Function invocation.
3. Verify Stripe refund created (check function logs for `stripe.refunds.create` execution).
4. Query `orders/{orderId}` — verify `status: REFUNDED`, `refundId` populated.
5. Verify inventory restored if physical goods (`products/stock` incremented).
6. Check function logs — verify refund email function executed.

### 7f — IDOR Cross-User Order Access (Security E2E)
> **`auth-security-architect` IDOR test protocol**

Using `browser_subagent` (if two test users available):
1. Sign in as User A, place order, capture `orderId`.
2. Sign out. Sign in as User B.
3. Attempt to navigate to `/orders/{orderId}` (User A's order).
4. Must return 403, redirect to home, or show "not found" — NEVER show order data.
5. Alternatively, test via direct Firestore query as User B's authenticated context.

### 7g — Admin Panel E2E
1. Sign in as admin user (`admin: true` custom claim required).
2. Navigate to admin orders panel (`/admin/orders`).
3. Verify ALL orders visible (not scoped to admin UID).
4. Update an order status → SHIPPED, enter tracking number.
5. Verify Firestore `orders/{orderId}.status === SHIPPED`, `updatedAt` timestamp updated.
6. Verify SHIPPED email triggered (check function logs).
7. Sign out → sign in as regular user → verify `/admin/orders` returns 403/redirect.

### 7h — Customer Order History E2E
1. Sign in as regular customer.
2. Navigate to order history (`/account/orders` or `/dashboard/orders`).
3. Verify only their orders displayed (IDOR at UI layer).
4. Click into specific order → verify all line items, pricing, and status correct.
5. Verify pagination works if > 10 orders.

---

## 🔄 SECTOR 8 — Performance & Scalability
> 🧠 **INVOKE SKILL**: `performance-engineer`
> Read `.agent/skills/performance-engineer/SKILL.md` before proceeding.

### 8a — Function Cold Start Audit
Use `mcp_firebase-mcp-server_functions_get_logs` for `createPaymentIntent` function.
Apply `performance-engineer` cold start analysis pattern:
- Identify cold start invocations (look for initialization logs).
- If average cold start > 3s → flag for `minInstances: 1` configuration.

### 8b — Firestore Index Coverage
Use `grep_search` for compound queries in functions source (e.g., `where('userId').orderBy('createdAt')`).
For each compound query, verify a composite index exists via:
`mcp_firebase-mcp-server_firestore_list_indexes`
Missing index = queries silently fail in production = **P1**.

### 8c — Checkout Function Rate Limiting
Use `grep_search` for rate limiting or abuse prevention on `createPaymentIntent`.
Missing rate limiting = fraudulent payment attempt risk = **P2**.
Per `performance-engineer` skill: recommend token bucket pattern if missing.

### 8d — Order History Query Optimization
Use `grep_search` for order history queries in API/functions.
Verify `limit()` is applied to all order history queries (no unbounded reads).
Verify `startAfter()` cursor pagination is used (not `offset()` — Firestore offset reads all docs).

---

## 🔍 SECTOR 9 — Discount, Tax, GDPR & Fraud
> 🧠 **INVOKE SKILL**: `ecommerce-reviewer` Domains 7, 8, 9, 10

### 9a — Discount Code Integrity
- Verify one-time codes are atomically consumed via `runTransaction`.
- Verify expired coupons rejected with `{ code: 'COUPON_EXPIRED' }`.
- Verify per-user limits enforced.
- Verify discounted price recalculated server-side before Stripe call.

### 9b — Tax Server-Authority
- Verify `req.body.taxAmount` is NEVER accepted — P0 if found.
- Verify `taxInCents` stored on order document.
- Verify tax included in Stripe PaymentIntent `amount`.

### 9c — GDPR / Data Retention
- Verify no raw card numbers stored (Stripe tokenizes — verify this).
- Verify "delete my data" function anonymizes PII without deleting financial records.
- Verify `stripe_events` older than 90 days are purged by scheduled function.

### 9d — Fraud Signal Audit
- Use `grep_search` for velocity checks, fraud scoring patterns.
- Verify Stripe Radar is noted for manual dashboard check.
- If no velocity check → flag **P2**: implement `> 5 orders/hour from same UID = auto-flag`.

### 9e — Webhook Error Dead-Letter Pattern
- Verify failed webhook events logged to `webhook_errors` collection.
- Verify dead-letter handling for events that fail > 3 times.
- Verify `failed_orders` collection exists for payment-succeeded-but-order-not-created scenarios.

---

## 🧹 SECTOR 10 — Mission State Update

Update `MISSION_STATE.md`:
```
- E-Commerce Audit: COMPLETE [date]
- Stripe Secrets: [SECURE/INSECURE]
- Pricing Integrity: [VERIFIED/VIOLATED]
- Discount/Tax Server-Authority: [ENFORCED/VIOLATED]
- Idempotency: [ENFORCED/MISSING]
- IDOR Verification: [PASSED/FAILED/SKIPPED]
- Email Delivery: [VERIFIED/MISSING TRIGGERS]
- E2E Tests: [PASSED/FAILED]
- Inventory Coherence: [BALANCED/LEAKED/OVERSOLD]
- Admin E2E: [PASSED/FAILED/SKIPPED]
- Financial Reconciliation: [BALANCED/DELTA: X cents]
```

---

## 📊 SOVEREIGN E-COMMERCE AUDIT REPORT

*Output this complete report at the end of every audit run:*

**🛒 Commerce Health Dashboard:**

| Domain | Status | Finding |
|---|---|---|
| Security & Credentials | 🟢/🟡/🔴 | |
| Product Catalog Integrity | 🟢/🟡/🔴 | |
| Order Lifecycle & State Machine | 🟢/🟡/🔴 | |
| Payment Processing | 🟢/🟡/🔴 | |
| Idempotency / Dedup | 🟢/🟡/🔴 | |
| Discount & Tax Server-Authority | 🟢/🟡/🔴 | |
| Database Integrity | 🟢/🟡/🔴 | |
| Email Delivery | 🟢/🟡/🔴 | |
| E2E Checkout (Happy Path) | 🟢/🟡/🔴 | |
| E2E Checkout (Declined) | 🟢/🟡/🔴 | |
| 3DS / SCA Compliance | 🟢/🟡/🔴 | |
| Refund Flow | 🟢/🟡/🔴 | |
| IDOR Security | 🟢/🟡/🔴 | |
| Admin Operations E2E | 🟢/🟡/🔴 | |
| Webhook Resilience | 🟢/🟡/🔴 | |
| Performance & Indexes | 🟢/🟡/🔴 | |
| Fraud Signal Detection | 🟢/🟡/🔴 | |

**Financial Integrity:**
- Revenue Coherence: [Firestore total vs Stripe — match/mismatch + delta]
- Inventory Coherence: [Balanced / Leaked / Oversold]
- Orphaned Records: [Count + types]

**Incident Tickets:**
- **[P0] CRITICAL:** [Immediate halt items — double billing, hardcoded keys, overselling, IDOR breach]
- **[P1] HIGH:** [Missing email triggers, unhandled webhooks, unprotected admin routes, missing 3DS]
- **[P2] MEDIUM:** [Missing indexes, stale carts, partial refund gaps, no fraud detection]
- **[P3] LOW:** [UI error quality, schema cleanup, deprecated API usage]

`🧹 E-commerce sovereignty enforced. Financial integrity sealed. No mortal shall exploit this system.`
