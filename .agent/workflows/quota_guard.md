---
description: Context Limit Emergency Save Protocol (R.A.P.S)
alwaysApply: false
---

# /quota_guard — Context Limit Emergency Save Protocol
# Infinity Protocol v10.0 (R.A.P.S)

## When to Invoke
Invoke this workflow when you notice ANY of these signals approaching:
- You have sent or are about to send a very long response
- You are mid-task on a major feature with uncommitted code
- The user has mentioned "context," "quota," "rate limit," or "running out"
- You have been working for many turns without sealing the state

## The Escape Hatch (2 Commands)

**Step 1 — Emergency fleet save:**
// turbo
```bash
dv quota-save "what you were doing — task state summary here"
```
This does **in 30 seconds**:
1. Commits ALL dirty repos in the fleet (no-verify, git stash as fallback)
2. Writes local R.A.P.S memory
3. Outputs a copy-paste resume block for the next LLM

**Step 2 — Tell the user:**
> "⚠️ Approaching context limit. I've run `dv quota-save` — all work is committed and state is sealed locally. Hand this to the next session: [paste the resume block output]"

---

## Resume Block Format

After `dv quota-save` runs, it outputs a block you can paste to the next LLM:
```
Project:   [project-name]
Phase:     [phase]
Commit:    <hash>
Saved at:  <timestamp>
Context:   <what you were doing>

RESUME INSTRUCTIONS:
1. Read MISSION_STATE.md and task.md
2. Do NOT use legacy Remote Brain MCP tools.
```
