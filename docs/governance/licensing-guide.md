# Licensing guide

## This repository

MIT licence (`LICENSE`). Every skill carries `license: MIT` in its frontmatter. The Kiro Power includes a copy of the licence.

Third-party material: two JSON schema files from agent-plugins.org are bundled under `scripts/validate/schemas/` for offline validation; they are reproduced as schema definitions with their source recorded. No other third-party text, fonts, images or code are included. Standards (WCAG, OWASP, NIST, SPDX) are cited by name and URL, not reproduced.

## Projects built with the system

- Every dependency, repository, model and dataset goes through `skills/oss-reuse-license` and lands in `templates/engineering/component-register.md` with SPDX identifier, use mode and obligations. Unknown licences block. Copyleft is analysed by use mode, not auto-rejected.
- Every font, image, icon, illustration, vector element and generated asset lands in `templates/branding/asset-provenance.md` with licence evidence. Generation does not establish rights.
- Names and marks go through `skills/naming-ip-screen` with the allowed statuses; nothing is "cleared" by an agent.
- Generate an SBOM when tooling is available and record tool, version and date; otherwise the component register is the stated substitute.
- The legal gate (`core/quality-gates/gates.yaml → legal`) is reviewed by `legal-licensing-reviewer` and needs human approval.

## What agents never do

File, register, purchase, sign, accept terms or contact regulators. Issue legal conclusions. Strip copyright notices. Use public availability as permission.

## Disclaimer

Everything the legal and licensing skills produce is preliminary research to prepare questions for qualified counsel. It is not legal advice.
