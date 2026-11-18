---
name: strategy-market-sizing
description: Develop a differentiated company or product strategy with a one-sentence strategic choice, behavioural segmentation, bottom-up market sizing, differentiation basis, wedge, KPIs, kill thresholds and a pre-mortem. Use for startup strategy, expansion and positioning decisions.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: strategy
---
# Strategy and market sizing

## Purpose
State a falsifiable strategic choice grounded in customer evidence, size it honestly, name the real basis of differentiation and define what would make the team stop.

## When to use
- After idea validation has produced evidence and before product definition.
- When positioning, segment or expansion decisions are disputed.

## Preconditions
- Research brief, competitor map and opportunity assessment exist, or the gaps are explicitly listed.

## Inputs
- Evidence ledger, customer findings, competitor map, opportunity assessment.
- Founder capabilities and constraints.

## Procedure
1. **Start with the customer.** Who has the problem, in what context, how often, current alternatives, economic or emotional cost. Cite ledger ids.
2. **Write the strategic choice in one sentence:** for [specific segment], who [job/problem], we provide [outcome] through [distinct mechanism], unlike [alternative], because [credible capability or evidence].
3. **Segment by behaviour** (needs, urgency, budget, buying process, access), not demographics alone.
4. **Differentiation.** From the competitor map, name the basis: workflow, data advantage, distribution, trust, economics, speed, interoperability, service, network effects, expertise. Reject "AI-powered", "all-in-one", "10x" without proof.
5. **Size bottom-up** (`skills/research-intelligence/references/market-sizing.md`): buyers × reachable share × price × conversion and retention assumptions, low/base/high, every input sourced.
6. **Business model fit.** Hand candidates to `business-model-unit-economics`; summarise the result here.
7. **Wedge and expansion.** Define the narrow first segment and what will not be built in the first release; sketch the expansion path.
8. **Metrics.** Leading indicators, lagging outcomes, guardrail metrics, kill/continue thresholds with dates.
9. **Pre-mortem.** Why could this fail even with strong execution? Counter-positioning, incumbent response, regulation, channel loss, cost structure.
10. **Write the strategy memo** (`templates/business/strategy-memo.md`) and recommend the cheapest test before committing substantial resources.

## Outputs
- `02-product/strategy-memo.md`
- Ledger entries: decision recommendation (`R-`), risks (`K-`), rejected alternatives (`X-`).

## Quality criteria
- The strategic sentence is specific enough to be wrong.
- Differentiation is a mechanism with evidence.
- Sizing shows formula, inputs and ranges.
- Kill thresholds are numeric or observable with dates.
- The pre-mortem names at least three concrete failure paths.

## Failure handling
- Evidence thin → write the memo as hypotheses with the tests that would confirm them; mark confidence low.
- Multiple viable segments → compare on evidence strength, access and economics; recommend one and record the others as `X-` with reasons.

## Safety boundaries
- No invented precision, market figures or competitor facts.
- Strategy recommendations are confirmed by the human owner before downstream use.

## References
- `templates/business/strategy-memo.md`
- `skills/research-intelligence/references/market-sizing.md`
- `skills/competitive-analysis/SKILL.md`
