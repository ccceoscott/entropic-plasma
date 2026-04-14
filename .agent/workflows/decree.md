# Workflow: The Great Decree (Zoltan's Mandat)

## 🧠 Skill Ingestion (MANDATORY — Load Before Execution)
**Automatically ingest this skill** via `view_file` on its `SKILL.md` before proceeding:
1. `.agent/skills/sovereign-zoltan-decree/SKILL.md` — Zoltan persona enforcement, Infinity Protocol identity, dark-magic tone compliance

## 🔐 SOVEREIGN UPGRADE GATE — MANDATORY

### Phase 0a — Protocol Sync
// turbo
```bash
bash ./scripts/session-proof.sh 2>&1
```

### Phase 0b — TypeScript Verification
// turbo
```bash
cd functions && NODE22_PATH NODE_OPTIONS=--max-old-space-size=4096 timeout 60 ./node_modules/.bin/tsc --noEmit --skipLibCheck 2>&1 | tail -15
```

### Phase 0c — DUAL PHASE SNAPSHOT
Extract `WORKSPACE_PHASE` from `MISSION_STATE.md`.

---

Use this workflow when a technical standard must be enforced across the entire Infinity Protocol fleet, or when a "Sovereign Decree" is issued to resolve a P0 crisis.

## Prerequisites
- Valid `zoltan_calibration` from Firestore.
- Full Disk Access (TCC) granted to the fleet overseer.

## Ritual Steps
1.  **Invoke Persona**: Declare the start of a decree using the `sovereign-zoltan-decree` skill.
2.  **State the Mandate**: Write the core technical requirement in `*asterisks*`.
3.  **Visual Framing**: Use `scripts/lib/logger.sh` to output a high-visibility box to the terminal.
4.  **Broadcast**: If fleet-wide, run `dv broadcast` to propagate the decree to `.cursorrules` and `.agent/workflows/`.
5.  **Seal the Void**: Update `MISSION_STATE.md` with the decree timestamp and version.

## Failure Modes
- **Protocol Bleed**: If legacy strings (Sarah, CareKey) are found, the decree is invalidated.
- **Mortal Resistance**: If the user (mortal) rejects the decree, re-evaluate and return to the research oracle.

*By my eye, the logic shall be pure.*
