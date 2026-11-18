---
name: business-model-unit-economics
description: Build and stress-test business models with transparent unit economics (pricing, gross margin including variable compute and AI costs, CAC, LTV, payback, churn, break-even, sensitivity) and low/base/high scenarios. Use when revenue, cost, pricing or runway figures are needed for a decision.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: finance
---
# Business model and unit economics

## Purpose
Turn a business idea into numbers that are honest about being estimates: every input is an explicit, ranged, sourced assumption; every output is a range; the most influential assumptions are named so they can be tested first.

## When to use
- Opportunity assessment needs revenue and cost reasoning.
- Pricing, packaging or a "free/unlimited" plan is proposed.
- Runway, break-even or funding needs are being discussed.

## Preconditions
- Segment, business model candidates and competitor pricing are available (from `business-idea-validation` and `competitive-analysis`).
- Spreadsheet or script available for arithmetic; prose is not a calculator.

## Inputs
- Business model options, target segment and buyer.
- Cost drivers: hosting, database, storage, egress, observability, third-party APIs, AI tokens by feature, payment fees, support, people.
- Competitor and substitute prices; any willingness-to-pay evidence.

## Procedure
1. **Choose the model(s) to evaluate** and define the unit (seat, account, transaction, workflow run).
2. **Revenue assumptions.** Price per unit (low/base/high), units per customer, conversion from trial/lead, churn per period, expansion, discounts, collection delay. Separate bookings, billings, cash and recognised revenue.
3. **Cost of goods.** Variable costs per unit including compute, storage, bandwidth, AI tokens (prompt and completion separately where priced so), third-party API calls, payment processing, support minutes. Compute gross margin per plan.
4. **Acquisition.** CAC by channel with the assumption trail (spend ÷ customers, or time cost for founder-led sales). Payback period = CAC ÷ monthly gross profit per customer.
5. **Lifetime value.** LTV from churn-derived lifetime × gross profit per period. State the churn assumption's evidence; LTV is only as good as churn.
6. **Operating costs.** People, software, security, legal, insurance, marketing, contingency.
7. **Scenarios and break-even.** Low/base/high for the five most influential inputs; compute break-even customers and date per scenario.
8. **Sensitivity.** Vary each key input ±25–50% and report the effect on gross margin, payback and break-even. Name the top three drivers.
9. **Pricing sanity checks.** No "unlimited" without a fair-use and cost policy; price anchored to value and alternatives, not cost alone; margin positive at base case including AI costs.
10. **Document** in `templates/business/business-model.md` with the assumption register: input, value range, source or reasoning, confidence, test that would firm it up.

## Outputs
- `02-product/business-model.md`
- `02-product/financial-model.(xlsx|csv|py)` with visible formulas or code
- Ledger assumptions (`A-`) with `review_by` dates.

## Quality criteria
- Every input has a range and a source or reasoning; no bare numbers.
- Variable AI and cloud costs appear in gross margin.
- Payback, LTV and break-even are reported per scenario, not as single points.
- Sensitivity identifies the drivers to test first.
- Estimates are labelled ESTIMATE in every table.

## Failure handling
- No willingness-to-pay evidence → use competitor anchors and mark price confidence low; propose a WTP test.
- Costs unknown → use vendor list prices with URL and date; mark as upper bound.
- Model shows negative margin → report it; do not tune assumptions until it looks good.

## Safety boundaries
- Do not present estimates as forecasts or facts.
- Tax, accounting treatment and securities matters require qualified professionals.
- No pricing goes to customers without human approval.

## References
- `templates/business/business-model.md`
- `standards/business/business-case-standard.md`
- `skills/finance-operations/SKILL.md` for the operating budget side
