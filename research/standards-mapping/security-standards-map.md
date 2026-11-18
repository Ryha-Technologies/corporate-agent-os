# Security standards mapping

Maps the requirements in `standards/security/secure-development.md` and the security-related skills to recognised external frameworks. The mapping shows where each requirement draws its intent; it is not a claim of conformance or certification against any framework. Framework names and URLs are in `research/source-register.md` (T2–T7); versions should be re-checked before citing in a project.

| Repository requirement | OWASP ASVS (chapter theme) | OWASP Top Ten (theme) | NIST SP 800-218 SSDF (practice group) | OWASP SAMM (practice) | OpenSSF / SBOM guidance |
|---|---|---|---|---|---|
| S1 Threat model maintained | Architecture, design and threat modelling | Insecure design | Prepare the Organization; Protect the Software | Design: Threat Assessment | — |
| S2 Authentication | Authentication | Identification and authentication failures | Produce Well-Secured Software | Implementation: Secure Build | — |
| S3 Session management | Session management | Identification and authentication failures | Produce Well-Secured Software | — | — |
| S4 Authorisation, tenant isolation | Access control | Broken access control | Produce Well-Secured Software | Verification: Security Testing | — |
| S5 Validation, encoding, injection, CSRF/CORS/SSRF, deserialisation, file handling | Validation, sanitisation and encoding; Business logic; File and resources; API and web service | Injection; Security misconfiguration; Software and data integrity failures; SSRF | Produce Well-Secured Software | Implementation: Secure Build | — |
| S6 Secrets management | Configuration; Stored cryptography | Cryptographic failures; Security misconfiguration | Protect the Software | Operations: Environment Management | — |
| S7 Cryptography, TLS | Stored cryptography; Communication | Cryptographic failures | Produce Well-Secured Software | — | — |
| S8 Logging, audit, monitoring | Error handling and logging | Security logging and monitoring failures | Respond to Vulnerabilities | Operations: Incident Management | — |
| S9 Dependencies, provenance, SBOM | Dependencies (within configuration/malicious code themes) | Vulnerable and outdated components; Software and data integrity failures | Protect the Software; Produce Well-Secured Software | Implementation: Secure Deployment | OpenSSF Scorecard and best practices; CISA SBOM guidance; SPDX |
| S10 AI components treated as untrusted | Validation and business logic (applied to model I/O) | Injection; Insecure design | Produce Well-Secured Software | Design: Threat Assessment | — |
| S11 Privacy by design | Data protection | Cryptographic failures (data exposure) | Prepare the Organization | Governance: Policy and Compliance | — |
| S12 Authorised testing scope | — (process) | — | Prepare the Organization | Governance | — |
| S13 Findings lifecycle with retest | Verification requirements | — | Respond to Vulnerabilities | Verification: Security Testing | — |
| S14 Incident response | — | Security logging and monitoring failures | Respond to Vulnerabilities | Operations: Incident Management | — |

## How to use this map in a project

1. Decide which frameworks the project must reference (customer requirements, sector regulation). Record the decision and the framework versions in an ADR.
2. For each repository requirement, record the project's control and evidence in `templates/security/threat-model.md` and the findings register.
3. Any statement of conformance to a framework is made by a qualified human after an assessment; agents produce the evidence index only.

## Known gaps

- No mapping to sector-specific regimes (payment card, health, financial) is provided; projects in those sectors add rows with counsel.
- Framework chapter names change between versions; the table uses theme names rather than numbered sections to reduce drift. Verify against the current publication before citing a section number.
