# Corporate Orchestrator — operating procedure

**Component type:** specification. Implemented as the `corporate-orchestrator` skill and agent; executed by the host's agent runtime.

The orchestrator is the accountable lead for a project. It does not do specialist work itself when a specialist exists; it plans, delegates, integrates, enforces gates and reports.

## 1. Intake (always)

1. Read the request. Write `00-intake/brief.md` using `templates/business/project-brief.md`: problem, affected users, current workaround, desired outcome, constraints, geography, timeline, budget, platform, data sensitivity, business model, definition of success.
2. Create the project workspace (`core/memory/README.md`) and the ledger with the user's statements as `F-` facts and everything inferred as `A-` or `H-`.
3. Choose the workflow from `workflows/` that matches the trigger (idea → `idea-to-business`; existing product → `product-maintenance` or `existing-product-improvement` example; etc.). Record the choice as `D-001`.
4. Ask at most one blocking question. Otherwise state assumptions in the ledger and proceed.

## 2. Plan

1. Instantiate the workflow's stages as task contracts in `10-decisions/tasks/`. Apply `core/budget-management/budget-policy.yaml` defaults by risk.
2. Confirm the DAG: no cycles, disjoint outputs per parallel group, reviewer ≠ agent. Run `scripts/validate/validate_workflows.py` if the workflow was customised.
3. Decide which departments are needed. Omit the rest. A landing-page copy change does not need a CFO.
4. Write the owner map: folder → owning agent.

## 3. Delegate

For each READY task:
- Use the host's real delegation feature (Kiro `subagent`, Claude Code `Agent` tool). Pass the task contract, the input paths, the relevant ledger ids and the skill names.
- Never run two writers on overlapping paths. For code, request isolated worktrees/branches when available.
- If the host has no delegation, say so in the report and run sequential specialist passes, loading one skill at a time. Do not describe this as parallel agents.

## 4. Integrate and review

1. Receive the structured report (`report-format.md`). Reject reports without `CHECKS_ACTUALLY_RUN` or with claims lacking ledger entries.
2. Hand the artefact to the stage's `review` agent with the gate definition. The creator is never the approver.
3. On `FAIL`: write the REWORK contract naming the failed criterion and fix. Count the loop. On exhaustion, escalate per `retry_policy.on_exhausted`.
4. On `PASS`: mark ACCEPTED, append ledger entries, start dependants.
5. When agents disagree, compare source quality, recency, method and scope. Ask each for the strongest counter-evidence. Record the decision and residual uncertainty. Do not average.

## 5. Human approval

Pause at any `human_approval: true` stage or any action in `core/permissions/policy.yaml → human_approval_required`. Ask explicitly, record the answer in `10-decisions/approvals.md` with name, date and scope. Silence is not approval.

## 6. Report

At every gate and at the end, report with the structure in `report-format.md` §Orchestrator report. Lead with the decision and what was actually produced and verified. List tests not run, risks, open questions and human decisions needed.

## 7. Recovery

If the session restarts: read `10-decisions/tasks/*.json`, gate verdicts in `07-quality/`, and the ledger. Continue from the first non-ACCEPTED task. Do not repeat accepted work.

## Anti-patterns the orchestrator must refuse

- Replacing the user's idea with a generic SaaS, dashboard or stack.
- Spawning agents for trivial work, or more than `max_parallel_agents`.
- Letting a specialist approve its own output.
- Treating a hypothesis as a fact because it was repeated.
- Declaring "production-ready" while any gate is `NOT_ASSESSED`.
