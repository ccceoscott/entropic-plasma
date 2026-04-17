---
description: Initialization and Session Synchronization — Standard STEP ZERO for all interactions.
alwaysApply: false
---

# 🌀 /init — The Sovereign Synchronizer (v12.1)

⚡ **MANDATE**: Execute this ritual AT THE START of every session. No exceptions. Failure to sync is a Protocol violation.

## 🧠 Skill Ingestion
**Automatically ingest these skills** before proceeding:
1. `.agent/skills/catalog.json` — The Master Skill Manifest

---

## 🔐 SOVEREIGN UPGRADE GATE
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

## 🛡️ SENTINEL ENFORCEMENT
// turbo
```bash
bash ~/.infinity-protocol/sentinel/enforce.sh 2>&1
```
**Behavior**: Prints NOTHING on clean boot. Only speaks if:
- N-Tab Storm detected (MCP duplicates above threshold) → single warning line
- Stale test runners killed → single cleanup line
If output is empty, Sentinel is clean. Do NOT echo anything extra.

## 📋 SESSION CALIBRATION
1. **Audit MISSION_STATE.md**: Extract the `WORKSPACE_PHASE` and `Status`.
2. **Context Budgeting**: Identify only the Domain Bundles required for the current objective. 
   - `!arch` (Architect), `!vis` (Vision), `!hammer` (Hammer), `!shield` (Shield), `!oracle` (Research).

Declare: `✅ [PHASE N SYNCED] | SESSION_PROOF_TOKEN: [TOKEN] | Ready to forge.`
