---
name: ui-ux-design
description: "Design distinctive, production-grade web or mobile interfaces from flows and IA: intentional visual direction per product category, all screen states, responsive and motion specs, accessibility notes and anti-template controls, plus implementation review against rendered UI. Use for product experience and interface design."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: design
---
# UI/UX design and product experience

## Purpose
Give the product an experience that completes its users' tasks, fits its brand and category, specifies every state, meets WCAG 2.2 AA and does not look like a template.

## When to use
- After IA and flows exist; before and during implementation.
- When an implemented UI needs review against its specification.

## Preconditions
- **Research before design (mandatory).** Follow `references/design-research-method.md` steps 1 to 4 before producing any screen, flow, component or layout: the job statement; a dated category research table (at least three direct competitors, two adjacent, one non-digital reference) with a pattern map of the category template; the psychology analysis from `references/layout-psychology.md` with the concrete implication of each chosen principle; and at least three genuinely different directions scored against job fit, uniqueness (swap test), psychology, accessibility and cost. Present the comparison for approval. The first idea is never built.
- PRD, brandbook or brand direction, IA and flows, design tokens (or this skill produces the first set with `design-system`).

## Inputs
- PRD, IA, flows, research findings, brandbook, competitor pattern map, platform constraints, existing product (if any).

## Procedure
1. **Before designing.** Read PRD, brandbook, research, platform constraints and existing code. Inspect the current product and competitor references. Confirm primary user, task, context, device, information hierarchy and critical path. Do not start from a dashboard template.
2. **Choose a visual direction** appropriate to the product category and audience (see `references/product-category-patterns.md`) and write the rationale. The same style must not be forced on every project.
3. **Wireframe** the important flows in low fidelity; validate navigation and task completion against the IA.
4. **Tokens and components.** Define or adopt tokens (colour, typography, spacing, radius, elevation, borders, motion, focus, semantic status) and a small coherent component set with variants and states (`design-system`).
5. **Realistic content.** Real text lengths, realistic data, no lorem ipsum, fake charts, arbitrary metrics or invented testimonials.
6. **Responsive design.** Breakpoints from content, not device names; specify how layout, navigation and density change.
7. **Accessibility.** Keyboard behaviour, focus order, labels, error messaging, screen-reader semantics, contrast, target size, reduced motion (`accessibility-audit`).
8. **All states** for every screen: initial, loading, empty, populated, error, offline, permission denied, expired session, success, destructive confirmation.
9. **Anti-template review.** Run `references/anti-template-review.md`: build the comparison set (competitor pattern map, category default, three template galleries), fill the structural comparison table, apply the swap test and the job test. Purple gradients, glassmorphism, floating blobs, giant rounded cards, icon tiles, decorative charts, oversized hero copy and generic headings are flagged by the job test unless they do a stated job. Record what is deliberately different in `design-rationale.md`; measure the result with `references/visual-design-checklist.md`.
10. **Handoff.** Specs, assets, tokens, component behaviour, acceptance tests.
11. **Implementation review.** Inspect rendered pages at representative viewports: overflow, alignment, wrapping, focus, contrast, responsive navigation, state completeness, console errors, real task completion. Compare screenshots to spec.

## Outputs
- `04-design/visual-direction.md`, `04-design/design-rationale.md`, `04-design/wireframes/**`, `04-design/screens/**`, `04-design/responsive-spec.md`, `04-design/motion-spec.md`, `04-design/states-matrix.md`, `07-quality/design-qa-report.md` (review)

## Quality criteria
- A written research record (job, category table and pattern map, psychology analysis, three scored directions, approved choice) exists and is attached; the result passes the swap test against three competitors and has zero unexplained hits on `evaluations/originality/slop-patterns.md`.
- Any motion follows `references/motion-standards.md`: every animated moment names its job, honours `prefers-reduced-motion`, and is listed in a motion table.
- Direction rationale cites brand and research; pattern-map comparison documented.
- All states specified per screen; realistic content throughout.
- Accessibility notes complete for every interactive component.
- Responsive behaviour stated per breakpoint.
- Implementation review based on rendered UI, not mockups.

## Failure handling
- Brandbook missing → design on neutral tokens, flag the gap, do not invent a brand.
- Browser unavailable for review → mark visual verification `NOT_RUN`.

## Safety boundaries
- No fake data in production flows; no unlicensed assets.
- No copying of competitor or gallery designs.

## References
- `references/product-category-patterns.md` — what differs across SaaS, enterprise, admin dashboards, marketplaces, e-commerce, social, fintech, education, healthcare, mobile, developer tools, websites and landing pages
- `references/visual-design-checklist.md` — measurable checks for hierarchy, type, spacing, colour, states, motion, content and rendered UI
- `references/anti-template-review.md` — structural comparison table, swap test, job test, direction-diversity check
- `templates/design/visual-direction.md`, `templates/design/design-rationale.md`, `templates/design/states-matrix.md`, `templates/design/design-qa-report.md`
- `standards/design/design-standard.md`, `standards/accessibility/wcag-2.2-aa-checklist.md`
- `references/design-research-method.md`, `references/layout-psychology.md`, `references/motion-standards.md`
