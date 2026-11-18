# Scripts

All scripts run with Python 3.10+. Validators and builders need PyYAML; the installer uses only the standard library.

| Folder | Script | Purpose |
|---|---|---|
| `validate/` | `run_all.py` | Run every validator; `--json <path>` writes a machine-readable report |
| | `validate_structure.py` | Required files, no empty dirs, VERSION consistency, JSON/YAML parse, secret and placeholder scan |
| | `validate_skills.py` | Agent Skills spec conformance, ten sections, line limit, references resolve |
| | `validate_agents.py` | Agent fields, tier tool ceilings, read-only reviewers, gate coverage |
| | `validate_departments.py` | Fifteen fields per role, startup-stage guidance, agent references |
| | `validate_workflows.py` | Schema, acyclic DAG, reviewer independence, gate rules, disjoint parallel outputs |
| | `validate_core.py` | Gates, policies, schemas, task and ledger examples |
| | `validate_tasks.py`, `validate_memory.py` | Project-side validators (also installed into projects) |
| | `validate_power.py` | Agent Plugins 1.0.0 manifest, Kiro requirements, byte-identical skills |
| | `validate_adapters.py` | Drift against a fresh render; allowed frontmatter fields; hooks and steering |
| | `validate_links.py` | Relative Markdown links resolve |
| | `validate_evaluations.py` | Dataset, golden tasks, rubrics, scorecard present and consistent |
| `package/` | `build_adapters.py` | Render Kiro and Claude Code agents and Codex AGENTS.md from `agents/**` |
| | `build_power.py` | Build the Kiro Power from canonical skills |
| | `render_roles.py` | Render department docs, agents directory and workflow stage tables |
| | `build_release.py` | Rebuild, validate, zip, verify, checksum |
| `install/` | `install.py` | Install into a project or user scope with plan, dry-run, manifest, backup, uninstall |
| `audit/` | `inventory.py` | File inventory with sizes and SHA-256 for audit reports |
| `maintenance/` | `refresh_schemas.py` | Re-download the Agent Plugins schemas (network) |
| | `check_source_dates.py` | Warn when source-register access dates are older than a threshold |
