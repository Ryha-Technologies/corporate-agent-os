# README quality audit

Date: 2026-11-18 · Version 0.2.0 · Auditor: the author's build session (Velluraju C's Corporate Agent OS), performing the three reviews the GitHub presentation brief requires. An independent reader has not yet repeated them.

## Changes made

- `README.md` rewritten: banner, one-sentence explanation, tagline, six static badges, quick links, problem/positioning table, capability table by department, Mermaid architecture and lifecycle diagrams, organisation table, compatibility table, quick start with verified commands, worked-run section with real screenshots, repository layout, quality/governance table, evaluation status, roadmap with 1.0 criteria, contributing, community, author.
- Added `docs/README.md` (documentation index), `docs/development/create-an-agent.md`, `create-a-workflow.md`, `create-an-adapter.md`, `docs/governance/release-process.md`, `docs/github/repository-metadata.md`, this audit.
- Added `.github/ISSUE_TEMPLATE/` (bug, feature, skill, agent, adapter, documentation, config), `.github/PULL_REQUEST_TEMPLATE.md`, `.github/DISCUSSION_TEMPLATE/README.md`. The validation workflow already existed.
- Added `docs/assets/banner.svg` + rendered `banner.png` (Signal palette: graphite #15181C, teal #2EE6C5), two screenshots copied from the worked run.
- Shipped the worked run under `examples/worked-runs/field-service-design/` (53 files).
- Author credit (Velluraju C) in LICENSE, Power manifest `author`, every skill's `metadata.author`, CHANGELOG, CONTRIBUTING, docs index, Power README and README footer.

## Information verified

| Claim in README | How verified |
|---|---|
| 39 skills, 58 agents, 22 departments / 110 roles, 9 workflows, 12 gates, 58 templates, 11 standards, 28 regression cases, 63 tests | Counted from the tree and the validators' output on 2026-11-18 |
| 10/10 validators pass | `python scripts/validate/run_all.py` (after this audit page was added; 9/10 before, the missing link was this file) |
| Every relative link and image target in README | Scripted check: 0 broken |
| Quick-start commands and paths | `scripts/validate/run_all.py`, `scripts/install/install.py --dry-run` executed; dry-run shows 113 files to create for `--target kiro` |
| Platform format statements | `research/source-register.md` S1–S16, accessed 2026-11-18 |
| Worked-run screenshots are real renders | Produced by headless Chrome from `examples/worked-runs/field-service-design/04-design/prototype/` |
| Badge values | License MIT, version 0.2.0, status beta, Python 3.10+, Agent Skills format, Agent Plugins 1.0.0 — all static and true |

## Information that could not be verified

- Live loading of skills/agents on Kiro IDE, Kiro CLI, Claude Code or Codex (no host session run yet; the README says "live run pending").
- The clone URL `https://github.com/ryha-technologies/corporate-agent-os.git` is correct only after the repository is created there.
- Linux/macOS behaviour of the installer.

## Broken links fixed
None found in the final README; one in `docs/README.md` (this page) resolved by creating it.

## Commands tested
`python scripts/validate/run_all.py`, `python -m pytest -q` (63 passed), `python -m pytest --collect-only -q`, `python scripts/install/install.py --target kiro --destination <dir> --dry-run`, headless Chrome render of the banner.

## Claims removed or corrected
- Dynamic GitHub badges omitted (repo not published; they would render invalid).
- No benchmark numbers shown; the evaluation section states none exist.
- The worked run is labelled as a single-model worked run with a FAIL gate verdict, not a benchmark or an approved brand.
- "Kaamline" labelled as an unscreened working title wherever it appears.
- Company/product homepage links removed from the Power manifest at the author's request; attribution is to the author, with the Ryha-Technologies organisation named only as the host.

## Review A — new developer
Understandable in the first screen (banner, one sentence, tagline, links); install in three commands with a dry-run first; a concrete first request and the expected files on disk; next guide linked. Gap: no video or GIF of a live session (none exists yet).

## Review B — senior engineer
Architecture diagram matches `core/` and `agents/` tiers; compatibility rows match the matrix and say what is not live-tested; commands and paths verified; dependencies stated (Python 3.10+, PyYAML dev-time; host supplies the model and keys); limitations linked. Gap: Mermaid rendering depends on GitHub's renderer and was not previewed on GitHub itself.

## Review C — open-source maintainer
Contribution paths, templates, security reporting, licence and author are explicit; blank issues disabled; PR template demands pasted validator output. Gap: Discussions, branch protection and private vulnerability reporting must be enabled in repository settings after publishing (listed in `repository-metadata.md`).

## Remaining limitations
Live host verification, benchmark runs, CI execution and an independent repetition of this audit.
