# Workflow engine

**Component type:** specification + executable validator. There is no runtime scheduler in this repository. The host platform (Kiro sub-agents, Claude Code Agent tool, or a human operator) executes the stages; this layer defines them as data so they can be validated, documented and reused across hosts.

## What a workflow file is

`workflows/<id>/workflow.yaml` conforming to `workflow.schema.json`. Each stage names an agent, the skills it should load, the artefacts it produces, its dependencies, an optional parallel group, an optional quality gate and an optional independent reviewer.

```yaml
id: brand-development
stages:
  - id: category-audit
    agent: brand-strategist
    skills: [brand-strategy-story, research-intelligence]
    objective: Audit category conventions and competitor identities before any creative work
    depends_on: [intake]
    outputs: ["03-brand/category-audit.md"]
    parallel_group: brand-foundation
    gate: brand
    review: brand-originality-auditor
```

## Execution semantics (what the orchestrator must do)

| Feature | Semantics |
|---|---|
| Sequential | Stage starts when all `depends_on` stages are ACCEPTED and their gates passed. |
| Parallel | Stages sharing `parallel_group` with satisfied dependencies may run concurrently. Their `outputs` must be disjoint (validator-enforced). |
| Conditional | `condition` is evaluated by the orchestrator from the memory ledger. A skipped stage is recorded as SKIPPED with the reason; dependants treat it as satisfied only if the workflow marks the stage optional via the condition text "optional:". |
| Review and revision | A stage with `review` cannot be ACCEPTED by its own agent. The reviewer returns PASS / FAIL with findings. FAIL sends the stage to REWORK. `retry_policy.max_review_loops` bounds the loop; `on_exhausted` says what happens then. |
| Human approval | `human_approval: true` pauses the workflow until a named human records approval in `10-decisions/approvals.md`. |
| Cancellation | Any stage may be CANCELLED by the orchestrator or a human; dependants become BLOCKED with the reason. |
| Retry / timeout | `timeout_minutes` per stage; a timed-out stage is BLOCKED, not silently retried. Retries consume the task budget. |
| Escalation | After exhausted loops or a critical finding: escalate to the department lead, then executive, then human, as stated in `on_exhausted`. |
| Recovery | Artefacts are files; a restarted workflow re-derives state from existing outputs and gate verdicts, never from chat history. |

## Isolation and merging

- Independent engineering stages should run in separate git worktrees or branches when the host supports it (Claude Code `isolation: worktree`; Kiro via the orchestrator creating `.worktrees/<stage>`).
- Integration is a stage of its own, owned by the lead engineer, with `review: code-reviewer`.
- Non-code artefacts use disjoint paths; the orchestrator owns `10-decisions/` and the memory ledger.

## Validator

```bash
python scripts/validate/validate_workflows.py            # all workflows
python scripts/validate/validate_workflows.py workflows/idea-to-business/workflow.yaml
```

Checks: schema conformance; unique stage ids; dependencies refer to existing stages; the graph is acyclic (Kahn's algorithm); `review != agent`; outputs are disjoint within a parallel group; every `gate` exists in `core/quality-gates/gates.yaml`; every `agent` and `review` exists under `agents/`; every skill exists under `skills/`; `human_approval: true` on any stage whose gate requires it.
