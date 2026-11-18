# Build validation report — 2026-11-18 — repository checks only

This report records what was executed while building release 0.2.0. It contains **no benchmark scores**: no regression case or golden task was run against a model on any host. Every behavioural dimension is NOT_RUN.

## Environment

- Windows 11, Python 3.12.10, PyYAML 6.0.3, pytest 8.3.3
- Repository: `build/corporate-agent-os` at version 0.2.0

## Executed

| Check | Command | Result |
|---|---|---|
| Structure | `python scripts/validate/validate_structure.py` | PASS |
| Skills (39) | `python scripts/validate/validate_skills.py` | PASS |
| Agents (58) | `python scripts/validate/validate_agents.py` | PASS |
| Departments (22 / 110 roles) | `python scripts/validate/validate_departments.py` | PASS |
| Workflows (9) | `python scripts/validate/validate_workflows.py` | PASS (warnings: high-risk stages reviewed downstream) |
| Core schemas, gates, policies, examples | `python scripts/validate/validate_core.py` | PASS |
| Kiro Power (Agent Plugins 1.0.0) | `python scripts/validate/validate_power.py` | PASS |
| Adapters (drift, fields, hooks, steering) | `python scripts/validate/validate_adapters.py` | PASS |
| Links | `python scripts/validate/validate_links.py` | PASS |
| Evaluation assets | `python scripts/validate/validate_evaluations.py` | PASS |
| Test suite | `python -m pytest -q` | 62 passed |
| Evaluation harness self-check | `python evaluations/run_evals.py --check` | PASS |

## Not executed

| Item | Status | Reason |
|---|---|---|
| Regression cases E01–E26 on any host | NOT_RUN | Requires a model session per host and human raters |
| Golden tasks A–E | NOT_RUN | Same |
| Live install verification on Kiro IDE / CLI, Claude Code, Codex | NOT_RUN | No agent session was started on a host in this build; formats verified against documentation only |
| Installer on Linux / macOS | NOT_RUN | Build machine is Windows |
| CI workflow (`.github/workflows/validate.yml`) | NOT_RUN | Not pushed to a CI service |

## Cost and time

Model usage for authoring this repository is not part of the evaluation and was not metered. NOT_MEASURED.
