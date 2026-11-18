---
name: brandbook-identity
description: Build a complete, usable brandbook and visual identity system (logo usage, colour with contrast pairings, licensed typography, grid, imagery, iconography, motion, voice, UI tokens, applications, misuse, governance) that another designer or engineer can reproduce. Use after brand strategy and logo work.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: branding
---
# Brandbook and identity system

## Purpose
Turn brand strategy and the chosen mark into a production specification. A brandbook is not a moodboard; its test is whether a stranger can produce on-brand work from it.

## When to use
- Brand strategy and logo direction are approved.
- An existing brand needs documentation or consolidation.

## Preconditions
- **Research before design (mandatory).** Follow `skills/ui-ux-design/references/design-research-method.md` steps 1 to 4 before producing any identity element, colour system, type system or layout rule: the job statement; a dated category research table (at least three direct competitors, two adjacent, one non-digital reference) with a pattern map of the category template; the psychology analysis from `skills/ui-ux-design/references/layout-psychology.md` with the concrete implication of each chosen principle; and at least three genuinely different directions scored against job fit, uniqueness (swap test), psychology, accessibility and cost. Present the comparison for approval. The first idea is never built.
- Approved brand strategy, logo system, competitor pattern map, asset provenance record.

## Inputs
- Brand strategy and messaging; logo assets; audience and channel list; accessibility target (WCAG 2.2 AA default).

## Procedure
1. **Foundation sections.** Essence, positioning, audience, promise, proof; story and message hierarchy (from `brand-strategy-story`).
2. **Logo system.** Primary, secondary, symbol, wordmark, responsive variants, safe area, minimum sizes, backgrounds, monochrome, incorrect uses with examples.
3. **Colour system.** Semantic roles (brand, neutral, status), HEX/RGB and CMYK where print matters, tints, light/dark behaviour, usage ratios, contrast pairings checked against WCAG 2.2 AA for text and controls.
4. **Typography.** Licensed families with licence record, weights, fallback stack, scale, line height, tracking, language coverage for the audience's scripts.
5. **Grid, spacing, layout, breakpoints.**
6. **Imagery and art direction.** Subjects, framing, lighting, texture, composition, prohibited clichés, sourcing and rights rules.
7. **Illustration, iconography, data visualisation style.**
8. **Motion.** Timing, easing, purpose, reduced-motion behaviour.
9. **Voice and tone** with sample copy and grammar rules.
10. **UI tokens and component examples** aligned with `design-system`.
11. **Applications.** Website, product, mobile, presentation, social, email, documentation, with real examples.
12. **Accessibility, localisation, governance, asset inventory, version history.**
13. **Distinctiveness check.** Compare the system to the competitor pattern map; document why it is recognisably different; choose one or two repeatable brand devices.
14. **QA.** Test across small/large, light/dark, print/screen, monochrome, low-quality reproduction, browser rendering, localisation.

## Outputs
- `03-brand/brandbook.md` (using `templates/branding/brandbook.md`), token export for design, `03-brand/assets/**`, updated asset provenance.

## Quality criteria
- A written research record (job, category table and pattern map, psychology analysis, three scored directions, approved choice) exists and is attached; the result passes the swap test against three competitors and has zero unexplained hits on `evaluations/originality/slop-patterns.md`.
- Every colour pairing used for text or controls meets the stated contrast target or is marked decorative-only.
- Every font, icon set, image and illustration has a recorded licence and permitted use.
- The book contains real applications, not only swatches.
- A distinctiveness section cites the pattern map.
- Misuse examples exist.

## Failure handling
- Font licence unclear → mark unusable until resolved; propose an alternative with clear terms.
- Direction resembles a competitor → return to `logo-design` territories; record rejection.

## Safety boundaries
- No unlicensed assets; no copying of competitor devices.
- Default AI aesthetics (arbitrary gradients, glowing purple/blue, glass cards, oversized rounded rectangles, random 3D blobs, generic dashboard tiles, template hero sections) need a documented brand reason; they are risk signals, not bans.

## References
- `templates/branding/brandbook.md`, `templates/branding/asset-provenance.md`
- `standards/brand/brand-standard.md`, `standards/accessibility/wcag-2.2-aa-checklist.md`
- `skills/design-system/SKILL.md`
- `skills/ui-ux-design/references/design-research-method.md`, `skills/ui-ux-design/references/layout-psychology.md`
