---
name: customer-success-support
description: Design customer onboarding, support operations, knowledge base, issue taxonomy, escalation, customer health signals and feedback-to-roadmap loops for software products, with honest service levels and privacy protection. Use for post-launch customer operations and retention work.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: customer-success
---
# Customer success and support

## Purpose
Get customers to value quickly, resolve issues truthfully within service levels the team can keep, and turn recurring problems into product improvements.

## When to use
- Before launch (support readiness) and continuously after.

## Preconditions
- Product documentation exists or is planned; support channels and capacity are known.

## Inputs
- PRD, user journeys, release notes, support capacity, privacy requirements.

## Procedure
1. **Lifecycle map.** Evaluation, purchase, onboarding, activation, adoption, renewal, expansion, offboarding; define first-value moment.
2. **Support model.** Channels, hours, severity definitions, response and resolution targets, escalation paths, ownership. Promise only what capacity supports.
3. **Knowledge base.** Setup guides, troubleshooting trees, release notes, known issues; verified against the product (`technical-documentation`).
4. **Issue taxonomy.** Type, product area, severity, recurrence, impact, root cause, resolution; protect personal data and credentials in tickets.
5. **Feedback triage.** Evidence, frequency, affected segments, workarounds, strategic fit; route to product with ledger entries; the loudest customer is not the market.
6. **Metrics.** Time to first value, activation, adoption, response/resolution time, reopen rate, customer effort, satisfaction, retention, churn reasons.
7. **Incident communication** templates and escalation (with `incident-response`).
8. **Systemic fixes.** Feed recurring issues to product, engineering, QA, security and docs; verify recurrence drops.

## Outputs
- `09-operations/support-policy.md`, `09-operations/onboarding-checklist.md`, `09-operations/knowledge-base-outline.md`, `09-operations/issue-taxonomy.md`, `09-operations/escalation-matrix.md`, `09-operations/feedback-process.md`.

## Quality criteria
- Service levels match capacity.
- Taxonomy enables root-cause reporting.
- Health signals are behavioural.
- Privacy handling in tickets defined.

## Failure handling
- Capacity unknown → define targets as provisional with a review date.
- Feedback contradicts research → record both; propose a test.

## Safety boundaries
- No personal data in examples or shared tickets; no SLA commitments without approval.

## References
- `templates/operations/support-policy.md`, `templates/operations/onboarding-checklist.md`
- `skills/technical-documentation/SKILL.md`, `skills/incident-response/SKILL.md`
