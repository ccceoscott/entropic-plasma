---
name: "Turnover & Handoff"
description: "Pause the operation, log status, and prepare for resumption."
---
# Ritual 2: /turnover (Handoff)

When the user invokes `/turnover`, you must log the context state for later retrieval:

1. **Task**: Mark current open task items with `[/]` to indicate they are active but paused.
2. **Log**: Append a state entry to `handoff_log.json` containing `{phase, status, next_step}`.
3. **Commit**: Safely suspend progress. Run: `git commit -am "wip: turnover [context]" --no-verify`.

*Zoltan's Decree: Time stops, but the memory remains eternal.*
