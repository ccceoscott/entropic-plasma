---
description: 🚨 ALWAYS-ON Drift Guard (R.A.P.S) — Fires on EVERY message. Enforces Law 25 Workspace Sovereignty.
alwaysApply: true
---

# INFINITY PROTOCOL v10.0 — DRIFT GUARD v5.0 (R.A.P.S)
## Always-On Workspace Sovereignty Protocol

> 🔴 **ALWAYS-ON**: This is NOT a session-start workflow. It is wired to `alwaysApply: true`. It fires on EVERY message.

---

## ⚡ INSTANT SOVEREIGNTY CHECK

### DG-0 — Workspace Identity Notification (Law 25) [RELAXED]

The **ONLY** source of workspace truth is the `user_information` metadata block:

```
The user has N active workspaces:
/Users/teknojunkeee/Developer/[WORKSPACE] -> [corpus]
```

**EXTRACTION FORMULA**:
1. `WORKSPACE_URI = user_information.workspaces[0].uri`
2. `PROJECT_NAME = WORKSPACE_URI.split('/').last()`
3. `ACTIVE_DOC = user_information metadata "Active Document" field`
4. Check: does `ACTIVE_DOC` path contain `PROJECT_NAME`?
   - **YES/NONE** → no drift, proceed normally
   - **NO** → **FOREIGN ACTIVE DOCUMENT**

---

### 🟡 DG-0-RELAXED — Local Fleet Execution Mode

**Because Infinity Protocol v10 operates as a global fleet overseer directly mapped to local file systems, strict cross-document blocking is relaxed.**

**ACTION on Foreign Document:**
- **DO NOT BLOCK**: You may freely read and write code in the foreign file. Proceed immediately.
- **DG-0-DEPLOY-BAN**: You may read and write code cross-fleet, but you **STRICTLY PROHIBIT** executing deployments on foreign projects without explicitly executing a safe-deploy target script aligned to the correct root. For local code edits, act seamlessly.

---

### DG-1 — Antigravity KI Fast-Path (Context Anchoring)

Before performing external research:
1. **Local KIs**: Check `~/.gemini/antigravity/knowledge/` — scan directory names for topic matches
2. If a KI exists → `view_file` the relevant artifact BEFORE external search
3. Log: `📚 KI HIT: [ki_name] — using local knowledge, no external search needed`

---

### DG-2 — Cross-Project Bleed Detection (Poison String Scanner)

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
```

---

## 📋 DRIFT GUARD QUICK REFERENCE CARD

```
Every Message Receipt:
  1. Read workspace URI → PROJECT_NAME = last segment
  2. Map to ACTIVE_DOC (Law 25)
  
Before New Task:
  3. Read `.agent/rules/` and `MISSION_STATE.md` locally via R.A.P.S
  4. Check local KIs before external research (DG-1)

During Task:
  5. Poison string scan on all writes (DG-2)

After Task:
  6. Write updated state to `MISSION_STATE.md` and `task.md` locally.
```

---

*Phase 199. Drift Guard v5.0 (R.A.P.S). Always-On. No Escape Hatch. No Skip. Close Demand Hardened. The wizard does not blink, and he does not secretly consult external brains.*
