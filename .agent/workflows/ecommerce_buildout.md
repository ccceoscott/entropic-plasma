# Sovereign CPQ & E-Commerce Buildout (/build-ecommerce)
Description: A strict sequential workflow to deploy E-Commerce/CPQ components correctly within the R.A.P.S. architecture.

## Directives
- Read the requirements from the user. Do not jump to the React front-end immediately.
- Adhere strictly to `.agent/rules/ui_commerce.md` and `.agent/rules/data_commerce.md`.

## Step 1: Database Probing via MCP
- Command the `.firebase-mcp-server` to fetch the current active database schema.
- If schema does not exist for the new product logic, use `write_to_file` to scaffold `zod` schema files inside `functions/src/types/` representing the exact payload shape.

## Step 2: Artifact Driven UI Mockup
- Create an `Artifact` rendering the proposed "Liquid Glass 2.0" Data Table or Shopping Cart implementation. 
- WAIT for the user to approve the mock UI. Do NOT write Next.js code until the conceptual mockup inside the artifact is stamped by the Architect.

## Step 3: Backend Logic (Cloud Functions)
- Only when the UI is conceptually approved, build the `onCall` or Webhook endpoint inside `functions/src/`.
- Ensure idempotency if processing payments.

## Step 4: Frontend Scaffolding
- Generate the React components using the validated Zod models.
- Ensure all states leverage Zustand stores and Framer Motion layout animations.
- Integrate error-handling that surfaces alerts via the globally mounted `<Toaster />`.
