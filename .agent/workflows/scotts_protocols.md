---
description: Scott's Standard Operating Protocols (God Mode)
---
# Scott's Antigravity God Mode Protocols — v9.0 Apex Sovereign

Codified operating rules for Scott (Constant Concepts). Run at the start of ANY complex session or when switching project contexts.

## 1. 🤝 Identity Handshake (Session Start — Mandatory)

- [ ] Confirm active workspace: `MISSION_STATE.md` must exist at project root
- [ ] Read `MISSION_STATE.md` → extract: current phase, active goals, blockers
- [ ] Read `task.md` → identify in-progress items
- [ ] Perform handshake: *"Infinity Protocol v9.0 Active: In [PROJECT_NAME], resuming from Phase [X]."*
- [ ] If `MISSION_STATE.md` is absent: create it immediately before any other action

## 2. 🛡️ Environment Verification (Before Any Code Changes)

```bash
dv doctor          # 9-point health check — Node, SOVEREIGN_LOCK, cron, git, env vars
dv scan-secrets    # Zero-tolerance key detection (single combined grep pass)
gcloud config get-value project  # Confirm correct Firebase project (no cross-project bleed)
firebase use       # Confirm active Firebase alias
```

- [ ] **CRITICAL**: Never use credentials from one project in another. Isolation is absolute.
- [ ] If `dv doctor` fails: resolve before proceeding. Gate 1 blocks all others.

## 3. 📚 Live Documentation (Context7 Mandate)

- [ ] **BEFORE** writing code for Next.js, Firebase, Framer Motion, Zustand, Radix UI:
    - Query Context7 MCP: `"latest [library] docs for [feature]"`
    - **DO NOT** rely on training data for evolving APIs
- [ ] **Knowledge Items (KIs)** check FIRST: `~/.gemini/antigravity/knowledge/`
    - If KI exists and is current (< 30 days on volatile topics) → use it
    - If KI absent → research via Brave Search + Context7 → create the KI

## 4. 🔥 Live Data Check (Firebase)

- [ ] **BEFORE** guessing a Firestore schema:
    - Use `firebase-mcp-server` to inspect live data
    - `firebase_get_documents` or inspect live collections
    - **NEVER** assume schema from code files alone — schema drift is real

## 5. 🌐 Web Intelligence (Brave Search)

- [ ] Immediately trigger `brave_web_search` when user mentions:
    - A specific error message not seen before
    - A competitor or pricing comparison
    - A recent API change, tech release, or current event
    - Anything where training data could be stale (post-2024)

## 6. 🚀 Execution Protocol (The dv Suite)

```bash
# Standard sovereign flow — run before deploying or when environment is uncertain
dv flow           # Full: purge→doctor→lint-rules→audit-security→broadcast→fleet-commit→locksheet→save→purge
dv flow --fast    # Hub-only: purge→doctor→lint-rules→audit-security→locksheet→save→purge (~15s)

# Targeted commands
dv broadcast      # Push .cursorrules + MDC rules to all 20 workspaces
dv fleet-commit   # Commit broadcast artifacts fleet-wide (surgical, no WIP touched)
dv purge          # Phantom purge after every browser subagent session (MANDATORY)
dv version        # Show SOVEREIGN_LOCK, protocol version, Node, npm at a glance
```

## 7. 🎨 Aesthetic Standard (Liquid Glass v9.0)

- [ ] All UI work must conform to **Liquid Glass v9.0** (glassmorphism, translucency, fluid typography)
- [ ] Stack: **Next.js App Router + TypeScript + Tailwind CSS v4 + Framer Motion**
- [ ] Node: **v22 LTS** | `NODE_OPTIONS=--max-old-space-size=4096` on ALL scripts
- [ ] No generic colors (plain red/blue/green) — HSL-tuned palettes only
- [ ] Use `generate_image` for any placeholder content (no grey boxes)
- [ ] Google Fonts mandatory (Inter, Outfit, Roboto) — no browser defaults

## 8. 🧹 Session Close Protocol

```bash
dv purge           # Phantom purge (Playwright processes + browser_recordings)
# Update MISSION_STATE.md: phase completed, decisions made, next actions
# Update task.md: mark [x] on completed items
```

- [ ] Every session end: `MISSION_STATE.md` updated with decisions + next steps
- [ ] Every browser subagent session: `dv purge` (non-negotiable — gigabyte bloat risk)
