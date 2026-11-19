---
name: design-system
description: Define design principles, machine-readable design tokens (colour roles, typography scale, spacing, radius, elevation, motion, focus, status), layout rules, breakpoints and component specifications with variants, states, usage and accessibility rules so designs are implemented consistently. Use when a product needs a reusable, implementable system.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: design
---
# Design system

## Purpose
Encode the visual and interaction decisions as tokens and component rules that both designers and engineers consume, keeping the system small enough to stay coherent.

## When to use
- After the visual direction is chosen; before component implementation.
- When inconsistency between screens or between design and code appears.

## Preconditions
- **Research before design (mandatory).** Follow `skills/ui-ux-design/references/design-research-method.md` steps 1 to 4 before producing any token set, component or pattern: the job statement; a dated category research table (at least three direct competitors, two adjacent, one non-digital reference) with a pattern map of the category template; the psychology analysis from `skills/ui-ux-design/references/layout-psychology.md` with the concrete implication of each chosen principle; and at least three genuinely different directions generated with `skills/ui-ux-design/references/creative-ideation.md` (one lens per direction from three families, derived from the job and never from a reference, with a distance table and sibling check) scored against job fit, uniqueness (swap test), psychology, accessibility and cost. Present the comparison for approval. The first idea is never built. Record everything in `04-design/research-record.md` (`templates/design/research-record.md`) and run `python skills/ui-ux-design/scripts/design_gate.py <workdir>`: it must print `DESIGN GATE OPEN` before any artefact is produced.
- Visual direction and brandbook (or brand direction) exist; accessibility target set (WCAG 2.2 AA default).

## Inputs
- Brandbook, visual direction, platform targets, existing component code (if any).

## Procedure
1. **Principles.** Three to five design principles tied to the product's tasks and brand; each with a "this means / this does not mean" pair.
2. **Tokens** as JSON (`templates/design/design-tokens.schema.json`): colour with semantic roles (background, surface, text, border, brand, status) and light/dark values; type scale with families, sizes, weights, line heights; spacing scale; radius; elevation; borders; motion durations and easings; focus ring; z-index. Every colour pairing used for text or controls lists its contrast ratio.
3. **Layout rules.** Grid, gutters, container widths, breakpoints from content, density modes if needed.
4. **Components.** Start with the smallest set the product needs (buttons, inputs, selects, checkboxes/radios, forms and validation, tables or lists, navigation, dialogs, toasts, empty states, loading). For each: anatomy, variants, sizes, states (default, hover, focus, active, disabled, loading, error, selected), content rules, accessibility requirements (role, name, keyboard, focus, announcements), do/don't examples.
5. **Patterns.** Forms, destructive actions with confirmation and undo, bulk actions, search and filter, pagination, error pages.
6. **Documentation.** How to use tokens in code, naming conventions, contribution and change process.
7. **Validation.** Tokens parse as JSON and validate against `templates/design/design-tokens.schema.json`; run `scripts/contrast_check.py <tokens.json> --write` to compute and record contrast ratios and flag roles below 4.5:1 (text) or 3:1 (non-text); components cover the states matrix. Start from `assets/design-tokens.example.json` rather than a blank file.

## Outputs
- `04-design/design-tokens.json`, `04-design/component-spec.md`, `04-design/design-system-docs/**`

## Quality criteria
- A written research record (job, category table and pattern map, psychology analysis, three scored directions, approved choice) exists and is attached; the result passes the swap test against three competitors and has zero unexplained hits on `evaluations/originality/slop-patterns.md`.
- Any motion follows `skills/ui-ux-design/references/motion-standards.md`: every animated moment names its job, honours `prefers-reduced-motion`, and is listed in a motion table.
- Tokens machine-readable; no hard-coded values in component specs.
- Each component lists all states and accessibility requirements.
- System size justified by the product's needs; no speculative components.
- Contrast ratios documented for text and control pairings.

## Failure handling
- Brandbook incomplete → define neutral tokens and flag brand tokens as pending.
- Engineering uses a UI library → map tokens to the library's theme and document gaps rather than forking the library.

## Safety boundaries
- No unlicensed fonts or icon sets; record licences in the asset provenance file.

## References
- `skills/ui-ux-design/references/library-catalogue.md` (verified motion, component, icon, logo, font and 3D sources with licences; choose by need and record)
- `skills/ui-ux-design/scripts/visual_quality_loop.py` (rendered-output score loop)
- `templates/design/design-tokens.schema.json`, `templates/design/component-spec.md`
- `standards/design/design-standard.md`, `standards/accessibility/wcag-2.2-aa-checklist.md`
- `skills/ui-ux-design/references/design-research-method.md`, `skills/ui-ux-design/references/layout-psychology.md`, `skills/ui-ux-design/references/motion-standards.md`
