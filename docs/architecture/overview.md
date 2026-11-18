# Architecture overview

## Layers

```
┌───────────────────────────────────────────────────────────────────────┐
│ Hosts: Kiro IDE/CLI · Claude Code · Codex · other Agent Skills clients│  execution, tools, permissions
├───────────────────────────────────────────────────────────────────────┤
│ Adapters: kiro/ · claude-code/ · codex/ · portable/  (generated)      │  platform formats
├───────────────────────────────────────────────────────────────────────┤
│ Agents: orchestrator · executives · leads · specialists · reviewers   │  roles, tools, scopes, prompts
├───────────────────────────────────────────────────────────────────────┤
│ Workflows: DAGs of stages → gates → reviewers → human approvals       │  coordination
├───────────────────────────────────────────────────────────────────────┤
│ Skills: 39 portable playbooks + references                             │  how work is done
├───────────────────────────────────────────────────────────────────────┤
│ Core: task contracts · memory ledger · permissions · budgets · gates  │  rules and schemas
├───────────────────────────────────────────────────────────────────────┤
│ Standards · Templates · Departments/Roles · Evaluations               │  quality bar and organisation
└───────────────────────────────────────────────────────────────────────┘
```

## Principles

1. **Canonical sources, generated adapters.** Skills, agents, departments, workflows and policies exist once. Platform files are rendered and drift-checked.
2. **Artefacts are the source of truth.** A project lives in files (`00-intake` … `10-decisions`), not in chat. Restart recovers from files.
3. **Provenance over confidence.** The memory ledger separates facts, hypotheses, assumptions, recommendations and decisions; each carries source and confidence.
4. **Independent review.** A creator never approves its own work. Twelve gates each name a read-only reviewer agent.
5. **Human accountability.** Production, publishing, money, legal, personal data, deletion and access changes pause for a named human.
6. **Simplest architecture that fits.** Applies to products the system designs and to the system itself (Python standard library, YAML, Markdown).
7. **Honest labels.** Specification versus implemented software; PASS versus NOT_RUN; beta versus production.

## Runtime shape

The host runs the orchestrator as the primary agent. The orchestrator reads a workflow, writes task contracts, and delegates each stage to a specialist sub-agent with the contract, inputs, ledger ids and skills. Specialists write only inside their ownership. Reviewers read the artefacts and the gate definition and return a verdict. The orchestrator integrates, appends to the ledger, pauses for approvals and reports. Where a host lacks sub-agents, the same roles run as sequential passes and the report says so.

## Where things live

| Concern | Path |
|---|---|
| How the orchestrator behaves | `core/orchestrator/`, `skills/corporate-orchestrator/` |
| What a task is | `core/task-management/` |
| What a workflow is | `core/workflow-engine/`, `workflows/` |
| What is remembered and how | `core/memory/` |
| What agents may do | `core/permissions/`, `agents/` |
| How much they may spend | `core/budget-management/` |
| What passes | `core/quality-gates/`, `standards/`, `evaluations/rubrics/` |
| How work is done | `skills/` |
| Who exists | `departments/`, `agents/`, `docs/organization/`, `docs/agents/` |
| How it reaches a host | `adapters/`, `powers/`, `scripts/install/` |
| How it is checked | `scripts/validate/`, `tests/`, `evaluations/` |
