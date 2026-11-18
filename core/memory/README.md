# Shared project memory

**Component type:** specification + schema + validator (`scripts/validate/validate_memory.py`).

Chat history is not memory. Every project keeps its state in files inside a project workspace, and every consequential statement is a line in a ledger with its type, provenance, confidence and timestamp.

## Project workspace layout

Created by the orchestrator at intake. Each folder is owned by one department; cross-department writes go through task contracts.

| Folder | Owner | Typical contents |
|---|---|---|
| `00-intake/` | orchestrator | `brief.md`, clarified objective, constraints, success definition |
| `01-research/` | research | research plan, evidence ledger, problem statement, competitor map, opportunity assessment |
| `02-product/` | product | thesis, PRD, acceptance criteria, business model, validation plan, roadmap |
| `03-brand/` | branding, naming-ip | category audit, brand strategy, naming report, rejected concepts, brandbook |
| `04-design/` | ux-research, design | flows, IA, tokens, component spec, states matrix, accessibility review, rationale |
| `05-architecture/` | architecture | architecture, ADRs, data model, API contract, threat model, cost model |
| `06-build/` | engineering | implementation notes, build/test logs (code lives in the product repository) |
| `07-quality/` | qa | gate verdicts, test reports, defect log |
| `08-legal-oss/` | legal | component register, asset provenance, issue register |
| `09-operations/` | infrastructure, operations, growth | runbooks, release checklist, launch plan, support docs |
| `10-decisions/` | orchestrator | `memory-ledger.jsonl`, `tasks/*.json`, `approvals.md`, `accepted-risks.md`, `open-questions.md` |

## Ledger rules

1. One JSON object per line in `10-decisions/memory-ledger.jsonl`, conforming to `memory-entry.schema.json`.
2. The `type` is explicit and the id prefix matches it: `F` fact, `H` hypothesis, `A` assumption, `R` recommendation, `D` decision, `K` risk, `L` lesson, `Q` open question, `X` rejected alternative.
3. Only `fact` entries may be cited as facts downstream, and a `fact` needs `provenance.kind` of `user_statement`, `primary_source`, `observation`, `experiment` or `human_decision`. An `agent_inference` can never be a `fact`.
4. Hypotheses and assumptions carry `review_by`. The orchestrator lists overdue ones at every gate; they are tested, downgraded, or withdrawn. They do not age into facts.
5. Entries are never deleted. A correction adds a new entry with `supersedes` and marks the old one `superseded`.
6. Decisions record who decided (`recorded_by: human:<role>` for human decisions) and link the alternatives rejected (`X-` entries) so the reasoning survives.
7. Lessons (`L-`) are written at retrospectives and at any gate failure, in the form "we believed X; evidence showed Y; next time do Z".

## What agents must do

- Read the ledger at task start (filter by `category` and `related`).
- Write new entries in their report under `LEDGER_ENTRIES`; the orchestrator appends them. Specialists do not append directly unless `10-decisions/` is in their write scope (normally only the orchestrator).
- Quote ledger ids in artefacts (`see H-004`) so claims stay traceable.

## Validation

```bash
python scripts/validate/validate_memory.py core/memory/examples/memory-ledger.jsonl
python scripts/validate/validate_memory.py <project>/10-decisions/memory-ledger.jsonl
```

Checks schema, id/type prefix agreement, the fact-provenance rule, unique ids, and that `supersedes` points to an existing entry.
