---
description: Environment Verification (God Mode)
---
# God Mode Environment Verification

Run this to ensure the "God Mode" stack is fully operational.

## 1. 🔌 MCP Server Status
- [ ] **GitHub:** Call `mcp_github-mcp-server_search_repositories` ("test").
- [ ] **Memory:** Call `mcp_memory_read_graph`.
- [ ] **Firebase:** Call `mcp_firebase-mcp-server_firebase_list_projects`.
- [ ] **Stripe:** Call `mcp_stripe_list_resources` ("stripe").

## 2. 🛠️ Global Binaries
- [ ] **Check Paths:**
    ```bash
    which firebase
    which stripe
    which gcloud
    ```
    - Should NOT be inside `node_modules` (unless scoped) or shimmed by `npx` excessively.

## 3. 🧠 Neural Link
- [ ] **Identity:**
    - Can the agent recall "Scott" and "More Bass"? (Via Memory MCP).

## 4. 🎨 Design & Rules
- [ ] **Artifacts:**
    - Verify `user_identity.md` exists.
    - Verify `global_rules.md` exists.
