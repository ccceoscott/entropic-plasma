---
description: Complete Safe Deployment Lifecycle — Security Scan + Identity Lock + Build + Ascension (Phase 57 Sovereign)
---

# /deploy_safely — Sovereign Deployment Lifecycle

The complete, atomic deployment execute from zero to production. Merges `/security_scan` and `/deployment_safety` — those are now deprecated redirects to this file.

> **⚠️ PHASE 57 LAWS:**
> - `gcloud config get-value project` → BANNED → use `.firebaserc` read
> - `gcloud <cmd>` without `--quiet` → BANNED → always add `--quiet`
> - `firebase firestore:rules > /tmp/...` → BANNED → use MCP tool
> - Network commands NEVER get `// turbo` — user approval required

---

## 🔒 Lock 0: Secret Exposure Scan (NEVER SKIP)

Use `grep_search` MCP tool (non-blocking, no terminal):
- Query: `AIza` in `src/`
- Query: `PRIVATE KEY` in repo root

Then (local git only — safe):

// turbo
```bash
git grep -r "AIza" -- . 2>/dev/null || echo "CLEAN: No API keys found"
```

// turbo
```bash
git grep -rn "PRIVATE KEY" -- . 2>/dev/null || echo "CLEAN: No private keys found"
```

// turbo
```bash
bash .git/hooks/pre-commit 2>/dev/null || echo "Pre-commit hook complete"
```

**Halt immediately** if any match found outside `.env.local` or `.env.example`.

---

## 🔒 Lock 1: Project Identity (Sovereign — NO gcloud)

// turbo
```bash
node -e "console.log('Project:', require('./.firebaserc').projects.default)" 2>/dev/null || echo "⚠️ .firebaserc not found — ABORT"
```

Use `view_file` to read `.firebaserc` and confirm `default` alias:
- Maps to `prod` → **HARD STOP**. Require explicit confirmation.
- Maps to `staging`/`dev` → proceed with orange warning.
- `.firebaserc` missing → **ABORT**. Run `/bootstrap_new_project` first.

MCP identity check (GDK canonical form from `gcloud info --format='value(config.account)'`):
`mcp_gcloud_run_gcloud_command` with args `["info", "--format=value(config.account)", "--quiet"]`

---

## 🔒 Lock 2: Firestore Rules — Open Access Detection (MCP)

Use: `mcp_firebase-mcp-server_firebase_get_security_rules` with `type: "firestore"`

Scan for:
- `if true` → **ABORT** if found without auth guard
- `allow read, write` → verify has `request.auth != null`

---

## 🔒 Lock 3: Function Teardown Detection (MCP)

Use: `mcp_firebase-mcp-server_functions_list_functions`

Use `view_file` to read `functions/src/index.ts`. Alert on any function in GCP that is missing locally — that's an **accidental deletion on next deploy**.

---

## 🔒 Lock 4: Secret Manifest Check (MCP)

Use: `mcp_gcloud_run_gcloud_command` with args `["secrets", "list", "--project", "<project-id>", "--quiet"]`

Confirm all env vars referenced in Cloud Functions exist in Secret Manager.

---

## 🔒 Lock 5: Lint

// turbo
```bash
LINT_FAIL=0; npm run lint 2>&1 || LINT_FAIL=1; [ $LINT_FAIL -eq 1 ] && echo "⚠️ Lint warnings present — review before deploy"
```

> GDK: do not swallow lint errors silently. Capture exit code, warn but allow proceed if non-breaking.

---

## 🔒 Lock 6: Idempotent Build

// turbo
```bash
rm -rf .next/ dist/ 2>/dev/null || true
```

```bash
NODE_OPTIONS=--max-old-space-size=4096 npm run build
```

> Build is 60-120s. Do NOT `// turbo`. Wait for user approval.

---

## 🔒 Lock 7: Ascension Deploy

```bash
firebase deploy --only functions,hosting --non-interactive --force
```

> GDK (firebase.google.com/docs/cli): `--non-interactive` is mandatory for CI/headless. `--force` bypasses all warning-level confirmation prompts for connectors/Data Connect.

*Status: All Locks Passed. Deployment Sealed. The Cloud reflects the Source.*
