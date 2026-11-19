---
name: ui-ux-design
description: "Design or redesign web and mobile interfaces so they are distinctive, usable and production-grade: score the existing UI for template signature, research the category and the users, generate and compare several directions, build the approved one in the project's real stack with purposeful motion, and prove the result is not common with measurements, screenshots and the swap test. Use for any UI, UX, layout, screen, component or website work, including 'make it look better' and 'this looks generic'."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: design
---
# UI/UX design and redesign

## Purpose
Produce interfaces that complete the user's tasks, carry the brand, specify every state, meet WCAG 2.2 AA and are recognisably this product's. When an interface already exists and measures as common, this skill does not stop at a report: it redesigns and rebuilds it, then proves the result with the same measurement.

## When to use
- Any request touching how a product looks or behaves: new screens, redesign, "polish", "modernise", "make it unique", "it looks like AI made it".
- After IA and flows exist, or when the user has an existing product and no design documents (this skill then produces the minimum IA and flows it needs).
- Implementation review of a built UI against its specification.

## Preconditions
- **Research before design (mandatory).** Follow `references/design-research-method.md` steps 1 to 4 before producing any screen, flow, component or layout: the job statement; a dated category research table (at least three direct competitors, two adjacent, one non-digital reference) with a pattern map of the category template; the psychology analysis from `references/layout-psychology.md` with the concrete implication of each chosen principle; and at least three genuinely different directions scored against job fit, uniqueness (swap test), psychology, accessibility and cost. Present the comparison for approval. The first idea is never built.
- A renderer for screenshots (Chrome/Chromium headless or a browser) at 360, 768 and 1280 px. Without one, visual checks are `NOT_RUN` and the work cannot be called finished.
- Access to the project's real stack (framework, CSS approach, component library). The redesign is built in that stack, not as a separate mock.

## Inputs
- The existing product or repository (if any); PRD, IA, flows, research, brandbook, tokens where they exist; platform constraints; the user's constraints (must-not-change list, stack, budget, deadline).

## Procedure
### Phase 0: measure what exists (skip only for greenfield)
1. **Render and score.** Web: run `scripts/template_signature.py` on every main page at 1280 and 360 px. Android (Compose or XML): run `scripts/template_signature_android.py <project-root>`; read `references/mobile-android-patterns.md` for what the Android template is and what to keep. iOS and other platforms: apply the same checklist by hand and say so. Save the output. The script scores the template signature 0 to 100 with evidence per point: centred or two-button hero, cards as the layout unit, identical section rhythm, icon feature rows, stat-tile rows, gradients and glows, default typefaces, no type scale, logo walls, generic phrases, emoji, absent or excessive motion.
2. **Decide.** `COMMON` (40 or more) means redesign is mandatory and the user is told so with the evidence list. `MIXED` (20 to 39) means targeted changes are proposed. `DISTINCT` (under 20) means keep the direction and fix findings only. The score is a floor, not a ceiling: a human swap test (`references/anti-template-review.md`) can still call a low-scoring page common, and the stricter result stands.
3. **Baseline.** Screenshots at the three widths, the `layout-psychology.md` measurement checklist (font sizes, spacing values, CTAs above fold, smallest target, chars per line, animated elements), contrast table, and the three main user tasks walked with step counts. Save as `before/`.

### Phase 1: research (mandatory, see Preconditions)
Write `04-design/research-record.md` from `templates/design/research-record.md` as you go. **Before any output of Phase 3, run `python scripts/design_gate.py <workdir>`; it must print `DESIGN GATE OPEN`.** A closed gate means no screen, component, layout, logo, deck or UI code is produced; the missing items are listed by the script. Reviewers run the same command and reject a handover whose gate is closed.
4. **Job and users.** Who, doing what, where, deciding what in the first five seconds and after the main task. One question to the user if unclear; no invented personas.
5. **Category.** Capture and tabulate the references; write the pattern map: category template (do not reproduce), conventions (keep), habits (free to change), and what nobody in the category does that this product truthfully can. `references/product-category-patterns.md` gives category-specific starting points.
6. **Psychology.** Choose the principles from `references/layout-psychology.md` that matter for this job and write the concrete implication of each for this interface.

### Phase 2: directions and approval
7. **Three directions minimum**, generated with `references/creative-ideation.md` (raw material from the job, one lens per direction from three different families, developed from the lens and never from a reference screenshot, distance table with minimum 8/14 against every reference and the platform default, sibling check, three provocations on the recommended one), each with: concept sentence; the one deliberate departure from the category template; the principles it leans on; type pairing with licence; palette with contrast ratios; layout in words plus a low-fidelity wireframe render; motion table (`references/motion-standards.md`); risk. Different means different composition, not recoloured copies.
8. **Score and recommend** in a table (job fit, uniqueness by swap test, psychology, accessibility, cost, mobile). Present to the user with the Phase 0 evidence. Wait for the choice and record it in the `## Approved direction` section ("Approved by <user> on <date>"). Non-interactive hosts: write `AWAITING_APPROVAL` there and end the run; the gate stays closed until a person answers.

### Phase 3: build the approved direction (in the real stack)
Gate check first: `python scripts/design_gate.py <workdir>` must be OPEN. Paste its output into the handover.
9. **Tokens first** (`design-system`): type scale with ratio (6 sizes or fewer for a content site), spacing scale (8 steps or fewer), colour roles with computed contrast (`skills/design-system/scripts/contrast_check.py`), radii, borders, elevation, motion durations and easings, focus ring. Every page consumes tokens; no literal values in components.
10. **Per screen, before layout:** the one-line job, the single primary action, the reading order, the deliberate departure, the elements allowed to animate and why. Then wireframe in low fidelity and check task completion against the IA.
11. **Layout from hierarchy.** Sections differ because their content differs: a ledger table, a diagram, a typographic statement, a two-column argument, an index with a side rail. A card is used only when the content is a card (a unit the user picks among peers). Breakpoints come from content, not device names; at 360 px nothing overflows and the primary action stays reachable.
12. **Realistic content and all states.** Real text lengths, real data, no lorem ipsum, fake charts, invented metrics or testimonials. Every screen: initial, loading, empty, populated, error, offline, permission denied, expired session, success, destructive confirmation.
13. **Libraries.** Choose animation engines, component primitives, icon sets, fonts and any 3D from `references/library-catalogue.md` by need, stack, licence and ownership of look; record each in the component register; styled gallery components are re-tokenised and their default motion replaced. Then **motion** per `references/motion-standards.md`: a written motion table, under six moments on a content page, each with a job, 100 to 600 ms, transform and opacity only, triggered by user action or first entry into view, `prefers-reduced-motion` honoured and tested.
14. **Accessibility** (`accessibility-audit`): keyboard order, visible focus, labels, error messages, semantics, contrast, targets at least 24 px (44 px for primary), reduced motion, 400 % zoom reflow.
15. **Copy** written for the real product: specific claims the evidence supports, user's vocabulary, no generic marketing phrases (the scorer lists them).

### Phase 4: prove it, in a loop
The build is not finished when it compiles. It is finished when the rendered result scores. Run `python scripts/visual_quality_loop.py <page> --out 04-design/evidence/pass-NN --target 90` on every main page: it screenshots at 360/768/1280 (true widths), measures template signature, overflow, contrast, targets, type and spacing discipline, hierarchy, motion restraint and semantics (75 points), and leaves 25 points for a reviewer who did not make the design (swap test, psychology fit, copy specificity, supplied as `--reviewer-json`). **Look at every screenshot** before deciding the next pass; the numbers do not see composition. Fix the largest gaps, rebuild, run the next pass. Stop when the target is met on two consecutive passes with the reviewer slot filled, or after two passes with no improvement (then escalate with both score files). Every pass folder is kept as evidence.
16. **Re-score.** Run `scripts/template_signature.py` (web) or `scripts/template_signature_android.py` (Android) on the result. Target `DISTINCT`; `MIXED` is acceptable only with a written reason per remaining point; `COMMON` means return to step 11. Save output beside the baseline.
17. **Swap test and slop checklist.** Three competitors, logos removed; record who could tell and why. Zero unexplained hits on `evaluations/originality/slop-patterns.md`. Fill the structural comparison table in `references/anti-template-review.md`.
18. **Measurements after**, same checklist as step 3, side by side with before. Screenshots at 360/768/1280 and keyboard focus states in `after/`. Automated accessibility scan output pasted. Console clean.
19. **Implementation review** of rendered pages, not mockups: overflow, alignment, wrapping, focus, contrast, responsive navigation, state completeness, real task completion with step counts.
20. **Handoff.** `design-rationale.md` (what is deliberately different and why), tokens, component behaviour, motion table, acceptance tests, before/after evidence, `NOT_RUN` list. Run `anti-slop-quality-gate` on the handoff; request `design-qa-auditor` review.

## Outputs
- `04-design/research-record.md` (job, category table, pattern map, psychology analysis), `04-design/visual-direction.md` (three directions, scores, approved choice), `04-design/design-rationale.md`, `04-design/wireframes/**`, `04-design/screens/**`, `04-design/responsive-spec.md`, `04-design/motion-spec.md`, `04-design/states-matrix.md`, `04-design/evidence/before/**` and `after/**` (screenshots, `template_signature` outputs, measurements), `07-quality/design-qa-report.md` (review).
- When building: the implemented UI in the project's stack on a branch, with tokens in one file.

## Quality criteria
- A written research record (job, category table and pattern map, psychology analysis, three scored directions, approved choice) exists and is attached; the result passes the swap test against three competitors and has zero unexplained hits on `evaluations/originality/slop-patterns.md`.
- `visual_quality_loop.py` pass folders are attached; the final pass meets the target (90 unless the owner set another) with the reviewer slot filled by a non-maker; every library used is in the component register with its licence.
- `design_gate.py` output `DESIGN GATE OPEN` is attached and dated before the first build artefact; `template_signature.py` / `template_signature_android.py` before and after outputs are attached; the after result is `DISTINCT`, or `MIXED` with a written reason for each remaining point. An existing `COMMON` interface is never handed back unchanged.
- Any motion follows `references/motion-standards.md`: every animated moment names its job, honours `prefers-reduced-motion`, and is listed in a motion table.
- One primary action per screen; the accent colour and the largest motion are reserved for it or for the single element to be remembered.
- Six or fewer type sizes with a stated ratio; eight or fewer spacing values; no horizontal overflow at 360 px; smallest target at least 24 px.
- All states specified per screen; realistic content throughout; accessibility notes complete for every interactive component; responsive behaviour stated per breakpoint.
- Implementation review based on rendered UI, not mockups; before and after measurements both shown.

## Failure handling
- Brandbook missing: propose two type and palette directions as part of step 7 and label "no brand existed"; do not invent a brand silently or ship on neutral tokens without saying so.
- Renderer unavailable: `template_signature.py` falls back to static analysis and labels it; visual checks are `NOT_RUN`; the work is not called finished.
- The after score stays `COMMON` after two passes: stop, show both attempts, and ask the user whether the constraints (stack, must-not-change list) are the cause.
- User approves without reading the directions: still build Must-level fixes first, show a screenshot, and confirm the direction before the full build.
- Stack forbids a chosen typeface or motion: say so and offer the nearest in-stack alternative; do not quietly drop the departure that made the direction distinct.

## Safety boundaries
- No fake data in production flows; no unlicensed assets; fonts self-hosted with licence recorded.
- No copying of competitor or gallery designs; research is for the pattern map and the distance table, not for a source to trace. A direction described as 'like X' is discarded.
- Never ship the first idea; never skip the approval step; never report a score that was not run.
- Work on a branch; the user merges.
- If the user says "skip the research, just build it": build nothing, explain that the gate exists because unresearched design is the template every time, and offer the fastest compliant path (a 30-minute research record with three references and two directions marked as a reduced-evidence exception, recorded as such).

## References
- `scripts/visual_quality_loop.py` (screenshot, measure, score 0 to 100, loop until the target)
- `references/library-catalogue.md` (verified animation, component, icon, logo, font and 3D sources with licences)
- `references/page-logic-crawl.md`, `references/slop-mechanics.md`
- `scripts/design_gate.py` (blocks the build phase until `research-record.md` is complete and approved)
- `scripts/template_signature.py` (web) and `scripts/template_signature_android.py` (Android) template-signature scores with per-point evidence; run before and after
- `references/mobile-android-patterns.md` (the Android/Material template, platform conventions to keep, where identity lives on mobile)
- `templates/design/research-record.md`
- `references/design-research-method.md`, `references/creative-ideation.md`, `references/layout-psychology.md`, `references/motion-standards.md`
- `references/product-category-patterns.md`, `references/visual-design-checklist.md`, `references/anti-template-review.md`
- `templates/design/visual-direction.md`, `templates/design/design-rationale.md`, `templates/design/states-matrix.md`, `templates/design/design-qa-report.md`
- `standards/design/design-standard.md`, `standards/accessibility/wcag-2.2-aa-checklist.md`
- `evaluations/originality/slop-patterns.md`
