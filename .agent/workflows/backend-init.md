# Workflow: Backend Feature Initialization (/backend-init)

**Objective:**
Execute this workflow whenever initializing a new backend feature, API layer, or database-driven component within the Infinity Protocol v3.0 ecosystem. This guarantees adherence to the strict Firebase synchronization and Ironclad CRUD mandates.

## 1. Context & Blueprint Ingestion
- Read the relevant `KNOWLEDGE.md` data schemas.
- If this is an e-commerce feature, review the `E-commerce Functionality Blueprint`.
- Propose an explicit "Goal/Data/Action/Edge" blueprint before writing code.

## 2. API Layer Construction
- Define the `zod` schema for the incoming payload.
- Create a single, centralized Cloud Function or API route.
- Implement explicit Error Path Analysis (EPA) with `try/catch`. 

## 3. Client-Side Synchronization 
- **Read Operations**: Establish a robust real-time `onSnapshot` listener. 
- **Write Operations**: Implement optimistic UI updates.
- Under NO CIRCUMSTANCES should a component handle ad-hoc database mutation logic outside a centralized API layer or context provider. 

## 4. Enterprise E-Commerce Primitive Rigor (If Applicable)
- **Cart/Checkout Integrity**: Validate all form inputs (zod). Ensure state synchronizes flawlessly between local context and the backend.
- **Payment & Webhook Idempotency**: Ensure successful transactions securely write back to Firestore. Implement Idempotency Keys to definitively prevent duplicate order execution.
- **Security & Caching**: Enforce Rate Limiting on checkout endpoints to block card testing. Ensure the product catalog utilizes Next.js ISR for sub-second loading.
- **Standardized Analytics**: Trigger standard Conversion API events tied directly to the payment state.
- **Absolute E2E Testing**: Add-to-cart, checkout form submissions, payment processing, and DB writing MUST be programmatically verified End-to-End. "Assuming" it works is forbidden.

## 5. Final Verification Check
- Verify that loading states and user-facing error boundaries (toasts/notifications) are present for the entire CRUD lifecycle.
- Confirm "Ironclad CRUD Locked."
