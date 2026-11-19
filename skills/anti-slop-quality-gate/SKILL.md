---
name: anti-slop-quality-gate
description: Self-check any AI-generated research, writing, code, UI, brand, image brief, deck or deliverable for generic patterns, fabricated claims, template visuals, placeholders, inconsistency and unverified functionality before submitting it for review. Use before calling any artefact final.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: qa
---
# Anti-slop quality gate (creator self-check)

## Purpose
Catch the common failure where output is fluent, long and polished but generic, unverified, visually templated, functionally incomplete or disconnected from the user and brand. Every creator runs this before handing work to the independent reviewer.

## When to use
- Before submitting any artefact to the orchestrator or a reviewer.
- Before any public or customer-facing output.

## Preconditions
- The brief, acceptance criteria and (where relevant) brandbook and pattern map are at hand.

## Inputs
- The artefact; its task contract; evidence ledger; brandbook; competitor pattern map.

## Procedure
1. **Universal checks.** Does every section answer the actual goal? Is every claim traceable to evidence or labelled as an assumption? Any fake citations, invented statistics, fabricated tests, testimonials or unverifiable feature claims? Repeated phrases, layouts, icons or patterns without reason? Consistent terminology across PRD, brandbook, UI, docs and code? Placeholders, TODOs, lorem ipsum, empty buttons, fake charts, dead links, unsupported promises? Edge cases, failure states, permissions and operational impact addressed? Complexity justified by user value? Can a reviewer reproduce the result?
2. **Visual and design checks.** Does the design reflect the real audience, IA and task flow? Is it differentiated from competitors and template galleries? Consistent with the brandbook? Hierarchy from importance, not decorative cards? Does each chart, icon, animation, gradient, border and shadow communicate something? Were real viewport screenshots inspected (mobile, desktop, keyboard focus, overflow, real text lengths)? Are images, fonts, icons and illustrations licensed? Challenge default styling (arbitrary purple/blue gradients, glassmorphism, neon glows, 3D blobs, giant rounded cards, generic dashboard grids, random abstract illustrations, identical hero layouts). Risk signals, not bans: each needs a stated purpose.
3. **Writing checks.** Run `python scripts/copy_slop_check.py <files, folders or URLs>` first and paste its output: it flags placeholders, "not just X, it's Y", slop verbs and adjectives, scene-setting, headline formulas, hype, hedges, fake social proof and urgency, emoji bullets and em-dash density with file:line and a fix; exit 1 means rewrite before submitting. Then by hand: Remove empty superlatives, stock phrases, repetitive introductions, fake urgency, generic founder stories, keyword stuffing and claims that could describe any company. Use concrete evidence, customer language, specific verbs, consistent voice.
4. **Code and product checks.** Run the build and tests; inspect the actual UI; verify API and data behaviour, errors, auth, accessibility, performance and security. A screenshot does not prove functionality; tests do not prove usability.
5. **Decision.** `ACCEPT` (submit), `REVISE` (fix first) or `BLOCK` (legal, safety, security, evidence or functionality blocker). For each finding record evidence, impact, fix and retest method in the report's `CHECKS_ACTUALLY_RUN`.

## Outputs
- Self-check section in the agent report; fixes applied before submission.

## Quality criteria
- `copy_slop_check.py` output is attached and passes (no placeholders, weighted hits within the limit) for every customer-facing text.
- No placeholder, unsupported claim or unverified functionality remains.
- Every decorative or structural element has a stated job.
- The artefact names what was not verified.

## Failure handling
- Cannot run the build or inspect UI → mark `NOT_RUN` and say so; never infer.
- Evidence missing for a key claim → convert to labelled assumption and open a `Q-` question.

## Safety boundaries
- Never pass an artefact because it looks polished.
- Never remove a disclosure to make the artefact look complete.

## References
- `scripts/copy_slop_check.py` (automated writing-tell scan for files, folders and rendered URLs)
- `skills/ui-ux-design/references/slop-mechanics.md` (why these patterns appear, with sources)
- `evaluations/originality/slop-patterns.md`
- `evaluations/originality/originality-scorecard.md`
- `skills/originality-audit/SKILL.md` (the independent counterpart)
