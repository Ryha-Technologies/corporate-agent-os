# Example: existing product improvement (illustrative)

Workflow: `product-maintenance`. Four audits run in parallel with disjoint outputs, then one consolidation.

## Intake (00-intake/brief.md excerpt)

```
Product: internal expense-approval web app. Access: repository, staging with test accounts, 90-day analytics
export, anonymised support tickets. Authorisation (F-003): defensive review of staging only; no production
testing. Goal: prioritised list of what to fix first with evidence. Decision owner: <role>.
```

## Parallel audit outputs

| Stage | Agent | Output | Example finding (illustrative) |
|---|---|---|---|
| product-audit | product-manager | `02-product/product-audit.md` | "<n>% of approvals use the mobile view (analytics, method: <query>), but the approval button is below the fold on common phone sizes." |
| ux-audit | ux-auditor | `07-quality/ux-audit.md` | "Task 'approve a pending expense' failed for <n>/<m> test accounts due to ambiguous status labels; WCAG 1.4.3 contrast fails on status chips (<ratio>:1)." |
| technical-audit | software-architect | `07-quality/technical-audit.md`, `08-legal-oss/component-register.md` | "<n> dependencies with advisories (scan tool <name> <version>, <date>); one component with NOASSERTION licence; N+1 query on approvals list (file:line)." |
| security-audit | security-engineer | `05-architecture/threat-model.md`, `07-quality/security-review-audit.md` | "Approval endpoint trusts client-supplied approver id (file:line) — high; session cookie missing attributes — medium. Scope: staging only (F-003)." |

## Consolidated roadmap (02-product/improvement-roadmap.md excerpt)

```
| 1 | Server-side approver authorisation fix | tests hypothesis: none (defect) | evidence: security finding S-01 | effort S | risk high if unfixed |
| 2 | Mobile approval layout and status labels | H-020: approval time drops <x>% | evidence: ux-audit U-03, analytics | effort M |
| 3 | Dependency updates with licence resolution | — | technical-audit T-07, component register | effort S |
| rejected | Full rewrite in <framework> | — | compared against targeted fixes; cost and risk not justified (X-004) |
```

## Maintenance plan (09-operations/maintenance-plan.md excerpt)

```
Monthly: dependency and advisory review with licence check; monitoring review; documentation refresh.
Quarterly: security review within written scope; threat model update; accessibility re-check of changed screens.
After any incident: postmortem within <days>; lessons to ledger.
```

What this example shows: four independent audits with evidence references, a roadmap that explains priority and records the rejected rewrite, and a maintenance cycle.
