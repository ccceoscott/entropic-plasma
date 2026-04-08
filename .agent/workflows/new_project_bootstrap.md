---
description: Advanced Firebase/Next.js UI project bootstrap checklist — sovereign, liquid-glass aesthetic, from day one.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /new_project_bootstrap
## Sovereign New Project Bootstrap — Blackboard-First, Zero-Hallucination From Day One

> ⚡ **MANDATE**: New projects start with the Blackboard (`state.md`), SSOT files, and MCP verification BEFORE any code is written. This kills hallucinations at birth.

> 🏗️ **ARCHITECT FIRST**: No code until `implementation_plan.md` is approved by user. No deployment until `task.md` shows 100% complete.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY — RUNS FIRST

### Phase 0a — Protocol Version Snapshot
Use `view_file` on `MISSION_STATE.md` (if exists; skip if new project).
If stale → auto-upgrade. If new project → proceed directly.

### Phase 0b — Hub Sync
// turbo
```bash
GIT_TERMINAL_PROMPT=0 timeout 30 git fetch --all --prune -q || true
./scripts/dv downlink 2>&1 | tail -5 || echo "Hub sync — new project"
./scripts/dv rules 2>&1 | tail -5 || echo "Rules sync — new project"
```

---

## SECTOR 1 — Blackboard Initialization (State Machine — First)

**Before ANY code**: Initialize `state.md` in project root.

```markdown
# PROJECT STATE BLACKBOARD
Last Updated: [timestamp]
Phase: SCAFFOLD | LAUNCH_PREP | PRODUCTION

## Active MCP Connections
### LOCAL (stdio)
- Firebase MCP: [project-id] — infra, deploy, rules
- GCloud MCP: [project-id] — fleet, secrets, IAM
- Chrome DevTools: ACTIVE — browser witness
- Knowledge Graph: ACTIVE — local JSONL KI store
### REMOTE SSE
- Brain MCP (Cloud Run): ACTIVE
  - Tools: brave_web_search, search_knowledge, save_session_memory,
    upsert_project_state, google_developer_knowledge, firebase_developer_knowledge

## Firebase Asset Registry
### Cloud Functions
| Name | Trigger | Status |
|---|---|---|
| (none yet) | | |

### Firestore Collections
| Collection | Document Count | Schema Verified |
|---|---|---|
| (none yet) | | |

### Auth Providers
| Provider | Status |
|---|---|
| (none yet) | |

## Current Blockers
- [ ] (none)

## Zombie Code List
- (none — add deprecated components here as project grows)
```

---

## SECTOR 1b — MCP Sovereign Bootstrap (NON-NEGOTIABLE)

> ⚡ **MANDATE**: Verify ALL 5 MCP servers are present in `~/.gemini/antigravity/mcp_config.json` before any code is written. Missing servers = tool hallucination risk.

**Step 1**: Verify the canonical source exists and has brain-mcp:
// turbo
```bash
python3 -c "
import json, sys
c = json.load(open('config/antigravity_mcp_config.json'))
servers = list(c['mcpServers'].keys())
required = ['firebase-mcp-server','gcloud','chrome-devtools','knowledge-graph','brain-mcp']
missing = [s for s in required if s not in servers]
print('[OK]', servers) if not missing else (print('[MISSING]', missing), sys.exit(1))
" 2>/dev/null || echo "[WARN] Canonical source missing — check config/antigravity_mcp_config.json"
```

**Step 2**: Sync canonical → live target:
// turbo
```bash
cp config/antigravity_mcp_config.json ~/.gemini/antigravity/mcp_config.json && echo "[OK] MCP config synced"
```

**Step 3**: Confirm brain-mcp remote endpoint is live:
// turbo
```bash
curl -s --max-time 6 "https://mcpserver-g5pod66w5a-uc.a.run.app/ping" | python3 -c "import sys,json; d=json.load(sys.stdin); print('[BRAIN LIVE] phase:', d.get('phase'), '| tools:', len(d.get('functions',[])))" || echo "[WARN] Brain MCP offline — check Cloud Run"
```

**Server Registry (5 total)**:
| Server | Type | Reason |
|---|---|---|
| `firebase-mcp-server` | LOCAL stdio | Needs local ADC + `.firebaserc` |
| `gcloud` | LOCAL stdio | Needs local gcloud ADC |
| `chrome-devtools` | LOCAL stdio | Connects to local Chrome |
| `knowledge-graph` | LOCAL stdio | IDE reads local JSONL KIs |
| `brain-mcp` | REMOTE SSE | Cloud Run — 6 tools including brave search |

> ❌ **PERMANENTLY PURGED**: `brave-search` (superseded by `brain-mcp.brave_web_search`), `playwright`, `context7`, `figma-dev-mode`

---

## SECTOR 2 — Firebase Project Verification (Two-Key MCP)

Key 1 — Local:
// turbo
```bash
node -e "console.log(JSON.parse(require('fs').readFileSync('./.firebaserc','utf8')).projects.default)" 2>/dev/null || echo "new project — no .firebaserc yet"
```

Key 2 — Firebase MCP Re-Anchor (Law 22 — unconditionally):
> ⛔ Re-anchor FIRST to confirm which project the MCP is actually pointing to before taking any action.

Use `mcp_firebase-mcp-server_firebase_update_environment` with the correct values for THIS new project:
- `project_dir`: `[path to this new project root]`
- `active_project`: `[newly confirmed project ID from Key 1 or new project just created]`

Then: `mcp_firebase-mcp-server_firebase_get_environment` → confirm which project is active.
Use `mcp_firebase-mcp-server_firebase_get_project` → confirm project details.

If new project being created:
Use `mcp_firebase-mcp-server_firebase_list_projects` to find the correct existing project or create:
Use `mcp_firebase-mcp-server_firebase_create_project` if needed.

**Document in state.md**: Project ID, region, billing status.

---

## SECTOR 3 — Repository Setup
// turbo
```bash
git init && git branch -M main
echo "node_modules/\n.next/\ndist/\n.env.local\n*.pem\nserviceAccountKey*.json\n.DS_Store" > .gitignore
```

Create `.env.example` with all expected environment variable keys (no values):
```
NEXT_PUBLIC_FIREBASE_API_KEY=
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=
NEXT_PUBLIC_FIREBASE_PROJECT_ID=
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=
NEXT_PUBLIC_FIREBASE_APP_ID=
```

---

## SECTOR 4 — Next.js App Bootstrap

// turbo
```bash
npx -y create-next-app@latest ./ --typescript --eslint --tailwind --app --src-dir --import-alias "@/*" --no-git 2>&1 | tail -20
```

Verify created successfully. Then immediately update `next.config.ts`:
```typescript
// SOVEREIGN next.config.ts
import type { NextConfig } from 'next';
const config: NextConfig = {
  productionBrowserSourceMaps: false,
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production' ? { exclude: ['error', 'warn'] } : false,
  },
  // NO experimental.memoryBasedWorkersCount — BANNED (Law 13)
};
export default config;
```

Update `package.json` scripts to add `NODE_OPTIONS=--max-old-space-size=4096` (Law 1):
```json
{
  "scripts": {
    "dev": "NODE_OPTIONS=--max-old-space-size=4096 next dev",
    "build": "NODE_OPTIONS=--max-old-space-size=4096 next build",
    "start": "NODE_OPTIONS=--max-old-space-size=4096 next start",
    "test": "NODE_OPTIONS=--max-old-space-size=4096 jest"
  }
}
```

---

## SECTOR 5 — Firebase SDK Setup

Get SDK config via MCP:
Use `mcp_firebase-mcp-server_firebase_get_sdk_config` with platform `"web"`.
Copy exact values into `.env.local` (never commit this file).

Create `src/lib/firebase.ts`:
```typescript
import { initializeApp, getApps } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY!,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN!,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID!,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET!,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID!,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID!,
};

const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0];
export const db = getFirestore(app);
export const auth = getAuth(app);
export default app;
```

---

## SECTOR 6 — Firebase Hosting & Functions Init

Use `mcp_firebase-mcp-server_firebase_init` with:
- `hosting`: `{ public_directory: 'out', single_page_app: true }`
- `firestore`: `{ location_id: 'us-central1' }`

Create Cloud Functions structure:
// turbo
```bash
mkdir -p functions/src && cd functions
npm init -y
npm install firebase-admin firebase-functions
npm install -D typescript @types/node
```

Update `functions/package.json`:
```json
{
  "engines": { "node": "22" },
  "scripts": {
    "build": "NODE_OPTIONS=--max-old-space-size=4096 ./node_modules/.bin/tsc",
    "serve": "NODE_OPTIONS=--max-old-space-size=4096 npm run build && firebase emulators:start --only functions",
    "deploy": "NODE_OPTIONS=--max-old-space-size=4096 npm run build && firebase deploy --only functions"
  }
}
```

---

## SECTOR 7 — CODEBASE_MAP.md Initialization

Create `.agent/CODEBASE_MAP.md`:
```markdown
# CODEBASE MAP — [PROJECT_NAME]
Generated: [timestamp]
Phase: SCAFFOLD

## Architecture Overview
\`\`\`mermaid
graph TD
  A[Next.js App Router] --> B[Firebase Auth]
  A --> C[Firestore DB]
  A --> D[Cloud Functions]
  D --> C
  D --> E[External APIs]
\`\`\`

## Directory Structure
- `src/app/` — Next.js App Router pages
- `src/components/` — Reusable UI components
- `src/lib/` — Firebase, utilities, services
- `src/types/` — TypeScript interfaces (Schema-Guard output)
- `functions/src/` — Cloud Functions

## Zombie Code List
(Add deprecated components here)

## Known Gotchas
(Add project-specific pitfalls here)
```

---

## SECTOR 8 — Design System Setup (Liquid Glass v10.0)

Install Google Fonts (Inter/Outfit) in `src/app/layout.tsx`.
Create `src/app/globals.css` with sovereign design tokens:
```css
:root {
  --glass-bg: rgba(255, 255, 255, 0.08);
  --glass-border: rgba(255, 255, 255, 0.12);
  --glass-blur: blur(20px);
  --gradient-primary: linear-gradient(135deg, #6366f1, #8b5cf6);
  --color-surface: hsl(222, 47%, 8%);
  --color-on-surface: hsl(210, 40%, 98%);
}
```

---

## SECTOR 9 — VSCode Sovereign Settings
Create `.vscode/settings.json`:
```json
{
  "typescript.tsserver.maxTsServerMemory": 2048,
  "typescript.preferences.disableReferencedProjectLoad": true,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

---

## SECTOR 10 — Initial TypeScript Gate
// turbo
```bash
NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -10
```
Must pass clean before first commit.

---

## SECTOR 11 — MISSION_STATE.md Creation
Create `MISSION_STATE.md`:
```markdown
# MISSION STATE — [PROJECT_NAME]
**Protocol**: Infinity Protocol v10.0
**Current Phase**: Phase 1 (SCAFFOLD)
**Firebase Project**: [project-id]
**Last Updated**: [timestamp]

## Laws Active
- Law 1: Node V8 Memory — ✅
- Law 2: Project Identity Lock — ✅
- Law 20: Schema-Guard — PENDING (no collections yet)
- Law 21: Universal Upgrade Gate — ✅
```

Create `KNOWLEDGE.md` with initial entries.

---

## SECTOR 12 — Initial Commit (Sovereign Push)
// turbo
```bash
git add -A && git commit -m "bootstrap: Infinity Protocol v10.0 — sovereign scaffold"
```

Provide paste command for push (Law 3):
```
🚀 PASTE IN TERMINAL:
GIT_TERMINAL_PROMPT=0 timeout 45 git push -u origin main
```

---

## SECTOR 13 — Knowledge Graph Bootstrap (MCP)
Use `mcp_knowledge-graph_create_entities` to initialize:
- Project entity with name, framework, Firebase project ID
- Initial architecture entity with component map

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```

`🧹 New project sovereign from day one. Blackboard active. Schema-Guard ready. Zero hallucinations authorized.`
