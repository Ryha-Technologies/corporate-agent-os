---
name: business-idea-validation
description: Investigate whether a rough or generic business idea is worth pursuing before any plan is written, by discovering the real problem, grading the evidence, assessing the opportunity, comparing business models, defining validation experiments, kill criteria and an MVP proposal. Use when a user brings an idea and wants to know if and how to pursue it.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: strategy
---
# Business idea discovery and validation

## Purpose
Stop the reflex of turning any idea into a generic business plan. Find out who has the problem, whether it matters, whether anyone pays to solve it, whether the business is feasible and attractive, and what cheap experiment would most reduce uncertainty. The output is an honest opportunity assessment with kill criteria, not a promise.

## When to use
- A user says "I want to build X" with little detail.
- An existing idea needs a go / pivot / stop decision.
- Before `product-discovery-prd`, `brand-strategy-story` or architecture work begins.

## Preconditions
- Intake brief exists (`00-intake/brief.md`).
- `research-intelligence` and `competitive-analysis` are available for the evidence work; this skill frames and judges, it does not replace them.

## Inputs
- The idea as stated, including the user's motivation and constraints.
- Geography, budget, timeline, founder capabilities.
- Prior evidence ledger, if any.

## Procedure
1. **Reframe the idea as problems.** Write at least three problem statements the idea might solve, each naming the person, the situation, the current workaround and the cost of the problem. Mark each as evidence-based or hypothesis.
2. **Problem discovery.** For each statement, gather: who experiences it, frequency, severity, current solutions and their frustrations, what people already spend (money, time), unmet needs, and shifts (market, technology, regulation, distribution) that change the picture. Separate observed customer evidence from AI-generated hypotheses in every table.
3. **Opportunity analysis.** Size bottom-up (`research-intelligence/references/market-sizing.md`) with low/base/high; assess market growth and timing, accessibility, competitive intensity, barriers, acquisition difficulty, willingness to pay, distribution options, retention potential and revenue potential. Each line carries evidence or an explicit assumption.
4. **Business model options.** Compare the plausible models (SaaS subscription, usage-based, transaction fee, marketplace take rate, enterprise contract, licensing, advertising, freemium, hybrid) on buyer/user match, gross margin including variable compute and AI costs, acquisition cost, payback, churn exposure, operating load. Hand the chosen candidates to `business-model-unit-economics` for the numbers.
5. **Differentiation.** From the competitor map, state the real advantage (experience, distribution, technology, cost, network effects, data, execution). Feature-list differences are not differentiation. Write what an incumbent would need to do to neutralise it.
6. **Grade the evidence.** For each pillar (problem, customer, willingness to pay, feasibility, differentiation, model) assign evidence quality: observed behaviour / stated intent / secondary data / assumption. Assign overall confidence.
7. **Risks and kill criteria.** List the five biggest assumptions. For each, define the experiment that tests it, the metric, the threshold that kills or pivots the idea, and the cost and time of the test.
8. **MVP proposal.** The smallest thing that tests the riskiest assumption with real behaviour (landing page with commitment action, concierge service, prototype test, pre-sales). State what it deliberately does not include.
9. **Pivot options.** Adjacent segments, jobs or models the evidence points to if the core idea fails.
10. **Write the assessment** using `templates/business/opportunity-assessment.md`, with recommendation (pursue / test first / pivot / stop), confidence, next actions and decision date.

## Outputs
- `01-research/problem-statements.md`
- `01-research/opportunity-assessment.md`
- `02-product/validation-plan.md` (experiments, metrics, thresholds, cost)
- Ledger entries: hypotheses, assumptions with `review_by`, risks, rejected alternatives.

## Quality criteria
- Observed evidence and hypotheses are visibly separated throughout.
- Market figures show formula and sources; no single-number markets.
- Kill criteria are numeric or observable and have a decision date.
- The recommendation could be "stop"; the document does not assume the idea must proceed.
- Differentiation is stated as a mechanism, not a feature list.

## Failure handling
- No customer evidence available → the assessment's recommendation is "test first" with the interview or landing-page plan; never upgrade confidence without behaviour.
- Idea too generic to frame → produce the three problem reframings and ask the user to choose or react; do not pick silently.
- User insists on skipping validation → record the decision as `D-` with the human owner and proceed with the assumptions clearly marked.

## Safety boundaries
- Never promise outcomes, valuations or growth rates.
- Never fabricate customer interviews, statistics or competitor facts.
- Regulatory or legal feasibility notes are preliminary research; route to `legal-risk-governance` and counsel.

## References
- `templates/business/opportunity-assessment.md`, `templates/business/validation-plan.md`
- `skills/research-intelligence/references/market-sizing.md`
- `skills/business-model-unit-economics/SKILL.md`
- `standards/business/business-case-standard.md`
