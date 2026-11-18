# Quality gates

**Component type:** specification (data file consumed by workflows, reviewers and the validator).

`gates.yaml` defines twelve gates. A workflow stage names a gate; the gate's `reviewer` (an independent agent) checks the `evidence` list and the `pass`/`fail` conditions and records a verdict.

## Verdicts

| Verdict | Meaning |
|---|---|
| `PASS` | All evidence present, no fail condition holds. |
| `PASS_WITH_ACCEPTED_RISK` | A `high` or `medium` finding remains; the named approver accepted it in writing (`10-decisions/accepted-risks.md`). `critical` findings cannot be accepted this way. |
| `FAIL` | At least one fail condition holds. The stage returns to REWORK with the finding, evidence and the exact fix. |
| `NOT_ASSESSED` | Evidence missing; the gate was not run. Never shown as a pass. |

## Rules

1. The agent that produced the artefact is never the gate reviewer. The workflow validator rejects a stage whose `review` equals its `agent`.
2. The orchestrator cannot waive `critical` findings in `security`, `legal`, `testing` or `release`.
3. `human_approval: true` gates need a named human in `10-decisions/approvals.md` before dependants start. The orchestrator asks; it does not infer approval from silence.
4. A gate verdict is recorded in `07-quality/gate-<id>-<date>.md` using `templates/testing/gate-verdict.md`.
5. Every finding carries: severity, evidence (path, line, screenshot or command output), impact, required fix, retest method.

## Mapping to reviewer agents

| Gate | Reviewer agent |
|---|---|
| discovery | research-auditor |
| opportunity | business-model-auditor |
| product | ux-auditor |
| brand | brand-originality-auditor |
| design | design-qa-auditor |
| architecture | architecture-reviewer |
| build | code-reviewer |
| security | security-auditor |
| testing, release | test-auditor |
| documentation | documentation-auditor |
| legal | legal-licensing-reviewer |

## Validation

`scripts/validate/validate_core.py` checks that every gate has the required keys, that reviewer ids exist under `agents/reviewers/`, and that every `gate:` used in `workflows/` exists here.
