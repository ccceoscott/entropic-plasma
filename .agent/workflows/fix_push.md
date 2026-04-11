---
description: Sovereign git push protocol — run_command git push is BANNED, always use paste command
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /fix_push
## Sovereign Git Push Protocol — Law 3 Enforcement

> ⚡ **LAW 3 ABSOLUTE**: `git push` via `run_command` is BANNED. SSH/HTTPS in non-interactive shells is a guaranteed hang vector that locks the terminal. This workflow provides the sovereign safe alternative.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Check
Use `view_file` on `MISSION_STATE.md` → verify current phase is current.
If stale → run (0b). If current → proceed.

### Phase 0b — Auto-Upgrade
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -5
```

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -5
```

---

## SSOT INGESTION (Before All Checks)

Use `view_file` on `MISSION_STATE.md` — confirm project identity.
Use `view_file` on `.firebaserc` — confirm project: `gen-lang-client-0386732425`.

---

## SECTOR 1 — Pre-Push Security Gate

### 1a — Secret Scan (MCP)
Use `grep_search` with the following patterns (one at a time):
- `AIzaSy` in `/Users/teknojunkeee/Developer/infinity-protocol-1/src`
- `AAAA` (Firebase Server Key prefix) in `src`
- `sk-` (OpenAI) in `src`
- `private_key` in `functions/src`
- `.env` in git staging

Any match outside of `.env.example` or `*.example.*` → **HALT**. Do not expose secrets.

### 1b — Poison String Scan (MCP)
Use `grep_search` for these strings across the entire project:
- `CareKey`, `FirstPick`, `SARAH`, `Soul Contract`, `epi-hab`

Any match in project code → **HALT**. Cross-project bleed detected.

### 1c — Project Identity Dual Verification
Key 1 — local:
// turbo
```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)"
```

Key 2 — Verify MCP Binding:
Use `mcp_firebase-mcp-server_firebase_get_environment` → must show `gen-lang-client-0386732425`.

Both must output `gen-lang-client-0386732425`. Mismatch → **HALT**.

---

## SECTOR 2 — Branch & Commit Verification
// turbo
```bash
git status --short && git branch --show-current && git log --oneline -5
```
Verify:
- Working tree has only expected changes
- Current branch is correct (not `main` if work is in progress)
- Last 5 commits are from this project

If untracked sensitive files exist → add to `.gitignore` before staging.

---

## SECTOR 3 — Stage & Commit (Auto-runnable)
// turbo
```bash
git add -A && git status --short
```
Verify staged files look correct. No `.env.local`, no `*.pem`, no credentials.

COMMIT — provide message based on actual changes:
// turbo
```bash
git commit -m "feat: [DESCRIBE ACTUAL CHANGE] — Infinity Protocol v10.0"
```

---

## SECTOR 4 — THE SOVEREIGN PASTE COMMAND (Law 3)

> **NEVER auto-run push. ALWAYS give the user a paste command.**

After commit is confirmed, display this exact block to the user:

```
🚀 SOVEREIGN PUSH COMMAND — Paste in your terminal:

GIT_TERMINAL_PROMPT=0 timeout 45 git push origin [BRANCH_NAME]

Replace [BRANCH_NAME] with: $(git branch --show-current)
```

Then wait for user to confirm push succeeded before proceeding.

---

## SECTOR 5 — Post-Push Verification (After user confirms)

// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 15 git log --oneline origin/[BRANCH]..HEAD 2>/dev/null | wc -l || echo "verify remotely"
```
0 lines → push succeeded (local HEAD matches remote).
Lines remaining → push may have failed — re-issue paste command.

---

## Knowledge Base Persistence (R.A.P.S)
Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Commit hash and branch pushed
- Any security blocks triggered (for pattern learning)

---

## SECTOR 7 — MISSION_STATE.md Update
Use `view_file` then `replace_file_content` on `MISSION_STATE.md`:
- Update `Last Commit:` field with commit message and hash
- Update `Last Push Attempt:` with timestamp

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Sovereign push protocol sealed. Law 3 honored.`
