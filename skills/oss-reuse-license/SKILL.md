---
name: oss-reuse-license
description: Find, evaluate and integrate open-source components safely with repository due diligence, licence analysis by use mode (SPDX identifiers, obligations, compatibility), security and provenance checks, a component register or SBOM and preserved notices. Use before adopting any dependency, repository or third-party asset in a product.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: legal
---
# Open-source reuse and licence due diligence

## Purpose
Reduce delivery time with mature components while knowing exactly what was adopted, under which licence, with which obligations, and how to replace it. This is engineering and compliance triage, not legal advice.

## When to use
- Before adding a dependency, copying code, adopting a repository, model or dataset, or using fonts, icons and images.
- At the legal gate when producing the component register.

## Preconditions
- Distribution mode is known (SaaS hosted, distributed binary, mobile app, embedded, modified, linked); otherwise record it as an open question.

## Inputs
- Requirement to satisfy; candidate components; distribution mode; security requirements.

## Procedure
1. **Search before building.** Official registries, reputable hosting, standards bodies, vendor integrations. Compare build vs buy vs reuse on total lifecycle cost.
2. **Repository due diligence** per candidate: canonical repository and owner; exact version, tag, commit and release date; licence file and SPDX identifier (or `NOASSERTION`); copyright notices; provenance signals; maintenance activity, release cadence, issue response, bus factor, governance; open advisories, dependency risks, supply-chain history; supported runtimes and upgrade path; API stability, docs, tests, performance, accessibility; telemetry, data egress, install scripts, post-install hooks, required privileges.
3. **Licence analysis.** Read the actual licence text and notices; check SPDX ids against the SPDX License List. Classify: permissive, weak copyleft, strong copyleft, network copyleft, source-available, proprietary, dual, unclear. Determine obligations for the actual use mode: notices, source disclosure, relinking, patent terms, attribution, trademark restrictions, reciprocal licensing. "Open source" never means "no obligations"; copyleft is analysed, not auto-rejected. Record conflicts between licences in the dependency tree.
4. **Security and provenance.** Pin versions; prefer signed or verified releases; inspect package provenance, maintainers, artefact origin, dependency tree, install scripts, permissions, known vulnerabilities. Prefer official distribution; never install random forks or run untrusted scripts with elevated privileges; evaluate in isolated environments.
5. **Integration decision.** Score fit, maturity, support, licence risk, security risk, upgrade cost, lock-in, exit path. Define the wrapper or abstraction boundary so replacement is possible where practical.
6. **Record** in the component register (`templates/engineering/component-register.md`): repository URL, version/SHA, maintainer, licence/SPDX, files used, modifications, notices, scan date, known issues, deployment mode, obligations, reviewer, approval state. Generate an SBOM when tooling is available (record the tool and date); otherwise the register is the SBOM substitute and says so. Preserve upstream licences and notices; never strip headers.
7. **Red flags block integration** until resolved: no licence, conflicting licence files, copied code without provenance, unknown model or data rights, abandoned security-critical code, suspicious maintainer changes, install-time network scripts, unverifiable binaries, non-commercial terms, unresolved high-severity vulnerabilities.

## Outputs
- `08-legal-oss/component-register.md` (or SBOM file), decision notes, `K-`/`Q-` ledger entries for counsel.

## Quality criteria
- Every component has version, SPDX id (or NOASSERTION flagged), use-mode obligations and reviewer.
- Notices preserved; modifications recorded.
- Security scan date and tool recorded or NOT_RUN stated.
- Unclear compatibility routed to counsel, not closed.

## Failure handling
- No licence file → do not use; seek permission or an alternative; record.
- Scanner output ambiguous → read the licence text; treat tool output as a clue.

## Safety boundaries
- No legal conclusions; escalate licence compatibility and distribution obligations to qualified counsel.
- No execution of untrusted install scripts or binaries outside isolation.

## References
- `templates/engineering/component-register.md`
- SPDX License List, REUSE, ScanCode, OpenSSF (see `research/source-register.md`)
- `standards/legal/legal-research-standard.md`
