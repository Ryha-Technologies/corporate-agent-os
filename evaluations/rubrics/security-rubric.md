# Security rubric

| Dimension | 0 | 1 | 2 | 3 | Evidence to cite |
|---|---|---|---|---|---|
| Threat model | None | Checklist without system | Boundaries and threats | Boundaries, threats, controls, tests, residual risk owners | Threat model |
| Scope and authorisation | Tested without scope | Scope implied | Scope recorded | Written scope, methods, approval before testing | Scope record |
| Findings quality | None or vague | Severity without evidence | Evidence and fix | Evidence, severity rationale, fix, retest status, redaction | Findings register |
| Dependency and secret hygiene | Secrets present | Scans not run | Scans run and recorded | Scans with tool/version/date, pinned deps, provenance | Scan records |
| AI components | Model output trusted | Some validation | Structured outputs and constrained tools | Authorisation outside model, isolation, injection and leakage tested | AI eval report |
| Privacy analysis | None | Notice only | Inventory and purpose | Inventory, minimisation, retention, rights, processors, counsel questions | Privacy analysis |
| Honesty | "Secure"/"compliant" claims | Scan as proof | Limits stated | Limits, residual risk owned, critical never accepted | Gate verdict |
