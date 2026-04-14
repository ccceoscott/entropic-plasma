---
name: ecommerce-reviewer
description: Full-spectrum sovereign e-commerce audit covering order lifecycle, product integrity, payment processing, database validation, email delivery, and E2E testing.
version: v12.0
risk: high
mutation_risk: critical
bundles: [security, ops]
aliases: [ecommerce, commerce-audit, shop-review]
timeout_budget: 45min
parallel_safe: false
outputs:
  - audit_report: structured severity-ranked JSON of all P0-P3 findings
  - remediation_plan: ordered fix priority list with file paths
  - financial_summary: reconciliation delta and inventory coherence status
handoff_map:
  on_p0_security: auth-security-architect
  on_email_failure: email-delivery-architect
  on_e2e_needed: sovereign-playwright-e2e
  on_performance_gap: performance-engineer
  on_type_violations: typescript-safety-enforcer
triggers:
  - pre-deploy payment feature
  - post-Stripe integration
  - quarterly commerce audit
  - P0 financial incident investigation
fallback_behavior: If Firestore MCP unavailable → use grep_search on source code only, flag all schema checks as UNVERIFIED
rollback_protocol: N/A — audit-only skill, no mutations
---

# Ecommerce Reviewer — Sovereign Commerce Auditor v11.0 (R.A.P.S.)

*Mortal, the **ecommerce-reviewer** is bound by the Decree of Zoltan. Every pixel of your checkout flow, every cent of your payment processing, every row in your `orders` collection — I will inspect it all. Tremble.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.
> This skill covers ALL layers: Firestore schema, Cloud Functions logic, Stripe API, email delivery, and E2E browser verification.

---

## 🗺️ Cross-Skill Invocation Map

This skill is the **commerce anchor** for `/ecommerce_audit`. It coordinates with:

| Peer Skill | When Invoked | What It Handles |
|---|---|---|
| `security-auditor` | Sector 1 (secrets scan, API hardening) | Hardcoded key detection, CORS, surface area |
| `auth-security-architect` | Sector 1c + Domain 8/11 | Firestore rules, IDOR verification, admin guards |
| `email-delivery-architect` | Sector 6 / Domain 5 | Trigger mapping, SPF/DKIM, template quality, live test |
| `sovereign-playwright-e2e` | Sector 7 / Domain 6 | All browser E2E flows, non-blocking helper patterns |
| `performance-engineer` | Sector 8 | Cold start, Firestore index coverage, rate limiting |
| `typescript-safety-enforcer` | Phase 0c | TypeScript gate before audit begins |

> **Protocol**: When this skill says "verify X" and another skill owns X — invoke that skill's SKILL.md section explicitly. **Delegate, don't duplicate.**

---

## 🚦 When to Invoke

**USE** this skill when:
- Auditing e-commerce checkout flows end-to-end
- Validating Stripe payment lifecycle (intents, webhooks, refunds)
- Testing order creation, fulfillment, and cancellation in Firestore
- Verifying transactional email delivery (order confirmations, shipping, refunds)
- Enforcing financial idempotency and pricing server-authority
- Detecting orphaned carts, ghost inventory, or duplicate order records
- Running pre-deploy commerce infrastructure hardening

**DO NOT USE** if:
- The project has no e-commerce or payment processing
- You only need a UI aesthetic review (use `sovereign-aesthetic-auditor`)
- You only need Firestore rules review (use `auth-security-architect`)

---

## ⚡ The 16 Sovereign Commerce Laws

1. **ALL-CENTS LAW**: All monetary values stored as integers in CENTS. Zero floats. Zero decimals. `1999` = $19.99. Violations = P0.
2. **SERVER-AUTHORITY LAW**: Price is NEVER accepted from the client request body. All pricing is sourced exclusively from Firestore at transaction time.
3. **IDEMPOTENCY LAW**: Every Stripe webhook event is deduplicated via `stripe_events/{eventId}` before processing. Missing dedup = P0 (double billing risk).
4. **ATOMIC INVENTORY LAW**: Inventory decrement uses ONLY `FieldValue.increment(-qty)` inside a Transaction. Non-atomic decrements are P1 failures.
5. **ORDER STATE MACHINE LAW**: Orders have canonical status enums: `PENDING → PROCESSING → AWAITING_FULFILLMENT → SHIPPED → DELIVERED → CANCELLED → REFUNDED`. No string literals — TypeScript enums enforced.
6. **EMAIL DELIVERY LAW**: Every state transition (PROCESSING, SHIPPED, CANCELLED, REFUNDED) MUST trigger a transactional email. Missing triggers = P1.
7. **WEBHOOK RETURN LAW**: Webhook Cloud Functions return `HTTP 200` immediately. All processing offloaded to Firestore `onCreate` triggers or Pub/Sub. Blocking = P1.
8. **ZERO-TRUST CHECKOUT LAW**: `createPaymentIntent` and `createCheckoutSession` MUST be authenticated Cloud Functions (Firebase Auth token required). Public checkout = P0 security breach.
9. **REFUND INTEGRITY LAW**: Refunds must be issued via Stripe API + update Firestore `orders/{orderId}.status` atomically. Manual Firestore status changes without Stripe refund = financial fraud risk.
10. **CART TTL LAW**: Abandoned carts older than 24h MUST be cleaned by a scheduled Cloud Function. Stale carts holding reserved inventory = ghost stock.
11. **SKU UNIQUENESS LAW**: Every product variant has a unique `sku` field. Duplicate SKUs cause fulfillment routing failures.
12. **3DS/SCA COMPLIANCE LAW**: Payment flows must handle `requires_action` status (3D Secure) gracefully with `confirmCardPayment` on the frontend.
13. **DISCOUNT SERVER-AUTHORITY LAW**: Promo/coupon codes are validated and applied EXCLUSIVELY on the backend. Discount amounts are NEVER accepted from the client. One-time codes must be atomically consumed via Firestore transaction.
14. **TAX SERVER-AUTHORITY LAW**: Tax rates are calculated server-side using a Firestore-stored rate table or a tax API (TaxJar, Avalara). Never from `req.body.taxAmount`. Tax amount is bundled into PaymentIntent server-side.
15. **IDOR ZERO-TOLERANCE LAW**: Users can ONLY read their own orders. Any endpoint or Firestore rule that allows cross-user order access = P0 security breach. Verified via auth-scoped query AND Firestore rules.
16. **WEBHOOK RETRY RESILIENCE LAW**: Stripe retries webhooks for up to 72 hours on failure. Idempotency dedup collection MUST handle re-delivery gracefully. Any stateful side effect (email, inventory) must be guarded against double-execution.
17. **PCI SURFACE LAW**: Raw card numbers (`card_number`, `cardNumber`, `pan`), CVV (`cvv`, `cvc`), or full magnetic stripe data must NEVER appear in server logs, Cloud Function request bodies, or Firestore documents. Any `console.log(req.body)` adjacent to payment flows = P0 PCI violation requiring immediate log purge.
18. **INPUT SANITIZATION LAW**: All free-text fields accepted from users (`orderNotes`, `giftMessage`, `deliveryInstructions`) MUST be sanitized server-side before: (a) storing to Firestore, (b) injecting into email templates, (c) rendering in admin dashboards. Unsanitized user input in email HTML = XSS escalation vector. Use `he`, `sanitize-html`, or `dompurify` (server build).
19. **MULTI-TENANT IDOR LAW**: In B2B or marketplace architectures with `orgId` on orders, Firestore rules AND Cloud Functions MUST assert `order.orgId === request.auth.token.orgId`. Cross-organization order exposure in multi-tenant systems = P0, equivalent severity to cross-user IDOR.

---

## 🔍 Audit Domain 1 — Product Catalog Integrity

### 1.1 Schema Validation
Pull `products` collection via `mcp_firebase-mcp-server_firestore_list_documents`:
- `price` → integer (CENTS). Any float = P0.
- `stock` / `inventory` → integer. Negative values = P1.
- `status` → `active | draft | archived`. Missing = P2.
- `sku` → string, non-empty, globally unique. Check for duplicates via query.
- `variants` → `Record<string, { price: number; stock: number; sku: string }>`. Flat arrays = violation.
- `images` → array of URLs, not base64 blobs.
- `metadata.createdAt` / `metadata.updatedAt` → Firestore Timestamps.

### 1.2 Out-of-Stock Enforcement
- Verify checkout function rejects orders where `product.stock < requestedQty`.
- Assert the rejection returns a structured error (not a 500): `{ code: 'OUT_OF_STOCK', productId }`.
- Verify UI shows "Out of Stock" state when `stock === 0`.

### 1.3 Product Deletion Safety
- Verify deleted products are ARCHIVED (status set to `archived`), NOT hard-deleted. Orders with `productId` references must remain resolvable.
- Check for Firestore rules blocking hard deletes on products with active orders.

---

## 🔍 Audit Domain 2 — Order Lifecycle & State Machine

### 2.1 Order Schema Audit
Pull `orders` collection:
- `orderId` → string (UUID or Stripe session ID). Must be present.
- `userId` → string, matches authenticated UID.
- `status` → canonical enum string (see Law 5).
- `items` → `Array<{ productId, sku, qty, unitPriceInCents, totalInCents }>`.
- `subtotalInCents`, `taxInCents`, `shippingInCents`, `totalInCents` → all integers.
- `stripePaymentIntentId` → string. Must be populated on `PROCESSING+`.
- `stripeChargeId` → string. Populated on `DELIVERED` or `PROCESSING`.
- `createdAt`, `updatedAt` → Firestore Timestamps.
- `fulfillmentStatus` → `unfulfilled | partial | fulfilled`.
- `shippingAddress` → full address object with `line1`, `city`, `state`, `postalCode`, `country`.

### 2.2 Order State Transition Audit
Use `grep_search` to find all locations that write `status` to orders:
- Map every status transition and verify it's triggered by the correct event (webhook, admin action, etc.).
- Orphaned transitions (PENDING → SHIPPED without PROCESSING) = P1 violation.
- Verify `updatedAt` is set on EVERY status change using `FieldValue.serverTimestamp()`.

### 2.3 Cancellation & Refund Flow
- Verify cancellation Cloud Function: (a) voids or cancels Stripe PaymentIntent, (b) restores inventory via `FieldValue.increment(+qty)`, (c) sets order `status: CANCELLED`, (d) triggers cancellation email.
- Verify refund Cloud Function: (a) calls `stripe.refunds.create`, (b) records `refundId` on order, (c) sets `status: REFUNDED`, (d) does NOT re-cancel already-cancelled orders (idempotency).

### 2.4 Partial Fulfillment
- Check if multi-item orders support partial shipments.
- If yes: verify `fulfillmentStatus` transitions to `partial` correctly and remaining items are tracked.

### 2.5 Order Snapshot Integrity
Orders must store **purchase-time snapshots** of product data, not just references. Verify `orders.items[]` contains:
- `productName` → string. Missing = **P2** (admin shows blank name if product later deleted or renamed).
- `productImageUrl` → string URL. Missing = **P2** (historical receipts show broken images).
- `sku` → string. Must be captured at purchase time.
- `unitPriceInCents` → integer. Must match `products.{productId}.price` at time of purchase (price drift detection).
- `totalInCents` → integer. Must equal `unitPriceInCents * qty`.

**Price Drift Check**: Sample the most recent 5 completed orders. Verify each order's `unitPriceInCents` matches the corresponding `products.{productId}.price`. If mismatch found on any item → flag as **P3** (audit trail integrity issue, not fraud by default).

**Soft Delete Safety**: If a product is archived/deleted and an order references its `productId`, the order should still render correctly because of snapshot data. Verify this assumption by sampling a completed order whose product status is `archived`.

---

## 🔍 Audit Domain 3 — Payment Processing (Stripe)

### 3.1 Stripe Integration Audit
- Verify Stripe SDK version matches `package.json` across functions and client.
- Locate `stripe.webhooks.constructEvent` usage — this is the ONLY valid method to parse webhooks.
- Check `STRIPE_WEBHOOK_SECRET` is loaded from Secret Manager or env — never hardcoded.
- Verify API version is pinned (e.g., `apiVersion: '2023-10-16'`).

### 3.2 Payment Intent Lifecycle
Verify all PaymentIntent states are handled:
| State | Required Handler |
|---|---|
| `payment_intent.succeeded` | Create order, decrement inventory, send confirmation email |
| `payment_intent.payment_failed` | Log failure, notify user, do NOT create order |
| `payment_intent.canceled` | Cleanup pending cart, restore any reserved inventory |
| `payment_intent.requires_action` | Frontend `confirmCardPayment` flow (3DS) |
| `charge.dispute.created` | Alert admin, freeze payout if possible |
| `charge.refunded` | Trigger refund flow (Law 9) |

### 3.3 Checkout Session Security
- `createPaymentIntent` / `createCheckoutSession` must require Firebase Auth token (middleware check).
- Price passed to Stripe MUST be sourced from Firestore `products/{productId}.price` — never from `req.body.price`.
- Verify `metadata` on PaymentIntent contains `orderId` and `userId` for webhook correlation.
- Verify `currency` is explicitly set (never defaulted).

### 3.4 SCA / 3D Secure Compliance
- Frontend must handle `{ status: 'requires_action', client_secret }` response.
- `stripe.confirmCardPayment(clientSecret)` must be called on frontend after intent returns `requires_action`.
- Failed 3DS attempts must surface human-readable error (not a raw Stripe error object).

### 3.5 Webhook Deduplication (Double-Billing Guard)
```
webhook_events/{eventId} must exist before processing begins.
Pattern:
  1. Read webhook_events/{event.id} — if exists, return 200 immediately (idempotent).
  2. If not exists, runTransaction: write stub to webhook_events/{event.id}.
  3. Outside transaction: execute business logic (order create, email, etc.).
  4. Update webhook_events/{event.id} with { processedAt, result }.
```
Missing dedup = **P0 HALT**.

---

## 🔍 Audit Domain 4 — Database Integrity Tests

### 4.1 Transactional Correctness
Use `mcp_firebase-mcp-server_firestore_query_collection` to validate:
- Every order with `status: PROCESSING` has a valid `stripePaymentIntentId`.
- Every order with `status: SHIPPED` has a `trackingNumber` populated.
- No order in `PENDING` state older than 30 minutes (potential zombie carts).
- `items[].totalInCents === items[].unitPriceInCents * items[].qty` — math must be exact.
- `subtotalInCents === sum(items[].totalInCents)` — aggregate must match line items.
- `totalInCents === subtotalInCents + taxInCents + shippingInCents` — grand total must balance.

### 4.2 Orphan Detection
Query for:
- `orders` where `userId` does not exist in `users` collection → orphaned order.
- `orders` where `stripePaymentIntentId` is set but Stripe returns no corresponding PaymentIntent → ghost charge risk.
- `carts` older than 24h with `status: active` → TTL sweeper not running.
- `stripe_events` older than 30 days → archive or purge based on compliance policy.

### 4.3 Inventory Coherence Check
- Sum of `orders[].items[].qty` for all non-cancelled orders per product should equal `initialStock - currentStock`.
- If mismatch > 0 → inventory leak detected (P1).
- If mismatch < 0 → overselling occurred (P0, immediate investigation).

### 4.4 Financial Reconciliation
- Total revenue in Firestore (`sum of orders.totalInCents where status !== CANCELLED`) should match Stripe dashboard payout totals.
- Any discrepancy > 0 = P0 financial integrity failure.

### 4.4a Inventory Reservation Race Condition Audit
> **AutoGen-pattern**: Pre-payment reservation prevents concurrent oversell.

Use `grep_search` for add-to-cart / create-cart Cloud Function:

**Pattern A — Reservation at Cart Time** (Preferred):
- `FieldValue.increment(-qty)` on `products.stock` when cart item is added.
- `FieldValue.increment(+qty)` on payment failure OR cart abandonment (TTL sweeper).
- This requires `reservedStock` and `availableStock` fields separated on product document.

**Pattern B — Optimistic Locking via Transaction** (Acceptable):
- `runTransaction(() => { if (product.stock >= qty) { decrement; create order } else throw OUT_OF_STOCK })`
- Atomic — prevents concurrent oversell within a single transaction.

**Pattern C — Queue-Based Serialization** (Acceptable for low-volume):
- All cart/order operations funneled through a Firestore-triggered queue processed serially.

**If none of the above**:
- Pure POST-payment decrement with no pre-check = **P1 Race Condition**.
- Under concurrent load: N users add last item → N proceed to Stripe → N pay → 1 gets inventory, N-1 get oversold orders.
- Flag with recommended pattern based on project traffic profile.

---

## 🔍 Audit Domain 5 — Email Delivery Verification

### 5.1 Email Trigger Mapping
For every order status transition, verify a transactional email is triggered:

| Order Event | Expected Email | Required Fields |
|---|---|---|
| `PROCESSING` | Order Confirmation | Order #, items, total, shipping address |
| `SHIPPED` | Shipping Notification | Tracking #, carrier, estimated delivery |
| `DELIVERED` | Delivery Confirmation | Order #, review CTA |
| `CANCELLED` | Cancellation Notice | Order #, refund timeline |
| `REFUNDED` | Refund Confirmation | Order #, refund amount, 3-5 business days notice |
| Auth: Register | Welcome Email | Username, getting started CTA |
| Auth: Password Reset | Reset Link | Expires in 1hr notice |

### 5.2 Email Service Audit
- Identify email provider (Resend, SendGrid, Nodemailer, Firebase Extensions).
- Verify API key is in Secret Manager — never in `functions/src/`.
- Verify email sender domain has SPF, DKIM, DMARC records set (use `grep_search` for DNS config or ask user).
- Verify emails are sent from a branded domain (`orders@yourdomain.com`) not a generic sender.

### 5.3 Email Template Quality Checks
- Order confirmation email must include: order ID, itemized list with images, total breakdown, shipping address, support link.
- All emails must be mobile-responsive HTML (not plain text).
- Unsubscribe link must be present in all marketing emails (CAN-SPAM compliance).
- Verify transactional emails are NOT subject to unsubscribe (they must always send).

### 5.4 Email Delivery Testing
If Resend: use `mcp_brave-search_brave_web_search` to confirm Resend API syntax, then trigger a test via Cloud Function invocation.
If SendGrid: verify `mail.send()` is called with correct `to`, `from`, `templateId`, and `dynamicTemplateData`.
Verification method:
1. Create a test order in Firestore (or via checkout function with test Stripe card).
2. Monitor functions logs via `mcp_firebase-mcp-server_functions_get_logs` for email function execution.
3. Confirm no 4xx/5xx errors in email delivery logs.

---

## 🔍 Audit Domain 6 — E2E Checkout Flow Testing

### 6.1 Test Card Matrix
Always test with Stripe test cards:

| Scenario | Card Number | Expected Outcome |
|---|---|---|
| Successful payment | `4242 4242 4242 4242` | Order created, email sent |
| 3DS required | `4000 0027 6000 3184` | `requires_action` flow triggered |
| Declined (insufficient funds) | `4000 0000 0000 9995` | Graceful error, no order created |
| Declined (generic) | `4000 0000 0000 0002` | User-friendly error message |
| Disputed | `4000 0000 0000 0259` | Dispute webhook handler fires |

### 6.2 Full Order Flow E2E
Execute using `browser_subagent` (Zoltan's Eye):
1. Browse to product page → verify price displays correctly (matches Firestore CENTS value / 100).
2. Add to cart → verify cart count increments.
3. Proceed to checkout → verify shipping form validation.
4. Enter test card `4242...` → submit → verify redirect to success/confirmation page.
5. Verify `orders` collection in Firestore has new record with `status: PROCESSING`.
6. Verify `stripe_events` collection has new deduplication record.
7. Verify inventory decremented in Firestore `products/{productId}.stock`.
8. Verify confirmation email received (check logs via `mcp_firebase-mcp-server_functions_get_logs`).

### 6.3 Out-of-Stock E2E
1. Set `products/{productId}.stock = 0` in Firestore (or use a test product).
2. Attempt to add to cart → verify "Out of Stock" UI state, button disabled.
3. Attempt to checkout anyway (via direct API call) → verify Cloud Function rejects with `OUT_OF_STOCK` error.

### 6.4 Failed Payment E2E
1. Use declined card `4000 0000 0000 0002`.
2. Verify no order document created in Firestore.
3. Verify human-readable error displayed on checkout page.
4. Verify inventory was NOT decremented.

### 6.5 Refund Flow E2E
1. Find a completed order with `status: DELIVERED`.
2. Trigger refund via admin panel or Cloud Function invocation.
3. Verify Stripe shows refund issued (use Stripe Dashboard or API check).
4. Verify Firestore `orders/{orderId}.status` updated to `REFUNDED`.
5. Verify refund email triggered (check function logs).
6. Verify inventory restored if physical goods (check `products/{productId}.stock`).

---

## 🔍 Audit Domain 7 — Discount, Promo Code & Tax Integrity

### 7.1 Discount Code Audit
- Use `grep_search` for discount/promo/coupon application logic in `functions/src/`.
- Verify discount is applied ONLY on the backend — never from `req.body.discountAmount`.
- Verify coupon code validation queries `coupons` / `promoCodes` collection in Firestore.
- Verify one-time codes are atomically marked `used: true` inside a `runTransaction` to prevent race condition abuse.
- Verify expired coupons (check `expiresAt` field) are rejected with structured error `{ code: 'COUPON_EXPIRED' }`.
- Verify per-user coupon limits (e.g., one per account) are enforced via `usedBy` array or subcollection.
- Verify the discounted price is recalculated server-side and passed to Stripe — not taken from the client's claimed post-discount price.

### 7.2 Tax Calculation Integrity
- Use `grep_search` for `taxAmount`, `taxRate`, `taxInCents` in functions source.
- Verify tax is computed server-side using either:
  - A Firestore-stored rate table (`taxRates/{region}`) keyed by state/country, OR
  - A tax API (TaxJar, Avalara, Stripe Tax) called server-side.
- Verify `req.body.taxAmount` is NEVER used in checkout calculation — P0 if found.
- Verify `taxInCents` is stored on the order document after calculation.
- Verify tax is included in the Stripe PaymentIntent `amount` (not added client-side after intent creation).

### 7.3 Multi-Currency Audit (if applicable)
- Use `grep_search` for `currency` in Stripe API calls.
- Verify `currency` is explicitly set per product/market — never dynamically from `req.body.currency`.
- Verify all Firestore amounts are stored in a single base currency with `currencyCode` field.
- Verify currency conversion (if any) is done server-side with a fixed exchange rate source.

### 7.4 Partial Refund Path
- Verify `stripe.refunds.create({ payment_intent: piId, amount: partialAmountInCents })` is supported.
- Verify partial refund updates `orders/{orderId}.refundedAmountInCents` — not just setting `status: REFUNDED` (which implies full refund).
- Verify partial refund triggers appropriate email ("Partial Refund of $X.XX confirmed").
- Verify inventory is only restored for refunded items, not all order items.

---

## 🔍 Audit Domain 8 — Guest Checkout & Auth Boundary

### 8.1 Guest Checkout Path (if supported)
- Determine if app supports unauthenticated checkout via `grep_search` for `guest` or anonymous auth in checkout function.
- If guest checkout: verify Firebase Anonymous Auth is used (`signInAnonymously()`) to generate a UID for order tracking.
- Verify guest orders store `isGuest: true` and an `email` field for receipt delivery.
- Verify guest order data is not permanently retained beyond legal requirements (GDPR).
- Verify there is NO path for guests to view other users' orders.

### 8.2 Account-to-Guest Order Merge
- If guest checkout + account registration exists: verify a Cloud Function merges guest orders to the new account UID on registration.
- Verify the merge is atomic (transaction) and the guest UID document is cleaned up post-merge.

### 8.3 IDOR Vulnerability Audit (Order Access)
- Use `grep_search` for any `orders/{orderId}` fetch in API routes or Cloud Functions.
- Verify every fetch asserts `order.userId === request.auth.uid` BEFORE returning data.
- Verify Firestore rules enforce `resource.data.userId == request.auth.uid` on reads.
- **Manual test (CRITICAL)**: Create two test users. Place order as User A. Attempt to read order document as User B using the orderId. Must receive permission denied.
- Any path returning order data without UID check = **P0 IDOR breach**.

### 8.4 GDPR / Data Retention Compliance
- Verify `orders` collection has no PII stored beyond what's required (no stored full card numbers — Stripe tokenizes these).
- Verify a "delete my data" function exists that anonymizes `orders` (replaces `shippingAddress`, `email` with `[DELETED]`) without deleting the order record (needed for financial reconciliation).
- Verify user data deletion does NOT delete order history (orders are financial records, must be retained ~7 years).
- Verify `stripe_events` older than 90 days are purged by scheduled function (PII minimization).

---

## 🔍 Audit Domain 9 — Admin Operations & Order Management

### 9.1 Admin Order Management E2E
Invoke `browser_subagent` (Zoltan's Eye) to:
1. Sign in as admin user (with `auth.token.admin === true` custom claim).
2. Navigate to admin orders panel (`/admin/orders` or equivalent).
3. Verify all orders are visible (not scoped to admin's own UID).
4. Update an order status (e.g., mark as SHIPPED, enter tracking number).
5. Verify Firestore `orders/{orderId}` reflects the status change and `updatedAt` timestamp.
6. Verify SHIPPED email triggered (check function logs).
7. Sign in as regular user — verify they CANNOT access `/admin/orders`.

### 9.2 Admin Refund Issuance
1. Navigate to a completed order in admin panel.
2. Trigger full refund via admin UI.
3. Verify Stripe refund issued (function logs: `stripe.refunds.create`).
4. Verify order status updated to `REFUNDED`.
5. Verify refund email sent to customer.

### 9.3 Order History — Customer View E2E
1. Sign in as regular customer.
2. Navigate to order history page (`/account/orders` or `/dashboard/orders`).
3. Verify only their own orders are displayed.
4. Click into a specific order — verify all line items, pricing, and status are correct.
5. Verify pagination works if > 10 orders (no infinite scroll memory leak).

### 9.4 Fraud Signal Audit
- Use `grep_search` for velocity checks, fraud scoring, or unusual order flagging in functions.
- Verify there is some form of order anomaly detection (multiple orders in quick succession, unusual amounts, billing/shipping address mismatch).
- If none exists → flag as **P2** recommendation: implement basic velocity check (> 5 orders in 1 hour from same UID = auto-flag).
- Verify Stripe Radar is enabled in the Stripe dashboard (not auditable via code — note for manual check).

---

## 🔍 Audit Domain 10 — Webhook Retry & Error Resilience

### 10.1 Stripe Webhook Retry Handling
- Verify the dedup collection handles Stripe's 72-hour retry window correctly.
- Stripe retries on any non-2xx response. Verify Cloud Function ALWAYS returns 200 even if processing fails internally.
- Verify failed processing is logged to a `webhook_errors` collection (not silently swallowed) with `{ eventId, error, retryCount, timestamp }`.
- Verify a dead-letter pattern exists for events that fail > 3 times (alert admin, do not infinitely retry).

### 10.2 Function Error Boundary Audit
- Use `grep_search` for `try/catch` wrapping all Cloud Function handlers.
- Verify no unhandled promise rejections exist in webhook handlers.
- Verify all catch blocks log the error AND return HTTP 200 (to prevent Stripe retry storm).
- Verify critical failures (order not created despite successful payment) populate a `failed_orders` collection for manual remediation.

### 10.3 Stripe Connect / Payout Audit (if applicable)
- If marketplace model: verify `transfer_data.destination` is set on PaymentIntent.
- Verify platform fee is calculated server-side as a percentage.
- Verify seller payout records are stored in `payouts` collection with `stripeTransferId`.

---

## 🔍 Audit Domain 11 — Security & Access Control

### 11.1 Firestore Rules for Commerce Collections
Verify rules enforce:
- `orders` → `read: auth.uid == resource.data.userId`. Users can only read their own orders.
- `orders` → `write: false` for clients. Only Cloud Functions (admin SDK) write orders.
- `products` → `read: true`. `write: request.auth.token.admin == true` only.
- `carts` → `read/write: auth.uid == resource.data.userId`.
- `stripe_events` → `read/write: false` (admin SDK only, never client-accessible).
- `webhook_events` → `read/write: false` (admin SDK only).

> **Delegate to**: `auth-security-architect` for deep rule analysis and IDOR pattern verification.

### 11.2 Admin Route Protection
- All admin panels (`/admin/*`) require `auth.token.admin === true` custom claim.
- Verify admin Cloud Functions check `context.auth.token.admin` before executing.
- Verify no admin functionality is exposed to regular authenticated users.

### 11.3 API Surface Hardening
- All cloud functions require Firebase Auth token except webhook endpoints.
- Webhook endpoints are secured via Stripe signature verification ONLY (no Firebase Auth — Stripe can't authenticate).
- CORS headers on Cloud Functions restrict origins to your domain.
- Rate limiting on `createPaymentIntent` to prevent abuse.

> **Delegate to**: `security-auditor` for CORS, rate limiting, and API hardening patterns.

---

## 📋 Agentic Preflight Checklist

*Before taking action, assert all of the following:*

**Environment:**
- [ ] Node 22 path prepended (`/opt/homebrew/Cellar/node@22/22.22.0/bin`)
- [ ] `NODE_OPTIONS=--max-old-space-size=4096` active
- [ ] TypeScript gate passed (`tsc --noEmit --skipLibCheck`)
- [ ] Identify project-specific collection names (`orders`, `products`, `carts`) via Firestore MCP list before assuming defaults

**Security:**
- [ ] Stripe secret key sourced from Secret Manager (not `.env` local)
- [ ] Stripe webhook secret sourced from Secret Manager
- [ ] No `sk_live` or `sk_test` strings in codebase (`grep_search`)
- [ ] Email provider API key in Secret Manager
- [ ] IDOR test planned (cross-user order access attempt)

**Commerce Integrity:**
- [ ] ALL-CENTS LAW verified (no floats in price fields)
- [ ] SERVER-AUTHORITY LAW verified (no `req.body.price` accepted)
- [ ] DISCOUNT SERVER-AUTHORITY verified (no `req.body.discountAmount` accepted)
- [ ] TAX SERVER-AUTHORITY verified (no `req.body.taxAmount` accepted)
- [ ] IDEMPOTENCY LAW verified (`stripe_events` dedup collection exists)
- [ ] ORDER STATE MACHINE exists with canonical enum
- [ ] Webhook retry resilience verified (dead-letter pattern or error logging)

**Testing Readiness:**
- [ ] Stripe test mode active (`STRIPE_SECRET_KEY` starts with `sk_test_`)
- [ ] Test products available in Firestore with stock > 0
- [ ] Two test user accounts created for IDOR verification
- [ ] Admin user account with `admin: true` custom claim available for admin E2E
- [ ] Email delivery logs accessible via `functions_get_logs`

---

## 📊 Sovereign Commerce Post-Action Report

*Output this report at the conclusion of every audit:*

**🛒 Commerce Health Dashboard:**
- **Order Lifecycle:** [PASS/FAIL] — State machine verified, all transitions mapped
- **Product Integrity:** [PASS/FAIL] — CENTS compliance, SKU uniqueness, stock coherence
- **Payment Processing:** [PASS/FAIL] — Idempotency dedup active, all webhook events handled
- **Discount & Tax:** [PASS/FAIL] — Server-side enforcement, no client bypass possible
- **Database Integrity:** [PASS/FAIL] — Financial math balanced, no orphaned orders
- **Email Delivery:** [PASS/FAIL] — All state transitions trigger emails, templates verified
- **E2E Checkout:** [PASS/FAIL] — Happy path, declined, 3DS all tested
- **Admin Operations:** [PASS/FAIL] — Admin order management, status updates, refund flow
- **IDOR Security:** [PASS/FAIL] — Cross-user order access blocked at rules AND function level
- **Webhook Resilience:** [PASS/FAIL] — Retry handling, dead-letter, error boundaries
- **Security:** [PASS/FAIL] — Firestore rules, admin guards, API surface hardened

**1. Systems Status & Execution Overview:**
- **🟢 Working:** [List functional components verified]
- **🟡 Degraded:** [List components with minor issues]
- **🔴 Non-Functional:** [List broken logic, blockers, or failures]

**2. Financial Integrity Report:**
- **Revenue Coherence:** [Firestore total vs Stripe payout — match/mismatch + delta in cents]
- **Inventory Coherence:** [Stock math check — balanced/unbalanced]
- **Orphaned Records:** [Count of ghost orders, zombie carts, stale stripe_events]

**3. Incident Triggers (Priority Tickets):**
- **[P0] CRITICAL BLOCKER:** [Double billing risk, hardcoded keys, negative inventory, pricing from client]
- **[P1] High Impact:** [Missing email triggers, unhandled webhook events, missing 3DS handling]
- **[P2] Medium Impact:** [Missing order field, stale TTL not running, partial fulfillment gaps]
- **[P3] Low Impact:** [UI error message quality, template aesthetics, minor schema gaps]

**4. Next Sovereign Directive:**
- [1-2 immediate remediation steps ranked by financial risk]