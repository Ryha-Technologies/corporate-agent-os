# Kiro guide

Formats verified 2026-11-18 (`research/source-register.md` S5–S13). Live host testing was not performed in this build.

## Live verification (Kiro CLI 3.3.0, 2026-11-18)

Installed with `install.py --target kiro` into a fresh project. Finding: `kiro-cli agent list` showed none of the Markdown agents and `kiro-cli agent validate` parsed `.md` as JSON. A minimal JSON agent in the same folder was listed. The adapter therefore renders Kiro agents as **JSON**; all 58 pass `kiro-cli agent validate`. Markdown agent files may work on newer builds or the IDE, but are not shipped.

## Install options

1. **Workspace install** (`python scripts/install/install.py --target kiro --destination <project>`): skills to `.kiro/skills/`, agents (JSON) to `.kiro/agents/`, steering to `.kiro/steering/`, hooks to `.kiro/hooks/`, project validators to `.corporate-agent-os/validators/`.
2. **Power import**: Powers → Add Custom Power → Import power from a folder → `powers/kiro/corporate-agent-os`. Keyword-activated; skills only.
3. Both: fine, but the skills will appear twice.

## Using the agents

Open the agent picker (IDE) or `kiro-cli chat --agent corporate-orchestrator` (CLI) and describe the project. The orchestrator can spawn only the agents listed as `subagent/<id>` in its tools; each spawn prompts (`effect: ask`). Department leads can spawn only their own department's specialists and reviewers.

## Permissions

Generated agents carry `permissions.rules`: `fs_write` allow matchers from the agent's write scope, shell allow/ask/deny from `core/permissions/policy.yaml`, and `subagent` ask rules. The parent session's `permissions.yaml` also applies; the stricter result wins. Add your own `.kiro/settings/permissions.yaml` rules to pre-approve test commands if the prompts are too frequent.

## Steering and hooks

`corporate-agent-os.md` is `inclusion: always`. The hooks file ships with two disabled `PostFileSave` validators (enable after confirming `python -c "import yaml"` works for Kiro's shell) and an enabled `Stop` reminder that asks the agent to list gate verdicts and NOT_RUN items before finishing.

## MCP

Design QA screenshots need a browser MCP server; see `adapters/kiro/mcp.example.json`. Add the server's tools to the relevant agent's `tools` (for example `@playwright`) in the YAML source and rebuild adapters, or allow it in your session.

## Sub-agent review loops

Kiro supports looping a stage back on a trigger word with `max_iterations` 1–10. The workflows' `retry_policy.max_review_loops` maps to this. The DAG is planned before execution and cannot change mid-run.

## Troubleshooting

Agents not listed → workspace not trusted, or files not under `.kiro/agents/`. Skills not activating → custom agents load skills only through `resources: skill://`; the generated agents include them. Sub-agent prompts for every tool call → add the sub-agent's allow rules to the parent agent or your user `permissions.yaml`.

## Running the orchestrator non-interactively (live-verified with Kiro CLI 3.3.0)
```
kiro-cli chat --agent corporate-orchestrator --no-interactive --trust-tools="fs_read,fs_write,shell,disclose_context,subagent*" "<your request>"
```
- `subagent*` is required: each specialist is a separate tool named `subagent_<agent-id>`; trusting `subagent` alone denies every delegation.
- `disclose_context` is required for the agent to load skills in non-interactive mode.
- Write ownership: Kiro treats `allow` rules as auto-approve only and a `deny` rule wins over any `allow`, so generated agents that do not delegate carry `deny` rules for every stage folder outside their own scope. Sub-agents inherit their parent's deny rules, so delegating agents (orchestrator, leads) carry none; their ownership is checked at each gate by `skills/corporate-orchestrator/scripts/ownership_check.py` (every deliverable has a `Made by: <agent-id>` line and the maker owns the folder). All three behaviours were probed live on 2026-11-18.
