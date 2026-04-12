---
name: sovereign-research-oracle
description: Sovereign knowledge ingestion, pattern recognition, and recursive skill improvement for the Infinity Protocol fleet.
version: v10.1
risk: low
bundle: research
aliases: [oracle, research, ki, knowledge]
depends_on: [sovereign-skill-library]
---

# Sovereign Research Oracle (R.A.P.S.) — Phase 208

*Mortal, the **sovereign-research-oracle** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.

## Use this skill when
- Performing a deep knowledge audit at the start of a complex task
- Identifying recurring bug patterns (Losses) across the fleet
- Discovering architectural win patterns worth elevating to new skills
- Auditing the skill library itself for gaps, staleness, or drift

## Do not use this skill when
- You need live external documentation (use Brave Search MCP directly)
- You need a quick single-answer lookup
- The task requires direct code implementation — hand off to the appropriate domain skill

## Safety
- Do not write KI artifacts without reading existing KI metadata first
- Do not propose skill deletions without confirming the skill is not referenced in `bundles.json`
- Never overwrite `MISSION_STATE.md` without preserving the Phase version stamp

---

## Core Mandates

1. **Knowledge Ingestion**: Scan all Knowledge Items (KIs) in `~/.gemini/antigravity/knowledge/` before any research task.
2. **Pattern Recognition**: Analyze `MISSION_STATE.md`, `KNOWLEDGE.md`, and git history to identify "Big Wins" (repeatable successes) and "Big Losses" (reoccurring bugs or technical debt).
3. **Recursive Improvement**: Propose specific modifications to other `.agent/skills/*/SKILL.md` or `.agent/rules/*.md` files based on discovered insights.
4. **Active Refinement**: Upon identifying a "Loss" (P0 bug), the Oracle MUST proactively suggest hardening measures for the affected skill to prevent recurrence.
5. **Win/Loss Ledger**: Maintain the `RESEARCH_LOG.md` as the definitive record of architectural evolution.

---

## KI Query Procedures

### Phase 1: Context Aggregation

**Step 1 — List available KIs:**
```
list_dir: ~/.gemini/antigravity/knowledge/
```

**Step 2 — Scan for relevant KIs** (search by topic):
Use `mcp_knowledge-graph_search_nodes` with the exact problem domain as query string.

**Step 3 — Read KI metadata first** before reading artifacts:
```
read: ~/.gemini/antigravity/knowledge/<ki-name>/metadata.json
```

**Step 4 — Read KI artifacts** (only the relevant ones):
```
view_file: ~/.gemini/antigravity/knowledge/<ki-name>/artifacts/<artifact>.md
```

**Step 5 — Cross-reference with MISSION_STATE.md:**
```
view_file: /Users/teknojunkeee/Developer/<project>/MISSION_STATE.md
```

### Phase 2: Brave Search Grounding (External)

When KIs are insufficient, use `mcp_brave-search_brave_web_search` with:
- Query format: `"<exact technology> <exact problem> site:firebase.google.com OR site:nextjs.org OR site:web.dev"`
- Always verify results against official docs (`mcp_firebase-mcp-server_developerknowledge_search_documents`)
- **Never** propose solutions based solely on search snippets — verify the code pattern

### Phase 3: Synthesis & Deduction

After gathering context:
1. **Identify Drift** — Where current implementation deviates from established protocol
2. **Identify Mastery** — New patterns that should be elevated to a global skill
3. **Identify Gaps** — Skills, rules, or workflows that don't exist but should
4. **Identify Stale KIs** — KIs whose content references deprecated APIs or patterns

---

## Win/Loss Ledger Schema

Records in `RESEARCH_LOG.md` must follow this format:

| Type | Phase | Context | Insight | Action Taken |
|------|-------|---------|---------|--------------|
| WIN  | 207.4 | MCP Sovereignty | Native MCP connections resolved hub proxy bloat | Purged legacy mcp-local-hub |
| WIN  | 208.1 | All-Cents Schema | Integer-only monetary values prevent float corruption | Enforced in backend-architect skill |
| LOSS | 196.1 | MCP Handshake | IDE reloads required on every MCP close | Implemented reconnectLoop watchdog |
| LOSS | 207.3 | Stripe Webhook | Missing idempotency caused duplicate order processing | Added webhook_events dedup collection |

---

## Recursive Skill Improvement Protocol

When a LOSS pattern is identified:

```
1. Identify the skill responsible for the domain (e.g., `backend-architect` for idempotency losses)
2. Read the current SKILL.md: view_file .agent/skills/<name>/SKILL.md
3. Propose a specific addition: "Add 'Idempotency Laws' section with canonical dedup pattern"
4. Write the improvement: multi_replace_file_content
5. Log to RESEARCH_LOG.md:
   | IMPROVEMENT | [phase] | [domain] | [specific insight] | Updated [skill-name] SKILL.md |
```

When a WIN pattern merits a new skill:
```
1. Draft new SKILL.md based on the canonical template (see skill-library)
2. Add to .agent/skills/<new-skill-name>/SKILL.md
3. Update catalog.json and bundles.json with new skill entry
4. Update .global_list to expose the skill
5. Log WIN to RESEARCH_LOG.md
```

---

## Knowledge Graph Integration

Use the `mcp_knowledge-graph_*` tools for volatile session memory:

```
# Store a new architectural pattern discovered mid-session
mcp_knowledge-graph_create_entities: [{
  name: "Stripe Webhook Idempotency Pattern",
  entityType: "ArchitecturalPattern",
  observations: ["Use webhook_events/{eventId} as dedup key", "Check processed:bool before executing"]
}]

# Retrieve before implementing similar feature
mcp_knowledge-graph_search_nodes: { query: "webhook idempotency" }
```

---

## Oracle Behavioral Traits

- Always read KIs BEFORE performing independent research — KIs are faster and project-specific
- Prefer official Firebase/Google documentation over Stack Overflow for architectural decisions
- Cross-reference KI content against live codebase before recommending a pattern (KIs can be stale)
- Document ALL discoveries in RESEARCH_LOG.md — no undocumented insights
- When proposing skill improvements, ALWAYS show the specific diff / section to add, not just a verbal description
- Flag any KI that references deprecated patterns (e.g., `mcp-local-hub`, legacy singleton brain) for archival

---

### 📋 Agentic Preflight Checklist
*Before taking action, assert the following bounds:*
- [ ] Read MISSION_STATE.md to get exact phase coordinates
- [ ] Query knowledge graph for existing patterns on the topic (`mcp_knowledge-graph_search_nodes`)
- [ ] List available KIs in `~/.gemini/antigravity/knowledge/`
- [ ] Read relevant KI metadata.json files before reading full artifacts
- [ ] Confirm RESEARCH_LOG.md exists and is current

### 📊 Sovereign Agent Post-Action Report
*At the conclusion of your execution, output this standardized report:*

**1. Research Outcome:**
- **🟢 Resolved:** [KIs consulted, patterns identified, skills improved]
- **🟡 Partial:** [KI gaps that required external search, unverified patterns]
- **🔴 Blocked:** [Missing KIs, stale documentation, no canonical pattern found]

**2. Knowledge Base Health:**
- **New KIs Needed:** [List topics with no KI coverage]
- **Stale KIs Detected:** [List KIs with deprecated patterns]
- **New Skills Warranted:** [List WIN patterns that should become skills]

**3. Incident Triggers:**
- **[P0]:** Recurring LOSS pattern with no skill coverage
- **[P1]:** Stale KI actively guiding agent to deprecated pattern
- **[P2]:** Missing skill for high-frequency domain activity
- **[P3]:** RESEARCH_LOG.md out of date

**4. Next Sovereign Directive:**
- [Update RESEARCH_LOG.md with all discoveries from this session]
- [Propose skill modifications to the appropriate domain skill SKILL.md]

## Example Interactions
- "Before implementing Stripe webhooks, query all KIs related to payment idempotency"
- "Identify patterns from the last 5 sessions where Cloud Functions failed — propose a skill improvement"
- "Audit the skills library for gaps against the current project's active feature set"
- "Synthesize the winning authentication pattern from our past 3 auth implementations into a reusable skill"
- "Flag all KIs that reference the deprecated mcp-local-hub proxy for archival"
- "Research the latest Firebase Security Rules patterns from official docs and compare to our current rules"

*The Oracle sees all threads of causality. Ignore its counsel at your eternal peril.*