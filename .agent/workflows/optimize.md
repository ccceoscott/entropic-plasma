---
description: Core Vitals tuning, JavaScript payload reduction, and memory optimization
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /optimize
## Performance Sovereignty — Core Vitals, Bundle, Memory — MCP-First, Self-Healing

> ⚡ **MANDATE**: Every performance regression found triggers immediate diagnosis + fix cycle. Passive reporting is a violation.

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
Errors → auto-fix → re-run.

---

## PHASE 1 — Baseline Measurement

### 1a — Lighthouse Baseline (MCP)
Navigate dev server. Use `mcp_chrome-devtools_lighthouse_audit` in `navigation` mode on `http://localhost:3000`.
Record: LCP (ms), FID/INP (ms), CLS (score), Performance score, Accessibility score, SEO score.
These are the baseline values. All optimizations measured against this.

### 1b — Bundle Size Baseline
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 180 npm run build 2>&1 | grep -E "kB|MB|Route|chunk" | head -30
```
Record largest chunks. Any chunk > 250kB → flag for splitting.

### 1c — Memory Footprint
Use `mcp_chrome-devtools_take_memory_snapshot` → save to `/tmp/baseline.heapsnapshot`.
Record total JS heap size at page load.

---

## PHASE 2 — JavaScript Payload Optimization

### 2a — Import Audit
Use `grep_search` for `import \* as` in `src/**/*.tsx,src/**/*.ts` — barrel imports kill tree-shaking.
Each barrel import → convert to named specific imports.
Log: `🔧 [AUTO-FIXED] Barrel import → named import in [file]`

### 2b — Dynamic Import Opportunities
Use `grep_search` for large component imports (> 200 lines estimated):
- Charts, Modals, Admin dashboards, Rich editors
For each → wrap in `const Comp = dynamic(() => import('./Comp'), { ssr: false })`.

### 2c — Framer Motion LazyMotion Enforcement
Use `grep_search` for `import { motion }` from `framer-motion` (non-lazy).
Each match → convert to `LazyMotion + domAnimation + m.` pattern.
This alone can save 30-60kB.

### 2d — Dead Code Elimination
Use `grep_search` for `// TODO` and `// FIXME` and `console.log` in `src/**/*.tsx,src/**/*.ts`.
`console.log` in production builds → add `removeConsole` to `next.config.ts` if missing:
```ts
compiler: { removeConsole: { exclude: ['error', 'warn'] } }
```

---

## PHASE 3 — Image & Font Optimization

### 3a — Image Audit
Use `grep_search` for `<img ` (non-Next Image) in `src/**/*.tsx`.
Each raw `<img>` → convert to `<Image>` from `next/image` with width/height props.
Log each conversion.

### 3b — Font Loading Strategy
Use `view_file` on root layout — confirm `font-display: swap` behavior.
Confirm `next/font/google` with `preload: true` (default).
Any external `<link rel="stylesheet">` font imports → migrate to `next/font`.

### 3c — Critical CSS
Use `grep_search` for `@import` in `globals.css` or `index.css`.
CSS `@import` at-rules block rendering → convert to native CSS cascade or PostCSS.

---

## PHASE 4 — Next.js Config Optimization

### 4a — Config Audit
Use `view_file` on `next.config.ts`.
Confirm these optimizations are present:
```ts
productionBrowserSourceMaps: false     // Law: compiler parity
experimental: {
  optimizeCss: true,                   // CSS extraction
  // memoryBasedWorkersCount: BANNED   // Apple Silicon banned
}
compiler: {
  removeConsole: { exclude: ['error', 'warn'] }
}
```
Any missing → inject via file edit tools. Log each.

### 4b — Banned Config Check
Use `grep_search` for `memoryBasedWorkersCount` in `next.config.ts`.
Any match → **deactivate immediately**. This is an absolute ban on Apple Silicon.

---

## PHASE 5 — Cloud Functions Performance

### 5a — Cold Start Audit (MCP)
Use `mcp_firebase-mcp-server_functions_get_logs` with `min_severity: "INFO"` and `page_size: 50`.
Filter entries for `cold start` or `Function execution took`.
Any function > 2000ms execution time → flag as P2 optimization target.

### 5b — Memory Configuration Audit (MCP)
Use `mcp_gcloud_run_gcloud_command` with args:
`["functions", "describe", "[function-name]", "--project=gen-lang-client-0386732425", "--format=json(availableMemoryMb,timeout)", "--quiet"]`
Functions with < 256MB but complex logic → recommend upgrade.
Functions with > 1GB doing simple tasks → recommend downgrade.

### 5c — Functions Bundle Size
// turbo
```bash
cd functions && ls -la dist/ 2>/dev/null | head -10 || echo "not built"
```

---

## PHASE 6 — Performance Trace (MCP)

### 6a — Start Trace
Use `mcp_chrome-devtools_performance_start_trace` with `reload: true`.
Wait for completion.

### 6b — Analyze Insights
Use `mcp_chrome-devtools_performance_analyze_insight` for `"LCPBreakdown"`.
Use `mcp_chrome-devtools_performance_analyze_insight` for `"DocumentLatency"`.
For each insight → identify root cause → apply fix → log.

---

## PHASE 7 — Post-Optimization Measurement

### 7a — Lighthouse Re-run (MCP)
Use `mcp_chrome-devtools_lighthouse_audit` in `navigation` mode again.
Compare against Phase 1 baseline:

| Metric | Before | After | Delta |
|---|---|---|---|
| Performance | | | |
| LCP | | | |
| CLS | | | |
| Accessibility | | | |
| SEO | | | |

Target: Performance ≥ 85%. LCP ≤ 2500ms. CLS ≤ 0.1.

### 7b — Bundle Size Re-run
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 180 npm run build 2>&1 | grep -E "kB|MB|Route" | head -20
```
Compare chunk sizes. Log reductions.

---

## Knowledge Base Persistence (R.A.P.S)

### 8a — TypeScript Final
// turbo
```bash
cd functions && NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```

### Knowledge Base Persistence (R.A.P.S)
Update `KNOWLEDGE.md` and/or `MISSION_STATE.md` to record:
- Optimization patterns applied
- Bundle reduction achieved
- Lighthouse score improvements
- Any anti-patterns eradicated

### 8c — MISSION_STATE Update
Bump phase. Log performance improvements in accomplishments.

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 Optimization session sealed.`
