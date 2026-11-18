# API contract

Filled by: software-architect / API engineer. Reviewed by: architecture-reviewer. The normative specification is the OpenAPI (or protocol-equivalent) file; this document records the decisions.

## Consumers and use cases

## Conventions
<Naming, casing, time formats, ids, pagination style, versioning scheme, deprecation policy.>

## Authentication and authorisation
| Operation | Auth required | Authorisation rule (ownership / role / tenant) |
|---|---|---|

## Error model
| HTTP status | Error code | When | Body fields | Client guidance |
|---|---|---|---|---|
<Correlation id in every error; no sensitive data.>

## Idempotency
<Which writes accept idempotency keys; natural idempotency; retry guidance.>

## Rate limits and quotas
<Limits, headers, behaviour when exceeded.>

## Events and webhooks (if any)
<Schema, delivery guarantees, signing, replay.>

## Resources and operations
| Resource | Operation | Request | Response | Errors | Example |
|---|---|---|---|---|---|

## Contract tests
<Where they live; what they cover.>
