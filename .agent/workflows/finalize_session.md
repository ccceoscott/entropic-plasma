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

## 3. ☁️ Cloud Sync — DISK IS AUTHORITATIVE

> **ROOT CAUSE FIXED (Phase 57.1):** The previous `curl` pattern sent a raw JSON body to `saveSessionMemory` which is an `onCall` function — not `onRequest`. Firebase `onCall` requires the payload wrapped as `{"data": {...}}` with a Firebase ID token in the `Authorization` header. A raw curl **always** produces a cold-start payload mismatch. This is not recoverable via curl.

**The correct pattern:**

- **KI disk write (Step 2) is the AUTHORITATIVE record.** It never fails and never requires a network call.
- Cloud sync is **deferred** — at the START of the next session, the MCP tool `mcp_firebase-mcp-server_firestore_add_document` or the `saveSessionMemory` onCall function (invoked via the Firebase SDK, not curl) handles persistence.
- **DO NOT attempt curl against onCall endpoints.** They will always mismatch without a valid Firebase ID token.

**If you want to verify cloud sync health**, use the `/ping` endpoint (onRequest — curl-safe):

```bash
curl -s --connect-timeout 5 --max-time 8 \
  "https://mcpserver-g5pod66w5a-uc.a.run.app/ping" \
  2>/dev/null || echo "[WARN] MCP hub unreachable — KI disk write is authoritative"
```

// turbo

> **Law (Phase 57.1):** Never curl an `onCall` function. KI disk write is always the authoritative finalization record. Cloud sync is a best-effort operation deferred to next session start.

---

## 4. 🐙 GitHub Sovereign Sync (run_command)

Execute an autonomous payload commit and remote push of all modified states, ensuring the Github repository matches local disk parity exactly.

// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 bash -c '
  echo "[SOVEREIGN] Enacting GitHub Sync..."
  git add .
  if git commit --no-verify -m "chore: Infinity Protocol v10.0 Auto-Sync [$(date +%Y-%m-%dT%H:%M:%SZ)]"; then
    git push origin main || echo "[WARN] GitHub Push blocked — check SSH keys or remote state."
  else
    echo "[INFO] No drift detected. Git parity maintained."
  fi
'
```

> **Phase 57 Guard:** Wraps git within `timeout 30` and blocks terminal prompts to prevent password hangs.

---

## 5. 🧹 Phantom Purge (run_command — local only, instant)

// turbo
Run these automatically — they are local-only `rm` operations, not network calls:

```bash
rm -rf ~/.gemini/antigravity/browser_recordings/ ~/.npm/_npx/
```

> **Safe to auto-run.** No network, no stdin, no hang risk. Duration: <100ms.

---

## 6. ✅ Confirmation (in chat response)

State in your chat response:
> "Session finalized. MISSION_STATE v[X] updated. KI written to disk. GitHub Sync executed. Phantom Bloat purged."

*Status: Sovereign. Precise guards. No overkill. No hangs.*

