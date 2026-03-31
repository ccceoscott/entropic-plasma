---
description: The Antigravity Memory Compactor (Phase 57 Sovereign — Precision Hang Guards)
---

# /finalize_session — The Antigravity Memory Compactor (Phase 57)

Run this workflow at the very end of every session to compress ephemeral Working Memory into permanent **KI disk storage**, update `MISSION_STATE.md`, purge bloat, and sync to the cloud.

> **⚠️ PHASE 57 PRECISION LAW — What is BANNED vs ALLOWED:**
>
> | Operation | Status | Reason |
> |---|---|---|
> | `gcloud auth print-identity-token` | ❌ BANNED | Network call — hangs without timeout |
> | `gcloud config get-value project` | ❌ BANNED | Hangs in non-interactive shells |
> | `git fetch` without guards | ❌ BANNED | SSH passphrase hang |
> | `npx playwright` | ❌ BANNED | Video bloat + zombie respawn |
> | `rm -rf` via `run_command` | ✅ ALLOWED | Local-only, instant, no hang risk |
> | `curl --max-time N` via `run_command` | ✅ ALLOWED | Bounded network call — safe |
> | `write_to_file` / `view_file` / `grep_search` | ✅ PREFERRED | MCP tools — zero terminal overhead |
>
> `// turbo-all` is REMOVED from this workflow — it caused the 3-phantom-command crisis.

---

## 1. 🧠 MISSION_STATE Update (File Tool — NO terminal)

Use `write_to_file` or `multi_replace_file_content` to update `MISSION_STATE.md`.

**Template fields to fill:**
- Version bump (e.g. v10.0.11)
- Completed Goals list
- Current Objectives
- Any new Blockers

> **NEVER** use `run_command` to write MISSION_STATE. Use `view_file` to read, `write_to_file` to write.

---

## 2. ☁️ KI Disk Write (write_to_file)

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

---

## 3. ☁️ Cloud Run Sync (run_command — bounded, safe)

Sync the KI to the Cloud Run memory hub using a bounded curl call:

```bash
curl -s --connect-timeout 5 --max-time 10 \
  -X POST "https://savesessionmemory-g5pod66w5a-uc.a.run.app/save" \
  -H "Content-Type: application/json" \
  -d "{\"project\":\"PROJECT_NAME\",\"summary\":\"BRIEF_SUMMARY\"}" \
  2>/dev/null || echo "[WARN] Cloud sync skipped (cold start or unreachable)"
```

// turbo

> This is a **bounded** network call (10s max). It is safe to run via `run_command`. If it fails, the KI disk write in step 2 is the authoritative fallback.

---

## 4. 🧹 Phantom Purge (run_command — local only, instant)

// turbo
Run these automatically — they are local-only `rm` operations, not network calls:

```bash
rm -rf ~/.gemini/antigravity/browser_recordings/ ~/.npm/_npx/
```

> **Safe to auto-run.** No network, no stdin, no hang risk. Duration: <100ms.

---

## 5. ✅ Confirmation (in chat response)

State in your chat response:
> "Session finalized. MISSION_STATE v[X] updated. KI written to disk. Cloud sync attempted. Bloat purged."

*Status: Sovereign. Precise guards. No overkill. No hangs.*
