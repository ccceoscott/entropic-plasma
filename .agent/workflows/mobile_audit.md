---
description: Complete iOS/Android + web mobile audit — native build, app store compliance, deep linking, push notifications, security, and viewport verification.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /mobile_audit
## Mobile Sovereignty Audit — iOS, Android, Web Viewport, Accessibility, App Store Launch Readiness

> ⚡ **MANDATE**: Mobile is a first-class citizen. This workflow covers BOTH the native app layer (Capacitor/React Native) and the web viewport layer. Run in full before any iOS/Android submission or major mobile release.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:` and `**WORKSPACE_PHASE**`.
Report both explicitly:
```
WORKSPACE_PHASE: [X]   (local workspace phase from MISSION_STATE.md)
PROTOCOL_PHASE:  [Y]   (global protocol phase from Brain / project_states Firestore)
PHASE_GAP:       [Y-X] (0 = synchronized | >0 = workspace is stale)
```
If PHASE_GAP > 0 → auto-upgrade (Phase 0b). If 0 → confirm (Phase 0c).

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

### Phase 0d — Mobile Framework Detection
Use `grep_search` for `capacitor` in `package.json`. If found → Capacitor mode.
Use `grep_search` for `react-native` in `package.json`. If found → React Native mode.
Log detected framework — all subsequent native phases adapt accordingly.

---

## PHASE 1 — NATIVE BUILD CONFIGURATION AUDIT

### 1a — Capacitor Config Audit
Use `grep_search` for `capacitor.config.ts` or `capacitor.config.json`.
Verify the following fields are set and correct for production:
- `appId` — reverse-DNS format (e.g., `io.constantconcepts.firstpick`)
- `appName` — human-readable, matches App Store listing
- `webDir` — must point to correct build output (`out` or `dist`)
- `android.buildOptions` — ensure release build is not in debug mode
- `ios.scheme` — matches Xcode scheme name

### 1b — Android Manifest Audit
Use `grep_search` for `android:debuggable` in `android/app/src/main/AndroidManifest.xml`.
**CRITICAL**: `android:debuggable="true"` MUST NOT be present in production builds. If found → flag as P0 blocker.
Also verify:
- `android:usesCleartextTraffic="false"` — enforces HTTPS
- Internet permission present: `android.permission.INTERNET`
- All listed permissions have corresponding rationale

### 1c — iOS Plist Audit
Use `grep_search` for `NSAppTransportSecurity` in `ios/App/App/Info.plist`.
**CRITICAL**: `NSAllowsArbitraryLoads` must be absent or `false` in production.
Also verify:
- `CFBundleIdentifier` matches App Store Connect bundle ID
- `CFBundleShortVersionString` (marketing version) is correct
- `CFBundleVersion` (build number) is incremented from last submission
- `get-task-allow` key is absent (Xcode sets to `false` in Archive mode — verify by checking release scheme)

### 1d — 64-Bit Architecture Compliance
Use `grep_search` for `abiFilters` in `android/app/build.gradle`.
Verify only `arm64-v8a` and `x86_64` are listed. Remove `armeabi-v7a` if present.
For iOS: Xcode Archive for release automatically excludes 32-bit — verify by confirming `VALID_ARCHS = arm64` in Xcode build settings (check `ios/App.xcodeproj/project.pbxproj` if accessible).

### 1e — Build Variant Matrix
Verify three build configurations exist (no production-debug mixing):
| Environment | Android | iOS |
|-------------|---------|-----|
| Debug | `debuggable=true`, dev server URL | Dev scheme |
| Staging | `debuggable=false`, staging API URL | Staging scheme |
| Production | `debuggable=false`, prod API URL | Release scheme / Archive |

---

## PHASE 2 — DEEP LINKING VERIFICATION

### 2a — Universal Links (iOS)
Use `grep_search` for `apple-app-site-association` in `public/` or `.well-known/`.
Verify the AASA file:
1. Is served at `https://[your-domain]/.well-known/apple-app-site-association`
2. Has correct `appID` format: `TEAMID.bundleIdentifier`
3. Includes all relevant path patterns
Test: simulate tapping a link in Safari (deep link must open app, not web)

### 2b — App Links (Android)
Use `grep_search` for `assetlinks.json` in `public/` or `.well-known/`.
Verify the Asset Links file is served at `https://[your-domain]/.well-known/assetlinks.json` with correct:
- `package_name` (matches `applicationId` in `build.gradle`)
- `sha256_cert_fingerprints` (matches release keystore)

### 2c — In-App Deep Link Routing
Use `grep_search` for `App.addListener('appUrlOpen'` (Capacitor) or universal link handler (RN) in `src/**/*.ts`.
Verify routing logic handles:
- App already open (foreground navigation)
- App in background (resume + navigate)
- App cold start (navigate after init)
- Unrecognized paths (fallback to home — no crash)

---

## PHASE 3 — PUSH NOTIFICATION AUDIT

### 3a — Firebase Cloud Messaging Config
Use `grep_search` for `google-services.json` and `GoogleService-Info.plist` in project root / `android/app` / `ios/App`.
**CRITICAL**: Verify production (not debug) FCM config is used in release builds.
Verify `google-services.json` is in `.gitignore` — never committed.

### 3b — APNS Configuration (iOS)
Verify in App Store Connect:
- Push Notifications capability is enabled
- APN key or certificate is uploaded and not expired
Check `ios/App/App.entitlements` for `aps-environment` = `production` (not `development`) in release builds.

### 3c — Permission Request UX
Use `grep_search` for `PushNotifications.requestPermissions` in `src/**/*.ts`.
Verify:
- Permission is requested at a contextually appropriate point (NOT on cold app launch)
- A pre-permission rationale dialog explains the value to the user before the native system dialog
- Denial is handled gracefully (no repeat nagging)

### 3d — Notification Payload Security
Use `grep_search` for `notification.body` or `FCM` payload construction in `functions/src/**/*.ts`.
Verify push payloads do NOT include:
- Sensitive user data (PII, auth tokens, financial data)
- Internal IDs that could aid enumeration attacks
Notification body → marketing-safe, user-facing text only.

---

## PHASE 4 — SPLASH SCREEN & COLD START AUDIT

### 4a — Splash Screen Configuration
Use `grep_search` for `SplashScreen` in `capacitor.config.ts` or `ios/App/App/Info.plist`.
Verify:
- `launchShowDuration`: 0–2000ms (not > 3000ms — Apple rejects long splash delays)
- `backgroundColor` matches brand primary color (no white flash on dark-themed apps)
- `androidSplashResourceName` points to correct vector drawable (not deprecated bitmap)

### 4b — Cold Start Performance
If dev server is running, use `mcp_chrome-devtools_performance_start_trace` on the web layer.
For native cold start timing, check Firebase Performance SDK integration:
Use `grep_search` for `@firebase/performance` or `FirebasePerformance` in `src/**/*.ts`.
Target: **< 3 seconds** to interactive from cold launch.
If Firebase Perf is absent → flag as P2 (add `firebase/performance` to Capacitor app).

### 4c — Launch Screen White Flash Check
Use `browser_subagent` to load app at mobile viewport with CPU throttle 4x.
Screenshot immediately after navigation. Verify no bare white/blank frame appears before content load.
Fix: ensure Tailwind or CSS root background color is set in `html` or `body`, not only in React components.

---

## PHASE 5 — MOBILE SECURITY AUDIT

### 5a — HTTPS + TLS Enforcement
Use `grep_search` for `http://` (not `https://`) in `src/**/*.ts` and `functions/src/**/*.ts`.
Any non-HTTPS endpoint in production code → P0 blocker. Fix immediately.
Exception: `http://localhost` dev server references — flag as ignored.

### 5b — Native Secrets Storage
Use `grep_search` for API keys or tokens hardcoded in `capacitor.config.ts`, `AndroidManifest.xml`, or `Info.plist`.
**CRITICAL**: Zero tolerance. All secrets → Secret Manager or env injection at build time.
Verify Capacitor HTTP plugin uses `Authorization: Bearer` headers, never query string tokens.

### 5c — Permissions Minimization
Use `grep_search` for `<uses-permission` in `AndroidManifest.xml`.
For each listed permission, verify it is actively used in the codebase:
- `CAMERA` → only if camera feature exists
- `READ_CONTACTS` / `WRITE_CONTACTS` → only if contacts feature exists
- `ACCESS_FINE_LOCATION` vs `ACCESS_COARSE_LOCATION` → request only what's needed
Unused permissions → remove immediately. This is a P1 rejection risk on Google Play.

### 5d — iOS Privacy Manifest (`PrivacyInfo.xcprivacy`)
Use `grep_search` for `PrivacyInfo.xcprivacy` in `ios/`.
Verify the file exists and accurately declares:
- All accessed required reason APIs (e.g., `NSPrivacyAccessedAPICategoryUserDefaults`)
- Data collected by the app and each bundled third-party SDK
Missing or incomplete privacy manifest → **App Store rejection since May 2024**.

---

## PHASE 6 — NATIVE PERFORMANCE AUDIT

### 6a — Firebase Performance Integration
Use `grep_search` for `getPerformance` or `FirebasePerformance` in `src/**/*.ts`.
If present → verify custom traces exist for key flows (login, data load, navigation).
If absent → add as P2 recommendation.

### 6b — Frame Rate & Jank Check
Use `browser_subagent` to navigate the app at `390x844,mobile,touch` viewport with CPU throttle 4x.
Scroll through main feed/list view. Check `mcp_chrome-devtools_list_console_messages` for:
- `Forced reflow` warnings
- Frame drop indicators
Any animation running `top/left/width/height` → convert to `transform/opacity` (GPU layer).

### 6c — WebView Memory Budget
For Capacitor apps, the WebView has a lower memory budget than native code.
Use `mcp_chrome-devtools_take_memory_snapshot` during typical usage flow.
Target: **< 150MB** retained heap. > 200MB → P1 memory audit required.
Flag any retained DOM nodes > 1000 in the snapshot summary.

### 6d — Network Payload Budget
Use `mcp_chrome-devtools_list_network_requests` on initial load.
Total transferred payload target: **< 1MB on first load** (mobile network budget).
Any individual JS chunk > 300KB → flag for code splitting.

---

## PHASE 7 — PRIVACY & STORE COMPLIANCE

### 7a — Data Collection Disclosure
Verify App Store Connect `App Privacy` section accurately reflects:
- Data types collected (name, email, device ID, usage data)
- Whether data is linked to identity
- Whether data is used for tracking
Cross-reference with what Firebase Analytics, Crashlytics, or FCM actually collect.

### 7b — Age Rating Compliance
Verify the content rating in Play Console and App Store Connect is appropriate.
Check for any user-generated content, gambling, or explicit material claims.

### 7c — GDPR / Privacy Policy
Use `grep_search` for privacy policy URL in `src/**/*.ts` or `capacitor.config.ts`.
Verify:
- Privacy policy URL is live and accessible
- Policy accurately describes data collected by the app
- GDPR consent flow exists for EU users (cookie/tracking consent)

---

## PHASE 8 — APP STORE ASSET READINESS

### 8a — App Icon Audit
Use `grep_search` for app icon in `android/app/src/main/res/` and `ios/App/App/Assets.xcassets/`.
Verify:
- iOS: All required sizes present (`20pt`, `29pt`, `40pt`, `60pt`, `76pt`, `83.5pt`, `1024pt`)
- Android: All densities present (`mdpi`, `hdpi`, `xhdpi`, `xxhdpi`, `xxxhdpi`)
- No transparency in iOS icons (App Store requirement — transparent areas rejected)
- Foreground icon visible against both light and dark wallpapers

### 8b — Screenshot Readiness
Verify screenshots are prepared for:
- **iOS**: iPhone 6.7" (iPhone 15 Pro Max), iPhone 6.1" (iPhone 15), iPad 12.9" (if iPad supported)
- **Android**: Phone (various aspect ratios), Tablet 7", Tablet 10" (if tablet supported)
Screenshots must NOT contain:
- Placeholder or test data
- Device bezels that don't match the declared device
- Price or promotional text that misrepresents the app

### 8c — Release Metadata
Verify in App Store Connect / Play Console:
- Version number is higher than last approved version
- "What's New" section accurately describes current release changes
- Support URL and marketing URL are live
- Content rating questionnaire is completed and accurate

---

## PHASE 9 — WEB VIEWPORT & SERVER AUDIT (Existing)

### 9a — Dev Server Check
// turbo
```bash
lsof -ti:3000 2>/dev/null | head -3 || echo "no dev server detected"
```
If not running → start:
```bash
NODE_OPTIONS=--max-old-space-size=4096 npm run dev &
```
Wait 8 seconds.

### 9b — Viewport Emulation Setup (MCP)
Use `mcp_chrome-devtools_emulate` with viewport `390x844,mobile,touch` (iPhone 15 viewport).

---

## PHASE 10 — MOBILE RESPONSIVE AUDIT (Web Layer)

### 10a — Viewport Meta Check
Use `grep_search` for `viewport` in `src/app/layout.tsx` or `public/index.html`.
Must contain: `<meta name="viewport" content="width=device-width, initial-scale=1">`.
Missing → **auto-inject** immediately.

### 10b — Touch Target Audit (Critical Law)
Use `browser_subagent` to navigate with mobile viewport.
Verify every button, link, and input has minimum **44x44px** touch target.
Any target smaller → auto-apply `min-height: 44px; min-width: 44px` in CSS.
Log: `🔧 [AUTO-FIXED] Touch target: [element] in [component]`

### 10c — Horizontal Scroll Check
Use `mcp_chrome-devtools_evaluate_script` with:
```javascript
() => document.body.scrollWidth > window.innerWidth
```
Returns `true` → horizontal overflow detected. Fix root cause + add `overflow-x: hidden`.

### 10d — Fixed Element Audit
Use `grep_search` for `position: fixed` and `position: sticky` in `src/**/*.css,src/**/*.tsx`.
Each fixed element → verify it does NOT obscure content on mobile.

---

## PHASE 11 — MOBILE LIGHTHOUSE + PERFORMANCE (Web Layer)

### 11a — Mobile Lighthouse
Use `mcp_chrome-devtools_lighthouse_audit` with `device: "mobile"` and `mode: "navigation"`.

### 11b — Score Analysis

| Metric | Score | Target | Action |
|---|---|---|---|
| Performance | | ≥ 75 mobile | |
| Accessibility | | ≥ 95 | |
| Best Practices | | ≥ 90 | |
| SEO | | ≥ 95 | |

### 11c — CLS Audit
Use `mcp_chrome-devtools_performance_analyze_insight` for CLS-related insights.
Any CLS > 0.1 → investigate skeleton states, image dimensions, font loading order.

### 11d — Animation GPU Audit
Use `grep_search` for `transition:` in `src/**/*.css` and `src/**/*.tsx`.
Prefer `transform` and `opacity` (GPU-composited). Convert `top/left/width/height` to transform-based.

### 11e — Image Loading
Use `grep_search` for `<img` in `src/**/*.tsx` without `loading="lazy"` → add it.
Each `<Image>` component → verify `sizes` prop for responsive behavior.

---

## PHASE 12 — MULTI-VIEWPORT TESTING (Eye of Zoltan)

### 12a — iPhone SE (375px — smallest common)
Use `mcp_chrome-devtools_emulate` with viewport `375x667,mobile,touch`.
Use `browser_subagent` to screenshot all key pages.

### 12b — iPhone 15 Pro (393px — current standard)
Use `mcp_chrome-devtools_emulate` with viewport `393x852,mobile,touch`.

### 12c — iPad (768px — tablet transition)
Use `mcp_chrome-devtools_emulate` with viewport `768x1024,mobile,touch`.
Confirm layout switches from mobile columns to tablet grid correctly.

### 12d — Desktop (1440px — full width)
Use `mcp_chrome-devtools_emulate` with viewport `1440x900`.
Confirm max-width containers are centered and not stretching.

---

## PHASE 13 — ACCESSIBILITY & NETWORK AUDIT

### 13a — Touch Focus State
Use `grep_search` for `:focus` in `src/**/*.css`.
Focus states must be visible (ring/outline, contrast ≥ 3:1).

### 13b — Screen Reader Labels
Use `grep_search` for `aria-label` in `src/**/*.tsx`.
Icon-only buttons without `aria-label` → add descriptive labels.

### 13c — Slow 4G Test
Use `mcp_chrome-devtools_emulate` with `networkConditions: "Slow 4G"`.
Use `browser_subagent` to navigate and measure time to interactive + skeleton quality.

### 13d — Offline Behavior
Use `mcp_chrome-devtools_emulate` with `networkConditions: "Offline"`.
Confirm: service worker offline page or meaningful error state (no blank white screen).

### 13e — Console + Network Errors
Use `mcp_chrome-devtools_list_console_messages` with types `["error", "warn"]`.
Use `mcp_chrome-devtools_list_network_requests` — filter for status >= 400.

---

## PHASE 14 — FINAL REPORT (MANDATORY — DO NOT SKIP)

Generate a truth table at the end of the audit:

```
╔══════════════════════════════════════════════════════════════╗
║        MOBILE AUDIT REPORT — [APP NAME] — [DATE]            ║
╠═══════════════════════════════════════╦═══════════╦══════════╣
║  Gate                                 ║  Result   ║  Status  ║
╠═══════════════════════════════════════╬═══════════╬══════════╣
║  WORKSPACE_PHASE                      ║  [X]      ║          ║
║  PROTOCOL_PHASE                       ║  [Y]      ║          ║
║  PHASE_GAP                            ║  [Y-X]    ║          ║
╠═══════════════════════════════════════╬═══════════╬══════════╣
║  Native Build Config (P1: Android)    ║           ║          ║
║  Native Build Config (P1: iOS)        ║           ║          ║
║  Deep Linking (Universal / AppLinks)  ║           ║          ║
║  Push Notifications (FCM / APNs)      ║           ║          ║
║  Splash Screen / Cold Start           ║           ║          ║
║  Security (HTTPS, Secrets, Perms)     ║           ║          ║
║  Privacy Manifest (iOS)               ║           ║          ║
║  App Store Assets                     ║           ║          ║
║  Web Viewport (Lighthouse)            ║           ║          ║
║  Accessibility                        ║           ║          ║
║  Offline / Network                    ║           ║          ║
╠═══════════════════════════════════════╬═══════════╬══════════╣
║  CRITICAL BLOCKERS (must fix)         ║  [N]      ║          ║
║  P1 ISSUES (fix before launch)        ║  [N]      ║          ║
║  P2 ISSUES (fix before next release)  ║  [N]      ║          ║
╠═══════════════════════════════════════╬═══════════╬══════════╣
║  OVERALL MOBILE SOVEREIGN STATUS      ║           ║  [🟢/🔴] ║
╚═══════════════════════════════════════╩═══════════╩══════════╝
```

For any ❌ gate, display an auto-heal repair block:
```
┌─ 🔧 AUTO-HEAL: [Gate Name] ────────────────────────┐
│ Issue: [what failed]                                 │
│ Auto-fix: [what was attempted]                       │
│ Result: [success / manual required]                  │
│ Manual Fix: [exact command or file edit]             │
│ Type "fix [gate]" to re-run this gate.               │
└──────────────────────────────────────────────────────┘
```

---

## ⚡ Reset Viewport & Phantom Purge

Use `mcp_chrome-devtools_emulate` with viewport `1440x900` to reset to desktop.
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Mobile audit sealed. Submit to test flight / internal track when all P0/P1 gates are green.`
