---
description: The Absolute Sovereign Design Protocol — Dark Mode Integrity, Lexical Mapping, and Visual Splendor
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /design
## The Architect's Decree: Visual Splendor, Thematic Integrity, and Aesthetic Sovereignty

> ⚡ **MANDATE**: The User Interface is the ultimate manifestation of the Infinity Protocol. A flat, lifeless, or poorly elevated DOM is considered a hostile structural failure. This workflow enforces the direct visual decrees issued by the Agency Owner, mapped directly from the Sovereign Brain.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest these skills** via `view_file` on each `SKILL.md` before proceeding:
1. `.agent/skills/liquid-glass-ui/SKILL.md` — Glassmorphism, Framer Motion, dark-mode component architecture
2. `.agent/skills/sovereign-aesthetic-auditor/SKILL.md` — FOUC detection, palette compliance, visual regression

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` to guarantee the workflow runs on a v10.0 synced environment.

### Phase 0b — Poison CSS Token Purge
Before any design execution, run a `grep_search` across `src/**/*.tsx` and `src/**/*.css` for poison design tokens.
> ⛔ **BANNED TOKENS**: `slate-`, `zinc-`.
If these flat, legacy tokens exist, they MUST be purged. You will transition all gray scales to the Premium Blue-Tinted Charcoal palette (`neutral-`, specifically matching the `#030712` base logic).

### Phase 0c — Liquid Glass Standard Constants
Strict volumetric depth enforcement must be maintained:
- **Shadows**: Base element shadows must use `shadow-2xl shadow-black/40` to project depth, never flat 0 opacity. 
- **Borders**: All structural boundaries must be translucent: `border-white/5` or `border-neutral-200/50`. Absolute colors like `border-gray-500` are banned.
- **Radii**: Employ `rounded-2xl`, `rounded-[24px]`, or `rounded-full` for all bounding containers.

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

---

## SECTOR 6 — Conversational Interface Architecture (Chat UI Mastery)

> ⚡ **MANDATE**: The LLM Chat interface is the brain's manifestation. Default widget templates are insulting. 

### 6a — Message Bubble Sovereignty
- **Agent Bubbles**: Must possess structural depth. Employ `bg-white/[0.04] backdrop-blur-xl border border-white/[0.08]` in dark mode. Flat `bg-gray-200` blocks are strictly forbidden.
- **User Bubbles**: Must utilize the core system accent (e.g., `bg-brand-primary` or a distinct gradient) paired closely with `shadow-[0_0_15px_rgba(var(--brand-primary),0.3)]` so user input physically glows over the background.

### 6b — The Interface Shell (Input & Frame)
- **Chat Input Frame**: Must NOT be a harsh solid rectangle. Enforce a floating, pill-shaped design utilizing `rounded-full` or `rounded-[32px]` with `border-white/10` and deep internal shadow `inset 0 1px 2px rgba(0,0,0,0.2)`. 
- **Micro-Typography**: Component labels, timestamps, and typing indicators must strictly be sized at `text-[10px]`, weighted `font-black`, and spaced `tracking-[0.2em] uppercase`.

---

## SECTOR 7 — Ambient Luminous Fields (Peripheral Glow)

> ⚡ **MANDATE**: A true Liquid Glass matrix must emit its own ambient light. Flat objects sitting on a void are disconnected.

### 7a — Sub-Surface Scattering (Background Blurs)
Key layout focal points (Primary CTA, Hero Headers, Dashboard metrics) MUST be backed by an ambient luminous field. 
- Ensure a structural underlying div employing `absolute -z-10 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-brand-primary/20 to-transparent blur-[120px]` exists behind critical sections to visually float the content above the `#030712` floor.

---

## SECTOR 8 — Scrollbar & Overflow Sovereignty

### 8a — Eradication of System Scrollbars
Native OS scrollbars shatter the illusion of a dimensional UI.
- All horizontally scrolling element arrays (e.g. Chat Chips, Carousels) MUST utilize `scrollbar-hide` (or equivalent `.no-scrollbar` CSS) to maintain unbroken borders.
- Vertical page scrollbars MUST be custom-profiled if visible, employing a dark track `bg-neutral-950` with a translucent thumb `bg-white/10 hover:bg-brand-primary/50`.

### 8b — Overflow Masking
Mask edges of scrollable content matrices utilizing linear gradients to fade them smoothly into the background, preventing harsh cut-offs at container bounds (`mask-image: linear-gradient(to_bottom, black_80%, transparent)`).

---

## SECTOR 9 — Typography Fluidity & Structural Balance

### 9a — The Death of Ragged Text
- All massive headers (`<h1>`, `<h2>`, `<header>`) MUST utilize `text-balance` to eradicate typographic widows and orphan lines.
- All body text and massive readable copy (`<p>`, `<blockquote>`) MUST utilize `text-pretty` (in Tailwind 3.4+) to fluidly stabilize wrapping.

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 UI Architecture solidified. The Aesthetic Sovereign is satisfied.`
