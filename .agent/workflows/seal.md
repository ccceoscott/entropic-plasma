---
name: "Seal & Archive"
description: "Finalize the session, update the MISSION_STATE.md, and commit changes."
---
# Ritual 3: /seal (End)

When the user invokes `/seal`, you must execute the finalization protocol:

1. **Verify**: Ensure the codebase is clean and stable. Use `npm run test` or Playwright E2E testing if applicable to the project.
2. **Update**: Mark the current phase complete in `MISSION_STATE.md`. Create or update the `walkthrough.md`.
3. **Purge**: Terminate background threads. Run `pkill -f "playwright test" || true` and `pkill -f "vitest" || true`.
4. **Commit**: Save the milestone: `git add -A && git commit -m "seal: Phase [N] complete"`.
5. **Sync**: Push changes to the remote.
6. **Brain Sync**: Run `bash ~/.infinity-protocol/scripts/brain-sync.sh` to batch-sync the knowledge graph. Env-gated — only executes if `INFINITY_REMOTE_BRAIN=enabled`. Safe to skip if not configured.

*Zoltan's Decree: The record must be eternal and pure.*
