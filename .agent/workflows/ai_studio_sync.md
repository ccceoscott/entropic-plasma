---
description: Automated induction and wiring of Google AI Studio web app exports with Law 20 precision.
alwaysApply: false
---

# INFINITY PROTOCOL v10.0 — /ai_studio_sync

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/ai-studio-integrator/SKILL.md` — Google AI Studio export induction, Next.js wiring, Law 20 precision
## Sovereign AI Studio Induction — Proto-to-Prod Transformation

The **/ai_studio_sync** workflow is the primary ritual for transforming "vibe-coded" AI Studio exports into hardened, production-ready Infinity Protocol applications.

---

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY
Execute Phase 0 established in `MISSION_STATE.md`.
1. **Downlink Check**: `./scripts/dv downlink`
2. **Rules Audit**: `./scripts/dv rules`
3. **TSC Gate**: `cd functions && ./node_modules/.bin/tsc`

---

## SECTOR 1 — Artifact Identification
Identify the nature of the imported "vibe" app.
1. **Grep Scan**: `grep -r "@google/generative-ai" .`
2. **Blueprint Generation**: Run `node scripts/ai-studio-align.cjs [PATH]` to generate `INDUCTION_BLUEPRINT.json`.
3. **Manifest Audit**: Review `INDUCTION_BLUEPRINT.json` for detected collections and inferred schemas.

---

## SECTOR 2 — Protocol Anchoring (Law 20)
Enforce **Schema-Guard** precision.
1. **Type Realization**: Append inferred interfaces from the blueprint to `types/firebase.d.ts`.
2. **Import Normalization**:
   - Swap `import { db } from "../firebase"` with standardized project path binders.
   - Use `types/firebase.d.ts` for all database calls (ZERO `any` usage).
3. **Law 1 Enforcement**:
   - Prefix all build/dev scripts in `package.json` with `NODE_OPTIONS=--max-old-space-size=4096`.

---

## SECTOR 3 — Blueprint Realization (APIs & Agents)
Scaffold the backend sovereign.
1. **API Realization**: Proactively scaffold `functions/src/triggers/on[Collection][Event].ts` for all detected collections.
   - Use standard trigger templates with Liquid Glass logging.
2. **Agent Provisioning**: Register a new "Service Agent" in the `agents` Firestore collection to curate the new data stream.
3. **Secret Registration**: Register any redacted keys in GCloud Secret Manager.

---

## SECTOR 4 — Aesthetic Infusion
Inject the **Liquid Glass** aesthetic.
1. **Index.css Alignment**: Ensure CSS translucency tokens are present.
2. **Component wrapping**: Apply `framer-motion` and `backdrop-blur` to root containers.
3. **Aesthetic Audit**: Use `sovereign-aesthetic-auditor` on primary routes.

---

## SECTOR 5 — Backend Handover
Wire the "vibe" app to the real world.
1. **Auth Handover**: Execute `/setup_auth` to configure real providers.
2. **Database Handover**: Execute `/setup_database` to deploy audited Security Rules.

---

## SECTOR 6 — Browser Witness Gauntlet
Verify the transformation.
1. **Spawn Eye**: Command the `browser_subagent` to test the wiring.
2. **E2E Check**: Verify Sign-in → Persistent Session → Firestore Write → Trigger Execution.
3. **Seal**: Update `MISSION_STATE.md` to Phase [N].

---

## ⚡ Phantom Purge
// turbo
```bash
rm -rf ~/.gemini/antigravity/browser_recordings
```
`🧹 AI Studio sync complete. Law 20 active. Service Agents commissioned.`
