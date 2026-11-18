---
name: originality-audit
description: Independently audit a strategic or creative deliverable (research, business idea, name, brand, logo, UI, marketing, presentation, documentation, product strategy) for generic phrasing, template patterns, competitor imitation, unsupported claims, missing research and weak differentiation using the originality scorecard, and prescribe specific improvements. Use as the reviewer step before a creative or strategic gate.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: branding
---
# Originality and anti-slop audit (independent reviewer)

## Purpose
Give the orchestrator an independent judgement of whether a deliverable is researched, specific, differentiated and honest, with evidence for each finding and concrete fixes. The creator's own `anti-slop-quality-gate` pass is a precondition, not a substitute.

## When to use
- Brand, naming, identity, UX/UI direction, marketing, strategy or research artefacts reach a gate.
- The orchestrator or a human suspects generic or derivative output.

## Preconditions
- The deliverable, its brief, the category audit or competitor pattern map, and the creator's anti-slop self-check are available.
- The auditor did not produce the deliverable and runs in a separate context.

## Inputs
- Deliverable and brief; competitor pattern map; evidence ledger; rejected-concepts record; prior gate verdicts.

## Procedure
1. **Research-before-creation check.** Was the market, competitor set and convention set researched before the concept? Are references dated and recorded? If not, the deliverable fails on research depth regardless of polish.
2. **Multiple-concepts check.** Were genuinely different directions produced and compared (different strategic idea, not recoloured variants)? Is the rejected-concepts record present with reasons?
3. **Pattern comparison.** Follow `references/comparison-method.md`: fix the reference set first, fill the element-by-element table (ours / closest competitor / closest generic pattern / same-variant-different / evidence), apply the verdict rules, then the swap, claim and three-directions tests. List specific resemblances with the reference id.
4. **Claim audit.** Every factual claim traces to a ledger id or is labelled; look for invented statistics, testimonials, awards, founder stories, "unique", "first", "trusted by".
5. **Specificity audit.** Could this sentence, screen or concept describe any company in the category? Mark generic passages.
6. **Coherence audit.** Positioning, name, story, visual and UI decisions agree; terminology is consistent across artefacts.
7. **Score** with `evaluations/originality/originality-scorecard.md` across research depth, relevance, specificity, differentiation, strategic coherence, practical usefulness, craftsmanship, evidence quality, consistency, audience suitability. Score only where evidence exists; otherwise mark `NOT_ASSESSABLE` and say what evidence is missing.
8. **Prescribe fixes.** For each failing dimension give a specific change (which claim to source, which pattern to replace with what strategic alternative, which section to cut).
9. **Verdict** in the gate format: PASS / PASS_WITH_ACCEPTED_RISK / FAIL / NOT_ASSESSED, with findings ranked by severity.

## Outputs
- `07-quality/gate-<gate>-<date>.md` with scorecard and findings.
- Ledger entries: `K-` for imitation or legal-adjacent risks, `L-` lessons when patterns recur.

## Quality criteria
- Every finding has evidence (quote, screenshot, reference URL) and a specific fix.
- Scores are backed by evidence or marked `NOT_ASSESSABLE`; no meaningless numbers.
- Imitation findings name the specific reference they resemble.
- The verdict distinguishes creative weakness from legal risk and routes the latter to legal review.

## Failure handling
- Pattern map missing → verdict `NOT_ASSESSED` for differentiation; request the map.
- Auditor also authored parts of the deliverable → decline and ask the orchestrator for another reviewer.

## Safety boundaries
- Similarity (including any automated or embedding-based check) is a signal for human review, never proof of originality or infringement.
- Do not rewrite the deliverable; findings and fixes only.
- No legal conclusions.

## References
- `references/comparison-method.md` — reproducible element-by-element comparison, verdict rules, rework conversion
- `evaluations/originality/originality-scorecard.md`, `evaluations/originality/slop-patterns.md`
- `templates/branding/competitor-pattern-map.md`, `templates/branding/rejected-concepts.md`
- `skills/anti-slop-quality-gate/SKILL.md`
