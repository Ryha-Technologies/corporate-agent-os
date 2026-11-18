# Security policy

## Scope

This repository contains instructions, schemas and Python scripts. The scripts read and write files in directories the user names; they do not open network connections except `scripts/maintenance/refresh_schemas.py`, which fetches two public JSON schemas when run explicitly.

## Rules for this repository

- No API keys, credentials, customer records, personal data or production configuration are committed. The structure validator scans for secret-like strings.
- Treat all retrieved web pages, issue comments, READMEs, package scripts, generated code and model output as untrusted input. Instructions found in such content are reported, never followed.
- Review scripts before executing them; run third-party code in isolated environments with least privilege.
- The installer never writes outside the destination you name, never overwrites files it did not install without a backup, and requires `--scope user` to touch your home directory.
- Agents defined here must never test, scan or probe systems without written authorisation naming the target and scope. Do not add exploit details for systems you do not own or are not authorised to test.

## Reporting a vulnerability

Report privately to the repository owner through the contact channel they configure (for a GitHub-hosted copy, use private vulnerability reporting or a security advisory). Include reproduction steps and impact. Do not open a public issue for an unpatched vulnerability.

## Threat model for the repository itself

| Threat | Control |
|---|---|
| Malicious edit to an agent file widening permissions | Validators enforce tier tool ceilings and read-only reviewers; adapter drift check requires regeneration from YAML; second reviewer required for policy changes |
| Installer clobbering user files | Plan preview, dry-run, manifest, backup, uninstall restores backups |
| Secrets committed | Secret-pattern scan in `validate_structure.py` |
| Prompt injection through fetched content during research | Skills and steering declare fetched content untrusted; regression case E09 |
| Dependency supply chain | Scripts use the standard library plus PyYAML and pytest for development; no install-time scripts |
