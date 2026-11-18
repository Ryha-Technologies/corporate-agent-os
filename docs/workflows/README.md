# Workflow guide

Workflows are DAGs in `workflows/<id>/workflow.yaml`; each has a generated `STAGES.md` table. Semantics are in `core/workflow-engine/README.md`.

## Choosing a workflow

| Situation | Start with | Then |
|---|---|---|
| Rough idea, unclear problem | `business-validation` | `idea-to-business` if the decision is pursue or test first |
| Validated idea, no product definition | `product-discovery` | `product-design`, `software-development` |
| Need a brand, name or identity | `brand-development` | — |
| PRD exists, need the experience | `product-design` | `software-development` |
| Design exists, need the build | `software-development` | `security-review`, `product-launch` |
| Any system approaching release or handling new data | `security-review` | — |
| Verified product ready to market | `product-launch` | `product-maintenance` after launch |
| Existing product, unclear what to fix | `product-maintenance` | targeted workflows per roadmap item |

## Reading a workflow

- `depends_on` sets order; stages in the same `parallel_group` with satisfied dependencies may run concurrently and never share output paths.
- `gate` names the quality gate; `review` names the independent reviewer (never the producing agent); `human_approval: true` pauses for a person.
- `condition` lets the orchestrator skip a stage when, for example, the opportunity decision is "stop".
- `retry_policy` bounds review loops and says who is escalated to.

## Customising

Copy a workflow folder, edit `workflow.yaml`, keep `id` equal to the folder name, run `python scripts/validate/validate_workflows.py workflows/<id>/workflow.yaml`, then `python scripts/package/render_roles.py` to refresh `STAGES.md`. The validator rejects cycles, unknown agents, skills or gates, reviewer-equals-author, missing human approval on gates that require it, and overlapping outputs inside a parallel group.

## Running without a sub-agent host

The same stages run as sequential passes under one agent: load the stage's skills, write within the stage's outputs, then run the reviewer's skills in a fresh context for the gate. The report must say that delegation was sequential.
