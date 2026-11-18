# Task management

**Component type:** specification + executable validator.

A task contract is the only way work moves between agents. The orchestrator writes one contract per unit of work, the assigned agent executes within its `file_ownership`, and the named `reviewer` (never the same agent) checks the `acceptance_criteria` with the `verification` method.

## Files

| File | Purpose |
|---|---|
| `task-contract.schema.json` | JSON Schema (draft 2020-12) for a task. Closed schema: unknown fields fail validation. |
| `examples/T-003-competitor-map.json` | A complete, valid example. |
| `../../scripts/validate/validate_tasks.py` | Validates every `*.json` under a project's `10-decisions/tasks/` folder or the examples here. |

## Lifecycle

```
PROPOSED → READY → RUNNING → REVIEW → ACCEPTED
                      ↓          ↓
                   BLOCKED     REWORK → RUNNING (max_retries)
                                 ↓
                              REJECTED / CANCELLED
```

- `READY` requires: every dependency `ACCEPTED`, inputs exist, owner has no other `RUNNING` task touching overlapping `file_ownership`.
- `REVIEW` is entered only by the assigned agent returning a structured report (see `core/orchestrator/report-format.md`).
- `REWORK` must name the failed criterion and the exact fix. After `budget.max_retries` reworks the orchestrator escalates instead of looping.
- `ACCEPTED` can be set only by the reviewer or, for `risk: low` tasks with no reviewer, by the orchestrator after reading the report. High and critical risk always need a reviewer and the listed `approval`.

## Writing good contracts

- `objective` states the outcome ("the product lead can decide the wedge"), not the activity ("research competitors").
- `acceptance_criteria` are testable. "At least 6 competitors with dated sources" passes or fails; "thorough analysis" does not.
- `file_ownership` is minimal. Two tasks in the same parallel group must not share a pattern; the workflow validator enforces this for stage outputs and the orchestrator must enforce it for ad-hoc tasks.
- `budget` is a ceiling, not a target. A task that needs more should be split.
- `approval` lists who must sign before the output is used downstream. `human` is mandatory for anything in `core/permissions/policy.yaml` → `human_approval_required`.

## Validation

```bash
python scripts/validate/validate_tasks.py core/task-management/examples
python scripts/validate/validate_tasks.py <project>/10-decisions/tasks
```

The validator checks schema conformance, that `reviewer != assigned_agent`, that dependencies reference existing task ids in the same folder, and that no two `READY`/`RUNNING` tasks have overlapping ownership globs.
