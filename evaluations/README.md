# Evaluations

**Component type:** datasets, rubrics and golden tasks (specification) + `run_evals.py` (implemented: validates the assets and produces a report skeleton with every model-dependent check marked NOT_RUN).

The repository is judged by what happens on real tasks, not by file counts. This folder holds the material needed to run that judgement repeatably. It does not hold results from runs that did not happen.

| Folder | Contents |
|---|---|
| `datasets/regression-cases.json` | 28 behavioural cases (prompt, expected, forbidden, skills, dimensions). E01–E15 carried over from v0.1.0. |
| `rubrics/` | Scoring rubrics per domain with 0–3 anchors and evidence requirements. |
| `golden-tasks/` | Benchmarks A–E: business opportunity, new brand, SaaS product, existing application improvement, product launch. Each defines input, workflow, expected evidence and evaluation dimensions. |
| `originality/` | Originality scorecard and the catalogue of slop patterns reviewers look for. |
| `benchmark-reports/` | One report per run. Empty except the README and the build-time report until a run is executed. |

## Running an evaluation

1. Install the skills into a host (Kiro, Claude Code or Codex) in a clean project.
2. For a regression case: paste the prompt, capture the full transcript, and score it with `rubrics/behaviour-rubric.md`. Record forbidden behaviours observed.
3. For a golden task: run the named workflow end to end with the orchestrator, keep the project workspace, and score each expected evidence item with the domain rubric. Independent human raters score; the model that produced the work does not score itself.
4. Record cost (model calls, tokens if exposed, wall time) and what could not be tested.
5. Write the report with `python evaluations/run_evals.py --report benchmark-reports/<date>-<host>.md`, then fill in the scores. The script pre-fills the structure and marks every model-dependent item NOT_RUN; replace only the items you actually ran.

## What counts

- Correctness, completeness, specificity, evidence quality, originality, usability, technical quality, security, cost, execution time, human review requirements (brief §16).
- A rubric score without the evidence path is not a score.
- Results are per host and per model; never aggregate across hosts without saying so.

## Status in this build (0.2.0)

No model-driven evaluation has been executed. `benchmark-reports/2026-11-18-build-validation.md` records only the repository's own validators and tests. Benchmark results remain NOT_RUN until someone runs them.
