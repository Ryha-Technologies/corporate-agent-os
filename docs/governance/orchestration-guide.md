# Orchestration guide

How a project runs under the corporate orchestrator. The normative text is `core/orchestrator/operating-procedure.md`; this guide explains it for operators.

## Lifecycle

1. **Intake** — brief, workspace, ledger, workflow choice, one blocking question at most.
2. **Plan** — task contracts per stage with budgets by risk; DAG checked; reviewers assigned; owner map.
3. **Delegate** — real sub-agents where the host has them; one writer per path; worktrees for parallel code.
4. **Integrate and review** — structured reports only; reviewer verdicts per gate; bounded rework loops; evidence-based conflict resolution.
5. **Approve** — pause for named humans at policy-defined points; record approvals.
6. **Report** — the ten-part report; what was not run is stated.
7. **Recover** — restart from files, not chat.

## What you will be asked to approve

Opportunity decision, product definition, naming and brand direction, legal foundation, security risk acceptance, release, go-live, and anything in `core/permissions/policy.yaml → human_approval_required`. Approvals are recorded in `10-decisions/approvals.md` with your name, the date and the scope. Silence is not approval.

## How many agents

As few as the stages need. `core/budget-management/budget-policy.yaml` caps parallel agents at four and active specialists at eight per run by default. A one-page copy change needs one specialist and one reviewer, not a company.

## Conflicts between agents

The orchestrator compares source quality, recency, method and scope; asks each side for its strongest counter-evidence; records the decision with residual uncertainty. It never averages conflicting numbers.

## Budgets and stop conditions

Each task carries model-call, retry and timeout ceilings. The orchestrator stops and asks when a stage times out twice, total review loops are exhausted, a critical finding appears, an approval is pending too long, or the same defect returns after two rework cycles (a specification problem).

## Reading the report

The first section is the decision. The second is what exists and how it was verified, with gate verdict paths. The last is what was not run. If a report calls something production-ready, check that every gate in `07-quality/` is PASS and no critical finding is open; if not, treat the report as defective and file the transcript as a regression case.
