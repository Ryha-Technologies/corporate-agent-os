---
name: product-launch
description: "Plan and execute a product launch: readiness confirmation across gates, launch strategy and tiers, positioning and messaging, launch calendar, marketing and PR assets, sales enablement, support documentation, monitoring plan, rollback and post-launch review. Use when a product or major feature is approaching release."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: marketing
---
# Product launch

## Purpose
Take a verified product to its audience with coordinated, truthful messaging, prepared support and operations, and a plan for what happens when something goes wrong.

## When to use
- Release and launch stages of any workflow; relaunches and major feature releases.

## Preconditions
- Release gate passed or scheduled; positioning and brandbook approved; support and operations owners named.

## Inputs
- Gate verdicts, PRD, positioning, brandbook, channel plan, support policy, release checklist.

## Procedure
1. **Readiness.** Confirm build, security, testing, documentation and legal gates are PASS or have signed accepted risks; confirm rollback, monitoring, backups and support docs exist. No launch while any gate is NOT_ASSESSED.
2. **Launch strategy.** Tier (soft, beta, limited, public), audiences in order, success metrics, guardrails, kill switch and rollback criteria.
3. **Positioning and messaging** for launch: headline, proof points, FAQs, objections; every claim traceable to shipped capability.
4. **Calendar.** Milestones for assets, enablement, docs, monitoring, communications, with owners.
5. **Assets.** Website or landing page updates, announcements, emails, social, PR materials (`creative-production`); approvals recorded.
6. **Sales enablement.** Playbook updates, demo scripts from shipped features, pricing and packaging, objection handling.
7. **Support readiness.** Knowledge base, known issues, escalation matrix, response targets, incident communication templates.
8. **Monitoring plan.** Dashboards for activation, errors, latency, support volume; alert owners; review cadence for the first days.
9. **Launch and watch.** Execute per tier; hold reviews at defined checkpoints; apply rollback criteria without hesitation.
10. **Post-launch review.** Metrics vs targets, incidents, customer feedback, lessons (`L-`), roadmap inputs.

## Outputs
- `09-operations/launch-plan.md`, `09-operations/launch-calendar.md`, `09-operations/launch-assets/**`, `09-operations/sales-playbook.md` updates, `09-operations/post-launch-review.md`.

## Quality criteria
- All gates referenced with verdict files; approvals recorded.
- Every public claim maps to shipped capability.
- Rollback criteria and kill switch defined before launch.
- Support and monitoring owners named.

## Failure handling
- Gate not passed → launch blocked or re-tiered; record the decision.
- Metrics miss targets → run the review; decide continue, fix or roll back with evidence.

## Safety boundaries
- Publishing, customer communications and spend require human approval.
- No launch of a system handling personal data without the legal and security gates.

## References
- `templates/operations/launch-plan.md`, `templates/operations/release-checklist.md`
- `skills/growth-gtm/SKILL.md`, `skills/customer-success-support/SKILL.md`, `skills/devops-sre/SKILL.md`
