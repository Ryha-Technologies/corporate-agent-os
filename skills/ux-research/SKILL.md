---
name: ux-research
description: Plan, run and synthesise user interviews, surveys, usability tests and journey mapping into evidence-based personas, jobs-to-be-done, severity-ranked findings and design requirements, with simulated personas always labelled as hypotheses. Use when product or design decisions need customer behaviour evidence.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: ux-research
---
# UX and customer research

## Purpose
Replace guesses about users with observed behaviour, and keep hypotheses labelled as such until they are tested.

## When to use
- Before product definition, IA or visual design.
- When a usability problem is suspected or a prototype needs testing.

## Preconditions
- Research questions are written; recruiting and consent approach is approved by a human when real participants are involved.

## Inputs
- Research questions, segment hypotheses, prototype or product (for usability tests), access to participants or existing data.

## Procedure
1. **Plan.** Questions, method per question (interview, survey, usability test, diary study, analytics review), participant criteria and screener, sample size and its limits, consent and data handling, analysis plan.
2. **Interview discipline.** Ask about recent real behaviour: last time the problem occurred, trigger, what they did instead, frequency, cost in time/money/risk, who else was involved, what they already pay for or tried. Never "would you use our app?". Recruit beyond friends and enthusiasts; segment by behaviour, context, need, budget and decision authority.
3. **Usability tests.** Define tasks and success criteria; facilitate without leading; record task success, errors, time, quotes with consent; rank issues by severity and frequency.
4. **Synthesis.** Separate observation from interpretation. Build affinity clusters, jobs-to-be-done statements, journey maps with pain points, evidence-based personas (or `HYPOTHESIS` personas when no data), severity-ranked findings with evidence excerpts.
5. **Convert to requirements.** Actionable design requirements and testable hypotheses; link to PRD items.
6. **Retest** revised flows and show what changed.

## Outputs
- `01-research/customer-research-plan.md`, `01-research/customer-findings.md`, `04-design/personas-and-journeys.md`, `07-quality/usability-report-*.md`

## Quality criteria
- Sample size, recruiting method and bias are stated.
- Quotes and counts come only from recorded sessions or supplied data.
- Personas carry an evidence basis or the `HYPOTHESIS` label.
- Findings have severity, frequency and a design implication.

## Failure handling
- No participants available → deliver plan, screener, script and `HYPOTHESIS` personas; mark findings as not yet obtained.
- Participants are friends or team → report the bias and lower confidence.

## Safety boundaries
- Never fabricate quotes, participants, session counts or success rates.
- Consent, incentives and personal data handling require human approval; store only what the analysis needs.
- Simulated or AI role-played users are not research; label them clearly if used for script rehearsal.

## References
- `templates/design/interview-guide.md`, `templates/design/usability-test-plan.md`
- `standards/research/research-standard.md`
