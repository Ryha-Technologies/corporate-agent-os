---
name: test-strategy
description: Derive a risk-based test strategy from the PRD, architecture and threat model; plan unit, integration, contract, end-to-end, regression, performance, accessibility, security and migration tests; build the traceability matrix and record results honestly. Use when planning or executing verification.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: qa
---
# Test strategy and execution

## Purpose
Make every acceptance criterion traceable to an executed test with an honest result, and spend testing effort where risk is.

## When to use
- After PRD and architecture; before and during implementation; before release.

## Preconditions
- Acceptance criteria exist; environments and tools are known; risk classification per feature.

## Inputs
- PRD, acceptance criteria, architecture, API contract, threat model, supported platforms and browsers.

## Procedure
1. **Test basis.** Collect the artefacts; list missing specifications as risks.
2. **Risk assessment.** Rate features by impact and likelihood of failure (data loss, money, safety, security, compliance); allocate depth accordingly.
3. **Layers and types.** Unit (logic, boundaries), integration (contracts, DB, external services with fakes), contract (API provider/consumer), end-to-end (critical user journeys), regression (previous defects), performance and load (budgets, p50/p95/p99, saturation), accessibility (with `accessibility-audit`), security (with `security-privacy`), migration (upgrade and rollback on realistic data), reliability (restart, dependency outage, timeout, retry).
4. **Traceability matrix** (`templates/testing/traceability-matrix.md`): criterion → test ids → result.
5. **Environments and data.** Realistic, anonymised test data; no production personal data; environment and version recorded for every run.
6. **Automation.** Deterministic, fast suites in CI; quarantine flaky tests with a ticket, never delete silently.
7. **Execution and recording.** For each test: environment, version, date, command, expected, actual, evidence, severity. Results: PASS / FAIL / BLOCKED / NOT_RUN / NOT_APPLICABLE. Never convert NOT_RUN to PASS.
8. **Defects.** Reproduction, expected/actual, scope, workaround, owner; close only after retest.
9. **Coverage as supporting evidence** only; name the risks that coverage numbers do not address.

## Outputs
- `07-quality/test-strategy.md`, `07-quality/test-plan.md`, `07-quality/traceability-matrix.md`, `07-quality/test-report-*.md`, defect log.

## Quality criteria
- Every acceptance criterion maps to at least one test with a result.
- High-risk features have negative, boundary, permission and recovery tests.
- Results carry environment, version and evidence.
- Flaky tests are tracked, not hidden.

## Failure handling
- Tool or environment missing → NOT_RUN with reason and the plan to run.
- Criteria untestable as written → send back to product with the ambiguity.

## Safety boundaries
- No load testing against shared or production systems without approval.
- No production personal data in test environments.

## References
- `templates/testing/test-plan.md`, `templates/testing/traceability-matrix.md`, `templates/testing/test-report.md`
- `standards/quality/quality-standard.md`
