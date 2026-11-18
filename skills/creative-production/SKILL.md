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
