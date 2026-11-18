# Engineering standard

Applies to all code, configuration, migrations and infrastructure definitions.

| # | Requirement | Verified by |
|---|---|---|
| E1 | Inspect the repository (language, package manager, structure, conventions, tests, CI) before editing; do not replace the stack. | Code review |
| E2 | Work in vertical slices with disjoint file ownership; parallel code work uses isolated worktrees or branches; integration is a reviewed step. | Build plan, code review |
| E3 | Maintainable code: focused functions, explicit types where supported, consistent naming, no duplication, no speculative abstraction, no dead code or debug output. | Code review |
| E4 | Input validated at trust boundaries; output encoded; parameterised queries; authorisation enforced server-side; errors handled and logged without sensitive data. | Code review, security review |
| E5 | Secrets come from environment or a vault; never in code, logs, test fixtures or repositories. | Secret scan, code review |
| E6 | Tests exist at the right layers (unit, integration, contract, e2e as applicable) including negative, boundary and failure cases; tests fail for the right reasons. | Test report, code review |
| E7 | Formatter, linter, type checker, tests and build run before submission; exact commands and output recorded. Failures are fixed or disclosed, never silenced. | CHECKS_ACTUALLY_RUN |
| E8 | Dependencies are pinned, licence-reviewed (component register) and provenance-checked before adoption. | Component register |
| E9 | Migrations are reversible, constraints explicit, indexes justified by named queries; destructive production changes need approval and backup. | Data model, code review |
| E10 | Observability: structured logs with correlation ids, metrics, traces; alerts have owners. | Architecture, DevOps review |
| E11 | Environment separation (dev, staging, production); reproducible builds; configuration externalised. | DevOps review |
| E12 | Documentation, examples, changelog and operational notes updated when behaviour changes; documented commands executed. | Documentation gate |
| E13 | Diff limited to task scope; no secrets, generated files or unrelated changes. | Code review |
| E14 | "Works" requires evidence (test output, rendered UI inspection); never because code was written. | Reviewer |
