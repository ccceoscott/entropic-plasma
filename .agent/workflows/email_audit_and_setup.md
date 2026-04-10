---
description: Comprehensive Email Infrastructure, Template Design, Compliance (CAN-SPAM/GDPR), and Delivery Testing Workflow — APEX EDITION
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /email_audit_and_setup
## Transactional & Marketing Email Sovereignty — Apex Edition

> ⚡ **MANDATE**: An unverified email pipeline is a silent black hole. This workflow enforces absolute UI consistency between web and email, guarantees strict GDPR/CAN-SPAM compliance, and fully maps the testing topology before production mailers are activated.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` to guarantee the workflow runs on a v10.0 synced environment.

### Phase 0b — Secrets Perimeter (Email Keys)
Use `grep_search` across `src/`, `functions/src/`, and `.env.local`:
- Identify keys for: `SendGrid`, `Resend`, `Postmark`, `Mailgun`, or `Mailtrap`.
- If keys are hardcoded outside of `.env.local` or Secret Manager → **HALT**. P0 leak.

---

## SECTOR 1 — Email Provider & Trigger Architecture Audit

### 1a — Transactional Trigger Map (E-commerce / Auth)
Use `grep_search` to map all email triggers in `functions/src/`:
| Trigger Event | Target Function | Delivery Service | Implemented |
|---|---|---|---|
| User Registration | (e.g. `sendWelcomeEmail`) | [Service] | ✅/❌ |
| Checkout Complete | (e.g. `sendOrderReceipt`) | [Service] | ✅/❌ |
| Password Reset | (Firebase Auth) | [Service] | ✅/❌ |
| Subscription Cancel | (e.g. `sendChurnSurvey`) | [Service] | ✅/❌ |
| Contact Form Submit | (e.g. `sendContactLead`) | [Service] | ✅/❌ |

> **Contextual Completeness**: 
> - **E-commerce**: Must have Order Confirmed, Shipping Updates, Refund Receipts.
> - **Lead Gen**: Must have Contact Form Auto-responders and Admin Lead Notifications.
*If any expected core triggers are missing for the project phase, flag them immediately.*

### 1b — Error Handling & Idempotency Check
Use `grep_search` for the email provider's `send()` function calls.
Verify that all email dispatches are wrapped in `try/catch` and utilize **Idempotency Keys** linked to Firestore event IDs.
> **Law**: A failed order confirmation email MUST NOT rollback a successful Stripe charge or document commit. Emails must fail-open and log to telemetry.
> **Law**: duplicate webhooks MUST NOT send duplicate emails. Firestore `eventId` maps must exist.

---

## SECTOR 2 — Design & UI Consistency (The Inbox Aesthetic)

Emails must match the visual sovereignty of the Next.js frontend, downgraded gracefully for HTML-table based email clients.

### 2a — React Email / Template Audit
Use `view_file` to inspect the email directory (e.g. `emails/`, `functions/src/templates/`).
- If raw HTML strings are used → **Convert to React Email / MJML** for cross-client consistency.
- Ensure the Liquid Glass aesthetic translates well (e.g., using solid `hsl(220, 15%, 8%)` fallbacks where `backdrop-filter` is unsupported).

### 2b — Typography, Branding, & Tailwind Parity
Confirm:
- Fonts matching the global brand (e.g., Inter fallback to sans-serif).
- Colors matching `--gradient-primary` and `--color-on-surface`.
- Border-radii on buttons matching frontend CTA buttons (e.g., `borderRadius: 8px`).

Use `grep_search` for `@react-email/tailwind` to ensure `<Tailwind>` config precisely mirrors `tailwind.config.ts`.
> **Danger**: Mismatched Tailwind configs result in padding/margin collapse on mobile clients. 

### 2c — Dark Mode & OS Media Queries
Search email directories for `@media (prefers-color-scheme: dark)`.
Emails MUST respect the user's OS dark mode to maintain the Liquid Glass aesthetic. Provide stark white text fallbacks for deep dark backgrounds on Outlook/Apple Mail.

Use `browser_subagent` to render the React Email dev server (if available) and visually verify desktop, mobile, and inverted dark-mode viewports.
Verify that **Logos** scale properly and global branding headers/footers are consistently applied across all templates.

### 2d — Data Context & Merge Tag Accuracy
Templates must pull accurate database items. Use `grep_search` to verify how templates map data:
- Confirm that contextual data (e.g., `order.total`, `user.firstName`) safely falls back if null.
- Verify array mapping for e-commerce receipts (looping through `cartItems` or `purchases`).
- Ensure Stripe webhook metadata perfectly bridges into the email merge variables without mismatch.

---

## SECTOR 3 — Compliance & Deliverability Strictness (GDPR / CAN-SPAM)

> ⛔ **P0 COMPLIANCE CHECK**: An email sent without an unsubscribe link or explicit consent is a legal liability.

### 3a — Unsubscribe & Physical Address Check
For EVERY marketing and transactional template:
- Use `grep_search` to verify standard footer variables (`{{unsubscribe_url}}`, physical business address).
- If absent → Block deployment. 

### 3b — Event Data PII Mappings
Review webhook payloads triggering marketing emails.
Verify: Credit card data, SSNs, or sensitive user-generated content are NEVER passed in the email payload object.

### 3c — Suppression List Integration
Confirm logic exists to check `email_preferences` from the user's Firestore document BEFORE sending non-critical emails.

### 3d — Deliverability Infrastructure Auditing (DNS/DMARC)
Use `run_command` with `dig` or `nslookup` (if available) to verify DNS records for the sending domain.
Verify existence of:
- **SPF** (`TXT` record containing `v=spf1`)
- **DKIM** (Selector `TXT` or `CNAME`)
- **DMARC** (`_dmarc.domain.com` with `p=quarantine` or `p=reject`)

*Missing DNS records mean your APEX-level UI will land straight in the spam folder.*

## SECTOR 4 — End-to-End Testing Workflows

### 4a — The Sandbox Environment
Confirm conditional provider logic based on environment:
```typescript
const provider = process.env.NODE_ENV === "production" ? new Resend(prodKey) : new Mailtrap(sandboxKey);
```

### 4b — Local Emulator Email Intercept
Verify the Firebase Auth Emulator is configured to intercept and print emails locally instead of attempting live dispatch during dev runs.

### 4c — Live Trigger E2E Test
Execute the `unit_testing.md` test suite that simulates:
1. `auth.user().onCreate`
2. `firestore.document('orders/{id}').onCreate`
Verify the mock email client receives the exact expected HTML payload.

---

## SECTOR 5 — Sovereign Declaration & Final Pulse

Output the final Email Setup Report:

```markdown
╔══════════════════════════════════════════════════════════════════╗
║  EMAIL SETUP & COMPLIANCE REPORT                                ║
╚══════════════════════════════════════════════════════════════════╝

┌─────────────────────────────┬────────┬──────────────────────────────┐
│ Criteria                    │ Status │ Notes                        │
├─────────────────────────────┼────────┼──────────────────────────────┤
│ Provider Keys Secured       │ ✅/❌  │ [Secret Manager / .env]      │
│ Idempotent Triggers         │ ✅/❌  │ [N mapped / zero duplicates] │
│ Component Completeness      │ ✅/❌  │ [Matches project type]       │
│ UI Parity, Logos, Tailwind  │ ✅/⚠️  │ [Matches brand / Dark Mode]  │
│ Merge Tags & DB Context     │ ✅/❌  │ [Accurate arrays & variables]│
│ Deliverability Config       │ ✅/❌  │ [SPF/DKIM/DMARC Verified]    │
│ CAN-SPAM (Unsubscribe)      │ ✅/❌  │ [Footer verified]            │
│ PII Sanitization            │ ✅/❌  │ [No sensitive data in payload]│
│ E2E Mailtrap/Sandbox        │ ✅/⚠️  │ [Local intercepts working]   │
└─────────────────────────────┴────────┴──────────────────────────────┘

OVERALL: [🟢 SOVEREIGN / 🟡 DEGRADED / 🔴 BLOCKED]
```

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Email infrastructure audited, templated, compliant, and sovereign.`
