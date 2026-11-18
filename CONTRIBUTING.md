# Contributing

Corporate Agent OS is created and maintained by Velluraju C. Contributions are welcome under the MIT licence; by contributing you agree your changes are licensed the same way.

## Principles

1. Canonical first. Change `skills/`, `agents/`, `departments/`, `workflows/`, `core/`, `standards/`, `templates/`; never edit generated files (`adapters/*/agents/`, `adapters/codex/AGENTS.md`, `powers/`, `docs/organization/`, `workflows/*/STAGES.md`). Rebuild with `python scripts/package/build_adapters.py`, `build_power.py`, `render_roles.py`.
2. Evidence over confidence. Platform claims cite `research/source-register.md` with an access date. Research claims cite sources. Nothing says "tested" unless a test ran.
3. One skill, one coherent workflow. Keep `SKILL.md` under 500 lines; move depth into `references/`.
4. Every skill has the ten sections and only the six specification frontmatter fields.
5. Every agent declares tier, department, skills, tools within its tier ceiling, write scope, autonomy, approvals and refusals. Reviewers are read-only.
6. Every workflow stage with a gate names an independent reviewer that is not the producing agent.
7. Add a regression case for any new failure mode you address. Add or update a rubric when you add a quality dimension.
8. Label component type in documentation: specification/playbook versus implemented and tested software.

## Workflow

```bash
python scripts/validate/run_all.py
python -m pytest -q
python scripts/package/build_release.py --out dist   # before a release
```

All validators and tests must pass. Warnings are reviewed, not ignored.

## Changes that need a second reviewer

Orchestrator policy, permission policy, agent tools or write scopes, gate definitions, installer behaviour, and anything that touches destructive actions or approvals.

## Third-party material

Do not add text, images, fonts, code or data without recording source and licence. Standards are cited, not copied. Search-result content is paraphrased and attributed.

## Versioning

Semantic versioning. `VERSION`, `CHANGELOG.md` and the Power manifest must agree; the structure validator checks this.
