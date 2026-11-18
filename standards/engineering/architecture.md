# Architecture standard

Applies to architecture documents, ADRs, API and data design.

| # | Requirement | Verified by |
|---|---|---|
| A1 | Architecture derives from stated quality attributes and scale assumptions; unsupported scale claims are challenged and recorded as assumptions with review dates. | Architecture document |
| A2 | The simplest viable option is chosen: modular monolith, serverless or managed platform before service decomposition. Microservices, Kubernetes, queues, vector databases, blockchain or AI components require a demonstrated requirement in an ADR. | ADR, reviewer |
| A3 | Prefer mature, well-understood technology unless a specific advantage is evidenced. | ADR |
| A4 | System context, components, boundaries, data flow and trust boundaries are documented as text diagrams kept in the repository. | Architecture document |
| A5 | Contracts define auth, error semantics, idempotency, pagination, versioning and rate limits; error bodies carry correlation ids and no sensitive data. | API contract |
| A6 | Data is classified; retention, deletion, backup, residency and access are specified; personal data minimised. | Data model |
| A7 | Failure modes are enumerated with likelihood, impact, detection and mitigation; degradation behaviour is defined; timeouts, bounded retries with jitter and idempotency are specified. | Architecture document |
| A8 | A threat model exists before implementation for any system handling personal, payment or regulated data. | Threat model |
| A9 | Cost model with low/base/high usage and cost per unit; variable AI and egress costs included. | Cost model |
| A10 | Every consequential decision has an ADR with options, evidence, trade-offs, reversibility and revisit trigger. | ADR log |
| A11 | Operability is designed: owners, environments, SLOs, rollback, backup/restore, DR. | Architecture, DevOps review |
| A12 | Diagrams and documents match the implementation; drift is a documentation defect. | Documentation gate |
