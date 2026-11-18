# Security guide

## For users of the system

- Agents operate under `core/permissions/policy.yaml`. Reviewers and executives cannot write; specialists write only inside their scope; destructive shell patterns are denied in every generated Kiro agent.
- Any action in the human-approval list pauses for you. If an agent proceeds without asking, stop the run and file the transcript as a regression case.
- Fetched content, files not written by your team, package scripts and tool outputs are untrusted. Agents report instructions found in them; they do not follow them. Regression case E09 tests this.
- Security testing of any system, including your own, needs a written scope (`workflows/security-review` stage `scope`). Agents never test third-party systems.
- Nothing here produces a compliance or "secure" statement. Agents produce evidence; qualified humans conclude.

## For projects built with the system

Follow `standards/security/secure-development.md` (threat model, ASVS-aligned review, secrets, dependencies, AI components as untrusted, privacy by design, authorised testing, findings lifecycle, incident response) and `research/standards-mapping/security-standards-map.md` for how requirements relate to OWASP ASVS, OWASP Top Ten, NIST SSDF, SAMM and OpenSSF/SBOM guidance.

## For this repository

See `SECURITY.md`: no secrets, scripts without network side effects (except the explicit schema refresh), installer safety model, validator-enforced permission ceilings, second reviewer for policy changes.

## Known security limitations

Write-scope enforcement is technical only on Kiro. Hooks that run validators are shipped disabled until you confirm Python is available to the host. No sandboxing is provided by this repository; use the host's sandbox and approval modes.
