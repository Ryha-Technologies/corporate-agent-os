# Create an agent

1. Pick the tier (`orchestrator`, `executive`, `department-lead`, `specialist`, `reviewer`) and the department (`departments/<id>`). Tools may not exceed the tier ceiling in `core/permissions/policy.yaml`; reviewers and executives never write.
2. Add an entry to the matching YAML under `agents/<tier-folder>/` with every field in `agents/README.md`: `id`, `tier`, `department`, `title`, `description` (≤ 200 chars, says when to delegate), `mission`, `skills`, `tools`, `write_scope`, `autonomy`, `approval_required`, `never`, `model_class`, `prompt`; reviewers add `reviews` with gate ids.
3. Add the agent to its department's `agents:` list in `departments/<id>/roles.yaml`.
4. If it reviews a gate, set the gate's `reviewer` in `core/quality-gates/gates.yaml` or add the gate to the agent's `reviews`.
5. Regenerate: `python scripts/package/build_adapters.py` and `python scripts/package/render_roles.py`.
6. Validate and test: `python scripts/validate/run_all.py` and `python -m pytest -q`.
7. Reference it from workflow stages where it belongs; add a regression case if it exists to prevent a failure mode.

What the validator rejects: unknown skills or department, tools above the ceiling, writing reviewers or executives, delegating specialists, descriptions over 200 characters, prompts under 120 characters, a gate with no reviewer.
