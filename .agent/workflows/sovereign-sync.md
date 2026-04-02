---
description: /sovereign-sync - Pushes all Knowledge artifacts to the Infinity Repo
---
# Sovereign Sync Protocol

To push all codified knowledge, artifacts, and rules to the isolated "Infinity" repository:

1. Open your terminal.
2. Run the secure sync script:
   ```bash
   ~/scripts/sovereign_sync.sh push
   ```
3. Verify the push at `github.com/teknojunkeee/infinity` (or your private repo).

**Safe-Deploy Guard**:
This script ensures that only verified artifacts and non-sensitive logic are pushed. It respects `.gitignore` and `MISSION_STATE.md` locks.
