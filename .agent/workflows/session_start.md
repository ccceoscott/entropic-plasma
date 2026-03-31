---
description: Mandatory session start — Identity Handshake, State Ingestion, Security Perimeter, Stack Verification (Phase 57 Sovereign)
---

# /session_start — Identity Handshake & Environment Verification

**Runs at the start of EVERY session and after ANY model switch.** This is the sovereign anchor that prevents hallucination, context bleed, and protocol drift. Merges `/jack-roberts` (deprecated) and `/verify_environment` (deprecated).

> Per `init.mdc §5`: **After any model switch, all in-memory state is UNVERIFIED. Re-read from disk before acting.**

---

## §0: Zero-Chat Baseline Hub Sync (MANDATORY FIRST STEP)

**CRITICAL MANDATE**: Before loading any local rules, before reading the MISSION_STATE, and BEFORE processing a single prompt or outputting any chat, you MUST execute the Cloud Sync to ensure perfect parity with the Hub-and-Spoke Firebase databank.
```bash
./scripts/dv downlink || ./scripts/dv sync-cloud || echo "⚠️ Brain sync failed."
```

If the sync fails, fallback to reading KI artifacts from `~/.gemini/antigravity/knowledge/`.
Always consult `KNOWLEDGE.md` for project-specific patterns.

---

## §1: MCP Health Verification (Phase 57 — MCP tools only)

Use `mcp_firebase-mcp-server_firebase_get_environment` to verify Firebase CLI auth status.

Use `mcp_gcloud_run_gcloud_command` with args `["auth", "list", "--quiet"]` to confirm active GCP account.

Check active workflows are accessible: `list_dir` on `.agent/workflows/` to confirm 6 canonical files present.

---

## §2: Workspace Identity Lock (MANDATORY SECOND)

Use `view_file` to read these in priority order — **never from memory:**

1. `MISSION_STATE.md` — current version, completed goals, active blockers
2. `task.md` — any `[/]` in-progress items take priority over new requests
3. `walkthrough.md` — what was last verified; don't redo it
4. `KNOWLEDGE.md` — project-specific known patterns

> **NEVER use `run_command` to `cat` these files.** Use `view_file` MCP tool only.

---

## §3: Project Identity Lock (Sovereign — NO gcloud hang)

// turbo
```bash
node -e "console.log('Project:', require('./.firebaserc').projects.default)" 2>/dev/null || echo "⚠️ .firebaserc not found — run /bootstrap_new_project"
```

// turbo
```bash
node --version && npm --version
```

// turbo
```bash
grep "NODE_OPTIONS" package.json 2>/dev/null || echo "⚠️ MACHINE LAW VIOLATION: NODE_OPTIONS missing from package.json"
```

// turbo
```bash
ls -la .git/hooks/pre-commit 2>/dev/null || echo "⚠️ Pre-commit hook not installed"
```

---

## §4: Source-First Anti-Hallucination Gate

Before writing ANY code:
- [ ] `view_file` the actual source — NEVER code from memory
- [ ] Verify imports exist in `package.json` via `view_file` or `grep_search`
- [ ] Source field/collection names from `MISSION_STATE.md` — never assume
- [ ] If uncertain: state it explicitly — **never guess confidently**

---

## §5: Secret Perimeter Check

Use `grep_search` MCP tool (non-blocking):
- Query `AIza` in `src/`
- Query `PRIVATE KEY` in repo root

All secrets → Google Cloud Secret Manager via `defineSecret()`. `.env.local` local-only. Never committed.

---

## §6: Stack & Aesthetic Standard

- **Stack**: Next.js App Router + TypeScript + Tailwind CSS + Framer Motion
- **Aesthetic**: Liquid Glass v10.0 — translucent borders, fluid typography, GPU-accelerated keyframes
- **UI**: Radix primitives, curated HSL dark mode, Framer micro-animations
- **Forbidden**: `style={{}}` inline styles, generic colors, grey placeholder boxes

---

## §7: Emit Handshake

After completing all sections above, emit verbatim:

> **"Infinity Protocol v10.0 Active: In [PROJECT_NAME], resuming from MISSION_STATE.md. Phase [N]. All state verified."**

*Failure to perform this ritual after a model switch is a Protocol violation. There is no excuse for skipping it.*
