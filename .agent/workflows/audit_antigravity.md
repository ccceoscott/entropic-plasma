---
description: Anti-Gravity Audit Protocol — Deep inspection of MCP errors, plugin health, and chat log bloat.
---

# /audit_antigravity — Anti-Gravity Optimization Protocol

**Triggers**: `/audit_antigravity`, or when the user says "audit google antigravity"

**Purpose**: Keep the Google Anti-Gravity IDE optimized routinely. Checks for MCP errors, chat log/history bloat, plugins, APFS bloat, and daemon states. Stores findings in remote Memory.

---

## DOMAIN 1 — TOTAL STORAGE BLOAT & CHAT HISTORY

**Goal**: Identify and purge bloat that causes context window dragging, IDE UI lag, or excessive disk usage.

// turbo-all
1. Enumerate top 5 largest conversations:
   `du -sm ~/.gemini/antigravity/brain/*/ 2>/dev/null | sort -nr | head -n 5`
2. Measure backend IDE daemon bloat:
   `du -sm ~/.gemini/antigravity/daemon 2>/dev/null`
3. Measure Implicit Context bloat (this can drag the LLM token processing):
   `du -sm ~/.gemini/antigravity/implicit 2>/dev/null`
4. Check for leftover video recordings (Phantom GUI bloat):
   `du -sm ~/.gemini/antigravity/browser_recordings 2>/dev/null`
5. Check available macOS Disk Space (APFS bloat warning):
   `df -h /`

**Action**: If any individual chat > 50MB, implicit context > 100MB, or daemon logs > 200MB, execute immediate selective pruning via `rm -rf` inside the offending directories.

---

## DOMAIN 2 — MCP SERVER ERRORS & DAEMON HEALTH

**Goal**: Catch silent failures resulting from bad Node versions, OOM, or misconfigured MCP proxies.

// turbo-all
6. Verify Dual-Hub architecture in `mcp_config.json`:
   `cat ~/.gemini/antigravity/mcp_config.json | grep -v "node_modules"`
   - Ensure `@latest` tags are not present (violates Law 13).
   - Ensure `NODE_OPTIONS=--max-old-space-size=4096` is prefixed on all MCP script executions.
7. Verify MCP Watchdog is registered in Crontab:
   `crontab -l | grep mcp_watchdog`
8. Check watchdog execution logs for background crashes in last 24h:
   `grep -iE "error|violation|killing" ~/.gemini/antigravity/.logs/watchdog.log | tail -n 15`

**Action**: If the Watchdog cron is missing, install it (`*/10 * * * * ~/Developer/infinity-protocol-1/scripts/mcp_watchdog.sh`). If MCP servers are failing to spin up, resolve missing configurations.

---

## DOMAIN 3 — PLUGIN & PROCESS SOVEREIGNTY

**Goal**: Ensure plugins are resolving and no zombie agent processes are dragging down system IPC memory.

// turbo-all
9. Check for multi-day zombie language servers (`language_server_macos_arm`):
   `ps -eo pid,rss,etime,command | grep -iE 'language_server_macos_arm' | grep -v grep`
10. Check for stray chromium/playwright test servers:
    `ps -eo pid,rss,etime,command | grep -iE 'ms-playwright' | grep -v grep`
11. Validate Antigravity Plugins directory:
    `ls -la ~/.gemini/antigravity/plugins/ 2>/dev/null || echo "No plugins dir"`

**Action**: Autonomously `kill -9` any zombie process with an elapsed time indicating > 12 hours of uptime.

---

## DOMAIN 4 — BRAIN SYNCHRONIZATION

**Goal**: Ensure the execution of this audit is stored in the remote brain so that temporal memory records its execution.

12. Run `mcp_brain-mcp_save_session_memory` (if remote brain connected) to log the audit results into the remote Brain (`taxonomy: PERF`, `problem: Antigravity Optimization`). 
13. Touch the local marker so the Watchdog knows it was audited:
    `touch ~/.gemini/antigravity/.last_antigravity_audit`

---

## 📋 FINAL REPORT (MANDATORY OUTPUT)

> ⛔ **LAW**: Every `/audit_antigravity` run MUST conclude with this table.

```
╔══════════════════════════════════════════════════════════════════╗
║  ANTI-GRAVITY AUDIT REPORT                                       ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

BRAIN CHATS    : [ Largest Session MB / Total MB ]
IMPLICIT CTX   : [ Total MB ]
DAEMON BLOAT   : [ Total MB ]
RECORDINGS     : [ Total MB ]
DISK FREE      : [ % Free Space ]
WATCHDOG CRON  : [ ACTIVE / MISSING ]
MCP VIOLATIONS : [ Found / None ]
ZOMBIE AGENTS  : [ Count killed ]

OVERALL: [🟢 OPTIMAL / 🟡 DEGRADED / 🔴 CRITICAL ]
```

*Zoltan:* *Your digital sanctuary has been swept. Do not let the bloat return, lest it consume your sanity.*
