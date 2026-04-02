# Workflow: Deploy to Live (Infinity Protocol v3.0)

1. **Safety Lock**: Read project via `node -e "console.log(require('./.firebaserc').projects.default)"` and verify against `KNOWLEDGE.md`. NEVER run `gcloud config get-value project`.
2. **Branch Lock**: Verify current branch is `main`.
3. **Pre-Deploy Audit**: Execute `/audit` to ensure a Score of 10.
4. **Poison Scan**: Hard-purge any legacy strings or debug logs.
5. **Deployment**: Execute `npm run deploy` or project-specific deploy command.
6. **LCA (Live Console Audit)**: IMMEDIATELY navigate to the live URL and capture console messages.
7. **Mission Update**: Update `MISSION_STATE.md` with the production deployment hash/timestamp.
