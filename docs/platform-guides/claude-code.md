# Claude Code guide

Formats verified 2026-11-18 (`research/source-register.md` S14, S15). Live host testing was not performed in this build.

## Install

`python scripts/install/install.py --target claude --destination <project>` writes skills to `.claude/skills/`, sub-agents to `.claude/agents/`, and `CLAUDE.md` (or `CORPORATE-AGENT-OS-CLAUDE.md` if one exists).

## Using

- `/corporate-orchestrator` starts the orchestrator skill in the main session. It delegates through the Agent tool to the sub-agents in `.claude/agents/`.
- Mention a sub-agent with `@` to invoke it directly, for example `@research-auditor review 01-research/research-brief.md`.
- Ask for `isolation: worktree` when parallel engineering stages run; the generated files do not set it so you keep the choice.

## Models and cost

All sub-agents use `model: inherit`. To route cheap mechanical work to Haiku, set `fast: haiku` in `adapters/claude-code/model-map.yaml` (already the default for `fast`), assign `model_class: fast` to the relevant agents in YAML and rebuild. Sub-agent descriptions are kept at or under 200 characters so the total stays well below the 15,000-token warning.

## Skills in sub-agents

The `skills:` field preloads full skill content into the sub-agent at start. Trim the lists in the YAML source if a sub-agent's context is tight.

## Permissions

Claude Code does not scope writes by path. Reviewers and executives have no Write/Edit tools; specialists are instructed to stay in scope and the `code-reviewer` checks diffs against task contracts. For shell pre-approval use your project `settings.json` permissions; none are shipped.

## Hooks

Not shipped. If you want the same guards as the Kiro hooks, add `PostToolUse` or `Stop` hooks in `.claude/settings.json` that run `python .corporate-agent-os/validators/validate_tasks.py 10-decisions/tasks` and `validate_memory.py`.

## Portability

Skills use only spec frontmatter fields, so they also upload to claude.ai and package with `package_skill.py` from anthropics/skills without changes.
