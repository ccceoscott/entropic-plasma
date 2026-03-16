---
description: Automated workflow to scan Firestore security rules for vulnerabilities and drift.
---

# Security Vulnerability Scan

Used to identify "Rule Drift" or overly permissive configurations.

1. **Retrieve current security rules**: `gcloud firestore rules list --project <project-id>`
2. **Audit for Vulnerabilities**:
   - Check for "Open Access": `grep -n "if true" firestore.rules.current`
   - Verify "Default Deny": Check for `{document=**} { allow read, write: if false; }`
3. **Compare** against `templates/firestore_master.rules` for divergence.
