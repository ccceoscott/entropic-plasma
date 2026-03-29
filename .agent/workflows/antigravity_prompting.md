---
description: Antigravity Prompting Mastery — Sovereign Workflow (v2.0 with Ecommerce)
---

# /antigravity_prompting — Sovereign Execution Protocol v2.0

Reference: `rules/antigravity_prompting_mastery.mdc` for full doctrine.

---

## Pre-Session Ritual (All Projects)

1. Read `MISSION_STATE.md` — current phase, active blockers, known patterns
2. Select model: Gemini 3 Pro (default) | Claude Opus 4.5 (checkout/arch/rules)
3. Select mode: AGENT-ASSISTED (default) | REVIEW-DRIVEN (checkout/webhooks/rules/auth)
4. Toggle Deep Think: OFF (default) | ON (Stripe logic, Firestore schema, architecture)
5. Inject Mission State Handoff if resuming after 30+ message session

---

## Pre-Session Ritual (Ecommerce Projects)

6. Verify Stripe mode: `stripe config get` — confirm test key active before any webhook work
7. Verify Firebase project: `gcloud config get-value project` — no project bleed
8. Confirm Cloud Functions pricing gate: `functions/src/createPaymentIntent.ts` exists
9. Confirm idempotency collection exists: `/webhook_events` in Firestore
10. Confirm inventory transaction pattern: `functions/src/reserveStock.ts` exists

---

## Prompt Construction Checklist

- [ ] Single clear outcome stated in first sentence
- [ ] Referenced by file PATH not description
- [ ] Explicit constraints listed (tech + design + security)
- [ ] Explicit NON-scope listed ("do NOT touch: webhook handler")
- [ ] "Done when" condition is measurable (test passes / screenshot shows X)
- [ ] Canonical example pointed to ("Match pattern in OrderList.tsx")
- [ ] Ecommerce domain block injected (see template below)
- [ ] Browser verification requested as final artifact
- [ ] Mode explicitly declared (AGENT-ASSISTED or REVIEW-DRIVEN)

---

## Ecommerce Domain Block (Prepend to ALL ecommerce prompts)

```
Stack: Next.js 15 App Router + TypeScript strict + Tailwind + Firebase + Stripe
Pricing rule: ZERO client-side pricing. Amounts = Cloud Functions only.
Auth gate: src/lib/firebase/auth.ts — custom claims: admin, wholesale_approved
Cart: src/store/cartStore.ts (Zustand) + useCart hook (React Query optimistic)
Types: src/types/product.types.ts | order.types.ts | cart.types.ts
Webhooks: idempotency via /webhook_events — always check event.id first
Security: REVIEW-DRIVEN for checkout, webhooks, Firestore rules, inventory
Design: Liquid Glass 2.0 — match src/components/products/ProductCard.tsx
```

---

## Slice Templates (Copy-Paste)

### General Feature Slice
```
Implement the complete [FEATURE] feature slice:
- [ComponentPath]: [visual/behavioral spec]
- [HookPath]: [React Query + Zustand spec]
- [APIPath]: [endpoint — Zod validation + auth guard + Firestore write]
- [TestPath]: [loading / error / success / edge case scenarios]
Pattern: [canonical reference file path]
Constraints: [tech + security + design limits]
Done when: [E2E passes] + [browser screenshot shows X]
Mode: AGENT-ASSISTED. Final artifact: browser screenshot.
```

### Ecommerce Checkout Slice
```
ECOMMERCE CHECKOUT TASK — REVIEW-DRIVEN:
Security mandate: Frontend sends cartId + userId + shippingAddress ONLY. No prices.
Cloud Function reads authoritative prices from /products/{sku}.
Math.max(0, total) enforced before PaymentIntent.create().
Atomic inventory reserveStock() transaction BEFORE PaymentIntent creation.
Idempotency: stripe.webhooks.constructEvent() + /webhook_events/{event.id} check.
[Remaining spec...]
Mode: REVIEW-DRIVEN. Show diff for each file before writing. I approve each.
Done when: stripe trigger payment_intent.succeeded → Firestore order shows processing.
```

### Ecommerce Firestore Rules
```
Firestore Rules Task — REVIEW-DRIVEN:
/products: read=true, write=admin claim only
/carts/{userId}: owner-only read+write
/orders/{orderId}: read=owner|admin, create=auth, update+delete=false (immutable ledger)
/audit_logs: read=admin, write=false (backend only)
/webhook_events: read=admin, write=false (backend only)
Mode: REVIEW-DRIVEN. Show complete rules file diff before applying.
Test: firebase emulators:exec — all scenarios pass.
```

---

## Session Handoff Template

```
MISSION STATE:
Project: [name] | Stack: [stack] | Port: [port] | Branch: [branch]
Firebase Project: [id] | Stripe Mode: TEST/LIVE

Accomplished: [list]
Modified files: [list]
Sealed (do NOT touch): [list]

Ecommerce patterns locked:
  - Pricing: functions/src/createPaymentIntent.ts
  - Inventory: functions/src/reserveStock.ts
  - Idempotency: /webhook_events collection

Next: [single clear goal]
Mode: [AGENT-ASSISTED / REVIEW-DRIVEN]
```

---

## Post-Session Cleanup

// turbo
1. Run phantom purge: `rm -rf ~/.gemini/antigravity/browser_recordings`
2. Update `MISSION_STATE.md` with session accomplishments
3. Verify no secrets exposed: `dv scan-secrets`
4. Verify Stripe test mode still active: `stripe config get`
