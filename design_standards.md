# UI & Design Standards (Strict Adherence Required)

## 1. Core Stack
- **Styling:** Tailwind CSS (Utility-first).
- **Components:** Shadcn/ui (Radix Primitives).
- **Icons:** Lucide React.

## 2. Spacing System (The 4px Grid)
*Never use arbitrary pixels (e.g., 13px, 55px).* Always use Tailwind spacing classes.
- **Small Spacing (Elements inside a card):** `gap-2` (8px) or `gap-3` (12px).
- **Medium Spacing (Between cards/sections):** `gap-6` (24px) or `gap-8` (32px).
- **Large Spacing (Page sections):** `py-12` (48px) or `py-24` (96px).
- **Container Padding:** Always use `p-4` or `p-6` for mobile, `p-8` for desktop.

## 3. Component Standards
- **Buttons:**
  - Primary: `bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md`
  - Secondary: `bg-secondary text-secondary-foreground hover:bg-secondary/80 h-10 px-4 py-2 rounded-md`
  - Destructive: `bg-destructive text-destructive-foreground hover:bg-destructive/90`
- **Cards/Modals:**
  - Border: `border border-border`
  - Shadow: `shadow-sm`
  - Radius: `rounded-xl` (Consistent across all apps)
  - Background: `bg-card text-card-foreground`

## 4. Typography Hierarchy
- **H1 (Page Titles):** `text-3xl font-bold tracking-tight lg:text-4xl`
- **H2 (Section Headers):** `text-2xl font-semibold tracking-tight`
- **H3 (Card Titles):** `text-xl font-semibold tracking-tight`
- **Body Text:** `text-sm text-muted-foreground` (for descriptions) or `text-base` (for reading).

## 5. Interactive States
- All interactive elements must have: `focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2`.
- All hover states must be standardized (e.g., `hover:bg-accent`).
