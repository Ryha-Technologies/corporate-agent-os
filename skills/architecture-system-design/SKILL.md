---
name: architecture-system-design
description: "Design the simplest secure, maintainable and cost-aware architecture that meets stated requirements: quality attributes, option comparison, system boundaries, data flow, trust boundaries, contracts, reliability, cost model and ADRs. Use before implementing anything non-trivial or when complexity is proposed."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: architecture
---
# System architecture and design

## Purpose
Derive architecture from real requirements, choose the simplest viable option, and write down boundaries, failure modes, costs and decisions so engineers, reviewers and operators share one picture.

## When to use
- Before building a new system or a major feature.
- When microservices, queues, Kubernetes, AI components or new platforms are proposed.
- When an existing system needs an architecture audit.

## Preconditions
- PRD with non-functional requirements; data classification; team capability and budget known or assumed explicitly.

## Inputs
- PRD, NFRs, data sensitivity, regulatory boundaries, availability targets, timeline, budget, existing systems.

## Procedure
1. **Derive requirements.** Use cases, quality attributes, scale assumptions (challenge unsupported ones), deployment environment, data sensitivity, regulatory boundaries, availability targets, budget, timeline.
2. **Compare the simplest viable options.** Modular monolith, service-oriented, microservices, serverless, managed platforms, open-source self-hosted. State why the chosen pattern fits. Avoid microservices or Kubernetes by default; prefer mature technology unless a specific advantage justifies novelty.
3. **Key contracts.** System context, component boundaries, request and data flows, API schemas, auth model, error semantics, idempotency, pagination, versioning, rate limits, event contracts, integration ownership (`api-database-design` for detail).
4. **Trust boundaries and failure modes.** Enumerate entry points, trust boundaries, what fails first and how the system degrades; hand to `threat-modeling`.
5. **Data architecture.** Entities, ownership, lifecycle, sensitivity, retention, deletion, backup, migration, audit, residency, access patterns, indexes, transaction boundaries. Minimise personal data; no secrets in data stores.
6. **AI-enabled components.** Task suitability vs deterministic code, provider options, routing, prompt and version governance, structured outputs, tool permissions, retrieval and data rights, guardrails, evaluation sets, fallbacks, budgets, latency SLOs, monitoring. Model output is untrusted input.
7. **Reliability and operability.** Timeouts, retries with jitter, circuit breaking where needed, queue semantics, idempotency, graceful degradation, concurrency limits, backpressure, observability, backup/restore, disaster recovery, rollback.
8. **Cost model.** Fixed and variable costs (hosting, database, cache, egress, storage, observability, third-party APIs, AI tokens, support, backup) with low/base/high usage and cost per active user or workflow.
9. **ADRs** (`templates/engineering/adr.md`) for every consequential choice: context, options, decision, evidence, trade-offs, security and cost effects, reversibility, assumptions, revisit trigger.
10. **Diagrams as text** (context, container/component, data flow) so they live in the repository and stay current.

## Outputs
- `05-architecture/architecture.md`, `05-architecture/adr/ADR-*.md`, `05-architecture/data-model.md`, `05-architecture/cost-model.md`, inputs to `threat-model.md` and `api-contract`.

## Quality criteria
- Every component exists because a stated requirement needs it.
- Trust boundaries, failure modes and degradation behaviour are written.
- Cost model has ranges and a per-unit figure.
- ADRs exist for consequential choices with revisit triggers.
- Diagrams match the text.

## Failure handling
- Scale unknown → design for the stated near-term scale with a documented path; record the assumption with a `review_by`.
- Stakeholder insists on complexity → record the request, the simpler alternative and the risks as an ADR for the human decision.

## Safety boundaries
- No architecture handling personal, payment or regulated data proceeds without a threat model.
- No paid platform commitments without approval.

## References
- `templates/engineering/adr.md`, `templates/engineering/architecture.md`, `templates/engineering/cost-model.md`
- `standards/engineering/architecture.md`
- `skills/threat-modeling/SKILL.md`, `skills/api-database-design/SKILL.md`
