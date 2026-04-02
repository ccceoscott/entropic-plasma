# Workflow: Debug Pro (Infinity Protocol v3.0)

1. **Live Capture (LCA)**: If the issue is on a live site, use **Playwright** (`browser_navigate`) to reach the URL.
2. **Console Audit**: Execute `browser_console_messages` to capture Chrome console errors.
3. **Visual Context**: Take a `browser_snapshot` to correlate errors with the current UI state.
4. **Deep Analysis (DAA)**: Draft a fix hypothesis in a `Thought` block using the console logs and codebase research.
5. **Repair**: Apply the fix.
6. **Live Validation**: Redeploy and re-run the **Console Audit** to verify the fix in production.
