---
description: Infinity Protocol Test Driven Operating Procedure
globs: *.test.ts, *.test.tsx, *.spec.ts, *.spec.tsx
---
# Infinity Protocol Test Suite Workflow

This document outlines the standard operating procedure for creating and running tests within an Infinity Protocol project.

## Initialization

If the current project does not have testing configured, run the setup script:
```bash
~/infinity/scripts/setup_testing.sh
```
This scaffold configures **Vitest** (Unit/Component) and **Playwright** (End-to-End).

## Running Tests

### Unit & Component (Vitest)
```bash
# Run all unit tests
npm run test

# Run tests with coverage reporting (v8)
npm run test:coverage

# Run in watch mode
npm run test:watch
```

### End-to-End & Visual (Playwright)
```bash
# Run all E2E tests in headless mode
npm run test:e2e

# Run with UI mode for debugging
npm run test:e2e:ui
```

### Continuous Integration
Projects scaffolded with `setup_testing.sh` automatically include `.github/workflows/test.yml`. This workflow:
1. Installs Node.js & dependencies.
2. Installs Playwright browsers.
3. Starts Firebase Emulators.
4. Executes Vitest (with coverage) and Playwright.

## Writing Tests

### Visual Regression
Use snapshots for stable, premium UI components:
```typescript
test('visual check', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveScreenshot('hero-section.png');
});
```

### Coverage Standards
- Strive for >80% coverage on shared UI components and utility libraries.
- Use `npm run test:coverage` to identify blind spots in business logic.
- **Run tests headed (visible browser)**: `npm run test:e2e --headed`
- **Run specific test file**: `npm run test:e2e e2e/login.spec.ts`

## Writing Tests

1. **Unit Tests (`*.test.ts`)**: Put these alongside the source code (`src/components/Button.tsx` -> `src/components/Button.test.tsx`).
2. **E2E Tests (`e2e/*.spec.ts`)**: Put these inside the `e2e/` folder at the project root.
3. Every public-facing API endpoint (`app/api/**/*`) MUST have an integration test verifying standard and erroneous inputs.
4. Always mock external payment APIs (Stripe) and use emulators for Firebase.

## Continuous Integration (CI)

When deploying, the CI pipeline automatically executes `npm run test` and `npm run test:e2e`. A failing test will hard-block deployment to production per the Apex Sovereignty protocol.
