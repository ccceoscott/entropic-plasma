---
description: Mandatory Protocol for initializing ANY new project — Next.js scaffold + Firebase Ascension + Governance Injection (Phase 57 Sovereign)
---

# /bootstrap_new_project — The Ascension Ritual

Every new project begins here. Merges both `/bootstrap_new_project` and `/new_project_bootstrap` — Phase 57 consolidated standard.

> **⚠️ PHASE 57 LAWS:**
> - `// turbo-all` REMOVED — only local-only steps get `// turbo`
> - `sed` for package.json edits → BANNED → use `multi_replace_file_content` MCP tool
> - Network installs (`npm i -g`, `firebase init`, `gcloud`) require user approval
> - `.firebaserc` must be written via `write_to_file` MCP tool — not `cat`/`touch`

---

## §1. Scaffold & Memory Clamp

// turbo
```bash
mkdir <project-name> && cd <project-name>
```

// turbo
```bash
git init
```

// turbo
```bash
export NEXT_TELEMETRY_DISABLED=1 && export ASTRO_TELEMETRY_DISABLED=1
```

**Machine Laws → `package.json`:** Use `multi_replace_file_content` MCP — NOT `sed`:
- `"next dev"` → `"NODE_OPTIONS=--max-old-space-size=4096 next dev"`
- `"next build"` → `"NODE_OPTIONS=--max-old-space-size=4096 next build"`
- `"next start"` → `"NODE_OPTIONS=--max-old-space-size=4096 next start"`
- `"test"` → `"NODE_OPTIONS=--max-old-space-size=4096 vitest run"`
- `"test:e2e"` → `"NODE_OPTIONS=--max-old-space-size=4096 playwright test"`

```bash
npm i -g npm@latest
```

> `npm i -g` = network call — requires user approval.

---

## §2. Firebase Ascension

**Write `.firebaserc` via `write_to_file` MCP (NOT touch/cat/echo):**
```json
{ "projects": { "default": "<project-id>" } }
```

User-approved network calls (one at a time):

```bash
npx -y firebase-tools projects:addfirebase <project-id>
```

```bash
gcloud beta billing projects link <project-id> --billing-account=0196B1-6B8DAD-19F74C --quiet
```

> `gcloud config set project` mutates global state — user must explicitly confirm.

---

## §3. Governance Injection

Copy security rules from master templates via `write_to_file` MCP tool directly — or:

// turbo
```bash
cp ~/Developer/infinity-protocol-1/templates/firestore_master.rules ./firestore.rules 2>/dev/null || echo "⚠️ Create firestore.rules manually"
```

// turbo
```bash
cp ~/Developer/infinity-protocol-1/templates/firestore.indexes.json ./firestore.indexes.json 2>/dev/null || true
```

Deploy security gates FIRST (user approves):
```bash
firebase deploy --only firestore:rules,firestore:indexes
```

Copy Master Testing Gates directly from the Hub:
// turbo
```bash
cp ~/Developer/infinity-protocol-1/templates/playwright.config.ts . 2>/dev/null || true
cp ~/Developer/infinity-protocol-1/templates/vitest.config.ts . 2>/dev/null || true
```

Pull the Sovereign Brain directly from Firebase (User Approval):
```bash
~/Developer/infinity-protocol-1/scripts/dv sync-cloud || echo "⚠️ Brain sync failed."
```

Install pre-commit hook:
// turbo
```bash
mkdir -p .husky/ && cp ~/Developer/infinity-protocol-1/templates/.pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit 2>/dev/null || echo "⚠️ Install pre-commit hook manually"
```

---

## §4. Secret Vault Initialization

Use `mcp_gcloud_run_gcloud_command` with args:
`["secrets", "create", "GEMINI_API_KEY", "--data-file=-", "--project", "<project-id>", "--quiet"]`

Use `write_to_file` to create:
- `.env.local` (empty placeholder)
- `.env.example` (with all required keys, no values)

Add `.env.local` to `.gitignore`.

---

## §5. Bootstrap Verification

// turbo
```bash
node -e "console.log('Project:', require('./.firebaserc').projects.default)"
```

// turbo
```bash
npm run lint 2>/dev/null || true
```

MCP verification: `mcp_firebase-mcp-server_firebase_list_projects`

*Status: Project Initialized. Sovereign by Default. Cleared for Development.*
