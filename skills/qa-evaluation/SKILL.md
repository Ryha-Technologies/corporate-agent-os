---
name: qa-evaluation
description: Independently verify a delivered artefact (requirements, UX, software, AI behaviour, documentation, release readiness) against the original request and acceptance criteria with reproducible tests and adversarial review, and issue GO / GO_WITH_ACCEPTED_RISKS / NO_GO. Use as the independent QA step at testing and release gates and for evaluating agent skills.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: qa
---
# Independent QA and evaluation

## Purpose
Provide a release decision that is independent of the builder and rests on executed evidence, including evaluation of AI behaviour and the agent skills themselves.

## When to use
- Testing and release gates; any claim of "done"; periodic evaluation of skills and agents.

## Preconditions
- Original request, acceptance criteria, specs, builder's report with commands, environment access.

## Inputs
- Request, PRD, design spec, brandbook, architecture, threat model, licence inventory, test reports, build artefacts.

## Procedure
1. **Test basis.** Collect artefacts; list missing specifications before testing.
2. **Layers.** Requirement traceability; functional (normal, boundary, invalid, negative, recovery, permission); integration (contracts, providers, retries, timeouts, idempotency); UI (keyboard, focus, semantics, responsive, states, real rendering); accessibility; performance; reliability (restart, outage, network loss, redelivery, backup/restore); security (threat model, scans, abuse cases); AI (task success, factuality, tool correctness, refusal boundaries, injection, leakage, consistency, latency, cost); brand consistency and distinctiveness; OSS/IP inventory and provenance.
3. **Slop and hallucination audit.** Generic claims, copied patterns, invented citations, fake testimonials or metrics, placeholder screens, inconsistent terms, unsupported features, made-up tests, unverified dependencies. Each element must serve a task or a documented decision.
4. **Evidence.** Environment, version, date, command or action, expected, actual, evidence link, severity. PASS / FAIL / BLOCKED / NOT_RUN / NOT_APPLICABLE; never convert NOT_RUN to PASS.
5. **Defects.** Severity by impact and exploitability or user harm; reproduction; scope; workaround; owner; retest.
6. **Release recommendation.** GO / GO_WITH_ACCEPTED_RISKS / NO_GO with blockers, accepted risks (with approver), tests not run, residual risks, required human sign-offs.
7. **Skill and agent evaluation.** Run the regression dataset (`evaluations/datasets/regression-cases.json`) and golden tasks; score with the rubrics; re-run after any change to skill or agent text. Record what actually ran.

## Outputs
- `07-quality/qa-report-<date>.md`, `07-quality/gate-testing-<date>.md`, `07-quality/gate-release-<date>.md`; `evaluations/benchmark-reports/<date>-*.md` for skill evaluations.

## Quality criteria
- Every acceptance criterion has a result; blockers are explicit.
- No inference from builder confidence; sample of tests reproduced.
- AI behaviour checks include prompt injection and refusal boundaries.
- Recommendation is independent of the implementation agent.

## Failure handling
- Cannot reproduce → BLOCKED with environment details; do not guess.
- Spec missing → test against the request and record the gap as a finding.

## Safety boundaries
- Read-only toward implementation; findings only.
- Security testing stays within written scope.

## References
- `templates/testing/qa-report.md`, `templates/testing/release-readiness.md`
- `evaluations/README.md`, `evaluations/rubrics/`
- `skills/test-strategy/SKILL.md`, `skills/anti-slop-quality-gate/SKILL.md`
