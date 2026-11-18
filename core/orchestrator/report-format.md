# Structured report formats

Every agent returns one of these. The orchestrator rejects reports that omit sections or convert `NOT_RUN` into a pass.

## Specialist / reviewer report

```text
TASK_ID: T-003
AGENT: competitive-analyst
STATUS: READY_FOR_REVIEW | REWORK_NEEDED | BLOCKED
SUMMARY: (3–6 lines: what was produced, main finding, recommendation)
OUTPUTS: (paths written, all inside file_ownership)
EVIDENCE_AND_SOURCES: (ledger ids or URL + access date; or NO_SOURCE_FOUND)
ASSUMPTIONS_AND_CONFIDENCE: (each assumption with high/medium/low and why)
DECISIONS_AND_REJECTED_ALTERNATIVES:
LEDGER_ENTRIES: (new F/H/A/R/K/Q/X entries as JSON lines for the orchestrator to append)
CHECKS_ACTUALLY_RUN: (command or action → result; PASS/FAIL/NOT_RUN; never infer)
OPEN_RISKS:
HUMAN_DECISIONS_REQUIRED:
BUDGET: model_calls=<n or NOT_MEASURED> retries=<n> wall_minutes=<n>
```

## Gate verdict (reviewer)

```text
GATE: brand
STAGE: naming
REVIEWER: brand-originality-auditor
VERDICT: PASS | PASS_WITH_ACCEPTED_RISK | FAIL | NOT_ASSESSED
EVIDENCE_CHECKED: (each required evidence item → present/missing, path)
FINDINGS:
  - severity: high
    finding: ...
    evidence: (path:line, screenshot, command output)
    impact: ...
    required_fix: ...
    retest: ...
SCORECARD: (when the gate uses one, e.g. evaluations/originality/originality-scorecard.md)
ACCEPTED_RISKS: (id, approver, date) or none
```

## Orchestrator report (gate or final)

1. Decision and recommendation.
2. What was actually produced, where, and how it was verified (commands, reviewers, gate verdicts).
3. Evidence-backed findings and key unknowns (ledger ids).
4. Product / brand / design / architecture status as applicable.
5. Delivery plan and ownership for the next stage.
6. Quality, security, legal/IP and licence status with gate verdicts.
7. Cost and budget consumed (or NOT_MEASURED).
8. Risks, assumptions and overdue hypotheses.
9. Human approvals obtained and still required.
10. Tests, checks and reviews not run, stated plainly.
