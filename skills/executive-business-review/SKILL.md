---
name: executive-business-review
description: CEO-level review of a product, company or idea that reads everything the organisation has produced, analyses competitors, revenue models, payments and pricing, costs and unit economics, risks and the problems they imply, then decides what to improve and lays out a staged plan with reviews from now to production. Use when a user wants the whole picture and a decision ("what should we do", "is this viable", "review my business", "plan this to launch").
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: executive
---
# Executive business review (CEO)

## Purpose
Give the owner one evidence-backed picture of the business: where it stands against competitors, how money comes in and goes out, what is broken or missing, what to change, in what order, with what checks, up to production and after it. The CEO decides on evidence and recommends; the human owner approves.

## When to use
- The user asks for a full analysis, a go/no-go, a plan to launch, or "what is wrong and how do we fix it".
- Before committing money, a public launch, or a pivot.
- At the start of the `idea-to-production` workflow (sets direction) and at its release gate (confirms it).

## Preconditions
- The ledger, gate verdicts and existing artefacts are read, not chat summaries.
- Where research does not exist yet, the CEO commissions it from the research, finance and product departments (`dept-research`, `dept-strategy-product`) rather than guessing. Nothing in this review is invented to fill a gap; gaps are listed.

## Inputs
- Brief, research brief, competitor map, customer findings, business model, PRD, architecture, security and legal registers, analytics or revenue data if the product exists, the owner's constraints (money, time, risk appetite, must-not-do).

## Procedure
1. **Facts first.** Build a one-page fact sheet from the ledger: what the product is, who pays, how much, how often, how they find it, what it costs to serve, what has been verified by evidence and what is assumption. Every line has a ledger id or is marked `ASSUMPTION`.
2. **Competitor analysis** (from `competitive-analysis`, commissioned if missing): for each direct competitor and the top substitute (including "do nothing" and spreadsheets): what they charge and how (pricing page captured with date), their revenue model, their payment methods and geography, their weakest reviews (source and date), where they win, where they lose, what they cannot do because of their model. Output a positioning map on the two axes customers actually choose on, not features.
3. **Revenue model analysis.** Enumerate the viable models for this product (one-time, subscription, usage, freemium with conversion, marketplace take rate, transaction fee, licence, services, advertising, hardware plus service). For each: who pays, trigger of payment, expected ARPU range with source, churn or repeat assumptions, collection risk, and fit with the customer's buying behaviour from research. Reject models that need a sales motion or scale the owner does not have. Pick one primary and one fallback with reasons (`business-model-unit-economics`).
4. **Payments and money movement.** Who collects, where, in which currencies; payment methods customers in that geography actually use (cards, UPI, bank transfer, wallets, cash on delivery, invoices); provider options with fee structures and settlement times (captured with date); refunds, disputes, taxes (GST/VAT/sales tax) and invoicing obligations as questions for counsel and an accountant; payout flows if there is a marketplace side; what happens when a payment fails. Fees and taxes go into the unit economics.
5. **Unit economics and runway.** Ranged (low/base/high) price, cost to acquire, cost to serve, gross margin, payback, break-even volume; monthly burn and runway given the owner's budget. Sensitivity on the two inputs that matter most. Numbers come from steps 2 to 4 with sources; no "industry standard" without a citation.
6. **Problem analysis.** From the fact sheet, research and the economics: list every problem that would stop this business or product. Categorise: demand (nobody wants it enough to pay), distribution (cannot reach them affordably), economics (margin or payback), product (does not do the job; UX measured as common; quality gates failed), delivery (cannot build or operate it), trust and legal (compliance, data, licensing, IP, payments regulation), team and money (runway, skills). For each: evidence, severity (kills / wounds / annoys), and whether it is a knowledge gap or a real defect.
7. **Improvements.** For each kills/wounds problem: the options to overcome it, the cheapest test that would show whether the option works, cost and time, and what it gives up. Prefer the narrow wedge with the clearest customer evidence over the biggest story. Include product and design improvements from `codebase-audit-upgrade` and the `template_signature` scores where a product exists.
8. **Decision.** Pursue, test first, pivot or stop. State the question, options, evidence ids, the assumption that matters most, the decision, and what would change it. Recommendations only until the human owner confirms.
9. **Staged plan to production.** Map the work onto `workflows/idea-to-production/workflow.yaml` (or the subset that applies): stages, owners (department skills), outputs, the gate and reviewer of each, the human approvals, kill criteria per stage, budget per stage, and the order. Each stage ends with a review that can stop the plan. Post-launch: the metrics that confirm or refute the key assumptions, read at fixed dates.
10. **Anti-slop pass.** Run `anti-slop-quality-gate` on this review: no claim without a source or an `ASSUMPTION` label, no generic strategy language ("leverage synergies", "disrupt"), no numbers without ranges and sources, no plan step without an owner, output and check. Then submit to `business-model-auditor`.

## Outputs
- `10-decisions/executive-review.md` with sections: Fact sheet, Competitors and positioning, Revenue models, Payments and money movement, Unit economics and runway, Problems, Improvements, Decision, Staged plan with reviews, Not run and open questions.
- `10-decisions/opportunity-decision.md` (the decision block alone) when used inside a workflow.

## Quality criteria
- Every number is a range with a dated source or is labelled `ASSUMPTION`; every competitor fact has a capture date.
- At least three revenue models were compared before one was chosen; payments, taxes and fees appear in the unit economics.
- Every problem rated kills or wounds has at least one improvement option with a cheapest test.
- The plan names an owner, output, reviewer, gate and kill criterion for every stage and ends at production plus a post-launch review date.
- Reviewed by `business-model-auditor`; the decision is marked as a recommendation pending human approval.

## Failure handling
- Missing research: commission it (list the tasks) and mark the dependent sections `BLOCKED` rather than guessing.
- Owner's constraints conflict with the only viable model: say so plainly and present the choice; do not stretch numbers to fit.
- Payments or tax law unclear for the geography: write the counsel and accountant questions; never state obligations as fact.

## Safety boundaries
- No fabricated or unsourced evidence; never override a critical security, legal or safety finding; no legal, tax or investment advice.
- No commitment of money, launch or public statement without the human owner.

## References
- `skills/competitive-analysis/SKILL.md`, `skills/business-model-unit-economics/SKILL.md`, `skills/strategy-market-sizing/SKILL.md`, `skills/business-idea-validation/SKILL.md`, `skills/codebase-audit-upgrade/SKILL.md`
- `templates/business/business-model.md`, `templates/business/competitor-matrix.md`, `templates/business/opportunity-assessment.md`, `templates/business/strategy-memo.md`
- `workflows/idea-to-production/workflow.yaml`, `core/quality-gates/gates.yaml`
- `evaluations/originality/slop-patterns.md`
