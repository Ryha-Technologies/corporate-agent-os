---
name: brand-strategy-story
description: Create a distinctive brand strategy, positioning, personality, promise, narrative in three lengths and a messaging system grounded in a category audit and audience research, with verified facts separated from brand framing. Use for company, product, service or feature brands before naming or identity work.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: branding
---
# Brand strategy and narrative

## Purpose
Build the strategic foundation of a brand so that every later creative decision (name, identity, voice, UI) can be traced to audience tension and category gaps rather than taste or trend.

## When to use
- A new company, product or feature needs a brand.
- An existing brand drifts or feels generic.
- Before `naming-ip-screen`, `logo-design`, `brandbook-identity`.

## Preconditions
- **Research before design (mandatory).** Follow `skills/ui-ux-design/references/design-research-method.md` steps 1 to 4 before producing any positioning, story or message hierarchy: the job statement; a dated category research table (at least three direct competitors, two adjacent, one non-digital reference) with a pattern map of the category template; the psychology analysis from `skills/ui-ux-design/references/layout-psychology.md` with the concrete implication of each chosen principle; and at least three genuinely different directions scored against job fit, uniqueness (swap test), psychology, accessibility and cost. Present the comparison for approval. The first idea is never built. Record everything in `04-design/research-record.md` (`templates/design/research-record.md`) and run `python skills/ui-ux-design/scripts/design_gate.py <workdir>`: it must print `DESIGN GATE OPEN` before any artefact is produced.
- Research brief and competitor pattern map exist (or this skill's step 1 produces the category audit).
- Verified facts about the company (founding, team, traction) are listed separately from aspirations.

## Inputs
- Strategy memo, customer findings, competitor pattern map.
- Verified company facts; brand constraints (existing marks, parent brands).

## Procedure
1. **Category audit before creation.** Audit direct and adjacent brands: conventions, customer language, visual patterns, naming patterns, promises, trust signals, tone, clichés. Record dated references. Classify each pattern as category convention (expected) or ownable signal. Look outside the category for craft, never for distinctive assets to borrow.
2. **Brand foundation.** Audience and their real tension or aspiration; frame of reference; positioning and alternatives; functional, emotional and social value; reason to believe and proof points; promise and boundaries; personality traits with behavioural meaning; values as observable decisions.
3. **Narrative.** The world before; the insight; the founding choice; what the brand believes; what it does differently; evidence; the future it works toward. Produce one-line essence, elevator story and long-form About. Mark every sentence as verified fact or brand framing. Never invent founder struggles, testimonials, traction, awards, partnerships or impact.
4. **Messaging system.** Core promise, pillars, proof points, audience-specific messages, elevator pitch, homepage headline and subheadline, product descriptions, feature naming rules, CTA principles, boilerplate, prohibited claims. Claims about performance, security, sustainability, AI or savings require evidence.
5. **Distinctiveness test.** Compare positioning, story, tagline, tone and proposed devices against the pattern map and a sample of adjacent brands. Change anything that relies on a cliché or resembles a recognisable brand. A visual or verbal audit is not a legal clearance.
6. **Directions.** For the open decisions (personality, tone, narrative angle) produce at least three genuinely different directions and compare them on the originality scorecard; record rejected directions with reasons.
7. **Governance.** Brand owner, approval process, source of truth, usage rights, update cadence.

## Outputs
- `03-brand/category-audit.md`, `03-brand/brand-strategy.md`, `03-brand/messaging.md`, `03-brand/rejected-concepts.md`
- Inputs to `brandbook-identity`.

## Quality criteria
- A written research record (job, category table and pattern map, psychology analysis, three scored directions, approved choice) exists and is attached; the result passes the swap test against three competitors and has zero unexplained hits on `evaluations/originality/slop-patterns.md`.
- Category audit has dated references and a cliché list.
- Verified facts and framing are visibly separated in the narrative.
- Values are behaviours, not adjectives.
- At least three directions compared; rejected ones recorded.
- No claim in the messaging lacks a proof point or an evidence task.

## Failure handling
- No verified company facts → write the narrative as proposed framing only, flagged for the founder to confirm or correct.
- Directions converge → change the framing (different audience tension, different proof) and regenerate; do not recolour the same idea.

## Safety boundaries
- No invented history, testimonials, numbers or endorsements.
- No reproduction of competitor distinctive assets.
- No "legally unique" or clearance language.

## References
- `templates/branding/brand-strategy.md`, `templates/branding/competitor-pattern-map.md`
- `evaluations/originality/originality-scorecard.md`
- `standards/brand/brand-standard.md`
- `skills/ui-ux-design/references/design-research-method.md`, `skills/ui-ux-design/references/layout-psychology.md`
