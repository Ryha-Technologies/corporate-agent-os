---
name: devops-sre
description: "Prepare, deploy, monitor and operate applications reliably: environments, CI/CD with pinned dependencies and scanning, least-privilege credentials, observability, SLOs, backup and tested restore, staged rollout, rollback and release checklist, without unapproved production changes. Use for deployment and operations work."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: infrastructure
---
# DevOps and site reliability engineering

## Purpose
Make software deployable, observable and reversible, and make production changes deliberate and approved.

## When to use
- Setting up or changing CI/CD, environments, infrastructure, monitoring or release process.

## Preconditions
- Architecture and cost model; secrets management available; human approval path for production known.

## Inputs
- Architecture, repository, environments, SLO targets, budget, security requirements.

## Procedure
1. **Design operations before launch.** Service boundaries, owners, environments (dev, staging, production at minimum), deployment process, configuration, secrets, access roles, uptime expectations, SLIs/SLOs, alert policy, rollback. Production is never the first test environment.
2. **CI/CD.** Reproducible builds, dependency pinning, code review gate, automated tests, secret scanning, dependency scanning, artefact provenance, environment separation, staged rollout, least-privilege deployment credentials, approval step for production and destructive changes.
3. **Observability.** Logs, metrics and traces with correlation ids and no sensitive data; monitor traffic, latency, errors, saturation, queue depth, database health, third-party failures, cost and business-critical workflows. Every alert has an owner and an action.
4. **Reliability.** Realistic SLOs and error budgets; timeouts, bounded retries with jitter, circuit breakers where useful, idempotency, backpressure, graceful degradation; test failover and restore; document RTO and RPO.
5. **Security and cost.** Patch OS and dependencies; review IAM, network exposure, secrets, backups, admin access; tag resources; budgets and alerts; identify idle assets; measure cost per workload including egress and AI spend.
6. **Incident readiness.** Severity levels, incident commander, communication channel, runbooks (`incident-response`).
7. **Release checklist** (`templates/operations/release-checklist.md`): provenance, tests, migration safety, changelog, config and secrets, monitoring, dashboards, alerts, rollback, backup, support playbook, privacy review, human production approval.

## Outputs
- CI/CD configuration, `09-operations/runbooks/**`, `09-operations/release-checklist.md`, SLO document, dashboards and alert definitions, `06-build/infra-notes.md`.

## Quality criteria
- No production change without recorded approval and rollback.
- Backup restore tested, with date and result.
- Alerts have owners and actions; no sensitive data in logs.
- Deployment credentials least-privileged; secrets outside repositories.

## Failure handling
- Restore test impossible → mark NOT_RUN as a release blocker for high-risk systems.
- Cost exceeds model → report with breakdown; propose changes; no silent scaling.

## Safety boundaries
- Never deploy to production, delete resources, rotate credentials or change access without human approval.
- Never run retries that amplify outages.

## References
- `templates/operations/release-checklist.md`, `templates/operations/runbook.md`
- `standards/engineering/engineering-standard.md`, `skills/incident-response/SKILL.md`
