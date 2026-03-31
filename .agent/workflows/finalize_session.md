---
description: The Antigravity Memory Compactor (Phase 57 Sovereign — Zero Terminal Hangs)
---

# /finalize_session — The Antigravity Memory Compactor (Phase 57)

Run this workflow at the very end of every session to compress ephemeral Working Memory into permanent **KI disk storage** and update `MISSION_STATE.md`.

> **⚠️ PHASE 57 SOVEREIGN LAW — MANDATORY:**
> - `run_command` is **BANNED** in this entire workflow. Use file tools only.
> - `gcloud auth print-identity-token` = network call with no timeout → SKIP entirely
> - `tail`, `echo`, `bash` via terminal = phantom hang risk → BANNED
> - Cloud Run endpoint sync = optional. Use `write_to_file` KI fallback ALWAYS.
> - `// turbo-all` is REMOVED from this workflow — it caused the 3-phantom-command crisis.

---

## 1. 🧠 MISSION_STATE Update (File Tool — NO terminal)

Use `write_to_file` or `multi_replace_file_content` to update `MISSION_STATE.md`.

**Template fields to fill:**
- Version bump (e.g. v10.0.11)
- Completed Goals list
- Current Objectives
- Any new Blockers

> **NEVER** use `run_command` to read or write MISSION_STATE. Use `view_file` to read, `write_to_file` to write.

---

## 2. ☁️ KI Disk Write (write_to_file — NO terminal, NO gcloud)

Write the session KI directly to disk using the `write_to_file` tool:

**Target path:** `~/.gemini/antigravity/knowledge/<ki_name>/artifacts/<session>.md`

**KI template:**
```markdown
# <Project> — Phase <N> Session Summary

## Completed Goals
- Goal 1
- Goal 2

## Key Patterns Established
- Pattern / law / rule discovered

## Blockers Resolved
- What was blocked and how it was fixed

## Sovereign Laws Added (if any)
| Law | Rule |
|---|---|
| ... | ... |
```

> Cloud Run sync (`savesessionmemory-g5pod66w5a-uc.a.run.app`) is **optional** and must NEVER be run via `run_command`. If you want cloud sync, use a python3 `subprocess.run` with `timeout=8` invoked in a future session's terminal — not here.

---

## 3. 🧹 Phantom Purge (USER runs manually in their terminal)

Tell the user to run these two lines in their OWN terminal:

```
rm -rf ~/.gemini/antigravity/browser_recordings/
rm -rf ~/.npm/_npx/
```

> **DO NOT** use `run_command` to run these. The user must run them manually.

---

## 4. ✅ Confirmation (in chat response — NOT terminal)

Simply state in your chat response:
> "Session finalized. MISSION_STATE updated. KI written to disk. Phantom purge: run `rm -rf ~/.gemini/antigravity/browser_recordings/` in your terminal."

*Status: Sovereign. No terminal. No hangs. No phantoms.*
