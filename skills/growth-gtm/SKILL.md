---
name: growth-gtm
description: "Create evidence-based go-to-market and growth plans: ICP and buyer confirmation, beachhead channel on access and economics, funnel events separating vanity from activation and revenue, pre-registered experiments, honest launch assets, privacy-minimised analytics and stop/scale thresholds. Use for marketing, channel and growth planning."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: marketing
---
# Growth and go-to-market

## Purpose
Reach and activate the right customers with claims that are true and experiments whose results can be trusted.

## When to use
- Before launch; when a channel or message needs to be chosen or tested; when growth stalls.

## Preconditions
- Positioning and brand voice; verified product capabilities; financial model with CAC and payback assumptions.

## Inputs
- Research findings, strategy memo, PRD, brandbook, financial model, analytics access.

## Procedure
1. **Confirm the target.** Segment, buyer, user, trigger event, value proposition, objections and alternatives from research; no new personas invented here.
2. **Channel selection.** Compare product-led, sales-led, community-led, partnerships, content, SEO, marketplaces and paid on audience access, economics and capacity; pick a beachhead.
3. **Funnel and metrics.** Define stages and measurable conversion events; separate vanity metrics from activation, retention, referral, revenue and contribution margin; set guardrail metrics.
4. **Experiments.** Message-market fit tests (landing page, demo, offer, price, onboarding) with pre-registered hypothesis, audience, sample or decision rule and metric (`templates/operations/experiment.md`).
5. **Launch assets** from verified capability and the brandbook; no invented logos, testimonials, benchmarks, partnerships, awards or scarcity.
6. **Analytics** with privacy minimisation and consent where required; verify data accuracy before using results.
7. **Run, report, scale.** Small experiments; report outcome and confidence; scale only when economics and operational capacity support it.
8. **Monitor** CAC, payback, conversion, activation, retention, churn, expansion, support load, gross margin.
9. **Lifecycle.** Customer education, onboarding, documentation, status and incident communication, feedback loops (with `customer-success-support`).

## Outputs
- `09-operations/positioning.md`, `09-operations/channel-plan.md`, `09-operations/experiment-backlog.md`, `09-operations/analytics-plan.md`, launch asset list.

## Quality criteria
- Channel choice justified by access and economics.
- Every experiment pre-registered; results carry confidence.
- Metrics distinguish vanity from value.
- No unsubstantiated or invented claims in assets.

## Failure handling
- No analytics → plan instrumentation first; do not report on guesses.
- Experiment inconclusive → say so; extend sample or redesign; no post-hoc rationalisation.

## Safety boundaries
- No dark patterns, fake urgency or misleading comparisons.
- Public claims and spend require human approval.

## References
- `templates/operations/experiment.md`, `templates/operations/launch-plan.md`
- `skills/product-launch/SKILL.md`, `skills/customer-success-support/SKILL.md`
