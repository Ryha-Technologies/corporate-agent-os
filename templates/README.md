# Templates

Fill-in documents for the artefacts that workflows produce. Every template states its purpose, who fills it, what each section must contain and the acceptance criteria a reviewer applies. Angle-bracket text `<like this>` is guidance to replace; a finished document contains no angle brackets.

| Folder | Artefacts |
|---|---|
| `business/` | project brief, research brief, evidence ledger, competitor matrix, opportunity assessment, validation plan, business model, strategy memo, legal issue register, proposal |
| `product/` | PRD, acceptance criteria, roadmap |
| `branding/` | brand strategy, competitor pattern map, naming clearance, rejected concepts, creative brief, brandbook, asset provenance |
| `design/` | interview guide, usability test plan, information architecture, states matrix, design rationale, design tokens schema, component spec, design QA report |
| `engineering/` | ADR, architecture, cost model, API design, data model, component register, AI eval report, release notes |
| `testing/` | gate verdict, test plan, traceability matrix, test report, accessibility report, QA report, release readiness |
| `security/` | threat model |
| `operations/` | release checklist, runbook, incident postmortem, experiment, launch plan, sales playbook, support policy, onboarding checklist, operating budget, approval matrix, vendor register, role charter, RACI |

Templates are Markdown so they live in the project workspace (`core/memory/README.md`) and diff well. Spreadsheet-shaped artefacts (financial model, tokens) have JSON or CSV companions.
