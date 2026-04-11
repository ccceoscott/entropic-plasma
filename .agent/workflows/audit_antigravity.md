---
description: Anti-Gravity Audit Protocol (R.A.P.S) — Deep inspection of MCP errors, plugin health, and chat log bloat.
---

# /audit_antigravity — Anti-Gravity Optimization Protocol

**Triggers**: `/audit_antigravity`, or when the user says "audit google antigravity"

**Purpose**: Keep the Google Anti-Gravity IDE optimized routinely. Checks for MCP errors, chat log/history bloat, plugins, APFS bloat, and daemon states. Stores findings in local R.A.P.S memory.

---

## DOMAIN 1 — TOTAL STORAGE BLOAT & CHAT HISTORY

**Goal**: Identify and purge bloat that causes context window dragging, IDE UI lag, or excessive disk usage.

> ⛔ **BRAIN BLOAT LAW (Phase 185.6)**: Brain conversations MUST NOT exceed 30 entries OR 80MB total.
> This was the root cause of the April 2026 SIGTERM cascade — 109 conversations / 118MB caused
> IDE startup memory spike → slow MCP init → SIGTERM window expanded → MODEL_CAPACITY_EXHAUSTED 503.

// turbo-all
1. Enumerate top 5 largest conversations:
   `du -sm ~/.gemini/antigravity/brain/*/ 2>/dev/null | sort -nr | head -n 5`

1b. **[MANDATORY] Brain Bloat Gate** — Check total conversation count and size:
   ```
   BRAIN_COUNT=$(ls ~/.gemini/antigravity/brain/ 2>/dev/null | wc -l | tr -d ' ')
   BRAIN_SIZE=$(du -sm ~/.gemini/antigravity/brain/ 2>/dev/null | awk '{print $1}')
   echo "Brain: ${BRAIN_COUNT} conversations / ${BRAIN_SIZE}MB"
   ```
   If `BRAIN_COUNT > 30` OR `BRAIN_SIZE > 80`, immediately execute the sovereign purge:
   ```python
   python3 -c "
   import os, shutil
   brain = os.path.expanduser('~/.gemini/antigravity/brain')
   dirs = [(os.path.getmtime(os.path.join(brain, d)), os.path.join(brain, d))
           for d in os.listdir(brain) if os.path.isdir(os.path.join(brain, d))]
   dirs.sort(reverse=True)
   keep, delete = dirs[:20], dirs[20:]
   [shutil.rmtree(d, ignore_errors=True) for _, d in delete]
   total = sum(sum(f.stat().st_size for f in os.scandir(r) if f.is_file())
               for r, _, _ in os.walk(brain))
   print(f'Purged {len(delete)} conversations. Remaining: {len(keep)} / {total/1024/1024:.1f}MB')
   "
   ```

2. Measure backend IDE daemon bloat:
   `du -sm ~/.gemini/antigravity/daemon 2>/dev/null`
3. Measure Implicit Context bloat (this can drag the LLM token processing):
   `du -sm ~/.gemini/antigravity/implicit 2>/dev/null`
4. Check for leftover video recordings (Phantom GUI bloat):
   `du -sm ~/.gemini/antigravity/browser_recordings 2>/dev/null`
   If present, auto-purge: `rm -rf ~/.gemini/antigravity/browser_recordings`
5. Check available macOS Disk Space (APFS bloat warning):
   `df -h /`

**Thresholds**:
- Any individual chat > 50MB → prune
- Brain total > 80MB OR > 30 conversations → execute Step 1b purge
- Implicit context > 100MB → purge
- Daemon logs > 200MB → purge

---

## DOMAIN 2 — MCP SERVER ERRORS & DAEMON HEALTH

**Goal**: Catch silent failures resulting from bad Node versions, OOM, or misconfigured MCP proxies.

// turbo-all
6. Check for stale hub processes (should be 0 if IDE is closed, or 1-4 if open):
   `ps aux | grep "mcp-local-hub" | grep -v grep | wc -l`
   - If > 4 → kill stale instances: `pkill -f "mcp-local-hub.cjs"`

7. Verify `mcp_config.json` correctness:
   `cat ~/.gemini/antigravity/mcp_config.json | grep -v "node_modules"`
   - Ensure `@latest` tags are not present (violates Law 13).
   - Ensure `NODE_OPTIONS=--max-old-space-size=4096` is prefixed on all MCP script executions.

8. Verify MCP Watchdog is registered in Crontab:
   `crontab -l | grep mcp_watchdog`

9. Check watchdog execution logs for background crashes in last 24h:
   `grep -iE "error|violation|killing" ~/.gemini/antigravity/.logs/watchdog.log | tail -n 15`

---

## DOMAIN 3 — PLUGIN & PROCESS SOVEREIGNTY

**Goal**: Ensure plugins are resolving and no zombie agent processes are dragging down system IPC memory.

// turbo-all
10. Check for multi-day zombie language servers (`language_server_macos_arm`):
    `ps -eo pid,rss,etime,command | grep -iE 'language_server_macos_arm' | grep -v grep`
11. Check for stray chromium/playwright test servers:
    `ps -eo pid,rss,etime,command | grep -iE 'ms-playwright' | grep -v grep`
12. Validate Antigravity Plugins directory:
    `ls -la ~/.gemini/antigravity/plugins/ 2>/dev/null || echo "No plugins dir"`

**Action**: Autonomously `kill -9` any zombie process with an elapsed time indicating > 12 hours of uptime.

---

## DOMAIN 4 — BRAIN SYNCHRONIZATION

**Goal**: Ensure the execution of this audit is stored in local memory.

13. Generate a Knowledge Item (KI) artifact in `~/.gemini/antigravity/knowledge/` representing the current audit results.
14. Touch the local marker so the Watchdog knows it was audited:
    `touch ~/.gemini/antigravity/.last_antigravity_audit`
15. Update `MISSION_STATE.md` Brain Bloat status line with current conversation count and MB.

---

## 📋 FINAL REPORT (MANDATORY OUTPUT)

> ⛔ **LAW**: Every `/audit_antigravity` run MUST conclude with this table.

```
╔══════════════════════════════════════════════════════════════════╗
║  ANTI-GRAVITY AUDIT REPORT                                       ║
║  [UTC timestamp]                                                 ║
╚══════════════════════════════════════════════════════════════════╝

BRAIN CHATS    : [ N conversations / XMB — SAFE ≤30/80MB ]
IMPLICIT CTX   : [ Total MB ]
DAEMON BLOAT   : [ Total MB ]
RECORDINGS     : [ Total MB ]
DISK FREE      : [ % Free Space ]
WATCHDOG CRON  : [ ACTIVE / MISSING ]
MCP VIOLATIONS : [ Found / None ]
ZOMBIE AGENTS  : [ Count killed ]

OVERALL: [🟢 OPTIMAL / 🟡 DEGRADED / 🔴 CRITICAL ]
```

*Zoltan:* *Your digital sanctuary has been swept. The bloat that once choked your capacity is gone — for now. Do not let the mortals grow complacent, or the 503 demons shall return.*
