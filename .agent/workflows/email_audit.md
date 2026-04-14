---
description: Transactional Messaging Audit — Delivery logs, DNS Verification, and Template Rendering.
alwaysApply: false
---

# 📧 /email_audit — The Deliverability Router (v12.0)

⚡ **MANDATE**: Execute this ritual to secure transactional communications, prevent spam-flagging, and enforce asynchronous email logging. NEVER trigger a transactional email without a verified telemetry entry.

## 🧠 Skill Ingestion
**Automatically ingest this Domain Bundle**:
1. `!hammer` — Sovereign Hammer (Ops, Testing, Execution)

---

## 🔍 THE DELIVERY PATH
1. **Provider DNS & Secrets**: Verify Resend/SendGrid secrets in Google Secret Manager. Confirm DMARC/SPF/DKIM domain alignments.
2. **Template Eradication**: Scour the backend for "Naked HTML" (emails built using hardcoded string interpolation inside Cloud Functions). Migrate them to externalized rendering logic or Handlebars/React Email.
3. **Delivery E2E Test**: Execute a manual trigger via `firebase functions:shell` or E2E UI flow to fire the confirmation email, monitoring response codes to prevent Silent Fails.
4. **Log Enforcement**: Ensure every outbound email leaves a permanent `email_logs` trace in Firestore strictly bound to `user.uid`. 

Declare: `✅ [EMAIL AUDIT COMPLETE] | Deliverability secured. Templates externalized.`
