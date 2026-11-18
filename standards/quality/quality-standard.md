# Quality standard

Applies to verification, release decisions and the evaluation of agents and skills.

| # | Requirement | Verified by |
|---|---|---|
| Q1 | Every acceptance criterion maps to at least one executed test with a result in the traceability matrix. | Traceability matrix |
| Q2 | Result categories are PASS, FAIL, BLOCKED, NOT_RUN, NOT_APPLICABLE; NOT_RUN is never converted to PASS; NOT_APPLICABLE needs a reason. | Test report |
| Q3 | Every result records environment, version, date, command or action, expected, actual and evidence. | Test report |
| Q4 | High-risk features have negative, boundary, permission and recovery tests, not only the happy path. | Test plan, auditor |
| Q5 | Coverage percentages are supporting evidence only; the risks they do not address are named. | QA report |
| Q6 | Flaky tests are quarantined with a ticket, never deleted silently; tests are never edited to pass without disclosure. | Code review |
| Q7 | The release recommendation (GO / GO_WITH_ACCEPTED_RISKS / NO_GO) is issued by a reviewer independent of the builder. | Gate verdict |
| Q8 | No release with any gate NOT_ASSESSED or any critical finding open; accepted risks are signed by named approvers with review dates. | Release readiness |
| Q9 | Agent and skill changes are followed by re-running the regression dataset and golden tasks; results are recorded with what actually ran. | Benchmark report |
| Q10 | Independent reviewers run in separate contexts (and different models where the host allows) from creators. | Orchestrator report |
| Q11 | Deliverables are never labelled production-ready, enterprise-grade or complete without the gate evidence that supports the label. | Reviewer |
