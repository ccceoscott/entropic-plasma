---
description: End-of-session sealing protocol (R.A.P.S.) — run before ending any work session or handing off to a new model
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 (R.A.P.S.) — /session_end
## Sovereign Session Sealing Protocol — Localized

> ⚡ **MANDATE**: Every session must be sealed with full state persistence locally into `MISSION_STATE.md`. The Remote Brain is DEPRECATED.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` before proceeding:
1. `.agent/skills/git-commit-formatter/SKILL.md` — Semantic commit messages, changelog generation, Infinity Protocol tagging

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY

### Phase 0a — Protocol Sync
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```

### Phase 0b — TypeScript Seal Check
// turbo
```bash
cd functions && NODE22_PATH NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```

---

## STEP 1 — Full Local Accomplishment Synthesis
1. Use `read_file` on `MISSION_STATE.md`.
2. Extract all completed goals using `read_file` on `task.md`.
3. Synthesize the findings locally.

---

## STEP 2 — Security & Poison String Final Sweep
Use `grep_search` across `src/` and `functions/src/`:
- Patterns: `AIza`, `sk-`, `PROTOCOL_PASSPHRASE\s*=\s*[^$]`, `apiKey:\s*['"]`
- Poison Strings: `CareKey`, `FirstPick`, `SARAH`, `Soul Contract`, `epi-hab`

---

## STEP 3 — Knowledge Item Generation (R.A.P.S Codex)
> ⚡ **LAW**: Write all persistent memory to `~/.gemini/antigravity/knowledge/`.
If the session involved architectural changes, complex fixes, or new patterns:
1. Generate an Antigravity Artifact natively and write it to the `knowledge/` directory.

---

## STEP 4 — MISSION_STATE.md Full Update
Update `MISSION_STATE.md` using file edit tools to reflect newly completed tasks and the NEXT entry point.

---

## STEP 5 — Walkthrough.md Generation
Generate `walkthrough.md` mapping the results of this session.

---

## STEP 6 — Git Staging & Commit
### 6a — Status
// turbo
```bash
git status --short && git diff --stat HEAD
```

### 6b — Commit
// turbo
```bash
git add -A && git commit -m "seal: Phase [N] session end (R.A.P.S.) — [accomplishment summary]"
```

### 6c — Auto-Push
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 45 git push origin main 2>&1 | tail -5
```

---

## 📋 COMMAND SEAL (R.A.P.S.)

Output:
```
╔══════════════════════════════════════════════════════════════════╗
║  SESSION END REPORT (R.A.P.S) — [PROJECT_NAME]                   ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

WORKSPACE_PHASE : [Phase]

┌─────────────────────────────┬────────┬─────────────────────────────┐
│ Seal Gate                   │ Status │ Notes                       │
├─────────────────────────────┼────────┼─────────────────────────────┤
│ TypeScript (functions)      │ ✅/❌  │ [0 errors / N errors]       │
│ Security Scan               │ ✅/❌  │ [clean / N issues]          │
│ MISSION_STATE Updated       │ ✅/❌  │ [sealed at phase N]         │
│ Git Push                    │ ✅/❌  │ [pushed origin/main]        │
└─────────────────────────────┴────────┴─────────────────────────────┘

OVERALL: [🟢 SEALED / 🔴 BLOCKED]
```

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
