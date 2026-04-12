---
description: Comprehensive Email Infrastructure, Template Design, Compliance (CAN-SPAM/GDPR), and Delivery Testing Workflow — APEX EDITION
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /email_audit_and_setup
## Sovereign Email Infrastructure — Zero-Spam, High-Delivery Apex Protocol

> ⚡ **LAW 22 (Email Delivery Integrity)**: NEVER trigger a transactional email without a verified `email_log` entry in Firestore. Missing tracking = P2 FAIL. Never hardcode email content in logic; use Templates or a specialized Dispatch Router.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` before proceeding:
1. `.agent/skills/email-delivery-architect/SKILL.md` — Resend/SendGrid/SES, SPF/DKIM/DMARC, template design, delivery verification

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

---

## SECTOR 1 — Provider & Secret Audit

### 1a — Secret Manager Check
Verify email API keys (Resend, SendGrid, Postmark) are in Secret Manager.
`["secrets", "list", "--project=...", "--format=json", "--quiet"]`

### 1b — Domain Verification Search
Use Brave Search to find the provider's Dashboard link if DNS settings are needed.
Search: `[Provider Name] domain verification dns records`

---

## SECTOR 2 — Firestore Email Logs (Tracking)

### 2a — Log Collection Verification
Verify `mail` or `email_logs` collection exists via MCP.

### 2b — Rules Bounding
```
match /mail/{mailId} {
  allow read, write: if false; // System only
}
```

---

## SECTOR 3 — Template Audit

Use `grep_search` for HTML strings in `functions/src`.
Flag any "Naked HTML" (emails written directly in TypeScript).
Refactor to use a `templates/` directory with e.g. `handlebars` or a simple string replacer.

---

## SECTOR 4 — Test Dispatch (Manual Trigger)

// turbo
```bash
firebase functions:shell
```
Call the email dispatch function with a test address.
Confirm delivery via Browser Subagent peering into an inbox (if authorized).

---

## SECTOR 5 — MISSION_STATE.md Update

Update `MISSION_STATE.md`:
- Email Infrastructure: AUDITED/BOOTSTRAPPED
- Provider: [Resend/SendGrid/etc.]
- Tracking: ACTIVE (Firestore logs)
- Templates: EXTERNALIZED

`🧹 Email infrastructure sealed. Delivery authorized.`
