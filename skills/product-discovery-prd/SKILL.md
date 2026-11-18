---
name: product-discovery-prd
description: Translate customer evidence and a validated idea into a product thesis, user journeys, a PRD with testable Given/When/Then acceptance criteria, non-functional requirements, prioritised scope and release slices. Use before implementation or major feature work.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: product
---
# Product discovery and PRD

## Purpose
Define the product so that a developer, a tester and a product owner would independently build and verify the same behaviour, with a scope narrow enough to learn one critical thing.

## When to use
- After idea validation and strategy; before design and architecture.
- For any feature large enough to need acceptance criteria.

## Preconditions
- Problem statements and opportunity assessment exist, or their absence is recorded as a risk.
- Target users and the critical hypothesis are named.

## Inputs
- Research brief, customer findings, strategy memo, validation plan.
- Constraints: platform, data sensitivity, regulation, timeline.

## Procedure
1. **Discovery.** Describe the user, context, trigger, desired progress and current workaround. Capture primary and secondary users, buyer, approver, administrator and affected non-users. Map the end-to-end journey including failure states, support needs and off-platform steps. Write problem statements without embedding the solution.
2. **Product definition.** Thesis, value proposition, use cases, jobs-to-be-done, key workflows, explicit non-goals. Personas only when evidence supports them; otherwise label them hypotheses.
3. **PRD** (`templates/product/prd.md`): context and problem; goals and measurable non-goals; segments and roles; scenarios; user stories with acceptance criteria; functional requirements; non-functional requirements (security, privacy, accessibility WCAG 2.2 AA, performance, reliability, scale, localisation, observability); data classification, retention and deletion; integrations; edge, empty, failure and recovery states; analytics events and success metrics; release, migration, support and rollback notes; risks, assumptions and open questions.
4. **Acceptance criteria.** Given/When/Then or equivalent, covering permissions, validation, error states, accessibility, responsive behaviour, analytics and data handling. Replace "intuitive", "fast", "secure" with measurable or observable definitions.
5. **Prioritise** on impact, evidence strength, urgency, reach, effort, risk and dependency. Must/should/could/later. Record rejected scope as `X-` ledger entries with the reason.
6. **Release planning.** Vertical slices delivering end-to-end value; explicit dependencies; reversible vs irreversible decisions; feature flags, migrations, operational readiness, support docs.
7. **Readability check.** Have the UX auditor (or a second reader) interpret three requirements; if two competent readers would implement different behaviour, refine.

## Outputs
- `02-product/prd.md`, `02-product/acceptance-criteria.md`, `02-product/roadmap.md`, `02-product/analytics-plan.md`
- Ledger entries for decisions, rejected scope and open questions.

## Quality criteria
- Every requirement has at least one testable acceptance criterion.
- Non-goals are explicit; not every item is P0.
- All states (initial, loading, empty, error, success, offline, permission denied, expired session) appear for each key screen or flow.
- Data classification, retention and deletion are specified.
- Personas are labelled evidence-based or hypothesis.

## Failure handling
- Conflicting stakeholder requirements → record both, name the decision owner, propose the smallest experiment that resolves it.
- Missing research → write requirements as hypotheses and attach the validation step; do not invent user needs.

## Safety boundaries
- Never fabricate research results, personas or metrics.
- Requirements touching personal data name the lawful-basis question for `legal-risk-governance`.

## References
- `templates/product/prd.md`, `templates/product/acceptance-criteria.md`, `templates/product/roadmap.md`
- `standards/documentation/documentation-standard.md`
- `skills/ux-research/SKILL.md`
