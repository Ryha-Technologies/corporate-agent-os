# Secure development standard

Applies across the lifecycle. Mapped to recognised frameworks in `research/standards-mapping/security-standards-map.md` (OWASP ASVS, OWASP Top Ten, OWASP SAMM, NIST SP 800-218 SSDF, OpenSSF, SBOM guidance). Framework names are references, not compliance claims.

## Requirements
| # | Requirement | Verified by |
|---|---|---|
| S1 | Threat model with assets, trust boundaries, entry points, threats, controls, detection and residual risk, maintained through implementation. | Threat model |
| S2 | Authentication: strong credential handling, secure recovery, MFA options where appropriate, no credential logging. | Security review |
| S3 | Session management: secure cookies/tokens, expiry, rotation, revocation. | Security review |
| S4 | Authorisation enforced server-side per operation, including tenant isolation and object ownership; deny by default. | Security review, tests |
| S5 | Input validation at boundaries; output encoding; protection against injection (SQL, command, template, path), CSRF, CORS misconfiguration, SSRF, unsafe deserialisation, unsafe file handling. | Security review, SAST |
| S6 | Secrets managed outside code; least-privilege credentials; rotation path. | Secret scan |
| S7 | Cryptography uses approved algorithms and libraries; keys managed; TLS everywhere. | Security review |
| S8 | Logging without sensitive data; audit trails for admin actions; monitoring and alerting. | Review |
| S9 | Dependencies pinned, scanned for advisories, provenance checked; component register or SBOM maintained. | Component register, scans |
| S10 | AI components: prompts, retrieved content, tool outputs and generated code treated as untrusted; tools constrained; authorisation outside the model; tenant-isolated retrieval; injection and leakage tested. | AI eval report, security review |
| S11 | Privacy by design: purpose, minimisation, retention, deletion, rights handling, processors, residency analysed; legal questions routed to counsel. | Privacy analysis |
| S12 | Security testing only within written, approved scope naming systems, environments and methods. | Scope record |
| S13 | Findings carry severity rationale, evidence, fix and retest; closed only after retest; critical findings block release and cannot be accepted as residual risk. | Findings register |
| S14 | Incident response: severities, commander, runbooks, communication templates, evidence preservation, postmortems. | Runbooks |

## Boundaries
- Offensive testing requires written authorisation; never test third-party systems.
- No exfiltration of data or credentials; no weaponisation of findings.
- A scan is a clue, not proof of security; "secure" and "compliant" are not conclusions this standard permits agents to state.
