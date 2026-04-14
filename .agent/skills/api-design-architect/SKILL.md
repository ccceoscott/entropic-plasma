---
name: api-design-architect
description: REST/gRPC API design authority — versioning strategy, rate limiting, OpenAPI spec generation, backward compatibility governance, and contract-first development.
phase: "209"
category: backend
tags: ["api-design", "REST", "gRPC", "OpenAPI", "versioning", "rate-limiting"]
---

# API Design Architect (R.A.P.S.) — Phase 209

## Overview
Contract-first API design authority for the Infinity Protocol fleet. Governs REST and gRPC API surface design, versioning strategies, OpenAPI specification generation, and backward compatibility enforcement. All APIs entering production must pass this skill's design review.

---

## Core Principles

### 1. Contract-First, Always
Every endpoint is defined in an **OpenAPI 3.1 spec** or a **Protobuf schema** BEFORE implementation begins. The contract is the source of truth.

```yaml
# openapi.yaml — sovereign API contract template
openapi: "3.1.0"
info:
  title: <Service Name> API
  version: "1.0.0"
  description: |
    <Purpose of the API>
  contact:
    email: hello@constantconcepts.io
servers:
  - url: https://<project>.cloudfunctions.net
    description: Production
  - url: http://localhost:5001/<project>/us-central1
    description: Local Emulator
```

### 2. Versioning Strategy
| Pattern | When to Use |
|---|---|
| URI versioning `/v1/`, `/v2/` | Public APIs with external consumers |
| Header versioning `Accept: application/vnd.api+json;version=2` | Internal fleet APIs |
| No versioning | Single-consumer internal functions |

**Rule**: Never break a published contract. Additive changes only on existing versions. Breaking changes = new version number.

### 3. Rate Limiting (Sovereign Law)
All public-facing Cloud Functions MUST implement rate limiting:

```typescript
// lib/rateLimiter.ts — Sovereign rate limit pattern
import { HttpsError } from "firebase-functions/v2/https";
import * as admin from "firebase-admin";

export async function enforceRateLimit(
  uid: string,
  action: string,
  maxPerMinute: number
): Promise<void> {
  const db = admin.firestore();
  const windowMs = 60_000;
  const now = Date.now();
  const windowStart = now - windowMs;

  const ref = db.collection("_rateLimits").doc(`${uid}_${action}`);

  await db.runTransaction(async (txn) => {
    const snap = await txn.get(ref);
    const data = snap.data() ?? { calls: [], updatedAt: now };

    // Evict calls outside the window
    const recentCalls: number[] = (data.calls as number[]).filter(
      (t) => t > windowStart
    );

    if (recentCalls.length >= maxPerMinute) {
      throw new HttpsError(
        "resource-exhausted",
        `Rate limit: max ${maxPerMinute} calls/minute for ${action}.`
      );
    }

    recentCalls.push(now);
    txn.set(ref, { calls: recentCalls, updatedAt: now });
  });
}
```

---

## REST Design Standards

### HTTP Verb Contract
| Action | Verb | Idempotent | Body |
|---|---|---|---|
| Fetch resource | GET | ✅ | None |
| Create resource | POST | ❌ | JSON |
| Replace resource | PUT | ✅ | JSON |
| Partial update | PATCH | ❌ | JSON |
| Delete resource | DELETE | ✅ | None |

### Response Envelope Standard
```typescript
// All API responses MUST use this envelope
interface SovereignResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;     // machine-readable: "PAYMENT_FAILED"
    message: string;  // human-readable
    details?: unknown;
  };
  meta?: {
    requestId: string;
    timestamp: string;
    version: string;
  };
}
```

### Status Code Governance
| Code | Usage |
|---|---|
| 200 | Success with body |
| 201 | Resource created |
| 204 | Success, no body (DELETE) |
| 400 | Invalid input (Zod validation failure) |
| 401 | Unauthenticated |
| 403 | Authenticated but unauthorized |
| 404 | Resource not found |
| 409 | Conflict (duplicate, already exists) |
| 429 | Rate limited |
| 500 | Internal server error (never expose stack trace) |

---

## Firebase Cloud Functions as REST APIs

### Pattern: `onRequest` with Router
For multi-route APIs, use Express-style routing within a single `onRequest` function:

```typescript
import { onRequest } from "firebase-functions/v2/https";
import express from "express";
import cors from "cors";

const app = express();
app.use(cors({ origin: true }));
app.use(express.json());

// Middleware: Auth guard
app.use(async (req, res, next) => {
  const token = req.headers.authorization?.split("Bearer ")[1];
  if (!token) return res.status(401).json({ success: false, error: { code: "UNAUTHENTICATED" } });
  try {
    req.user = await admin.auth().verifyIdToken(token);
    next();
  } catch {
    res.status(401).json({ success: false, error: { code: "INVALID_TOKEN" } });
  }
});

app.get("/v1/sales/:id", async (req, res) => { /* ... */ });
app.post("/v1/tickets", async (req, res) => { /* ... */ });

export const api = onRequest({ cors: true, secrets: ["STRIPE_SECRET_KEY"] }, app);
```

---

## OpenAPI Code Generation

### Generate TypeScript client from spec:
```bash
npx openapi-typescript openapi.yaml --output src/lib/api.d.ts
```

### Validate spec:
```bash
npx @stoplight/spectral-cli lint openapi.yaml --ruleset .spectral.yaml
```

### Sovereign Spectral Ruleset (`.spectral.yaml`):
```yaml
extends: ["spectral:oas"]
rules:
  operation-description: error      # All operations must have descriptions
  operation-operationId: error      # All operations must have operationId
  oas3-api-servers: error           # Must define servers
  info-contact: warn                # Should have contact info
```

---

## Backward Compatibility Laws

1. **NEVER remove a field** from a response — mark as deprecated, keep returning it
2. **NEVER change a field's type** — add a new field with the new type
3. **NEVER make an optional field required** — always additive
4. **ALWAYS version breaking changes** — `/v2/` endpoint, announce deprecation of `/v1/`
5. **Sunset headers** — include `Deprecation` and `Sunset` headers on deprecated endpoints

```typescript
// Deprecated endpoint pattern
app.get("/v1/legacy-endpoint", (req, res) => {
  res.set("Deprecation", "true");
  res.set("Sunset", "2026-12-31");
  res.set("Link", '</v2/new-endpoint>; rel="successor-version"');
  // ... handler
});
```

---

## Audit Checklist — API Design Review

Before any API endpoint goes to production:

- [ ] OpenAPI spec or Protobuf schema exists and is committed
- [ ] All endpoints have `operationId`, description, and response schemas
- [ ] Rate limiting applied to any unauthenticated or high-frequency path
- [ ] Auth guard applied to all non-public endpoints
- [ ] Response envelope standard used (`success`, `data`, `error`)
- [ ] No stack traces exposed in error responses
- [ ] Breaking changes versioned with new `/vN/` prefix
- [ ] Deprecated endpoints have `Deprecation` + `Sunset` headers
- [ ] Zod validation applied to all request bodies (see `zod-backend-dmz` skill)
- [ ] TypeScript gate passes: `tsc --noEmit`

---

## Post-Action Report Template

After designing or auditing an API, document:
```
API: <name>
Version: v<N>
Endpoints reviewed: <count>
Breaking changes detected: <YES/NO>
Rate limits applied: <YES/NO>
OpenAPI spec path: <path>
Outstanding concerns: <list>
```
