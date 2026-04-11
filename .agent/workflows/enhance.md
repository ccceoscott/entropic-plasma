---
description: Zoltan-Tier aesthetic updates, Liquid Glass enforcement, and micro-animations
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /enhance
## Aesthetic Sovereignty — Liquid Glass v10.0, Framer Motion, Micro-Animations

> ⚡ **MANDATE**: Every visual change is browser-verified via subordinate Eye-of-Zoltan agent before sealing. No untested aesthetic ships.

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

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Errors → auto-fix → re-run.

### Phase 0d — Confirmation
`✅ [UPGRADE GATE PASSED] Enhancement commencing on clean codebase.`

---

## PHASE 1 — Aesthetic Grounding & Target Identification

### 1a — Current State Snapshot (MCP)
Use `browser_subagent` to navigate to `http://localhost:3000` and capture screenshot.
Record: current color palette, animation state, glassmorphism depth.
Store as baseline comparison.

### 1b — KI Aesthetic Feedback Load
Search standard KIs (`~/.gemini/antigravity/knowledge/`) or `KNOWLEDGE.md` for context.
Load user's documented aesthetic preferences — premium dark mode requirements, glassmorphism depth, animation timing preferences.

### 1c — Component Inventory
Use `list_dir` on `src/components/` recursively.
Use `grep_search` for `backdrop-blur` in `src/**/*.tsx` — identify all components with glass effects.
Use `grep_search` for `motion.` in `src/**/*.tsx` — identify all animated components.

### 1d — Aesthetic Violations Scan
Use `grep_search` for declared anti-patterns:
- `background:\s*white` or `bg-white` without opacity → flat anti-pattern
- `color:\s*black` → harsh contrast anti-pattern
- `border-radius: 0` on interactive cards → sharp edges anti-pattern
- `transition: none` on interactive elements → dead animation anti-pattern

For each violation → flag in enhancement queue.

---

## PHASE 2 — Typography Sovereignty

### 2a — Font Verification
Use `view_file` on `src/app/layout.tsx` or equivalent root layout.
Confirm Google Font imports: Inter, or Outfit, or Roboto Mono for code.
Missing → inject `next/font/google` imports immediately.

### 2b — Heading Color Sovereignty
Use `view_file` on global CSS (`globals.css` or `index.css`).
Confirm heading color variables use brand palette (NOT raw `red`, `blue`, `green`).
Pattern: HSL-based, eg: `--color-heading: hsl(220, 85%, 60%)`.
Missing or hardcoded → inject CSS variables and update all heading selectors.

### 2c — Typography Scale Check
Confirm `h1` through `h4` use `clamp()` or `fluid` typography:
`font-size: clamp(1.5rem, 4vw, 3rem)` pattern.
Any fixed pixel headings → convert to fluid.

---

## PHASE 3 — Liquid Glass Enforcement

> **Liquid Glass Standard**: Each glass card must have:
> - `background: rgba(255,255,255,0.04)` to `rgba(255,255,255,0.08)` (dark mode)
> - `backdrop-filter: blur(20px) saturate(180%)`
> - `border: 1px solid rgba(255,255,255,0.08)`
> - `box-shadow: 0 8px 32px rgba(0,0,0,0.3)`

### 3a — Glass Component Audit
For each component with identified glass effects (from 1c):
- Use `view_file` to inspect current glass values
- Missing `saturate()` in backdrop-filter → add immediately
- Opaque background on a "glass" card → fix to translucent rgba

### 3b — Dark Mode Depth Layers
Confirm 3 distinct depth layers in dark mode:
- Layer 0 (deepest bg): `hsl(220, 15%, 8%)`
- Layer 1 (cards): `rgba(255,255,255,0.04)`
- Layer 2 (elevated): `rgba(255,255,255,0.08)`
Any compressed layer system → expand to full 3-layer depth.

---

## PHASE 4 — Framer Motion & Micro-Animations

### 4a — LazyMotion Enforcement
Use `grep_search` for `import { motion }` from `framer-motion` (non-lazy).
For each match → convert to `LazyMotion` + `domAnimation`:
```tsx
import { LazyMotion, domAnimation, m } from 'framer-motion'
// wrap root or component with <LazyMotion features={domAnimation}>
// replace motion.div with m.div etc.
```
Log: `🔧 [AUTO-CONVERTED] [component]: motion → LazyMotion`

### 4b — Enter Animation Audit
Use `grep_search` for `initial={{` in `src/**/*.tsx`.
Confirm enter animations use standard protocol:
```tsx
initial={{ opacity: 0, y: 20 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 0.4, ease: 'easeOut' }}
```
Missing animations on hero/card components → inject.

### 4c — Hover Micro-Animations
Use `grep_search` for `whileHover` in `src/**/*.tsx`.
Interactive cards/buttons without `whileHover` → add:
```tsx
whileHover={{ scale: 1.02, y: -2 }}
transition={{ type: 'spring', stiffness: 300 }}
```

### 4d — Performance Guard
Use `grep_search` for `useAnimation` or `AnimatePresence` — confirm no synchronous animations on critical path.
Confirm no `animate` prop inside a map() with large arrays without `key` prop.

---

## PHASE 5 — Color Palette Sovereignty

### 5a — Anti-Generic Color Audit
Use `grep_search` for raw color names in `src/**/*.css,src/**/*.tsx`:
- `color: red`, `color: blue`, `color: green`, `color: black`, `color: white` (direct)
For each → replace with HSL variable from design system.

### 5b — Gradient Verification
Use `grep_search` for `linear-gradient` in `src/**/*.css,src/**/*.tsx`.
Confirm gradients use 2+ stops with coherent HSL relationship.
Flat single-color "gradients" → replace with actual multi-stop gradient.

### 5c — Brand Color Enforcement
Use `view_file` on design system CSS file.
Confirm:
- Primary: indigo/violet family (`hsl(250, 80%, 60%)`)
- Accent: cyan/teal family (`hsl(185, 70%, 55%)`)
- Surface: dark slate family (`hsl(220, 15%, 8%)` to `hsl(220, 20%, 15%)`)

---

## PHASE 6 — Browser Verification (Eye of Zoltan)

### 6a — Dev Server Check
// turbo
```bash
lsof -ti:3000 2>/dev/null | head -3 || echo "no dev server"
```
If not running → start:
```bash
NODE_OPTIONS=--max-old-space-size=4096 npm run dev &
```
Wait 8 seconds for hydration.

### 6b — Visual Verification
Use `browser_subagent` to:
1. Navigate to `http://localhost:3000`
2. Screenshot above-the-fold
3. Click through to 3 key sections
4. Screenshot each
5. Capture any console errors
6. Report: glass depth visual quality, animation smoothness, color harmony

Compare against KI aesthetic preferences. Report pass/fail per criterion.

### 6c — Mobile Viewport Check
Use `mcp_chrome-devtools_emulate` with viewport `390x844,mobile,touch` (iPhone 14 Pro).
Use `browser_subagent` to screenshot mobile render.
Confirm: touch targets ≥ 44px, no content clipping, fluid typography working.

---

## PHASE 7 — TypeScript Final Verification
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Any errors from Framer Motion additions → fix immediately.

---

## Knowledge Base Persistence (R.A.P.S)

### 8a — Aesthetic Feedback Record (MCP)
Update `KNOWLEDGE.md` with entity details:
- Any new preference observed during this session
- Any component pattern proven successful
- Any anti-pattern eradicated

### 8b — MISSION_STATE Update
Bump phase. Log in `Last Major Accomplishments`.

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Phantom purge complete. Aesthetic enhancement sealed.`
