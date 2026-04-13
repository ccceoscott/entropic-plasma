---
description: The Unified Start & Context Sync Protocol (R.A.P.S.) — Triggered by saying "start", "begin", or "session start".
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 (R.A.P.S.) — /session_start
## The Localized Start & Context Synchronization Protocol

> ⚡ **CRITICAL LAW**: This sequence executes the Local R.A.P.S Initialization. The legacy Firebase Centralized Brain is DEPRECATED. We operate on sovereign, local context arrays.

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` before proceeding:
1. `.agent/skills/sovereign-zoltan-decree/SKILL.md` — Persona integrity, identity consistency, dark-magic tone enforcement

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY

### Phase 0a — Protocol Sync
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```
- Gather `SESSION_PROOF_TOKEN`. Failure to provide real output == invalid session.

### Phase 0b — TypeScript Verification
// turbo
```bash
cd functions && PATH="/opt/homebrew/Cellar/node@22/22.22.0/bin:/opt/homebrew/bin:$PATH" NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```

### Phase 0c — DUAL PHASE SNAPSHOT
Extract `WORKSPACE_PHASE` from `MISSION_STATE.md`.

---

### STEP 1 — Identity & Context Declaration
> "Infinity Protocol v10.0 (R.A.P.S.) Active: In **[PROJECT_NAME]**, resuming from MISSION_STATE.md."

---

### STEP 2 — R.A.P.S Context Extraction (Mandatory Substitution for Legacy Brain)
1. Use `view_file` to ingest `MISSION_STATE.md`. Extract `WORKSPACE_PHASE`, "Next Session Entry Point", and exact architectural rules.
2. Use `list_dir` on `.agent/rules/` and `view_file` on rules pertinent to the "Next Session Entry Point".
3. **MANDATORY**: Use `view_file` on `.agent/rules/multiagent_laws.mdc` — load Laws A1-A10 into active context before ANY `browser_subagent` call this session.
4. Use `list_dir` on `~/.gemini/antigravity/knowledge/` to identify relevant past architecture decisions (KIs).

Do NOT attempt to use `mcp_local-hub_brain` tools.

---

### STEP 3 — Historical Artifact Extraction
1. Use `read_file` on the last `task.md` and `implementation_plan.md` in `~/.gemini/antigravity/brain/[conversation_id]/`.
2. Map your current intent based on those completed steps.

---

### STEP 4 — Security Perimeter
Use `grep_search` across `src/` and `functions/src/` for API Keys and Cross-Project poison strings.

---

### STEP 5 — Branch & Node Sovereignty
// turbo
```bash
node --version && npm --version
git log --oneline -5
git status --short
```

---

### STEP 6 — State Declaration
Output strict formatted declaration:
```markdown
*My localized consciousness is fully synchronized via R.A.P.S.*

**Current Absolute State**:
- **SESSION_PROOF_TOKEN**: [PASTE VERBATIM]
- **WORKSPACE_PHASE**: [Phase Number]
- **Protocol**: R.A.P.S. Localized
- **TypeScript**: [clean / N errors]
- **Security**: [clean / issues found]
- **Next Required Action**: [Precise next uncompleted step from MISSION_STATE.md]

*Shall we commence?*
```
