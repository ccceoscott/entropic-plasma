---
name: typescript-safety-enforcer
description: Eliminates `any` casts, enforces strict type-safety, and governs TypeScript excellence across the Infinity Protocol fleet.
version: v10.2
risk: low
mutation_risk: low
bundle: core-dev
aliases: [ts, types, typesafety, strict]
depends_on: [zod-backend-dmz]
timeout_budget: 15min
parallel_safe: true
outputs:
  - any_cast_report: list of `any` usages with file paths and suggested types
  - strict_mode_gaps: tsconfig settings diverging from strict standard
  - type_coverage_score: percentage of typed surface area
success_criteria:
  - Zero `any` casts in payment/order logic
  - tsconfig.json has strict:true
  - No @ts-ignore comments without justification comment
handoff_map:
  on_validation_gap: zod-backend-dmz
  on_api_contract: api-design-architect
fallback_behavior: Run tsc --noEmit via run_command as fallback if grep_search misses inferred any
---

# TypeScript Safety Enforcer (R.A.P.S.) — Phase 208

*Mortal, the **typescript-safety-enforcer** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.

## Use this skill when
- Auditing or eliminating `any`, `unknown`, or unsafe casts across a codebase
- Enforcing strict TypeScript config (`strict: true`) on a project
- Migrating plain JS files to typed TypeScript
- Typing third-party SDK integrations (Firebase Admin, Stripe, Capacitor)
- Resolving `tsc` build errors without resorting to type suppression

## Do not use this skill when
- The task requires runtime schema validation (use `zod-backend-dmz`)
- The task is a quick single-type fix — just fix it directly
- Typing would require major architectural refactor outside current scope

## Safety
- **Never** silence TypeScript errors with `// @ts-ignore` or `// @ts-nocheck` — document the reason OR fix the root cause
- **Never** widen a type to `any` to bypass a compilation error
- **Acceptable `any` exceptions**: Firebase Admin SDK internals, Capacitor native plugin maps, third-party SDKs that ship untyped — document these with `// SAFE: <reason>`

---

## Core Mandates

1. **Zero `any` Policy (Rule 14)**: All `any` casts must be eliminated or explicitly documented with a `// SAFE:` comment
2. **`strict: true` Sovereignty**: All fleet projects must run `"strict": true` in `tsconfig.json`
3. **Zod as Runtime SSOT**: TypeScript types on the boundary are inferred from Zod schemas — never duplicate type definitions
4. **Generic Precision**: Use generics over `any` for flexible, reusable utility types
5. **Exhaustive Guards**: Always use discriminated unions + exhaustive switches for state machines

---

## tsconfig.json Sovereign Standard

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true
  }
}
```

> [!WARNING]
> `noUncheckedIndexedAccess` will surface array access bugs. Treat each one as a real bug, not noise.

---

## The `any` Eradication Playbook

### Pattern 1: Unknown API Response → Infer via Zod
```typescript
// ❌ BEFORE
const data: any = await fetchOrder(id);
const total = data.total_cents;

// ✅ AFTER — Zod schema as SSOT
import { z } from 'zod';
const OrderSchema = z.object({ id: z.string(), total_cents: z.number().int() });
type Order = z.infer<typeof OrderSchema>;
const data: Order = OrderSchema.parse(await fetchOrder(id));
```

### Pattern 2: Firebase Firestore DocumentData → Typed Converter
```typescript
// ❌ BEFORE
const snap = await db.collection('orders').doc(id).get();
const order = snap.data() as any;

// ✅ AFTER — Typed converter
import { FirestoreDataConverter, QueryDocumentSnapshot } from 'firebase-admin/firestore';
interface Order { id: string; total_cents: number; userId: string; }
const orderConverter: FirestoreDataConverter<Order> = {
  toFirestore: (order) => order,
  fromFirestore: (snap: QueryDocumentSnapshot): Order => {
    const d = snap.data();
    return { id: snap.id, total_cents: d.total_cents, userId: d.userId };
  },
};
const snap = await db.collection('orders').withConverter(orderConverter).doc(id).get();
const order = snap.data(); // Order | undefined — fully typed
```

### Pattern 3: Event Handlers / Callbacks
```typescript
// ❌ BEFORE
const handleChange = (e: any) => setValue(e.target.value);

// ✅ AFTER
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => setValue(e.target.value);
```

### Pattern 4: Discriminated Unions Over String Enums
```typescript
// ❌ BEFORE
type Status = string;
if (status === 'pending') { ... }

// ✅ AFTER — Exhaustive discriminated union
type OrderStatus = 'pending' | 'processing' | 'shipped' | 'delivered' | 'cancelled';
const handleStatus = (status: OrderStatus): string => {
  switch (status) {
    case 'pending': return 'Awaiting payment';
    case 'processing': return 'In fulfillment';
    case 'shipped': return 'On the way';
    case 'delivered': return 'Complete';
    case 'cancelled': return 'Cancelled';
    default: {
      const _exhaustive: never = status; // Compile-time exhaustiveness check
      throw new Error(`Unhandled status: ${_exhaustive}`);
    }
  }
};
```

### Pattern 5: Generic Utility Types (Replace Boilerplate)
```typescript
// Nullable wrapper
type Nullable<T> = T | null;
type Optional<T> = T | undefined;

// API response envelope
type ApiResponse<T> = { data: T; meta: { cursor?: string } } | { error: { code: string; message: string } };

// Firestore document with ID
type WithId<T> = T & { id: string };

// Partial deep update (for Firestore merge updates)
type DeepPartial<T> = { [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P] };
```

---

## Acceptable `any` Exceptions (Document These)

| Context | Why `any` Is Acceptable | Required Comment |
|---|---|---|
| Firebase Admin SDK internal | Admin SDK ships some untyped internals | `// SAFE: Firebase Admin internals — no public type` |
| Capacitor native plugin bridge | Native plugins use dynamic object maps | `// SAFE: Capacitor native bridge — untyped by design` |
| `JSON.parse()` result | Truly unknown external data | Use `unknown` + Zod parse instead — do NOT reach for `any` |
| Error catch clause | Pre-TS 4.0 pattern | Use `catch (err: unknown)` and `instanceof Error` guard |

---

## Type Audit CLI Commands

```bash
# Count all `any` occurrences in project
grep -r --include="*.ts" --include="*.tsx" " any" src/ | wc -l

# Find all @ts-ignore suppressions
grep -rn "@ts-ignore\|@ts-nocheck\|as any" src/ --include="*.ts" --include="*.tsx"

# Run tsc with strict checking (no emit — audit only)
PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" \
  ./node_modules/.bin/tsc --noEmit --strict 2>&1 | head -50
```

---

## Behavioral Traits
- Never reaches for `any` as a quick fix — investigates the root type contract
- Treats `// @ts-ignore` as a P1 incident requiring immediate root-cause analysis
- Infers types from Zod schemas rather than duplicating type definitions
- Uses `unknown` as the safe alternative to `any` for external data
- Mandates Firestore typed converters for all document reads
- Documents all acceptable `any` exceptions with `// SAFE:` comments

---

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Run `tsc --noEmit` to get the full error list before making changes
- [ ] Identify all `as any`, `@ts-ignore`, `@ts-nocheck` occurrences in scope
- [ ] Confirm `"strict": true` is in `tsconfig.json`
- [ ] Map each `any` to its root cause (bad SDK type, missing schema, lazy cast)
- [ ] Check if a Zod schema already exists that can be `z.infer<typeof Schema>`-ed

### 📊 Sovereign Agent Post-Action Report

**1. Systems Status:**
- **🟢 Resolved:** [`any` casts eliminated, strict config enabled, Zod types inferred]
- **🟡 Acceptable:** [Documented `// SAFE:` exceptions with justification]
- **🔴 Blocked:** [Third-party SDK types unavailable, requires `@types/` package]

**2. Type Safety Metrics:**
- **`any` count before:** X
- **`any` count after:** Y (Z remaining are documented SAFE exceptions)
- **`tsc --noEmit` exit code:** 0 = pass

**3. Incident Triggers:**
- **[P0]:** `@ts-nocheck` at file level suppressing real type errors
- **[P1]:** Financial data typed as `number` without cents enforcement
- **[P2]:** Firestore reads cast with `as any` instead of typed converter
- **[P3]:** String enums used where discriminated unions provide exhaustiveness

**4. Next Sovereign Directive:**
- [Run `dv scan-secrets` after type refactor to confirm no leaked values]
- [Update Zod schemas in `zod-backend-dmz` to stay in sync with inferred types]

## Example Interactions
- "Audit the entire `src/` directory and report all `any` casts with fix recommendations"
- "Type the Stripe webhook handler — it currently uses `as any` for the event payload"
- "Add a Firestore typed converter for the `orders` collection"
- "Migrate our string-based status type to a discriminated union with exhaustive handling"
- "Why is `noUncheckedIndexedAccess` flagging this array access? What's the safe fix?"
- "Infer all our domain types from existing Zod schemas instead of duplicating them"
- "Fix the 23 TypeScript errors from the Stripe v22 upgrade without using `@ts-ignore`"

*Type safety is not a suggestion. It is the ward that prevents your production system from descending into chaos.*
