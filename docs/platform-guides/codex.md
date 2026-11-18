# Codex guide

Formats verified 2026-11-18 (`research/source-register.md` S16). Live host testing was not performed in this build.

## Install

`python scripts/install/install.py --target codex --destination <project>` writes skills to `.agents/skills/` and `AGENTS.md` (or `CORPORATE-AGENT-OS-AGENTS.md` if one exists). For a personal install use `--scope user` (`~/.agents/skills`).

## Using

- `$corporate-orchestrator` starts the orchestrator. Codex has no sub-agents, so the orchestrator runs roles sequentially and must say so.
- Reviews are separate turns under a reviewer role, ideally in a fresh session, so the reviewer does not share the creator's context.
- `AGENTS.md` contains the role table, hard rules and approval list generated from `agents/**`.

## Context budget

Codex lists skills within roughly 2% of the model's context window and shortens descriptions first. With 50 skills, install a subset for a given project:

```bash
python scripts/install/install.py --target codex --destination <project> --skills corporate-orchestrator,anti-slop-quality-gate,business-idea-validation,research-intelligence,competitive-analysis,business-model-unit-economics
```

or raise `skills.max_context_tokens` in `~/.codex/config.toml` (up to 10,000). Explicit `$skill-name` invocation works regardless of the list.

## Limits

No per-role tool restrictions; rely on Codex sandbox and approval modes. No parallelism. No hooks. `agents/openai.yaml` metadata is not shipped.
