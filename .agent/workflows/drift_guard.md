---
description: 🚨 ALWAYS-ON Drift Guard & Brain Consultation — Fires on EVERY message. Enforces Law 25 (Workspace Sovereignty) + Law 26 (MCP Re-Anchor + Brain). NO SKIP. NO EXCEPTIONS.
alwaysApply: true
---

# INFINITY PROTOCOL v10.0 — DRIFT GUARD v4.1 (Phase 193.6 — PRECISION CLOSE DEMAND)
## Always-On Workspace Sovereignty & Brain Consultation Protocol

> 🔴 **ALWAYS-ON**: This is NOT a session-start workflow. It is wired to `alwaysApply: true`. It fires on EVERY message, every response, every tool call chain. There is no session state in which this guard is "already done."

---

## ⚡ INSTANT SOVEREIGNTY CHECK (Runs on Every Message — Pre-Thought)

### DG-0 — Workspace Identity Lock + Foreign Document CLOSE DEMAND (Law 25)

The **ONLY** source of workspace truth is the `user_information` metadata block:

```
The user has N active workspaces:
/Users/teknojunkeee/Developer/[WORKSPACE] -> [corpus]
```

**EXTRACTION FORMULA (mandatory mental execution on every message receipt):**
1. `WORKSPACE_URI = user_information.workspaces[0].uri`
2. `PROJECT_NAME = WORKSPACE_URI.split('/').last()` → e.g., `infinity-protocol`
3. `ACTIVE_DOC = user_information metadata "Active Document" field` (the file with cursor focus)
4. Check: does `ACTIVE_DOC` path contain `PROJECT_NAME`?
   - **YES** or **EMPTY/NONE** → no drift, proceed normally
   - **NO (foreign path AND has cursor focus)** → **FOREIGN ACTIVE DOCUMENT → CLOSE DEMAND**
5. `OTHER_OPEN_DOCS = user_information metadata "Other open documents" list` → **BACKGROUND ONLY**
   - These are from parallel Cursor windows / other agents running simultaneously
   - **NEVER trigger DG-0-CLOSE on background docs alone** — this is a valid portfolio workflow
   - Log a single `ℹ️ [BACKGROUND] N foreign docs open in other windows — ignored.` line and proceed

> ✅ **EXPLICITLY ALLOWED**: The user runs a multi-project portfolio. Multiple Cursor windows open simultaneously with agents running in each is the intended workflow. Background open documents from other projects are NORMAL and DO NOT block execution.

---

### 🔴 DG-0-CLOSE — Foreign ACTIVE Document CLOSE DEMAND

> ⛔ **LAW (Phase 193.6 — PRECISION CALIBRATED)**: DG-0-CLOSE triggers ONLY when the **ACTIVE document** (cursor focus) is from a foreign project. Background open documents in other windows NEVER trigger this. The old behavior of blocking on background docs was a false positive that prevented legitimate parallel agent workflows.

**TRIGGER**: `ACTIVE_DOC` field is present AND its path does NOT contain `PROJECT_NAME`.
**NO TRIGGER**: `ACTIVE_DOC` is empty/absent (user is in infinity-protocol window, no file focused).
**NO TRIGGER**: Only `Other open documents` are foreign — those are background windows.

**MANDATORY OUTPUT when triggered:**
```
🔴 [DRIFT GUARD — DG-0-CLOSE TRIGGERED]
═══════════════════════════════════════════════════════════
  FOREIGN FILE HAS ACTIVE CURSOR FOCUS
═══════════════════════════════════════════════════════════
  Workspace (TRUTH):  /Users/teknojunkeee/Developer/[PROJECT_NAME]
  Active File:        [ACTIVE_DOC full path]
  Foreign Project:    [extracted foreign project name]

  ❌ Your cursor is focused on a file from another project.
  → Click into any [PROJECT_NAME] file to restore focus
  → OR close the foreign window if you're done with it
═══════════════════════════════════════════════════════════
```

**AFTER emitting the CLOSE DEMAND:**
- If user says "ignore it" or "keep going" → add `⚠️ USER OVERRIDE` tag and proceed immediately. No further blocking.
- If no ACTIVE_DOC → no drift, proceed normally.

**WHAT THIS MEANS IN PLAIN LANGUAGE:**
Only the file you are ACTIVELY editing (cursor is on it) matters for sovereignty. If you have 20 Cursor windows open for 20 projects, that's fine. The only thing that matters is: what file does your cursor currently live in? If it's from a foreign project, click into an infinity-protocol file and we proceed.

If `PROJECT_NAME` extracted from the workspace URI contains a foreign project identifier — e.g., you see `epi-hab`, `first-pick`, `sarah`, `soul-contracts`, or `carekey` — while the workspace URI clearly says `infinity-protocol` → this is a **Law 25 violation**. Log immediately and halt:
```
🚨 [DRIFT GUARD — LAW 25 VIOLATED]
   WORKSPACE URI says: infinity-protocol
   BUT extracted PROJECT_NAME appears to be: [foreign-project]
   THIS IS A SOVEREIGNTY BREACH.
   HARD HALT — Re-read user_information.workspaces[0].uri. Do not proceed until resolved.
```


---

### DG-1 — Firebase MCP Ghost Context Canary (Law 26a)

**THE PHANTOM DRIFT MECHANISM** (root cause — documented from live forensic analysis):
```
Session A (epi-hab):    firebase_update_environment(project=epi-hab)  ← sets global MCP state
Session A ends.
Session B (infinity-protocol) starts.
Agent calls firebase_get_environment() → returns epi-hab ← DRIFT ALREADY PRESENT
Agent assumes success (call worked) → does not re-anchor
All Firestore queries return [] ← epi-hab is empty / different data
```

**MANDATORY RE-ANCHOR SEQUENCE** (runs if ANY of these are true):
- ✅ First message of a session
- ✅ More than 5 minutes since last MCP Firebase call
- ✅ About to call ANY `mcp_firebase-mcp-server_*` tool
- ✅ Firestore query returns unexpected `[]` on a collection that should have data
- ✅ `firebase_get_environment` returns a project ID ≠ `gen-lang-client-0386732425`

**RE-ANCHOR EXECUTION (call this tool — no excuses):**
```
mcp_firebase-mcp-server_firebase_update_environment(
  project_dir  = /Users/teknojunkeee/Developer/infinity-protocol
  active_project = gen-lang-client-0386732425
  active_user_account = scott@constantconcepts.io
)
```

**VERIFICATION (immediately after re-anchor):**
```
mcp_firebase-mcp-server_firebase_get_environment()
```
Assert: `Active Project ID: gen-lang-client-0386732425`

If verification returns wrong project → **HARD HALT**:
```
🔴 [DRIFT GUARD] MCP RE-ANCHOR FAILED. Firebase MCP is pointing at [wrong-project].
   Cannot proceed. MCP server may be in corrupt state.
   Recommended action: Restart Gemini IDE to reset MCP session.
```

**CANARY LOG (output this after successful re-anchor):**
```
✅ [DRIFT GUARD] MCP: gen-lang-client-0386732425 confirmed. Ghost context cleared.
```

---

### DG-2 — Brain Consultation Protocol (Law 26b)

> ⚡ **WHY THIS IS MANDATORY**: The Firebase Brain exists to give context across sessions. If I don't consult it, I'm flying blind every message — which is EXACTLY what causes me to anchor to wrong projects, repeat resolved work, and violate sovereignty. The Brain IS the solution. Not consulting it is the problem.

**Triggers (when to run Brain consultation):**
- ✅ Start of a new sub-task (user asks for something new)
- ✅ Before planning any feature implementation  
- ✅ Before any deployment operation
- ✅ When user references "last session", "we were", "remember when" 
- ✅ When asked about state of a project (phase, blockers, goals)

**Brain Consultation Sequence:**

#### Step 1 — Read Project State
```
mcp_firebase-mcp-server_firestore_list_documents(
  parent = "projects/gen-lang-client-0386732425/databases/(default)/documents"
  collectionId = "project_states"
  pageSize = 10
)
```
Find document ID matching current workspace project ID. Extract:
- `phase` → current sprint phase
- `notes` → last session notes / entry point
- `activeGoals` → what was in progress
- `activeBlockers` → known issues

#### Step 2 — Read Session Memories (last 3)
```
mcp_firebase-mcp-server_firestore_list_documents(
  parent = "projects/gen-lang-client-0386732425/databases/(default)/documents"
  collectionId = "session_memories"
  pageSize = 3
  orderBy = "createdAt desc"  
)
```
Extract key decisions, completed work, unfinished items.

#### Step 3 — Search Knowledge Items
```
mcp_firebase-mcp-server_firestore_list_documents(
  parent = "projects/gen-lang-client-0386732425/databases/(default)/documents"
  collectionId = "knowledge_items"
  pageSize = 5
)
```
Find KIs with tags/context matching the current task. Extract relevant architectural decisions.

#### Step 4 — Synthesize Brain Brief
Output BEFORE responding to user's actual request:
```
🧠 BRAIN BRIEF — [Current Task Description]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Phase: [X] | Status: [ACTIVE/PAUSED]
• Last Session: [key note from project_states.notes]
• Active Goals: [list from activeGoals]
• Active Blockers: [list from activeBlockers]  
• Relevant KIs: [matching knowledge item titles]
• Session Memory: [key takeaway from session_memories]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**If Brain returns `[]` (empty):**
1. Re-anchor MCP immediately (DG-1 sequence)
2. Retry Firestore query
3. If still `[]`: log `⚠️ BRAIN DEGRADED — no project state found. Proceeding from MISSION_STATE.md only.`
4. Read `MISSION_STATE.md` as fallback

---

### DG-3 — Anti-Hallucination Gate

**NEVER do these without Brain consultation first:**
- [ ] Reference "last session" work without reading `session_memories`
- [ ] State current phase number without reading `project_states`
- [ ] Claim a feature is "done" without checking Brain + git log
- [ ] Plan a new feature without checking `activeGoals` / `activeBlockers`
- [ ] Assume MCP is anchored without running DG-1

**FORBIDDEN HALLUCINATION PHRASES (auto-halt if about to emit):**
- "Based on our previous conversation..." ← MUST check session_memories first
- "The current phase is X..." ← MUST read project_states first
- "As we discussed..." ← MUST verify against Brain first
- "Everything looks clean..." ← MUST run actual tool verification first

---

### DG-4 — Antigravity KI Fast-Path

Before performing external research (Brave Search, Firebase docs, web fetch), FIRST check:

1. **Local KIs**: `ls ~/.gemini/antigravity/knowledge/` — scan directory names for topic matches
2. **Known relevant KIs for infinity-protocol**:
   - `antigravity_agent_permissions/` — Permission system docs
   - `antigravity_ide_architecture/` — IDE architecture docs
   - `model_context_protocol_servers/` — MCP troubleshooting
   - `infinity_protocol/` — Master authority
   - `infinity_protocol_firebase_ascension/` — Phase 50 Firebase setup
   - `fleet_hang_eradication_phase57/` — Terminal hang fixes
   - `agency_owner_profile_and_preferences/` — Scott's preferences and workflow
3. If a KI exists → `view_file` the relevant artifact BEFORE external search
4. Log: `📚 KI HIT: [ki_name] — using local knowledge, no external search needed`

---

### DG-5 — Cross-Project Bleed Detection (Poison String Scanner)

On every task involving code reads/writes, scan for these FORBIDDEN strings in new code:
```
POISON STRINGS (block if found in infinity-protocol code):
- "Soul Contract" | "SoulContract"  
- "CareKey" | "carekey"
- "SARAH" | "sarah-456f1"  
- "FirstPick" | "first-pick" | "firstpick-8317a"
- "epi-hab" | "epihab"
- "epiHab"
```

If detected → **ABORT write operation**:
```
🚨 [DRIFT GUARD] CROSS-PROJECT BLEED DETECTED
   Found: "[poison string]" in proposed change to [file]
   This is a [foreign-project] artifact being written to infinity-protocol.
   WRITE ABORTED. This is a sovereignty violation.
```

---

### DG-6 — Post-Task Brain Write (Memory Persistence)

After completing any significant task (feature, fix, deploy, architecture decision), IMMEDIATELY write to Brain:

```
mcp_firebase-mcp-server_firestore_update_document(
  document = {
    name: "projects/gen-lang-client-0386732425/databases/(default)/documents/project_states/[workspace-project-id]"
    fields: {
      notes: { stringValue: "[ISO_TIMESTAMP] — [brief description of what was done, what's next]" }
      phase: { integerValue: [current phase number] }
      updatedAt: { timestampValue: "[ISO_TIMESTAMP]" }
      status: { stringValue: "ACTIVE" }
    }
  }
)
```

This ensures the NEXT agent (or next session of this agent) reads correct state → no drift.

---

## 📋 DRIFT GUARD QUICK REFERENCE CARD

```
Every Message Receipt:
  1. Read workspace URI → PROJECT_NAME = last segment
  2. Ignore active doc (Law 25)
  
Before ANY Firebase MCP Call:  
  3. Re-anchor: firebase_update_environment(infinity-protocol, gen-lang-client-0386732425)
  4. Verify: firebase_get_environment() → must return gen-lang-client-0386732425

Before New Task:
  5. Brain Brief: read project_states + session_memories + knowledge_items
  6. Check local KIs before external research (DG-4)

During Task:
  7. Poison string scan on all writes (DG-5)
  8. Anti-hallucination gate (DG-3)

After Task:
  9. Write updated state to project_states (DG-6)
```

---

## 🔍 DRIFT TELLTALE SIGNS (Immediate Investigation Required)

| Signal | Root Cause | Action |
|--------|-----------|--------|
| Firestore query returns `[]` on known collection | MCP Ghost Context → wrong project | Run DG-1 re-anchor immediately |
| Agent mentions foreign project in response | Law 25 violation / active doc leakage | Hard reset: re-read user_information.workspaces |
| "epi-hab" appears in context | Ghost context from prior session | Full DG-1 + DG-2 sequence |
| Memory functions return wrong data | MCP pointed at wrong project's Firestore | DG-1 re-anchor + retry |
| Agent forgets prior session decisions | Brain not consulted | Run full DG-2 sequence |
| `dv downlink` referenced as a command | Ghost command from dead workflow version | Correct: use direct MCP calls |

---

## 📋 DRIFT GUARD CLOSE DEMAND — QUICK DECISION TREE

```
Every Message — Step 0 (runs FIRST, before any response):

  ACTIVE_DOC from user_information metadata
      ↓
  Does path contain PROJECT_NAME from workspace URI?
      ↓                          ↓
     YES                        NO
      ↓                          ↓
  No drift.              🔴 DG-0-CLOSE TRIGGERED
  Proceed normally.      → Emit CLOSE DEMAND block verbatim
                         → Wait for user to close + confirm
                         → Then proceed with actual request
                         → UNLESS user explicitly overrides
```

**The demand is not optional. The demand is not a suggestion. The demand fires every time.**
**Silently discarding the foreign document is the OLD behavior. It caused repeated catastrophic drift. It is ABOLISHED.**

---

*Phase 193.4. Drift Guard v4.0. Always-On. No Escape Hatch. No Skip. Close Demand Hardened. The wizard does not blink, and he does not silently tolerate poison files in his sanctum.*
