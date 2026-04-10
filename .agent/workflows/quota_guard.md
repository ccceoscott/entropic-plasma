# /quota_guard — Context Limit Emergency Save Protocol
# Infinity Protocol v10.0 — Phase 192.2

## When to Invoke
Invoke this workflow when you notice ANY of these signals approaching:
- You have sent or are about to send a very long response
- You are mid-task on a major feature with uncommitted code in multiple repos
- The user has mentioned "context," "quota," "rate limit," or "running out"
- You have been working for many turns without sealing the Brain

## The Escape Hatch (2 Commands)

**Step 1 — Emergency fleet save:**
```bash
dv quota-save "what you were doing — task state summary here"
```
This does **in 30 seconds**:
1. Commits ALL dirty repos in the fleet (no-verify, git stash as fallback)
2. Writes a Brain session memory (fire-and-forget, WAL fallback if Cloud Run cold)
3. Outputs a copy-paste resume block for the next LLM

**Step 2 — Tell the user:**
> "⚠️ Approaching context limit. I've run `dv quota-save` — all work is committed and Brain is sealed. Hand this to the next session: [paste the resume block output]"

---

## Manual Brain Seal (if dv is not available)

```bash
/opt/homebrew/bin/node /Users/teknojunkeee/Developer/infinity-protocol/scripts/brain-commit.cjs \
  --project infinity-protocol \
  --phase 192 \
  --status ACTIVE \
  --context "What you were doing and where things stand"
```

---

## Registry Loss Recovery

If the Brain shows fewer projects than expected (should be ~16), run:
```bash
dv fleet-register
```
This re-discovers all repos with `.firebaserc` and upserts them into `project_states`.

---

## WARNING: Never Use These MCP Tools — They Hang

```
mcp_mcp-local-hub_brain_batch_write         ← hangs 30-60s on Cloud Run cold start
mcp_mcp-local-hub_brain_save_session_memory ← same
mcp_mcp-local-hub_brain_upsert_project_state ← same
mcp_mcp-local-hub_brain_list_project_states ← same
mcp_mcp-local-hub_brain_brave_web_search    ← same
```

**Only safe Brain MCP tool:** `mcp_mcp-local-hub_hub_status` (local, no Cloud Run call)

---

## Resume Block Format

After `dv quota-save` runs, it outputs a block you can paste to the next LLM:
```
Project:   infinity-protocol (gen-lang-client-0386732425)
Phase:     193.2
Commit:    <hash>
Saved at:  <timestamp>
Context:   <what you were doing>

RESUME INSTRUCTIONS:
1. Read MISSION_STATE.md in /Users/teknojunkeee/Developer/infinity-protocol/
2. Run: dv brain-commit --ping
3. Read last 3 Brain session_memories for full context
4. DO NOT call brain_* MCP tools directly — use CLI
5. Firebase/gcloud MCP: do IDE reload first (pipe corruption)
```
