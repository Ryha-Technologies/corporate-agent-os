# Changelog

All notable changes to Corporate Agent OS (created and maintained by Velluraju C). Format follows Keep a Changelog; versions follow Semantic Versioning.

## [0.2.0] — 2026-11-18

Beta. Evaluation required. Not labelled 1.0.0 because no model-driven benchmark run exists for this build and platform formats are still moving.

### Added
- Organisation model: 22 departments and 110 roles with fifteen fields each (`departments/`), rendered to `docs/organization/`.
- Agent model: 58 canonical agents in five tiers including 11 independent reviewers (`agents/`), rendered to Kiro, Claude Code and Codex adapters by `scripts/package/build_adapters.py`.
- Core specifications with schemas and validators: task contracts, workflow DAGs, memory ledger, permission policy, model routing, budget policy, twelve quality gates.
- Nine workflow DAGs with an acyclicity, ownership, reviewer-independence and gate validator.
- Fourteen new skills: business-idea-validation, competitive-analysis, business-model-unit-economics, information-architecture, design-system, accessibility-audit, threat-modeling, test-strategy, code-review, api-database-design, product-launch, originality-audit, technical-documentation, incident-response.
- `references/` material for market sizing, source evaluation, trademark offices, product-category design patterns, a measurable visual design checklist, an anti-template review procedure (comparison table, swap test, job test) and a reproducible originality comparison method.
- `skills/design-system/assets/design-tokens.example.json` (schema-validated starter) and `scripts/contrast_check.py` (computes WCAG contrast per role and flags failures); `templates/design/visual-direction.md`.
- Eleven standards, 58 templates, seven rubrics, five golden benchmark tasks, originality scorecard, slop catalogue, evaluation harness.
- Installer with plan preview, `--dry-run`, manifest, backups, `--uninstall`, project/user scope and skill subsets.
- Repository validators (structure, skills, agents, departments, workflows, core, power, adapters, links, evaluations) and a pytest suite.
- Release builder producing `dist/corporate-agent-os-final.zip`, `dist/corporate-agent-os-kiro-power.zip`, SHA-256 sums and a verified manifest.
- Platform compatibility matrix, installation guide, platform guides, governance guides, troubleshooting, FAQ, known limitations.
- Source register with access dates; audit of the v0.1.0 inputs; assessment of the research report.

### Changed
- All 25 v0.1.0 skills restructured into ten sections (Purpose, When to use, Preconditions, Inputs, Procedure, Outputs, Quality criteria, Failure handling, Safety boundaries, References) with `license` and `metadata` frontmatter. Procedural content preserved.
- Kiro Power moved to `powers/kiro/corporate-agent-os/` as a build output; keywords narrowed to reduce false activation.
- Kiro agents gain `permissions.rules` and explicit `subagent/<id>` allow-lists; Claude Code sub-agents gain tool lists, preloaded skills and `model: inherit`; reviewers are read-only on both.
- Regression cases E01–E15 carried over with the same ids; eleven new cases added.

### Removed
- Duplicate skill copies under `powers/corporate-agent-os/` and the separate Power archive tree (the Power is now generated).
- The v0.1.0 `scripts/validate_repo.py`, `scripts/install.py` and `scripts/build_kiro_power.py`, replaced by `scripts/validate/`, `scripts/install/` and `scripts/package/`.
- `docs/sources-and-compatibility.md`, superseded by `research/source-register.md` and `docs/platform-compatibility-matrix.md`.

### Added (GitHub presentation)
- README rewritten with banner, Mermaid architecture and lifecycle diagrams, compatibility and quality tables, worked-run screenshots, roadmap and 1.0 criteria; `docs/README.md` index; development guides; release process; issue and PR templates; repository metadata and README quality audit under `docs/github/`.
- Worked design and brand run shipped as `examples/worked-runs/field-service-design/`.
- Author credit: Velluraju C in the licence, Power manifest, every skill and the docs.

### Changed (after first publish)
- Kiro agents are rendered as JSON instead of Markdown: Kiro CLI 3.3.0 did not discover Markdown agent files in a live install; all 58 JSON agents pass `kiro-cli agent validate` and are listed by `kiro-cli agent list`.
- CI (`validate` workflow) runs on ubuntu, windows and macos for Python 3.10 and 3.12 and passes; a Python 3.10 nested f-string bug found by CI was fixed.

### Known gaps
See `docs/known-limitations.md`.

## [0.1.0] — 2026-11-17

Initial foundation: 25 skills, six agent profiles for Kiro and Claude Code, Codex `AGENTS.md`, ten template skeletons, fifteen regression prompts, a frontmatter validator, a copy-based installer and a Kiro Power copy of the skills.
