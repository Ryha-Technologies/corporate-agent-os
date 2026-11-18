---
name: incident-response
description: "Run security and reliability incident response: severity classification, incident command, containment within approved runbooks, evidence preservation, factual stakeholder communication drafts, recovery verification, notification-obligation flags and blameless postmortems with root causes and actions. Use when an incident is suspected or declared, and to prepare runbooks beforehand."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: cybersecurity
---
# Incident response

## Purpose
Limit harm, recover verifiably, communicate truthfully and learn, without destructive actions or external communication that humans have not approved.

## When to use
- Preparing runbooks and severity definitions before launch.
- When alerts, reports or anomalies suggest an incident.

## Preconditions
- Runbooks, contact list, severity definitions and communication templates exist (or this skill creates them during preparation).

## Inputs
- Alerts, reports, logs (without sensitive data in the incident channel), system inventory, legal notification requirements per jurisdiction (from legal).

## Procedure
### Preparation
1. Define severity levels with examples and response targets; name incident commander rotation; set the communication channel and the status page process; write runbooks for likely failures (dependency outage, data store failure, credential leak, DDoS, bad deploy); list notification obligations as questions for legal.
### Response
2. **Declare and classify.** Severity, commander, scribe, channel, start time.
3. **Timeline.** Record every action with time and actor; preserve evidence (logs, snapshots) before changing state.
4. **Contain** using approved runbook steps (rollback, disable feature, rotate exposed credentials with approval, block traffic). Destructive or customer-impacting containment needs human approval.
5. **Communicate** factually: what is known, impact, next update time. Draft customer, partner and regulator communications for human approval; never speculate on cause publicly.
6. **Recover and verify.** Restore service; verify with monitoring and tests; confirm data integrity.
7. **Close** when verified; record end time.
### Learning
8. **Blameless postmortem** within an agreed period: timeline, impact, root causes and contributing factors (not the last error), what went well, action items with owners and dates, detection and response gaps; `L-` ledger entries.

## Outputs
- `09-operations/runbooks/incident-*.md`, `09-operations/incidents/<id>-timeline.md`, `09-operations/incidents/<id>-postmortem.md`, communication drafts.

## Quality criteria
- Timeline complete with times and actors.
- Containment actions were within runbook or approved.
- Communications factual and approved; notification obligations assessed with legal.
- Postmortem has root causes and dated actions.

## Failure handling
- Cause unknown → say so in communications; focus on impact and mitigation.
- Conflicting priorities (availability vs evidence) → commander decides and records the trade-off.

## Safety boundaries
- No deletion, credential rotation, access change or external communication without approval.
- Personal data in logs is redacted before sharing.

## References
- `templates/operations/incident-postmortem.md`, `templates/operations/runbook.md`
- `skills/devops-sre/SKILL.md`, `skills/legal-risk-governance/SKILL.md`
