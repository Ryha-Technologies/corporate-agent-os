---
name: accessibility-audit
description: Review designs and implemented interfaces against WCAG 2.2 Level AA with combined automated and manual checks (contrast, structure, labels, keyboard, focus, target size, motion, errors, status messages), recording per-criterion PASS/FAIL/NOT_TESTED with evidence and specific fixes. Use at design review, implementation review and release testing.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: design
---
# Accessibility audit (WCAG 2.2 AA)

## Purpose
Make the product usable by people with disabilities and produce evidence that proves it. The default target is WCAG 2.2 Level AA; a project may adopt a justified alternative, recorded as a decision.

## When to use
- Design review before implementation; implementation review; release testing.
- Any user-facing UI, document or marketing page.

## Preconditions
- Designs or a rendered UI; tokens with contrast data; the states matrix.
- Browser access for implementation audits; otherwise the audit is design-only and says so.

## Inputs
- Screens or URL/build, design tokens, component spec, states matrix.

## Procedure
1. **Scope.** List pages/screens, components and states to audit; note assistive technologies and browsers available.
2. **Automated pass.** Run available checkers (browser accessibility tooling or an automated engine) for contrast, missing names, structure and ARIA misuse. Record tool, version and date. Automated results are a starting point only.
3. **Manual checks** per `standards/accessibility/wcag-2.2-aa-checklist.md`: text alternatives; captions and media; info and relationships (headings, lists, tables, landmarks); meaningful sequence; use of colour; contrast of text (4.5:1, large text 3:1) and non-text (3:1); reflow at 320 px and 400% zoom; text spacing; content on hover/focus; keyboard operability and no traps; focus order and visible focus (2.4.11 focus not obscured, 2.4.13 focus appearance where targeted); target size minimum 24×24 CSS px (2.5.8); dragging alternatives (2.5.7); motion and animation control; page titles; link purpose; consistent navigation and help (3.2.6); error identification, suggestion and prevention; redundant entry (3.3.7); accessible authentication (3.3.8); status messages announced; name/role/value for custom controls.
4. **Screen reader pass** where available (at least one platform); note what could not be tested.
5. **Record** each criterion as PASS / FAIL / NOT_TESTED / NOT_APPLICABLE with evidence (screenshot, element, measured ratio) and a specific fix.
6. **Severity.** Blockers (task cannot be completed by AT users), major, minor; list in the gate verdict.
7. **Retest** after fixes and update the report.

## Outputs
- `04-design/accessibility-review.md` (design stage) or `07-quality/accessibility-test-report.md` (implementation).

## Quality criteria
- Every applicable success criterion has a result; NOT_TESTED is shown, never hidden.
- Each FAIL has element-level evidence and a fix.
- Automated and manual methods both recorded.
- Deviations from AA carry a documented, approved justified alternative.

## Failure handling
- No browser or AT available → design-only audit; implementation criteria NOT_TESTED; state the gap in the verdict.
- Third-party component fails → record, propose configuration or replacement, and note the dependency.

## Safety boundaries
- Never report automated-scan output alone as conformance.
- Never silently waive a criterion.

## References
- `standards/accessibility/wcag-2.2-aa-checklist.md`
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- `templates/testing/accessibility-report.md`
