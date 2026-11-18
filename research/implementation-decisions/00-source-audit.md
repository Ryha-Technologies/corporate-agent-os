# Source audit — Corporate Agent OS v0.1.0 inputs

Audit date: 2026-11-18. Method: full file listing with sizes and MD5 hashes, reading of every Markdown, JSON and Python file in both source trees, and the complete research report.

## 1. Inventory

| Input | Path (workspace-relative) | Files | Notes |
|---|---|---|---|
| Corporate Agent OS repository v0.1.0 | `corporate-agent-os/` | 94 | Extracted tree. The original `.zip` was not present in the workspace; only the extracted folder was available. |
| Corporate Agent OS Kiro Power v0.1.0 | `corporate-agent-os-kiro-power-v0.1.0/` | 27 | `plugin.json`, `README.md`, 25 × `skills/<name>/SKILL.md` |
| Deep research report | `research.txt` | 1 | 22,151 bytes, narrative report |

Total: 122 files. No `.zip` archives were found, so archive integrity checks could not be run; the extracted trees were audited in place and left unmodified.

### 1.1 Repository v0.1.0 contents

- Root: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `LICENSE` (MIT), `SECURITY.md`, `.gitignore`
- `skills/` — 25 skills, each a single `SKILL.md` (1.5–8.4 KB). No `references/`, `scripts/` or `assets/` anywhere.
- `adapters/claude/` — `CLAUDE.md` + 6 sub-agent profiles (`name`, `description` frontmatter only)
- `adapters/kiro/` — `plugin.json`, `steering/corporate-agent-os.md`, 6 agent profiles in IDE 1.x Markdown format (`tools`, `resources: skill://`, `welcomeMessage`)
- `powers/corporate-agent-os/` — `plugin.json`, `README.md`, 25 skills
- `docs/` — 7 documents (architecture, anti-slop standard, departments/failure modes, quality gates, research protocol, sources, workflow contract)
- `templates/` — 10 heading-only skeletons (224–743 bytes)
- `evals/cases.json` — 15 behavioural regression cases, no runner
- `scripts/` — `install.py`, `validate_repo.py`, `build_kiro_power.py`

### 1.2 Duplication

All 25 `SKILL.md` files exist three times with identical MD5 hashes: `corporate-agent-os/skills/`, `corporate-agent-os/powers/corporate-agent-os/skills/` and the Kiro Power tree. `plugin.json` is identical in `adapters/kiro/` and both power locations. `README.md` of the power is identical in both power locations.

Decision: `skills/` is the only canonical copy. The Power becomes a reproducible build output (`scripts/package/build_power.py`), verified byte-for-byte by the validator, never hand-edited.

## 2. Quality assessment

### 2.1 What is good and was preserved
- The procedural content of the 25 skills is specific, evidence-oriented and already contains the right guardrails (no fabricated quotes, `NOT_RUN` states, trademark statuses, licence due diligence). It was kept and restructured rather than rewritten.
- The orchestrator skill's gate sequence (Intake → Discovery → Product → Brand → Experience/Architecture → Build → Verification → Release → Learn) is sound and became the backbone of `workflows/idea-to-business`.
- Kiro agent profiles already use the current Markdown agent format.
- The 15 eval cases are good behavioural tests and were carried into `evaluations/datasets/regression-cases.json`.
- MIT licence, security policy and contribution rules are reasonable.

### 2.2 Defects found

| # | Defect | Where | Severity | Resolution |
|---|---|---|---|---|
| D1 | Skills have no `license`/`metadata` frontmatter, no Inputs/Outputs/Preconditions/Failure/Safety sections | all skills | medium | Ten-section structure applied to every skill |
| D2 | No `references/`; long reference material (trademark offices, standards) sits inline or is missing | all skills | medium | `references/` added where material is heavy |
| D3 | Validator only checks a regex on frontmatter and total length; does not parse YAML, check links, agents, power layout or JSON schemas | `scripts/validate_repo.py` | high | New `scripts/validate/` package |
| D4 | Installer: no dry-run, no manifest, no backup, no uninstall; `copytree(dirs_exist_ok=True)` silently overwrites same-named skills; writes a `dist/` folder into the *target* project | `scripts/install.py` | high | New installer with plan, manifest, backup, uninstall |
| D5 | `plugin.json` keywords include broad words (`company`, `ui`, `qa`, `security`, `engineering`) that will activate the Power on unrelated tasks | manifest | medium | Keywords narrowed |
| D6 | Kiro orchestrator agent grants `subagent` with no `permissions` block and no restriction on which agents it may spawn | `adapters/kiro/agents/orchestrator.md` | medium | Orchestrator lists `subagent/<name>` entries plus `permissions.rules` |
| D7 | Claude sub-agent profiles omit `tools`, so every sub-agent inherits all tools including write access for reviewers | `adapters/claude/agents/*.md` | medium | Reviewers get read-only tools |
| D8 | Only six agents; no executive, department-lead or distinct reviewer roles; single auditor reviews everything | adapters | high | Agent model with tiers and eleven reviewers |
| D9 | No department/role model beyond a one-table doc | `docs/departments-and-ai-failure-modes.md` | high | `departments/*/roles.yaml` |
| D10 | Templates are empty heading lists | `templates/` | medium | Rewritten with field guidance |
| D11 | No workflow definitions as data; the DAG rules exist only as prose | docs | high | `workflows/*/workflow.yaml` + validator |
| D12 | No task contract or memory schema | — | high | `core/` schemas and validators |
| D13 | No tests | — | high | `tests/` with pytest |
| D14 | Codex docs URL in `docs/sources-and-compatibility.md` points to a page that redirects elsewhere; no access-date discipline for other sources | docs | low | `research/source-register.md` |
| D15 | README claims "Codex-compatible skills installation" works; Codex has no sub-agent config so the orchestrator's delegation protocol cannot run there | README | low | Compatibility matrix states the limitation |
| D16 | `.gitignore` ignores `dist/` but the installer writes to `dist/` of another project | scripts | low | Installer no longer does this |

### 2.3 Security review of inputs
- No secrets, credentials or personal data found in any file.
- `install.py` executes no downloaded code; it copies local files. It can overwrite a target project's `.kiro/skills/<same-name>/` without warning (D4).
- No scripts in skills; nothing executable is shipped inside the Power.
- `SECURITY.md` is adequate but has no reporting channel configured.

## 3. Gap analysis against the brief

| Brief area | v0.1.0 state | Gap | Addressed in |
|---|---|---|---|
| Organization model (§4) | 1 table | roles, 15 fields, startup stages | `departments/`, `docs/organization/` |
| Agent hierarchy (§5.1) | 6 agents | executives, leads, specialists, 11 reviewers | `agents/` |
| Task contracts (§5.2) | prose fields | schema + validator | `core/task-management/` |
| Workflow coordination (§5.3) | prose | DAG files + validator | `workflows/`, `core/workflow-engine/` |
| Shared memory (§5.4) | folder names only | schema with provenance/claim type | `core/memory/` |
| Resource governance (§5.5) | none | policies | `core/permissions`, `model-routing`, `budget-management` |
| Idea validation engine (§6) | inside strategy skill | dedicated skill + workflow + templates | `skills/business-idea-validation`, `workflows/business-validation` |
| Anti-slop engine (§7) | one skill + doc | scorecard, audit skill, rejected-concept record, pattern map | `skills/originality-audit`, `evaluations/originality/` |
| Brand (§8) | 4 skills | naming jurisdictions reference, brandbook template | kept + references |
| UI/UX (§9) | 2 skills | IA, design system, accessibility audit, design QA reviewer | new skills + reviewer |
| Engineering (§10) | 3 skills | API/database design, code review, test strategy | new skills |
| Security (§11) | 1 skill | threat modelling, standards mapping, incident response | new skills + `research/standards-mapping/` |
| Legal (§12) | 2 skills | privacy/licensing references, asset provenance template | references + templates |
| Adapters (§13) | Kiro, Claude, Codex (thin) | generated agents, hooks, steering, compatibility matrix | `adapters/`, `docs/platform-compatibility-matrix.md` |
| Repo QA (§15) | 1 validator | full validator set + tests + installer tests | `scripts/validate/`, `tests/` |
| Benchmarks (§16) | 15 regression prompts | 5 golden tasks, rubrics, runner | `evaluations/` |
| Docs (§17) | 7 docs | 20-item documentation set | `docs/` |

## 4. Risk report

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Platform formats change (Kiro, Claude Code, Codex all moved in 2026) | high | medium | Source register with access dates; validators encode only verified fields; CHANGELOG notes re-verification cadence |
| Instruction-only components are mistaken for executable software | medium | high | Every README labels components "specification/playbook" vs "implemented and tested" |
| Benchmark results are expected but cannot be produced without model runs | certain | medium | Harness ships; reports record NOT_RUN; version stays 0.2.0 beta |
| Over-broad Power keywords cause unwanted activation | medium | low | Narrowed keyword list |
| Installer touches user configuration | medium | high | Project scope default, manifest, backup, dry-run, uninstall |

## 5. Consolidation strategy (applied)

1. Canonical layers: `skills/`, `agents/`, `departments/`, `workflows/`, `core/`, `standards/`, `templates/`.
2. Generated layers: `powers/kiro/corporate-agent-os/` and `adapters/*/agents/` are produced by scripts and validated for drift.
3. Where v0.1.0 and the Power differed (they did not), the repository copy would win. No conflicts existed.
4. The old `evals/cases.json` was moved to `evaluations/datasets/regression-cases.json` with the same case IDs so history is traceable.
5. Old docs were merged into the new documentation set; superseded files are not carried over.
6. Version moves from 0.1.0 to 0.2.0 (beta). The research report's "v1.0.0" label is not adopted because its claimed artefacts and test runs do not exist (see `research/research-findings/research-report-assessment.md`).
