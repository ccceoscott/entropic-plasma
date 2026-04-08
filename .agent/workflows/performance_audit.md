---
description: Deep system performance auditing, lighthouse checks, and memory capacity clamping
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /performance_audit  
## Deep Performance Analysis — Core Vitals, Memory, Functions, Bundle — MCP-First

> ⚡ **MANDATE**: Performance regressions are P2 minimum. Every regression → root cause + fix before sealing.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` → extract `**Current Phase**:`.
If stale → auto-upgrade (0b). If current → confirm (0c).

### Phase 0b — Auto-Upgrade
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -10
./scripts/dv rules 2>&1 | tail -10
```

### Phase 0c — TypeScript Gate
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```

---

## PHASE 1 — Memory Sovereignty Audit

### 1a — package.json Script Scan
Use `view_file` on `package.json` and `functions/package.json`.
EVERY script with `dev`, `build`, `test`, `lint` MUST have `NODE_OPTIONS=--max-old-space-size=4096`.
Missing entries → auto-add immediately. Log each.

### 1b — Banned Config Scan
Use `grep_search` for `memoryBasedWorkersCount` in `next.config.ts` and `next.config.js`.
Any match → **auto-delete that line**. Absolute ban on Apple Silicon.

### 1c — JVM Sovereignty Verification
// turbo
```bash
cat ~/.zshenv | grep JAVA_OPTIONS || echo "JVM env var missing"
```
Must contain: `_JAVA_OPTIONS="-Xmx2048m"`
Missing → document as P2 (user must add to ~/.zshenv).

### 1d — ulimit Check
// turbo
```bash
ulimit -n
```
Expected: 65536 or higher. < 10000 → document as P2. Instruct user to add `ulimit -n 65536` to `~/.zshrc`.

---

## PHASE 2 — Lighthouse Full Audit (MCP)

### 2a — Ensure Dev Server Running
// turbo
```bash
lsof -ti:3000 2>/dev/null | head -3 || echo "no server"
```
If not running → `NODE_OPTIONS=--max-old-space-size=4096 npm run dev &` and wait 8 seconds.

### 2b — Desktop Lighthouse
Use `mcp_chrome-devtools_lighthouse_audit` with `device: "desktop"` and `mode: "navigation"`.
Record all scores.

### 2c — Mobile Lighthouse
Use `mcp_chrome-devtools_lighthouse_audit` with `device: "mobile"` and `mode: "navigation"`.
Record all scores.

### 2d — Score Analysis

| Metric | Desktop | Mobile | Target | Action Required |
|---|---|---|---|---|
| Performance | | | ≥85 | |
| Accessibility | | | ≥95 | |
| Best Practices | | | ≥90 | |
| SEO | | | ≥95 | |

For any score below target → run `/optimize` workflow for that category.

---

## PHASE 3 — Core Web Vitals Deep Dive (MCP)

### 3a — Performance Trace
Use `mcp_chrome-devtools_performance_start_trace` with `reload: true`.

### 3b — LCP Breakdown
Use `mcp_chrome-devtools_performance_analyze_insight` with `insightName: "LCPBreakdown"` and appropriate `insightSetId`.
LCP > 2500ms → identify: TTFB / Server Response / Render Blocking Resources / Image Loading.
Auto-fix identified issues.

### 3c — Document Latency
Use `mcp_chrome-devtools_performance_analyze_insight` with `insightName: "DocumentLatency"`.
TTFB > 600ms → investigate SSR or CDN issues.

### 3d — Memory Profile
Use `mcp_chrome-devtools_take_memory_snapshot` → save to `/tmp/perf_audit.heapsnapshot`.
Record: total heap size. If > 50MB at initial load → flag detached DOM or listener leak.

---

## PHASE 4 — Bundle Analysis

### 4a — Production Build
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 180 npm run build 2>&1 | grep -E "kB|MB|Route (Static|Dynamic|ISR)" | head -30
```

### 4b — Anomaly Detection
For any JS chunk > 250kB → identify the chunk name → use `grep_search` to find largest imports.
Waterfall investigation: chunk → import → source → optimization opportunity.

### 4c — Third-Party Script Audit
Use `grep_search` for `<Script` in `src/app/**/*.tsx`.
Any external script with `strategy="beforeInteractive"` → justify or downgrade to `afterInteractive`.

---

## PHASE 5 — Cloud Functions Performance (MCP)

### 5a — Execution Time Analysis
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "INFO"` and `page_size: 100`.
Parse for function execution times. Build a table:

| Function | Avg Execution (ms) | Max (ms) | Status |
|---|---|---|---|

Execution > 5000ms → P2 optimization target.
Execution > 10000ms → P1 optimization target.

### 5b — Cold Start Analysis
Look for patterns in logs where first execution of a function is notably slower.
Cold starts > 3000ms → consider keeping functions warm or increasing memory allocation.

### 5c — Error Rate Analysis
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "ERROR"` and `page_size: 50`.
Calculate error rate per function. > 5% error rate → P1 investigation.

---

## PHASE 6 — Database Query Performance (MCP-first)

### 6a — Index Verification
Use `mcp_firebase-mcp-server_firestore_list_indexes` for the default database.
Confirm indexes exist for all known compound queries.
Missing indexes → create via `mcp_firebase-mcp-server_firestore_create_index`.

### 6b — Query Pattern Audit  
Use `grep_search` for `.where(` in `functions/src/**/*.ts,src/**/*.ts`.
For each compound query (2+ where clauses) → verify corresponding composite index exists.
Document all unindexed compound queries as P2.

---

## PHASE 7 — Network Performance

### 7a — Network Request Audit (MCP)
Use `mcp_chrome-devtools_list_network_requests` after page load.
Filter for requests > 500ms.
For each slow request → identify: server endpoint, payload size, caching headers.

### 7b — Cache Header Verification
Use `grep_search` for `Cache-Control` in `functions/src/**/*.ts` (HTTP functions).
Missing cache headers on read-heavy endpoints → add appropriate TTL.

---

## PHASE 8 — Reporting & Knowledge Seal

### 8a — Performance Audit Report
Generate complete findings table with before/after comparisons.

### 8b — Knowledge Graph Persistence (MCP)
Use `mcp_knowledge-graph_add_observations` to record:
- Performance baselines for this session  
- Any optimization applied
- Any P1/P2 findings deferred

### 8c — MISSION_STATE Update
Bump phase. Log performance metrics to accomplishments.

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Performance audit sealed.`
