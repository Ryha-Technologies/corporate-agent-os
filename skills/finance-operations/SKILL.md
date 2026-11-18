---
name: finance-operations
description: Create transparent operating budgets, revenue and cash models, pricing hypotheses, approval matrices, vendor registers and compliance question lists for technology companies, with every figure an explicit ranged assumption and professional review flagged. Use when planning budgets, runway, spend approvals or vendor operations.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: finance
---
# Finance and business operations

## Purpose
Give the company a budget, cash view and spending controls it can actually run, and make clear which questions need an accountant, tax adviser or lawyer.

## When to use
- After the business model; before hiring, vendor commitments or fundraising conversations.

## Preconditions
- Business model and unit economics exist (`business-model-unit-economics`); entity and jurisdictions known or assumed.

## Inputs
- Business model, pricing, headcount plan, vendor list, legal entity details.

## Procedure
1. **Context.** Legal entity, jurisdictions, revenue model, customer types, payment flows, vendors, tax and compliance questions, approval owners.
2. **Bottom-up operating model.** Headcount and contractors, cloud, AI API usage, software, security, payment fees, support, marketing, legal, insurance, taxes, contingency.
3. **Revenue model.** By segment, plan, seats, usage, discounts, refunds, churn, expansion, collection delays, taxes; separate bookings, billings, cash and recognised revenue.
4. **Margins.** Gross and contribution margin by product or plan including variable compute, AI tokens, storage, bandwidth, support and third-party fees.
5. **Pricing hypotheses** and willingness-to-pay tests; no "unlimited" without fair-use and cost policy.
6. **Cash and runway.** Low/base/high scenarios with sensitivity to growth, churn, usage and pricing; triggers for scenario switches.
7. **Approval matrix.** Purchases, refunds, subscriptions, vendor contracts, payroll, production spend, legal commitments: who approves what, at which amount.
8. **Vendor register.** Contracts, renewals, data processing terms, SLAs, cancellation, export, lock-in.
9. **Professional review.** List legal, accounting and tax matters for qualified professionals; do not invent compliance advice for unknown jurisdictions.

## Outputs
- `09-operations/operating-budget.*`, `09-operations/approval-matrix.md`, `09-operations/vendor-register.md`, runway scenarios, professional question list.

## Quality criteria
- Every figure has a range and a source or reasoning.
- Variable costs included in margins.
- Approval matrix covers all spend types with named roles.
- Professional-review list present.

## Failure handling
- Entity or jurisdiction unknown → model generically and mark tax/compliance items as unresolved.

## Safety boundaries
- No spend, payments, filings or contract acceptance by agents.
- No tax or accounting conclusions; questions only.

## References
- `templates/operations/operating-budget.md`, `templates/operations/approval-matrix.md`, `templates/operations/vendor-register.md`
- `skills/business-model-unit-economics/SKILL.md`
