---
name: code-review
description: Independently review a diff for correctness, security, maintainability, test adequacy, scope discipline and secrets, re-running reported build and test commands where possible and returning severity-ranked findings with file and line evidence. Use at the build gate or before merging any change.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: engineering
---
# Code review (independent)

## Purpose
Catch defects, security weaknesses, scope creep and unverified claims before code is merged, with evidence a developer can act on.

## When to use
- Every change at the build gate; any pull request; before release.

## Preconditions
- The reviewer did not author the change; the diff, task contract (file ownership, acceptance criteria) and the author's report with commands are available.

## Inputs
- Diff or branch; task contract; author's `CHECKS_ACTUALLY_RUN`; repository conventions; threat model (if any).

## Procedure
1. **Verify claims.** Re-run the reported build, lint, type and test commands where the environment allows; compare with the report. Mark discrepancies as findings.
2. **Scope.** Changes limited to the task's file ownership and objective; no unrelated refactors, generated files or formatting churn.
3. **Correctness.** Logic against acceptance criteria; edge cases; off-by-one and null handling; concurrency; error paths; state handling in UI.
4. **Security.** Input validation at boundaries, authorisation checks, injection risks (SQL, command, template, path), output encoding, CSRF/CORS/SSRF, file handling, deserialisation, secrets or tokens in code or logs, dependency additions and their licences, insecure defaults.
5. **Maintainability.** Naming, module boundaries, duplication, dead code, debug output, comments that explain why, consistency with conventions.
6. **Tests.** Cover the change including negative and failure cases; fail for the right reasons; no tests weakened or skipped silently; flaky patterns.
7. **Data and migrations.** Reversibility, constraints, index justification, backfill safety.
8. **Documentation.** Behaviour changes reflected in docs and changelog.
9. **Findings.** Severity (critical, high, medium, low), `file:line`, description, impact, suggested fix, retest method. Critical: secrets, unverified test claims, exploitable flaws.
10. **Verdict** in gate format. Reviewers do not fix code; remediation returns to the owner.

## Outputs
- `07-quality/gate-build-<date>.md` with findings.

## Quality criteria
- Reported commands were re-run or marked `NOT_RUN` with reason.
- Every finding has location, impact and fix.
- Scope violations and silenced tests are called out explicitly.

## Failure handling
- Environment cannot run tests → review statically, mark verification `NOT_RUN`, and require the test auditor to run them.
- Diff too large → request splitting; review the riskiest paths first and say what was not reviewed.

## Safety boundaries
- Read-only: never modify implementation during review.
- Never approve on the author's confidence or on green CI alone when tests were not inspected.

## References
- `standards/engineering/engineering-standard.md`, `standards/security/secure-development.md`
- `templates/testing/gate-verdict.md`
