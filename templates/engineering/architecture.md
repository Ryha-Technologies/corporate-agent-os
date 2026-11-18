# Architecture

Filled by: software-architect. Reviewed by: architecture-reviewer (architecture gate).

## Requirements driving the architecture
| Quality attribute | Requirement | Source (PRD section / ledger id) | Confidence |
|---|---|---|---|
| Scale (users, data, throughput) | | | |
| Availability | | | |
| Latency | | | |
| Data sensitivity and residency | | | |
| Regulatory boundaries | | | |
| Team capability and timeline | | | |
| Budget | | | |

## Options compared
<Modular monolith / serverless / managed platform / service-oriented / microservices / reuse; why the chosen one is the simplest that fits.>

## System context
<Text diagram: users, external systems, the system boundary.>

## Components and boundaries
<Text diagram and table: component, responsibility, owner, interfaces, data owned.>

## Data flow and trust boundaries
<Where data crosses trust boundaries (internet, tenant, admin, third party, model); controls at each crossing.>

## Contracts
<Links to API contract and data model; auth model; error semantics; idempotency; versioning.>

## Reliability and operability
<Timeouts, retries with jitter, circuit breaking, queues, degradation, backpressure, observability, backup/restore, DR, rollback; RTO/RPO.>

## AI components (if any)
<Task suitability vs deterministic code; routing; structured outputs; tool permissions; evaluation; fallback; budgets.>

## Failure modes
| Failure | Likelihood | Impact | Detection | Mitigation |
|---|---|---|---|---|

## Cost model summary
<Link to cost-model.md; cost per active user or workflow at low/base/high.>

## Decisions
<ADR list.>

## Risks and open questions
<K-, Q- ids.>
