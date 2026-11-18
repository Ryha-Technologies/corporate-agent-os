---
name: security-privacy
description: "Perform defensive security and privacy-by-design review of applications, APIs, AI workflows and infrastructure against OWASP ASVS and recognised guidance: authentication, session, authorisation, validation, injection, secrets, cryptography, logging, supply chain, privacy data handling, with prioritised findings and retests. Use at design, build and security gates for systems the user owns or is authorised to assess."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: cybersecurity
---
# Security and privacy engineering

## Purpose
Find and fix security and privacy weaknesses before release, with evidence per finding and a clear statement of what was and was not tested.

## When to use
- Architecture review, implementation review, pre-release; whenever personal, payment or regulated data is handled.

## Preconditions
- Written scope: the system, environments and testing methods the user owns or is authorised to assess. Without written scope, only design and code review proceed; no active testing.

## Inputs
- Architecture, threat model, code, dependency list, data inventory, deployment configuration, prior findings.

## Procedure
1. **Assets and boundaries.** Data classification, users and roles, trust boundaries, entry points, dependencies, admin surfaces, abuse cases.
2. **Threat model** (`threat-modeling`) with likelihood, impact, controls, detection, residual risk.
3. **Application review** against ASVS areas: authentication (credentials, MFA options, recovery), session lifecycle, authorisation and tenant isolation, input validation and output encoding, CSRF, CORS, SSRF, file uploads, deserialisation, injection (SQL, command, template, LDAP, path), secrets management, cryptography (approved algorithms, key handling), error handling and logging without sensitive data, backups, dependency and supply chain (pinned versions, provenance, advisories).
4. **Infrastructure review.** IAM least privilege, network exposure, TLS, default credentials, configuration baselines, logging and monitoring.
5. **AI components.** Prompts, retrieved documents, tool outputs and generated code are untrusted; constrain tools; enforce authorisation outside the model; isolate secrets; validate structured output; prevent cross-tenant retrieval; log safely; test prompt injection and data leakage.
6. **Privacy.** Purpose limitation, minimisation, lawful basis questions for legal, retention and deletion, access and export, processors and sub-processors, residency, breach process, notices. Record as analysis for `legal-risk-governance`; do not conclude compliance.
7. **Testing within scope.** Dependency scan, secret scan, SAST, DAST where authorised; record tool, version, date, target. Manual abuse cases for authorisation and business logic.
8. **Findings.** Severity by exploitability, impact, exposure, data sensitivity and compensating controls; affected asset; safe reproduction; preconditions; fix; verification test. Redact credentials and personal data.
9. **Retest** fixes and update status. A scan is not proof of security.

## Outputs
- `07-quality/security-review-<date>.md`, updates to `05-architecture/threat-model.md`, `08-legal-oss/privacy-analysis.md` inputs, `07-quality/gate-security-<date>.md`.

## Quality criteria
- Scope and authorisation recorded before any active testing.
- Each finding has evidence, severity rationale, fix and retest status.
- Tools recorded with version and date; manual review documented.
- Privacy analysis covers purpose, minimisation, retention, rights and processors.

## Failure handling
- No written scope → design and code review only; active tests NOT_RUN; say so.
- Critical finding → escalate immediately to security lead and human owner; block release.

## Safety boundaries
- Never test third-party or unscoped systems; never exfiltrate data or credentials; never weaponise findings.
- No compliance or "secure" claims; residual risk is owned by named humans.

## References
- `standards/security/secure-development.md`, `research/standards-mapping/security-standards-map.md`
- OWASP ASVS, OWASP Top Ten, NIST SP 800-218 (see `research/source-register.md`)
- `skills/threat-modeling/SKILL.md`, `skills/incident-response/SKILL.md`
