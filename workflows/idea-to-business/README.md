# idea-to-business

The end-to-end spine: from a rough idea to a reviewed plan covering opportunity, strategy, product, brand, experience, architecture, build planning, legal foundation and launch planning.

## Shape

```
intake → research-plan → { desk-research | competitor-map | customer-research-plan } → discovery-synthesis [gate: discovery]
  → { opportunity-assessment | business-model } → opportunity-decision [gate: opportunity, human]
  → strategy-memo → { product-definition [gate: product, human] | brand-foundation → naming [gate: brand, human] }
  → { experience-design [gate: design] | architecture [gate: architecture] } → build-plan
  → legal-foundation [gate: legal, human] ; launch-plan → final-report [human]
```

## What this workflow does not do

- It does not write production code. `build-plan` hands off to `software-development`.
- It does not run security testing. `architecture` produces the threat model; `security-review` runs later against an implementation.
- It does not launch anything. `launch-plan` prepares; `product-launch` executes with its own release gate.

## Stopping early is a valid outcome

If `opportunity-decision` recommends stop or pivot, the `condition` on `strategy-memo` is false and downstream stages are skipped. The final report then documents the evidence, the decision and the pivot options.

## Duration drivers

Customer research with real participants (recruiting, consent) and naming screens across several jurisdictions are the slow stages. Everything else is bounded by the task budgets in `core/budget-management/budget-policy.yaml`.

## Human approvals

Opportunity decision, product definition, naming, legal foundation and final report. The orchestrator records each in `10-decisions/approvals.md`.
