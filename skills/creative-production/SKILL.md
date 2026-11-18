---
name: creative-production
description: Produce differentiated, accurate creative deliverables across documents, presentations, web copy, campaigns, graphics, image and video briefs with intake, multiple directions, brand and rights gates, rendered-output review and recorded provenance. Use for any creative output beyond product UI.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: branding
---
# Creative production across media

## Purpose
Deliver creative work that communicates one clear idea to a specific audience, follows the brand, is factually accurate, has recorded rights, and has been inspected in its final medium.

## When to use
- Decks, documents, web copy, campaigns, social assets, image or video briefs, print.

## Preconditions
- **Research before design (mandatory).** Follow `skills/ui-ux-design/references/design-research-method.md` steps 1 to 4 before producing any deck, document, image brief, video brief, poster, email or campaign asset: the job statement; a dated category research table (at least three direct competitors, two adjacent, one non-digital reference) with a pattern map of the category template; the psychology analysis from `skills/ui-ux-design/references/layout-psychology.md` with the concrete implication of each chosen principle; and at least three genuinely different directions scored against job fit, uniqueness (swap test), psychology, accessibility and cost. Present the comparison for approval. The first idea is never built. Record everything in `04-design/research-record.md` (`templates/design/research-record.md`) and run `python skills/ui-ux-design/scripts/design_gate.py <workdir>`: it must print `DESIGN GATE OPEN` before any artefact is produced.
- Brandbook or brand direction; verified facts for any claims; purpose and audience stated.

## Inputs
- Brief: medium, audience, purpose, desired action, context of use, channel, dimensions/format, brand system, accessibility needs, source material, rights constraints, deadline, success criteria.

## Procedure
1. **Intake.** Confirm every brief element; do not choose a medium or format without a user intent or deliverable requirement.
2. **Creative direction.** Research audience expectations, category conventions and references (recorded with sources). Identify the communication problem and a single creative idea. Where the decision is open, produce genuinely different directions with trade-offs; avoid derivative imitation and decoration without purpose.
3. **Production by medium.** Writing: concrete claims, audience language, structure, proof, consistent voice. Presentations: one argument per slide, meaningful data visualisation with sources, narrative arc. Documents: audience, objective, hierarchy, references, version control. Web/content: IA, responsive, accessible, conversion path. Images/illustrations: composition, subject, style, usage context, rights and provenance; never misrepresent people or fabricate evidence. Video/audio: audience, duration, hook, narrative, shot/audio plan, captions, pacing, rights, consent, platform specs. Campaigns: message hierarchy, variants, audience, channel, CTA, claim substantiation, measurement.
4. **Originality.** Use references to learn craft and codes, not as templates. List elements that must not be copied. Compare the draft to references and brandbook. Generated media does not establish originality or commercial-use rights; record generator terms.
5. **Review.** Facts, coherence, hierarchy, consistency, typography/layout, accessibility (alt text, captions, contrast), export/render quality, links, licensing, real-world usability. Inspect rendered output; read the full text; operate interactive artefacts. Run `anti-slop-quality-gate`.
6. **Handoff.** Editable source, exports, dimensions, asset inventory with rights, brandbook references, limitations, evidence of review.

## Outputs
- `03-brand/creative/**` or `09-operations/marketing-assets/**` with `asset-provenance.md` entries.

## Quality criteria
- A written research record (job, category table and pattern map, psychology analysis, three scored directions, approved choice) exists and is attached; the result passes the swap test against three competitors and has zero unexplained hits on `evaluations/originality/slop-patterns.md`.
- Any motion follows `skills/ui-ux-design/references/motion-standards.md`: every animated moment names its job, honours `prefers-reduced-motion`, and is listed in a motion table.
- One clear idea per deliverable; audience-specific language.
- Every claim substantiated; every third-party element licensed and recorded.
- Rendered output inspected in its medium; accessibility handled.
- Directions compared where the decision was open.

## Failure handling
- Facts unavailable → leave claims out or mark as placeholders for the owner; never invent.
- Rights unclear → replace the asset; do not ship.

## Safety boundaries
- No misrepresentation of people, fabricated evidence or fake urgency.
- Public assets need human approval.

## References
- `templates/branding/asset-provenance.md`, `templates/branding/creative-brief.md`
- `standards/brand/brand-standard.md`
- `skills/ui-ux-design/references/design-research-method.md`, `skills/ui-ux-design/references/layout-psychology.md`, `skills/ui-ux-design/references/motion-standards.md`
