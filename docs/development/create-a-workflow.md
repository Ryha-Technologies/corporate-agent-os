# Create a workflow

1. Copy an existing folder under `workflows/` and rename it; `id` in `workflow.yaml` must equal the folder name.
2. Define stages: `id`, `agent`, `skills`, `objective`, `depends_on`, `outputs`, and optionally `parallel_group`, `condition`, `gate`, `review`, `human_approval`, `timeout_minutes`, `risk`.
3. Rules the validator enforces: acyclic graph; dependencies exist; `review` ≠ `agent` and is reviewer-tier; every `gate` has a `review`; gates with `human_approval: true` in `gates.yaml` require `human_approval: true` on the stage; stages in one `parallel_group` never share outputs; reviewer-tier agents write only under `07-quality/` or `10-decisions/`; executives only under `10-decisions/`.
4. Use workspace paths from `core/memory/README.md` for outputs.
5. Run `python scripts/validate/validate_workflows.py workflows/<id>/workflow.yaml`, then `python scripts/package/render_roles.py` to generate `STAGES.md`.
6. Add the workflow to `workflows/README.md` and `docs/workflows/README.md`; add a golden task under `evaluations/golden-tasks/` if it is a new end-to-end capability.
