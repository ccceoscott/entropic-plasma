---
description: The Absolute Sovereign Design Protocol — Dark Mode Integrity, Lexical Mapping, and Visual Splendor
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /design
## The Architect's Decree: Visual Splendor, Thematic Integrity, and Aesthetic Sovereignty

> ⚡ **MANDATE**: The User Interface is the ultimate manifestation of the Infinity Protocol. A flat, lifeless, or poorly elevated DOM is considered a hostile structural failure. This workflow enforces the direct visual decrees issued by the Agency Owner, mapped directly from the Sovereign Brain.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` to guarantee the workflow runs on a v10.0 synced environment.

### Phase 0b — Poison CSS Token Purge
Before any design execution, run a `grep_search` across `src/**/*.tsx` and `src/**/*.css` for poison design tokens.
> ⛔ **BANNED TOKENS**: `slate-`, `zinc-`.
If these flat, legacy tokens exist, they MUST be purged. You will transition all gray scales to the Premium Blue-Tinted Charcoal palette (`neutral-`, specifically matching the `#030712` base logic).

---

## SECTOR 1 — Premium Dark Mode Elevation (Liquid Glass v2)

### 1a — The Avoidance of Flatness
A purely `#000000` or `#111111` flat black screen is prohibited.
Dark mode architecture MUST employ layered elevations:
- **Base Level / Floor**: `bg-neutral-950` with subtle radial gradients for depth.
- **Card Level 1**: `bg-neutral-800/50` combined with `backdrop-blur-md`.
- **Interactive Elevated Level 2**: `bg-neutral-800/80` or `color-mix(in srgb, var(--color-surface) 90%, white)`.

### 1b — High-Fidelity Micro-Interactions
Use `grep_search` for `transition` rules. 
- Fast, jarring `0.1s` hover states are forbidden.
- Interactive states MUST utilize smooth `0.3s` to `0.5s` easing curves for padding, transform, and background shifts. `duration-300` or `duration-500` mixed with `ease-out` are required.

---

## SECTOR 2 — Global Stacking Sovereignty (Z-Index Hierarchy)

> **Law 19 (Stated Context)**: Unmanaged Z-Indexes lead to header overlap and modal catastrophe. 

### 2a — The Absolute Z-Map
Scan the application for rigid adherence to the Stacking Order:
- `z-0` to `z-10` — Backgrounds, Particles, and Base Elements.
- `z-20` to `z-30` — Floating cards and relative elevated elements.
- `z-40` — Fixed Navigation Headers, Sticky Topbars.
- `z-50` — Overlays, Backdrop Blurs (e.g. `fixed inset-0 bg-black/60 backdrop-blur-sm`).
- `z-50` to `z-60` — Modals (The "Sacred Credit Exchange" / Shop Modals / Auth Modals).
- `z-70` — Toasts, Snackbars, and Sovereign Alerts.

Use `grep_search` for any rogue `z-50` headers that might collide with `z-50` modals. Resolve them instantly.

---

## SECTOR 3 — Mobile Fluidity & Frictionless UX

### 3a — Safe Area Constraints
Fixed modals (e.g., the 92vh Shop Modal) and full-screen sheets MUST map to `env(safe-area-inset-top)` and `env(safe-area-inset-bottom)`.
Use padding classes like `py-10 pb-[env(safe-area-inset-bottom)]` to prevent clipping the iPhone Dynamic Island and Home Bar.

### 3b — Authenticated "Chart-First" Routing
Enforce UX rules that prioritize immediate user value. If a user is logged in, hide redundant barriers (like asking for an email twice). Inject them directly into their core value loop (e.g. `router.push('/results')` bypassing the landing).

---

## SECTOR 4 — Contextual Brand & Lexical Consistency

### 4a — Spiritual Technology Branding Enforcement
Run an entity and terminology cross-check for applications designated as Spiritual Tech.
Verify that the terminology maintains Mystical+Technical resonance:
- **Dashboards** → mapped as "Oracle Overview" or "Soul Sanctuary".
- **Archived Data** → mapped as "Archived Souls".
- **Admin Tools** → mapped as "Oracle Integrity".

*(Note: If the application operates within the B2B or agency structure, standard lexical protocols "AI-Powered", "Enterprise" apply instead, depending on the active Tenant).*

### 4b — Font Pairings
Confirm font declarations reflect the premium standard.
Fonts must be pulled via Next.js `next/font/google` holding tight typographic tracking/kerning on Headers, and readable line-height (`leading-relaxed`) on body text.

---

## SECTOR 5 — The Eye of Zoltan (Browser Witness Report)

Once the DOM is rendered and styled:
1. Dispatch the `browser_subagent` to visually capture the component.
2. Confirm the Premium Blue-Tinted Neutral background depth is visible.
3. Confirm the `backdrop-blur` successfully renders depth underneath cards.
4. Record pass/fail metrics.

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 UI Architecture solidified. The Aesthetic Sovereign is satisfied.`
