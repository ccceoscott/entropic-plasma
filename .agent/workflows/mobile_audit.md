---
description: Complete iOS/Android + web mobile audit — native build, app store compliance, deep linking, push notifications, security, and viewport verification.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /mobile_audit
## Sovereign Mobile Infrastructure — Native Bridge, App Store Ready

> ⚡ **LAW 23 (Capacitor/Native Bridge)**: NEVER modify native code (`ios/`, `android/`) without first checking `capacitor.config.ts`. Drifting native state from config = P1 FAILURE.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest these skills** via `view_file` on each `SKILL.md` before proceeding:
1. `.agent/skills/capacitor-mobile-architect/SKILL.md` — iOS/Android deep linking, push notifications, App Store compliance
2. `.agent/skills/sovereign-playwright-e2e/SKILL.md` — Production E2E, Stripe CSP, multi-environment matrix

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
If stale → auto-upgrade (0b). If current → confirm (0c).

---

## SECTOR 1 — Capacitor / Native Bridge Audit

### 1a — Config Audit
Use `view_file` on `capacitor.config.ts`.
Verify:
- `appId` matches App Store/Play Store records.
- `webDir` points to correct build folder (`out`, `dist`, or `.next`).
- `bundledWebRuntime` status.

### 1b — Plugin Inventory
Use `grep_search` for `@capacitor/` in `package.json`.
Verify all plugins have corresponding native implementations.

---

## SECTOR 2 — Viewport & Touch Audit (Browser Witness)

Spawn browser subagent:
1. Emulate iPhone 14 Pro Max.
2. Check for "Tap Targets" (buttons too small/close).
3. Verify "Bottom Navigation" visibility.
4. Check for "Notch Interference" (safe-area-inset).

---

## SECTOR 3 — Push Notification Infrastructure (Firebase)

### 3a — FCM Config Check
Verify `google-services.json` (Android) and `GoogleService-Info.plist` (iOS) are present in native folders.

### 3b — Token Collection Audit
Check Firestore `fcm_tokens` collection structure via MCP.
Verify UIDs are correctly bound to tokens.

---

## SECTOR 4 — App Store Compliance Audit

- Check for "Delete Account" button in settings (MANDATORY).
- Verify Privacy Policy URL is reachable.
- Verify Version number in `package.json` vs `ios/App/App.xcodeproj`.

---

## SECTOR 5 — MISSION_STATE.md Update

Update `MISSION_STATE.md`:
- Mobile Audit: COMPLETE
- Native Bridge: VERIFIED
- Viewport Compliance: ✅
- Push Infrastructure: [Status]

`🧹 Mobile infrastructure audited. Native sovereignty confirmed.`
