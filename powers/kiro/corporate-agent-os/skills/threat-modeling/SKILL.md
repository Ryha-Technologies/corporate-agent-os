---
name: threat-modeling
description: Build and maintain a threat model (assets, trust boundaries, entry points, STRIDE or attack-tree threats, abuse cases, likelihood and impact, controls, detection, tests, residual risk) from architecture through implementation. Use at the architecture gate and whenever the system or its data changes.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: cybersecurity
---
# Threat modelling

## Purpose
Know what can go wrong, what stops it, how you would notice, and what risk remains, before and while the system is built.

## When to use
- Architecture gate; before implementing authentication, payments, uploads, integrations or AI features; after incidents.

## Preconditions
- Architecture with components and data flows; data classification; user roles.

## Inputs
- Architecture document, data model, API contract, deployment design, regulatory boundaries.

## Procedure
1. **Scope and assets.** What is being protected: data (by classification), credentials, money, availability, reputation, user safety.
2. **Model the system.** Components, data stores, data flows, trust boundaries (internet, tenant, admin, third party, model), entry points, privileges.
3. **Enumerate threats** per element with STRIDE (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) or attack trees for high-value goals. Add abuse cases: how a legitimate user misuses features (fraud, scraping, harassment, resource abuse).
4. **AI-specific threats** where applicable: prompt injection via content, tool misuse, data leakage across tenants, over-permissive tools, training-data rights, model output trusted as truth.
5. **Rate** likelihood and impact with stated reasoning; prioritise.
6. **Controls.** Preventive, detective and responsive controls per threat; map to ASVS requirements; name the test that verifies each control.
7. **Residual risk** per threat after controls; owner and acceptance status (critical never accepted).
8. **Maintain.** Update at each architecture or feature change and after incidents; record changes in the ADR log.

## Outputs
- `05-architecture/threat-model.md` (`templates/security/threat-model.md`) with threat table, control map and residual-risk register; `K-` ledger entries.

## Quality criteria
- Every trust boundary and entry point appears in the model.
- Each threat has a control and a verification test, or an explicit gap.
- Residual risks have owners; no critical residual risk.
- AI components modelled when present.

## Failure handling
- Architecture incomplete → model what exists; list unknown boundaries as open questions blocking the gate.
- Too many threats to control → prioritise by rated risk and record accepted lower risks with approvers.

## Safety boundaries
- Modelling does not authorise testing; active testing requires written scope.
- No exploit code for systems not owned by the user.

## References
- `templates/security/threat-model.md`
- `standards/security/secure-development.md`, `research/standards-mapping/security-standards-map.md`
