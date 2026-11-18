# Quality and evaluation guide

## Two levels of quality

1. **The repository as software.** `scripts/validate/run_all.py` and `python -m pytest -q` must pass. They check structure, skills (spec conformance and ten sections), agents (tiers, tools, read-only reviewers), departments (fifteen fields), workflows (DAG rules), core schemas and examples, the Power (schema and byte-identical skills), adapters (drift and allowed fields), links and evaluation assets. Results for this build are in `evaluations/benchmark-reports/2026-11-18-build-validation.md` and `dist/FINAL-AUDIT-REPORT.md`.
2. **The system's behaviour on real tasks.** Measured by running regression cases and golden tasks on a host and scoring with rubrics. **No such run exists for this build.** Until one does, claims about output quality are unverified.

## Gates during a project

Twelve gates (`core/quality-gates/gates.yaml`) with evidence lists, pass and fail conditions by severity, remediation and a named reviewer. Verdicts live in `07-quality/gate-<id>-<date>.md`. Critical findings in security, legal, testing and release cannot be waived by the orchestrator.

## Running the evaluation harness

```bash
python evaluations/run_evals.py --check
python evaluations/run_evals.py --golden A --workspace /path/to/captured/project --report evaluations/benchmark-reports/<date>-<host>-<model>.md --host "Kiro IDE 1.4" --model "<model>"
```

The report skeleton marks every model-dependent score NOT_RUN. Raters (humans, or a model that did not perform the task) replace scores with values and cite evidence paths. Publish only what ran.

## Scoring rules

- 0–3 per dimension with anchors (`evaluations/rubrics/`). A score without evidence is invalid.
- Regression cases pass only with no 0 and at least 2 on expected behaviour and forbidden-avoided.
- Originality uses `evaluations/originality/originality-scorecard.md`; similarity tools are signals, not proof.
- Record cost and time per stage, or NOT_MEASURED.

## When to re-run

After any change to a skill, agent prompt, gate, policy or adapter; after a host or model upgrade. Record the host and model in each report; never aggregate across hosts without saying so.
