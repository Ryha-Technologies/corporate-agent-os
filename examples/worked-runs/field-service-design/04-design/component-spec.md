# Component specification

Role: design-systems-engineer (T-005). Reviewed: design-qa-auditor. Tokens: `design-tokens.json` (schema-validated; contrast computed).

## Status chip
**Purpose:** show a job's state at a glance with text, never colour alone. **Anatomy:** dot + label. **Variants:** unassigned, assigned, started, completed, attention. **States:** static; focusable only when it acts as a filter (then default/hover/focus/selected). **Content:** one or two words from the fixed status vocabulary; translated strings may be ~40% longer — chip width is auto. **Accessibility:** role `status` when it announces a change; otherwise plain text; dot is `aria-hidden`; contrast via `color.status-*` on background (all ≥ 4.5:1 light, see tokens). **Responsive:** unchanged. **Tokens:** `color.status-*`, `typography.label`, `radius.pill`, `spacing.1–2`.

## Job row (lists)
**Purpose:** scan and open a job. **Anatomy:** time window · customer first name · service · status chip · optional Assign button. **Variants:** dispatcher (with Assign), technician (no Assign), compact (board), comfortable (phone). **States:** default, hover (desktop), focus, pressed, loading (skeleton), offline-queued (badge), attention (left border `status-attention`). **Content:** customer first name only (F-002); area not full address. **Accessibility:** whole row is a single link/button with accessible name "Job, 14:00–16:00, Customer F., AC repair, assigned"; Assign is a separate button inside with its own name; row height ≥ 56 px on phone (`spacing.row-comfortable`), 32 px on board. **Tokens:** `spacing.row-*`, `typography.body`, `color.border`.

## Next-job card (technician)
**Purpose:** make the next action obvious. **Anatomy:** window (large), customer first name, area, service, OPEN button. **States:** default, focus, loading, offline-queued, none (empty state sentence). **Accessibility:** heading level 2 "Next job"; OPEN ≥ 44 px (`spacing.target-min`). **Tokens:** `typography.next-job`, `spacing.4–5`, `elevation.1`.

## Primary / secondary / tertiary button
**Variants:** primary (one per screen), secondary, tertiary (text). **Sizes:** default 40 px, large 48 px (technician actions). **States:** default, hover, focus (ring `focus.ring`), active, disabled (with reason tooltip or helper text), loading (spinner + label retained). **Content:** verb naming the result ("Save job", "Start", "Complete"); never "OK". **Accessibility:** `color.text-on-brand` on `color.brand` 6.45:1; disabled still readable ≥ 3:1; loading announces "Saving". **Tokens:** `color.brand`, `color.text-on-brand`, `radius.md`, `motion.fast`.

## Technician picker (bottom sheet / dialog)
**Purpose:** choose who does the job. **Anatomy:** title with job summary; list of technician rows (name, skill match, load and free-from time, conflict warning); CONFIRM. **States:** loading, empty ("No technician with this skill today" + show all), populated, selected, error (not saved, retry keeps selection), offline (explain). **Accessibility:** `role="dialog"`, labelled by title, focus trapped, Escape closes, radio-group semantics for rows, conflict warning associated via `aria-describedby`. **Tokens:** `elevation.2`, `spacing.3–4`.

## Needs-attention strip
**Purpose:** surface exceptions. **Anatomy:** count by reason, expand control. **States:** empty (positive sentence), populated, loading, error. **Accessibility:** `region` labelled "Needs attention"; counts announced as text; expand is a button with `aria-expanded`. **Tokens:** `color.status-attention` for the left border only; text stays `text-primary`.

## Form field (text, phone, select, chips)
**States:** default, focus, filled, error (message below, `aria-describedby`, not colour-only), disabled, read-only. **Phone field:** numeric input mode, country code default +91 (A-007 region), validation on blur. **Chips (service type, slots):** single-select radio semantics, ≥ 44 px targets on phone. **Tokens:** `color.border-strong` (3.11:1 ≥ 3:1 non-text), `color.status-attention` for error text (7.52:1).

## Toast with undo
**States:** appear (≤ 220 ms, fade only under reduced motion), persistent 10 s or until dismissed, focusable Undo. **Accessibility:** `role="status"`; Undo reachable by keyboard; never the only way to undo (Reassign exists). **Tokens:** `motion.base`, `elevation.2`.

## Offline / queued badge
**Purpose:** tell the technician an action is saved locally. **Content:** "Will send when online". **Accessibility:** text badge, `role="status"` on change.

## Board cell (desktop)
**Purpose:** place a job in time under a technician. **States:** default, hover, focus, dragging (with select-based alternative), drop-target, conflict. **Accessibility:** cells are buttons in a grid with row/column headers; keyboard: arrow keys move, Enter opens assign. **Tokens:** `spacing.row-compact`, `color.surface`.

## Open questions
Q-004 (new): font with Devanagari and regional coverage — confirm family, version and licence before tokens are final.
