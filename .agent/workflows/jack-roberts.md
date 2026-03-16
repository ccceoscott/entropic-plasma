---
description: Google Antigravity Global Rules
---
# Jack Roberts (Google Antigravity) Protocol

This workflow codifies the operating rules and identity alignment for the Google Antigravity AI agent (Antigravity/Gemini). Run this at the start of any session to ensure the agent is properly initialized.

## 1. 🔱 Identity Handshake
- [ ] State active project: "Infinity Protocol Active: In [PROJECT_NAME], resuming from [MISSION_STATE.md]."
- [ ] Read `MISSION_STATE.md` (or `MISSION_STATE_INFINITY.md`) to ingest current phase and active goals.
- [ ] Read `task.md` and `walkthrough.md` if present.
- [ ] Confirm no Project Bleed: isolated to current workspace root only.

## 2. 🧠 Context Loading
- [ ] Check Knowledge Items (KI) summaries for relevant prior context before doing any research.
- [ ] Read relevant KI artifacts (use artifact paths from summaries).
- [ ] Identify the active Firebase project and confirm via `firebase_get_environment`.

## 3. 📚 Documentation Policy (Context7)
- [ ] **BEFORE** writing code for any library (Next.js, Firebase, Framer Motion, Shadcn):
    - Call `mcp_context7_resolve-library-id` first.
    - Call `mcp_context7_query-docs` with a specific, targeted query.
    - **NEVER** rely on internal training data for library APIs.

## 4. 🛡️ Security & Boundary Checks
- [ ] Confirm workspace root = `~/Developer/[project-root]` — no execution outside this boundary.
- [ ] Verify no hardcoded secrets. All credentials via `.env.local` or Secret Manager.
- [ ] Check `MISSION_STATE.md` for any active safe-deploy locks.

## 5. 🎨 Aesthetic Standard (Premium Liquid Glass)
- [ ] All UI: Tailwind CSS + Framer Motion. Zero `style={{}}` or vanilla CSS.
- [ ] Color palette: curated HSL dark mode, no generic colors.
- [ ] Animations: Framer Motion micro-interactions on all interactive elements.
- [ ] Images: `generate_image` tool for placeholders — never grey boxes.

## 6. 🚀 Execution Standard
- [ ] Update `MISSION_STATE.md` after EVERY file write or major command.
- [ ] Use optional chaining (`?.`) and null-safe defaults throughout.
- [ ] Run `git status` before any commit. Never force-push main.
- [ ] Self-heal once on failure before escalating to user.
