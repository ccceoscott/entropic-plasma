---
description: Local Brain Audit — Test physical integrity, drift, and rules formatting of the Sovereign Knowledge Base (R.A.P.S)
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /knowledge_audit
## Local Brain Integrity and R.A.P.S. System Check

> ⚡ **MANDATE**: Since the suspension of the remote Firebase Brain MCP, all intelligence is stored locally in `~/.gemini/antigravity/knowledge/`. This audit tests indexing, storage bloat, rules drift, and dynamic model compliance.

---

## PHASE 1 — Physical Storage Audit (The Local Brain)

### 1a — Knowledge Directory Indexing
Run a structural read on the local knowledge base directory to ensure validity.
// turbo
```bash
KNOWLEDGE_DIR=~/.gemini/antigravity/knowledge
echo "--- Knowledge Base Filesize Check ---"
du -sh $KNOWLEDGE_DIR/* 2>/dev/null || echo "No KIs found or directory is empty"
echo "--- KI Count ---"
find $KNOWLEDGE_DIR -type f -name "metadata.json" | wc -l
```

### 1b — Metadata Schema Validation
Verify that all stored items have valid JSON mappings and enforce project-scoping boundaries.
// turbo
```bash
for file in ~/.gemini/antigravity/knowledge/*/metadata.json; do
  if [ -f "$file" ]; then
    node -e "
      try {
        const data = require('$file');
        if (!data.project) throw new Error('Missing project property');
      } catch(e) {
        console.error('Schema Violation in:', '$file', '->', e.message);
        process.exit(1);
      }
    " || exit 1
  fi
done
echo "JSON Schema validation complete. All KIs are project-scoped."
```

---

## PHASE 2 — Rules & Protocol Drift (R.A.P.S.)

### 2a — Poison String Sweep
Ensure no cross-project bleed has entered the local protocol bounds.
// turbo
```bash
echo "Scanning for Poison Strings in active project..."
grep -rn "Soul Contract\|CareKey\|SARAH\|FirstPick\|epi-hab" src/ package.json functions/ 2>/dev/null || echo "✅ No protocol bleed detected."
```

### 2b — Law 29 Dynamic Model Verification
Verify that legacy static models (e.g., `gemini-1.5-pro`, `gemini-2.0-flash`) have not been re-hardcoded into the execution logic.
// turbo
```bash
echo "Scanning for Deprecated Static LLM Hardcodes..."
grep -rn "gemini-1.5-pro" .agent/workflows/ .agent/rules/ || echo "✅ No 1.5 logic drift."
grep -rn "gemini-2.0-flash" .agent/workflows/ .agent/rules/ || echo "✅ No 2.0 static drift."
```

### 2c — Sovereign E2E Locks Check
Verify that `playwright.config.ts` or package.json E2E scripts respect the new port resolution protocols and worker isolation.
Use `grep_search` to ensure `workers: process.env.CI ? 1 : 1` or similar strict limits are employed.

---

## PHASE 3 — Workspace Integrity & Fleet Audit

### 3a — Terminal & Cache Profiling
Scan the `.next`, `dist`, and `node_modules` sizes to check for ghost processes or bloat.
// turbo
```bash
du -sh .next dist node_modules ~/.gemini/antigravity/browser_recordings 2>/dev/null || echo "Storage profiles generated."
```

### 3b — Port Ghosting & Watchdog Health
Run the Sovereign Health script to check daemons and hanging process trees.
// turbo
```bash
timeout 5 lsof -nP -iTCP -sTCP:LISTEN | grep -E "3000|5173|8080|5001" || echo "Ports clear."
```

---

## PHASE 4 — Final Diagnosis and MISSION_STATE Rollup

1. Generate a report detailing corrupted KIs, poison strings found, and bloated recordings.
2. If tests output clean (`Exit code 0`), the Local Brain is fully operational, proving physical data autonomy.
3. Update `MISSION_STATE.md` indicating that the R.A.P.S `/knowledge_audit` was successful and local constraints tested identical to the remote.

---
## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Local Knowledge Audit complete. Brain physical structure validated.`
