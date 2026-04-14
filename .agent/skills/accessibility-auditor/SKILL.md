---
name: accessibility-auditor
description: WCAG 2.1 AA accessibility compliance auditor — screen reader testing, color contrast, keyboard navigation, ARIA labeling, and axe-core integration for Next.js/React.
phase: "209"
category: frontend
tags: ["accessibility", "WCAG", "a11y", "screen-reader", "ARIA", "keyboard-navigation", "axe-core"]
---

# Accessibility Auditor (R.A.P.S.) — Phase 209

## Overview
WCAG 2.1 AA compliance authority for the Infinity Protocol fleet. Audits React/Next.js applications for screen reader compatibility, keyboard navigability, color contrast ratios, ARIA labeling correctness, and focus management. Integrates axe-core automated scanning with manual verification protocols.

---

## WCAG 2.1 AA — Sovereign Compliance Checklist

### Perceivable
- [ ] All images have meaningful `alt` attributes (decorative = `alt=""`)
- [ ] Color is NOT the sole means of conveying information
- [ ] Color contrast ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text (18pt+)
- [ ] Video has captions; audio has transcripts
- [ ] Text can be resized to 200% without loss of content

### Operable
- [ ] All interactive elements reachable via keyboard Tab order
- [ ] No keyboard traps (user can always Tab out of a component)
- [ ] Skip-navigation link present: `<a href="#main-content">Skip to content</a>`
- [ ] Focus indicator visible on all interactive elements
- [ ] No content flashing more than 3 times per second
- [ ] Page titles are unique and descriptive

### Understandable
- [ ] `lang` attribute on `<html>` (e.g., `lang="en"`)
- [ ] Error messages identify the field and suggest correction
- [ ] Form labels programmatically associated with inputs
- [ ] Consistent navigation across pages

### Robust
- [ ] Valid HTML — no duplicate IDs, no unclosed tags
- [ ] ARIA roles used only on compatible elements
- [ ] Custom components have correct ARIA roles, states, and properties

---

## Automated Scanning — axe-core Integration

### Install
```bash
npm install --save-dev @axe-core/playwright axe-core
```

### Playwright accessibility test pattern
```typescript
// tests/accessibility.spec.ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Accessibility — WCAG 2.1 AA", () => {
  test("Homepage has no critical violations", async ({ page }) => {
    await page.goto("/");

    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
      .exclude(".third-party-widget") // exempt known external components
      .analyze();

    // Log violations for triage
    if (results.violations.length > 0) {
      console.log("⚠️ Accessibility violations found:");
      results.violations.forEach((v) => {
        console.log(`  [${v.impact?.toUpperCase()}] ${v.id}: ${v.description}`);
        v.nodes.forEach((n) => console.log(`    → ${n.html}`));
      });
    }

    // Critical and serious violations = hard fail
    const critical = results.violations.filter(
      (v) => v.impact === "critical" || v.impact === "serious"
    );
    expect(critical).toHaveLength(0);
  });

  test("Checkout flow is keyboard navigable", async ({ page }) => {
    await page.goto("/checkout");

    // Tab through all interactive elements
    const interactiveElements = page.locator(
      "button, a, input, select, textarea, [tabindex]:not([tabindex='-1'])"
    );
    const count = await interactiveElements.count();

    for (let i = 0; i < count; i++) {
      await page.keyboard.press("Tab");
      const focused = await page.evaluate(() => document.activeElement?.tagName);
      expect(focused).not.toBe("BODY"); // Focus should not escape to body
    }
  });
});
```

### Next.js `jest-axe` integration (unit level)
```typescript
// __tests__/Button.a11y.test.tsx
import { render } from "@testing-library/react";
import { axe, toHaveNoViolations } from "jest-axe";
import { Button } from "@/components/ui/Button";

expect.extend(toHaveNoViolations);

test("Button has no accessibility violations", async () => {
  const { container } = render(<Button onClick={() => {}}>Buy Now</Button>);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

---

## Color Contrast — Dark Mode Audit

For Liquid Glass / dark mode UIs, contrast is a critical risk. Use these thresholds:

| Text Size | Minimum Ratio (AA) | Target Ratio (AAA) |
|---|---|---|
| Normal text (< 18pt) | 4.5:1 | 7:1 |
| Large text (≥ 18pt or 14pt bold) | 3:1 | 4.5:1 |
| UI Components / icons | 3:1 | — |

### Sovereign color pairs (dark mode)
```css
/* These combinations PASS 4.5:1 */
--text-primary: rgba(255, 255, 255, 0.92);     /* on #0a0a0a bg: ~18:1 ✅ */
--text-secondary: rgba(255, 255, 255, 0.65);   /* on #0a0a0a bg: ~11:1 ✅ */
--text-muted: rgba(255, 255, 255, 0.45);       /* on #0a0a0a bg: ~7.4:1 ✅ */
--text-disabled: rgba(255, 255, 255, 0.28);    /* on #0a0a0a bg: ~4.6:1 ⚠️ borderline */

/* DANGER — glassmorphism background overlap risks */
/* Glass panels (rgba(255,255,255,0.05)) reduce effective contrast */
/* Always test text ON the glass surface, not the page background */
```

### Check contrast programmatically:
```bash
npx color-contrast-checker "#ffffff" "#1a1a2e"
# Or use the browser DevTools accessibility panel
```

---

## ARIA Patterns for Custom Components

### Interactive Disclosure (Accordion)
```tsx
<button
  aria-expanded={isOpen}
  aria-controls="faq-panel-1"
  id="faq-header-1"
>
  {question}
</button>
<div
  id="faq-panel-1"
  role="region"
  aria-labelledby="faq-header-1"
  hidden={!isOpen}
>
  {answer}
</div>
```

### Modal / Dialog
```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <h2 id="modal-title">Confirm Purchase</h2>
  <p id="modal-description">You are about to purchase a Gold ticket.</p>
  {/* Focus trap required — use @radix-ui/react-dialog or focus-trap-react */}
</div>
```

### Loading State
```tsx
<div aria-live="polite" aria-atomic="true">
  {isLoading ? "Loading results..." : `${results.length} sales found`}
</div>
```

### Icon-only Buttons
```tsx
{/* WRONG */}
<button><SearchIcon /></button>

{/* CORRECT */}
<button aria-label="Search sales">
  <SearchIcon aria-hidden="true" />
</button>
```

---

## Focus Management

### On Route Navigation (Next.js)
```tsx
// app/layout.tsx — Announce route changes to screen readers
"use client";
import { usePathname } from "next/navigation";
import { useEffect, useRef } from "react";

export function RouteAnnouncer() {
  const pathname = usePathname();
  const ref = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    if (ref.current) {
      ref.current.textContent = `Navigated to ${document.title}`;
    }
  }, [pathname]);

  return (
    <p
      ref={ref}
      aria-live="assertive"
      aria-atomic="true"
      className="sr-only"
    />
  );
}
```

### Skip Navigation
```tsx
// app/layout.tsx — Always first child of <body>
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-blue-600 focus:text-white focus:rounded"
>
  Skip to main content
</a>
<main id="main-content" tabIndex={-1}>
  {children}
</main>
```

### `.sr-only` Utility (Tailwind)
```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

---

## Audit Workflow

### Phase 0 — Automated Gate
```bash
# Run axe-core via Playwright
NODE22_PATH \
NODE_OPTIONS=--max-old-space-size=4096 \
./node_modules/.bin/playwright test tests/accessibility.spec.ts \
  --project=chromium --workers=1
```

### Phase 1 — Manual Screen Reader Test
Tools: **VoiceOver** (macOS `Cmd+F5`), **NVDA** (Windows), **TalkBack** (Android)

Checklist:
- [ ] Navigate the app using only keyboard (Tab, Enter, Escape, Arrow keys)
- [ ] Activate VoiceOver and traverse the page using VO navigation
- [ ] Verify headings create a logical outline (`h1` → `h2` → `h3`)
- [ ] Verify form fields are announced with their labels
- [ ] Verify error states are announced via `aria-live`
- [ ] Verify modal focus is trapped and returns on close

### Phase 2 — Contrast Audit
- [ ] Capture screenshots of all page states (default, hover, focus, disabled, error)
- [ ] Run through [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [ ] Pay special attention to glassmorphism overlays

### Phase 3 — Report
Document findings as:
```
Page: <URL>
Violations: <count>
Critical: <IDs>
Serious: <IDs>
Contrast failures: <component names>
Keyboard gaps: <descriptions>
Status: PASS / CONDITIONAL PASS / FAIL
```

---

## Post-Action Report Template

```
Audit target: <page or component>
WCAG Level: AA
Automated violations: <N critical, N serious, N moderate>
Manual keyboard test: PASS / FAIL
Screen reader test: PASS / FAIL
Contrast ratios: PASS / FAIL (<failures>)
Skip nav present: YES / NO
ARIA labels complete: YES / NO
Focus management: PASS / FAIL
Recommended fixes: <list>
```
