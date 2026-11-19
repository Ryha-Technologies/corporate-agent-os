# Concepts

Short definitions, how they relate, and where each lives. Terms are used consistently across the repository.

| Term | Definition | Example | Lives in |
|---|---|---|---|
| **Skill** | A portable, self-contained procedure a model loads on demand: `SKILL.md` with frontmatter (name, description) and a ten-section body, plus optional `references/`, `scripts/`, `assets/`. Follows the Agent Skills specification so any compliant host can use it. | `skills/naming-ip-screen/` | `skills/` |
| **Agent** | A role definition executed by the host: tier, department, mission, skills to load, tools, write scope, autonomy, approvals, refusals and a system prompt. Rendered per platform. | `naming-specialist` | `agents/` → `adapters/*/agents/` (Kiro JSON, Claude Code Markdown) |
| **Orchestrator** | The one agent accountable for a project: intake, planning, delegation, integration, gates, approvals, reporting. Never does specialist work when a specialist exists; never approves work itself. | `corporate-orchestrator` | `agents/orchestrator/`, `core/orchestrator/` |
| **Reviewer** | A read-only agent that judges a gate independently of the creator and returns PASS / PASS_WITH_ACCEPTED_RISK / FAIL / NOT_ASSESSED with evidence. | `brand-originality-auditor` | `agents/reviewers/` |
| **Department / role** | Organisational function and the human roles within it, each with fifteen defined fields. Agents operate within departments; roles describe the human job the agent supports. | `naming-ip` department, `trademark-screening-researcher` role | `departments/`, `docs/organization/` |
| **Workflow** | A DAG of stages, each naming an agent, skills, inputs, outputs, dependencies, parallel group, gate, reviewer and approval flag. Validated for cycles and ownership conflicts. | `brand-development` | `workflows/`, `core/workflow-engine/` |
| **Task contract** | The unit of delegation: objective, inputs, outputs, file ownership, budget, acceptance criteria, verification, risk, approvals, status. JSON validated against a schema. | `10-decisions/tasks/T-003.json` | `core/task-management/` |
| **Quality gate** | A checkpoint with required evidence, pass and fail conditions by severity, remediation, a named reviewer and whether a human must approve. | `brand` gate | `core/quality-gates/gates.yaml` |
| **Memory ledger** | Append-only JSON Lines of typed statements (fact, hypothesis, assumption, recommendation, decision, risk, lesson, question, rejected alternative) with provenance and confidence. | `10-decisions/memory-ledger.jsonl` | `core/memory/` |
| **Power** | Kiro's installable package following Agent Plugins 1.0.0: `plugin.json` + `skills/` (+ optional `mcp.json`). Here, a generated bundle of the 52 skills. | `powers/kiro/corporate-agent-os/` | `powers/` |
| **Steering** | Kiro-specific always-on or conditional context files (`.kiro/steering/*.md`). Here, one file that tells every Kiro session how this operating model works. | `corporate-agent-os.md` | `adapters/kiro/steering/` |
| **Hook** | Kiro-specific automation triggered by events (file save, tool use, stop) running a command or injecting a prompt. Here, two optional validators and one Stop reminder. | `corporate-agent-os-guards.json` | `adapters/kiro/hooks/` |
| **Adapter** | The platform-specific rendering of canonical agents and policies plus hand-written host instructions and install mapping. | Claude Code sub-agent files | `adapters/` |
| **Standard** | The quality bar for a domain, with numbered requirements and how each is verified. | `standards/design/design-standard.md` | `standards/` |
| **Template** | A fill-in document with field guidance and acceptance criteria for an artefact a workflow produces. | `templates/branding/naming-clearance.md` | `templates/` |
| **Rubric** | A 0–3 scoring guide with anchors and evidence requirements used by raters and reviewers. | `evaluations/rubrics/brand-rubric.md` | `evaluations/rubrics/` |
| **Golden task** | A benchmark input with expected evidence and forbidden behaviours used to evaluate the whole system on a host. | Benchmark A | `evaluations/golden-tasks/` |

## How they fit together

A **workflow** stage names an **agent**, which loads **skills** and writes artefacts using **templates** to the **standards**; the orchestrator wraps each stage in a **task contract**; a **reviewer** judges the **quality gate**; statements and decisions go into the **memory ledger**; **adapters** make the agents and skills loadable by a host, and on Kiro the skills also ship as a **Power** with **steering** and **hooks**.
