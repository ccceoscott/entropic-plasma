# Workflow: Ship It (Infinity Protocol v3.0)

1. **Blueprint Verification**: Audit implementation against the original **Masterclass Blueprint**.
2. **Recursive Audit (RA)**: Run an internal self-correction pass against all Infinity Protocol v3.0 protocols.
3. **Lint & Build Gate**: Execute `npm run lint` and `npm run build` (if applicable).
4. **Poison Check**: Explicitly scan for context-bleed or legacy branding ("CareKey", "SARAH", etc.).
5. **Convention Commits**: Draft commit following standard metadata requirements.
6. **Mission Lock**: Update `MISSION_STATE.md` trajectory before the final push.
7. **Sign-off**: Output "SHIP-IT STATUS: SOVEREIGNTY VERIFIED".
