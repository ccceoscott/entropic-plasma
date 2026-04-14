---
description: Native Mobile & PWA Audit — Capacitor Bridge, Safe-Areas, Touch Targets, and Compliance.
alwaysApply: false
---

# 📱 /mobile_audit — The Capacitor Bridge (v12.0)

⚡ **MANDATE**: Execute this ritual to verify native iOS/Android compliance, Capacitor bindings, and mobile viewport architecture.

## 🧠 Skill Ingestion
**Automatically ingest this Domain Bundle**:
1. `!vis` — Sovereign Visual Domain (Aesthetics, CSS Tokens)

---

## 🔍 THE APP PATH
1. **Native Config Sync**: Audit `capacitor.config.ts`. Ensure `appId` and `webDir` are bound directly to the production artifact structure.
2. **Viewport & Touch Guards**: Emulate iOS Safari/Android Chrome via Browser Subagent (`/reveal`). Verify "Safe Area Insets" (notch clearance), ensure bottom navigation is reachable, and strictly enforce minimum 44px touch targets.
3. **Push Notifications (FCM)**: Verify Firebase Cloud Messaging configuration. Ensure device tokens are correctly mapped to User IDs in the database without overwriting or leaking.
4. **App Store Compliance**: Ensure a hard "Delete Account" capability exists in Settings. Verify Privacy Policy URLs resolve. Verify deep-linking/universal routing executes correctly in headless state.

Declare: `✅ [MOBILE AUDIT COMPLETE] | Native bindings sealed. App Store compliance verified.`
