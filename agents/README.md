# Agents

**Component type:** specification (canonical YAML) → generated adapters. Agents are role definitions a host runtime executes as sub-agents or as the primary session agent. They do nothing on their own.

## Layout

| Folder | Tier | Autonomy default | Count |
|---|---|---|---|
| `orchestrator/` | orchestrator | execute | 1 |
| `executive/` | executive | advise | 8 |
| `department-leads/` | department-lead | propose, may delegate | 10 |
| `specialists/` | specialist | propose | 28 |
| `reviewers/` | reviewer | advise, read-only | 11 |

A YAML file holds one or more agents of the same tier (`agents:` list). Each agent has exactly one canonical definition; `scripts/package/build_adapters.py` renders it to `adapters/kiro/agents/<id>.md` and `adapters/claude-code/agents/<id>.md`, and lists it in `adapters/codex/AGENTS.md`.

## Agent fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | `[a-z0-9-]+`, unique across all tiers |
| `tier` | yes | orchestrator / executive / department-lead / specialist / reviewer |
| `department` | yes | id from `departments/` |
| `title` | yes | Human role title |
| `description` | yes | One sentence the host uses to decide when to delegate (≤ 200 chars) |
| `mission` | yes | What the agent is accountable for |
| `skills` | yes | Skill ids under `skills/` the agent loads |
| `tools` | yes | Subset of the abstract tools in `core/permissions/policy.yaml`, never wider than the tier default |
| `write_scope` | yes | Globs inside the project workspace (empty for reviewers and executives) |
| `autonomy` | yes | execute / propose / advise |
| `approval_required` | yes | Decisions that need a lead, executive or human |
| `never` | yes | Hard refusals specific to the role |
| `reviews` | reviewers only | Gate ids from `core/quality-gates/gates.yaml` |
| `model_class` | yes | reasoning / balanced / fast (see `core/model-routing`) |
| `prompt` | yes | Platform-neutral system prompt body |

## Rules enforced by `scripts/validate/validate_agents.py`

- ids unique; skills exist; department exists; tools within tier defaults; reviewers have no `write`; executives have no `write`/`shell`; reviewer `reviews` gate ids exist; every gate has at least one reviewer; `description` ≤ 200 characters.
- Generated adapter files must match a fresh render (drift check).
