---
name: api-database-design
description: Design API contracts (resources, auth, error semantics, idempotency, pagination, versioning, rate limits) and database schemas (entities, constraints, indexes justified by queries, migrations, retention, backups) from the architecture and data model. Use before implementing services or persistence.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: engineering
---
# API and database design

## Purpose
Specify the contracts between clients and services and the shape of persisted data precisely enough that implementation, tests and documentation agree.

## When to use
- After architecture; before backend implementation.
- When adding or changing endpoints, entities or migrations.

## Preconditions
- Architecture document and data model; consumer list (web, mobile, partners); data classification.

## Inputs
- Architecture, data model, PRD scenarios, NFRs, consumers.

## Procedure
### API
1. **Resources and operations** from scenarios; naming conventions; consistent casing.
2. **Auth model.** Authentication method, token lifetimes, authorisation per operation (ownership, role, tenant), least privilege for machine clients.
3. **Error semantics.** Status codes, error body schema with stable codes, validation error format, correlation id, no sensitive data in errors.
4. **Idempotency** for writes (keys or natural idempotency); retries safe.
5. **Pagination, filtering, sorting** with limits; **rate limits** and quota headers; **versioning** and deprecation policy.
6. **Events/webhooks** where needed: schema, delivery guarantees, signing, replay.
7. **Specification** in OpenAPI (or the protocol's equivalent) with examples; **contract tests** planned.
### Database
8. **Schema** with explicit constraints (NOT NULL, unique, foreign keys, checks), data types, ownership and tenancy columns.
9. **Indexes** justified by named query patterns; avoid speculative indexes.
10. **Migrations** reversible; safe rollout for large tables (backfills, dual writes where needed); never destructive in production without approval and backup.
11. **Lifecycle.** Retention, deletion propagation, archival, audit columns, PII minimisation and encryption where required.
12. **Operations.** Backup schedule and tested restore, connection limits, pooling, transaction boundaries, integrity tests.

## Outputs
- `05-architecture/api-contract.(yaml|md)`, `05-architecture/data-model.md`, migration plan in `06-build/`.

## Quality criteria
- Every operation has auth rules, error cases and an example.
- Writes are idempotent or documented as not retry-safe.
- Every index names the query it serves.
- Migrations reversible; restore tested or `NOT_RUN` stated.
- Personal data fields classified with retention.

## Failure handling
- Consumers unknown → design for the primary client and mark partner-facing decisions provisional.
- Legacy schema constraints → document the compromise and the migration path as an ADR.

## Safety boundaries
- No production migrations, drops or data deletions without recorded human approval and backup.
- No secrets or tokens stored in plain text.

## References
- `templates/engineering/api-design.md`, `templates/engineering/data-model.md`
- `standards/engineering/engineering-standard.md`, `standards/security/secure-development.md`
