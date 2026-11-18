# Workflows

**Component type:** specification (DAG data) + executable validator. Executed by the host's agent runtime under the orchestrator; see `core/workflow-engine/README.md` for semantics.

| Workflow | Trigger | Final deliverables |
|---|---|---|
| `idea-to-business` | "I want to build X" with little detail | Opportunity assessment, strategy, PRD, brand foundation, design direction, architecture, build plan, launch plan |
| `business-validation` | An idea needs a go / test / pivot / stop decision | Problem statements, opportunity assessment, business model, validation plan with kill criteria |
| `brand-development` | A product or company needs a brand | Category audit, brand strategy, naming report, identity concepts, brandbook |
| `product-discovery` | Evidence exists; the product needs definition | Research synthesis, thesis, PRD, acceptance criteria, roadmap |
| `product-design` | PRD exists; the experience needs design | Flows, IA, tokens, components, screens with all states, accessibility review, design QA |
| `software-development` | Design and PRD exist; build it | Architecture, ADRs, API/data design, implementation slices, tests, code review, build gate |
| `security-review` | A system needs a security and privacy review | Threat model, security review, privacy analysis, findings and retests, security gate |
| `product-launch` | Product is verified and ready to go to market | Launch plan, assets, enablement, support readiness, monitoring, post-launch review |
| `product-maintenance` | An existing product needs audit and improvement | Product, UX, technical and security audits, prioritised roadmap |

Each folder has `workflow.yaml` (the DAG) and a `README.md` describing stage intent and typical duration drivers.

Validate all: `python scripts/validate/validate_workflows.py`.

## Composition

`idea-to-business` is the end-to-end spine; it references the others by stage objective. In practice the orchestrator runs `idea-to-business` through the opportunity gate, then branches into `brand-development`, `product-discovery` and `product-design`, then `software-development` and `security-review`, then `product-launch`. Running the smaller workflows alone is the normal case for existing companies.

## Project workspace convention

Stage outputs use the `00-intake … 10-decisions` folders defined in `core/memory/README.md`. Parallel stages never share output paths; the validator enforces this.
