# Assessment of the "Deep Research: Corporate Agent OS v1.0.0" report

Assessed 2026-11-18 against the inspected source trees and official platform documentation. The report is a useful requirements source. It is not an accurate description of an existing build.

## 1. Claims that are unsupported or incorrect

| Report claim | Finding | Consequence |
|---|---|---|
| "The deliverable is a production-ready repository v1.0.0 (with all code, skills, adapters, tests)" | No v1.0.0 artefact exists in the inputs. The only build is v0.1.0 with 25 skills and no tests. | Version label for this build is 0.2.0 beta. |
| "the structural validator passed on all" skills across Claude, Kiro and Codex | The v0.1.0 validator only checks frontmatter regexes; there is no cross-platform installation test. | New validators and pytest tests; compatibility matrix distinguishes tested from untested. |
| "Running Test 03 on a sample SaaS idea produced a working Next.js demo app and Figma files in /examples" | No `examples/`, `tests/` or Next.js code exists in any input. | Recorded as fabricated. Examples in this build are worked specifications, labelled as such. |
| "Download links are below" (two ZIPs) | No links or archives were supplied. | None. |
| "We use WIPO's Global Brand Database (50M+ records)" and "If any existing mark conflicts, it flags REVISION NEEDED" | No tool integration exists; WIPO record counts not verified here. | Naming skill keeps manual database procedure and does not quote record counts. |
| "We only allow permissively licensed repos (MIT, Apache 2.0) by default … We reject GPL-encumbered code" | Blanket rejection is not sound: obligations depend on use mode (SaaS hosting, linking, distribution, modification). | `oss-reuse-license` keeps use-mode analysis; GPL-family components are flagged for review, not auto-rejected. |
| "name is linguistically unique (no high embedding overlap with competitors)" and "semantic similarity checks to known corpuses" as originality tests | Embedding similarity is not evidence of legal or creative originality and no such tool exists in the inputs. | Originality scorecard treats similarity as a signal and requires human review; no tooling claim. |
| "ensemble multiple models … randomize prompts (temperature, synonyms)" to avoid repetition | No runtime exists to do this; host platforms control sampling. | Model-routing policy describes what the host can do and what it cannot. |
| "we include mini user tests … show them to a small panel (in simulation …)" | Simulated panels are not user research; the brief forbids inventing research results. | UX research skill labels simulated personas/panels as hypotheses only. |
| "CI/CD pipeline (GitHub Actions or equivalent) that runs on each commit" | Not present. | A GitHub Actions workflow for the repository's own validators is added (untested in CI here; runs locally). |
| Citations shown as numbered references ("[9]", "[11]") with no resolvable list | The report's sources cannot be checked. | None of the report's statistics or quotes are reused. |

## 2. Requirements matrix derived from the report

| Research requirement | Existing (v0.1.0) | Gap | Required improvement | Verification |
|---|---|---|---|---|
| Model every corporate role with inputs/outputs/decisions/KPIs | one summary table | no per-role data | `departments/*/roles.yaml` with 15 fields; rendered docs | `scripts/validate/validate_departments.py` |
| Hierarchical multi-agent design, DAG, one-writer-per-file | prose in orchestrator skill | not machine-checkable | `workflows/*.yaml` + `validate_workflow.py` (acyclic, ownership disjoint) | pytest `tests/unit/test_workflow_validator.py` |
| Creation / quality / governance separation | one auditor agent | reviewers per domain | 11 reviewer agents; workflow validator rejects self-review | validator + tests |
| Timeouts, budget limits, retries, tool allow-lists | none | policies | `core/budget-management`, `core/permissions` | schema validation |
| Research-driven UX, IA, design system, WCAG 2.2 AA | 2 skills | IA, tokens, audit | new skills + `standards/accessibility` | skill validator |
| Design QA comparing implementation to spec | mentioned | no procedure | `design-qa-auditor` agent + `templates/design/design-qa-report.md` | manual |
| Architecture, coding, security scanning, tests, CI/CD, code review, observability | 3 skills | review, test strategy, release | new skills + standards | skill validator |
| Trademark search (WIPO/USPTO/EUIPO/IP India), licence scanning, SBOM, privacy | 2 skills | jurisdiction references, asset provenance | `references/trademark-offices.md`, templates | links validated |
| Anti-slop: research before creation, multiple concepts, independent critique, rubrics, golden set | 1 skill + doc | scorecard, dataset | `skills/originality-audit`, `evaluations/originality/` | eval runner |
| Opportunity discovery: problem space, sizing, competitors, business model, kill criteria, MVP | inside strategy skill | dedicated flow | `skills/business-idea-validation`, `workflows/business-validation` | workflow validator |
| Install to Claude/Kiro/Codex | installer without safety | dry-run, manifest, backup, uninstall | new installer | `tests/integration/test_installer.py` |
| Compatibility matrix | one doc | evidence-based statuses | `docs/platform-compatibility-matrix.md` | manual review |
| Changelog | none | — | `CHANGELOG.md` | structure validator |

## 3. Recommendations adopted with modification

- "Prefer boring, mature technology" and "no microservices by default": adopted as written in `standards/engineering/architecture.md`.
- "Human-in-the-loop for high-risk": adopted; the approval list lives in `core/permissions/policy.yaml`.
- "Golden set regression suite": adopted as `evaluations/golden-tasks/`; results are recorded only when a run happens.
- "Corporate memory so agents don't copy earlier outputs": adopted as the project memory ledger; the "model collapse" framing is dropped as speculative.

## 4. Statements treated as speculative and not implemented

- Claims about LLM "repeat curse", "model collapse" and ensemble debiasing as solved problems.
- Any numeric targets quoted in the report (Lighthouse > 90, 99.9% uptime, 100% coverage) are examples, not requirements; the standards documents define targets per project.
