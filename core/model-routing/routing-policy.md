# Model routing and context policy

**Component type:** specification. The host platform selects models; this policy tells the orchestrator which model class to request per task and how to manage context. Where a host offers no model choice, the policy degrades to context management only.

## Model classes

| Class | Use for | Examples of host settings |
|---|---|---|
| `reasoning` | Orchestration, architecture, business-model analysis, independent review verdicts, security findings | Claude Code `model: opus` / `inherit` on the main session; Kiro default model for the orchestrator agent |
| `balanced` | Specialist drafting (research synthesis, PRD, brand strategy, code implementation) | Claude Code `model: sonnet`; Kiro `model:` set per agent in `.kiro/agents/<id>.md` |
| `fast` | Mechanical passes: link checking, format conversion, extracting tables, summarising a single document | Claude Code `model: haiku` sub-agents |

Rules:
1. Reviewers run on `reasoning` or `balanced`, never `fast`. A cheap reviewer is a false sense of safety.
2. A reviewer should run on a different model or at least a different context than the creator when the host allows it. Different model families reduce shared blind spots; this is a mitigation, not a guarantee of independence.
3. Model names are host-specific and change. Agent files use the class names; `scripts/package/build_adapters.py` maps them with the table in `adapters/<host>/model-map.yaml`. Never hard-code a model id in a skill.
4. Do not use a model where deterministic software is cheaper and more reliable (schema validation, link checking, licence lookups, arithmetic in a financial model).

## Context management

- Load skills by description; read the full `SKILL.md` only when the stage needs it. Keep `SKILL.md` bodies under 500 lines and move depth into `references/`.
- Each specialist receives: the task contract, the inputs it names, the relevant ledger entries, and the skill(s). Not the whole project.
- Reports back to the orchestrator follow `core/orchestrator/report-format.md` and are bounded (summary first, evidence second, raw logs by file path).
- Long research outputs are written to files; the ledger holds the claims. The orchestrator never carries raw research in its own context.
- On compaction or restart, the orchestrator re-derives state from `10-decisions/` and gate verdicts.

## Divergence for creative work

For naming, brand directions, visual concepts and positioning, the orchestrator asks for at least three directions produced under different framings (different persona, constraint or reference set) rather than one prompt sampled three times. Where the host allows separate sub-agents, run them in parallel with different briefs. This is the practical substitute for "ensemble sampling"; sampling parameters are not controllable from skills on any supported host.

## Cost awareness

Every task contract carries `budget.max_model_calls` and optionally `max_cost_usd`. The orchestrator records actual calls where the host exposes them (Kiro usage, Claude Code `/cost` or usage output) in `10-decisions/budget-log.md`. Where the host exposes nothing, the log says `NOT_MEASURED`.
