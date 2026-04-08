---
description: Advanced Firebase/Stripe e-commerce bootstrapping, zero-trust rules, idempotency engines, and storefront hardening.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /ecommerce_bootstrap
## Sovereign E-Commerce Bootstrap — Schema-First, Idempotency-Native, Zero-Trust

> ⚡ **MANDATE**: Bootstrap execution follows strict Schema-Guard (Law 20) → Auth Claim-Check (Law 19) → Code order. The agent NEVER generates e-commerce code before live schema and auth claims are verified via MCP.

> 💰 **FINANCIAL SOVEREIGNTY**: All payment operations use `runTransaction`. All webhook handlers implement idempotency guards. All amounts are stored in CENTS. Zero exceptions.

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

---

## SSOT INGESTION

Use `view_file` on `MISSION_STATE.md`.
Use `view_file` on `KNOWLEDGE.md`.
Use `view_file` on `.agent/CODEBASE_MAP.md` (if exists).

Verify that `/setup_database` and `/setup_auth` have been completed (check MISSION_STATE).
If not → **HALT**: run those workflows first. E-commerce requires working foundation.

---

## SECTOR 1 — Pre-Bootstrap Verification

### 1a — Firestore State (Two-Key MCP)
Use `mcp_firebase-mcp-server_firestore_list_databases` → confirm DB exists and is ACTIVE.
Use `mcp_firebase-mcp-server_firestore_list_collections` → check if e-commerce collections already exist.
If `orders`, `products`, or `carts` collections exist → **WARNING**: data already present. Confirm bootstrap won't overwrite.

### 1b — Existing Functions Check
Use `mcp_firebase-mcp-server_functions_list_functions` → check for existing payment functions.
Existing Stripe/payment functions → merge with, do NOT overwrite.

### 1c — Secret Verification
Use `mcp_gcloud_run_gcloud_command` with args:
`["secrets", "list", "--project=gen-lang-client-0386732425", "--filter=name:STRIPE", "--quiet", "--format=json"]`
- `STRIPE_SECRET_KEY` → must exist
- `STRIPE_WEBHOOK_SECRET` → must exist
Missing → **HALT**. User must add secrets to Secret Manager before bootstrap.

---

## SECTOR 2 — Schema-Guard Bootstrap (Law 20)

Define canonical e-commerce TypeScript interfaces. Save to `types/ecommerce.d.ts`:

```typescript
// types/ecommerce.d.ts — Sovereign Schema — DO NOT GUESS FIELD NAMES
import { Timestamp, DocumentReference } from 'firebase/firestore';

export type OrderStatus = 'PENDING' | 'PROCESSING' | 'COMPLETED' | 'CANCELLED' | 'REFUNDED';
export type PaymentStatus = 'UNPAID' | 'PAID' | 'FAILED' | 'REFUNDED';

export interface Product {
  id: string;
  name: string;
  description: string;
  priceCents: number; // ALWAYS CENTS — never floats
  stripePriceId: string;
  stripeProductId: string;
  stock: number;
  imageUrl: string | null;
  active: boolean;
  createdAt: Timestamp;
  updatedAt: Timestamp;
}

export interface CartItem {
  productId: string;
  productRef: DocumentReference;
  name: string;
  priceCents: number;
  quantity: number;
  imageSrc: string | null;
}

export interface Cart {
  userId: string;
  items: CartItem[];
  totalCents: number;
  updatedAt: Timestamp;
}

export interface Order {
  id: string;
  userId: string;
  stripeSessionId: string; // idempotency key
  stripePaymentIntentId: string | null;
  items: CartItem[];
  subtotalCents: number;
  taxCents: number;
  totalCents: number;
  currency: 'usd'; // explicit
  status: OrderStatus;
  paymentStatus: PaymentStatus;
  shippingAddress: ShippingAddress | null;
  createdAt: Timestamp;
  updatedAt: Timestamp;
  fulfilledAt: Timestamp | null;
}

export interface ShippingAddress {
  line1: string;
  line2: string | null;
  city: string;
  state: string;
  postalCode: string;
  country: string;
}
```

**Law**: ALL subsequent e-commerce code in this session MUST use ONLY these interfaces.

---

## SECTOR 3 — Firestore Security Rules (Zero-Trust E-Commerce)

Generate rules anchored to Schema:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Products: anyone can read, ONLY Functions can write
    match /products/{productId} {
      allow read: if true;
      allow write: if false; // Cloud Functions only via Admin SDK
    }

    // Carts: owner can read/write their own cart
    match /carts/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Orders: owner can read ONLY, Functions write
    match /orders/{orderId} {
      allow read: if request.auth != null
        && request.auth.uid == resource.data.userId;
      allow write: if false; // Cloud Functions only
    }

    // Inventory: NEVER writable by clients
    match /inventory/{productId} {
      allow read: if false;
      allow write: if false;
    }
  }
}
```

Validate: Use `mcp_firebase-mcp-server_firebase_validate_security_rules` with type `"firestore"`.

---

## SECTOR 4 — Cloud Functions Scaffold

### 4a — createCheckoutSession
```typescript
// functions/src/ecommerce/createCheckoutSession.ts
export const createCheckoutSession = onCall({
  memory: '512MiB',
  timeoutSeconds: 30,
}, async (request) => {
  if (!request.auth) throw new HttpsError('unauthenticated', 'Login required');
  
  const { cartItems, successUrl, cancelUrl } = request.data;
  
  // Validate items against live Firestore schema
  // Run inventory check in transaction before creating Stripe session
  // ...
  
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    mode: 'payment',
    success_url: successUrl,
    cancel_url: cancelUrl,
    client_reference_id: request.auth.uid, // uid binding
    metadata: { userId: request.auth.uid },
    line_items: cartItems.map(item => ({
      price: item.stripePriceId,
      quantity: item.quantity,
    })),
  });
  
  return { sessionId: session.id, url: session.url };
});
```

### 4b — stripeWebhook (Idempotency Engine)
```typescript
// functions/src/ecommerce/stripeWebhook.ts
export const stripeWebhook = onRequest({ cors: false }, async (req, res) => {
  const sig = req.headers['stripe-signature']!;
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET!;
  
  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(req.rawBody, sig, webhookSecret);
  } catch {
    res.status(400).send('Webhook signature verification failed');
    return;
  }
  
  // IDEMPOTENCY GUARD — prevents double-processing
  const eventRef = db.collection('stripe_events').doc(event.id);
  const existing = await eventRef.get();
  if (existing.exists) {
    res.status(200).send('Duplicate event — already processed');
    return;
  }
  
  // Mark as processing
  await eventRef.set({ processed: false, createdAt: FieldValue.serverTimestamp() });
  
  res.status(200).send('Received'); // Respond to Stripe immediately
  
  // Process async
  switch (event.type) {
    case 'checkout.session.completed':
      await fulfillOrder(event.data.object as Stripe.Checkout.Session);
      break;
    case 'payment_intent.payment_failed':
      await handlePaymentFailure(event.data.object as Stripe.PaymentIntent);
      break;
  }
  
  await eventRef.update({ processed: true, processedAt: FieldValue.serverTimestamp() });
});
```

### 4c — fulfillOrder (Transaction-Safe)
```typescript
async function fulfillOrder(session: Stripe.Checkout.Session): Promise<void> {
  const userId = session.metadata?.userId;
  if (!userId) throw new Error('Missing userId in Stripe metadata');
  
  await db.runTransaction(async (transaction) => {
    // Read inventory
    // Deduct stock (never go below 0)
    // Create order document with COMPLETED status
    // Clear user's cart
    // All in one atomic transaction
  });
}
```

---

## SECTOR 5 — Composite Index Creation

For expected query patterns, create indexes now (not after runtime errors):
```
orders: userId ASC + createdAt DESC
products: active ASC + createdAt DESC
stripe_events: processed ASC + createdAt ASC
```

Use `mcp_firebase-mcp-server_firestore_create_index` for each.

---

## SECTOR 6 — Seed Data (Test Mode Only)

Use `mcp_firebase-mcp-server_firestore_add_document` to create 2-3 test products.
Use real Stripe test price IDs from Stripe Dashboard (never fake strings).

---

## SECTOR 7 — Build & Validate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 120 npm run build 2>&1 | tail -20
```
Build errors → auto-fix → re-run once.

---

## SECTOR 8 — E2E Browser Witness

Spawn browser subagent:
1. Navigate to `/products` (or storefront page)
2. Add item to cart
3. Click checkout → Stripe Checkout loads
4. Complete with test card `4242 4242 4242 4242`
5. Screenshot: order confirmation
6. Query MCP: `mcp_firebase-mcp-server_firestore_list_documents` on `orders` → confirm new document
7. Screenshot: Firestore order document in DevTools
8. Check Function logs: `mcp_firebase-mcp-server_functions_get_logs` → no errors

**No browser witness = e-commerce NOT verified.**

---

## SECTOR 9 — Knowledge Graph Persistence (MCP)
Use `mcp_knowledge-graph_create_entities` to establish:
- E-commerce schema entity (canonical field definitions)
- Idempotency pattern entity
- Webhook event coverage map

---

## SECTOR 10 — MISSION_STATE.md Update
Update: E-commerce: BOOTSTRAPPED | Schema: GENERATED | Idempotency: ACTIVE | Browser Witness: CONFIRMED

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 E-commerce sovereignty sealed. Every transaction is atomic. Every webhook is idempotent.`
