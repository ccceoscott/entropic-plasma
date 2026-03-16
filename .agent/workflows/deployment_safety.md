---
description: Automated workflow to verify project aliases and prevent accidental production deployments.
---

# Deployment Safety Verification

Used to prevent accidental production deployments.

1. **Check Active Project Alias**: `firebase use`
   // turbo
2. **Check Defined Aliases**: `cat .firebaserc`
3. **Safety Logic**:
   - If active project is a `prod` alias, REQUIRE manual confirmation.
   - If active project is `staging` or `dev`, proceed with warning.
4. **Verify Functions (Prevent Deletion)**: Check for potential function teardowns before confirming.
5. **Proceed** to `firebase deploy`.
