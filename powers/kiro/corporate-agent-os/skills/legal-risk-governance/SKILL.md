---
name: legal-risk-governance
description: Identify legal, regulatory, contractual, privacy, consumer-protection, IP and governance issues in technology products and company operations through sourced research by jurisdiction, producing an issue register and counsel questions without giving legal advice. Use at brand, legal and release gates and whenever personal data, payments, minors, health, finance, advertising claims or cross-border processing are involved.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: legal
---
# Legal, regulatory and governance issue spotting

## Purpose
Surface every legal question early with its jurisdiction, source and counsel owner so that qualified humans decide, and nothing automated is mistaken for legal clearance.

## When to use
- Naming and brand gate; data handling design; terms, privacy notices and contracts; advertising claims; launch in a new jurisdiction; incidents with notification questions.

## Preconditions
- Entity type, operating and customer jurisdictions, sectors and data categories are known or explicitly assumed.

## Inputs
- Product description, data flows and inventory, jurisdictions, vendors and processors, planned claims, contracts.

## Procedure
1. **Intake.** Entity, jurisdictions, sectors, data categories (personal, health, financial, biometric, children's), payments, marketplaces, AI decisions, advertising, employment, IP, cross-border processing.
2. **Questions and jurisdictions.** List the legal questions per area: trademark and copyright (with `naming-ip-screen`), patents and design rights (flag only), software and asset licensing (with `oss-reuse-license`), model and dataset licences, privacy and data protection, consumer protection, advertising claims, contracts and terms, sector regulation, cross-border transfers, employment.
3. **Research** current official statutes, regulator guidance, standards and decisions; record source, date, scope, uncertainty. Distinguish enacted law from draft bills, guidance, industry standards and vendor statements. Do not cite stale law as current.
4. **Map obligations** to features, data flows, contracts, notices, retention, security, user rights, incident handling, operating processes; identify vendor, processor, sub-processor, marketplace, consumer, employment and IP obligations.
5. **Issue register** (`templates/business/legal-issue-register.md`): question, jurisdiction, source, applicability assumption, risk, affected feature, mitigation, counsel owner, status.
6. **Asset and dependency provenance.** Confirm the component register and asset provenance record exist and are complete; flag gaps.
7. **Counsel questions.** Prepare a prioritised list for qualified local counsel before launch, contract signature, filing or spend.
8. **Disclaimer** on every output: preliminary research, not legal advice; qualified counsel required for conclusions.

## Outputs
- `08-legal-oss/issue-register.md`, `08-legal-oss/jurisdiction-map.md`, `08-legal-oss/counsel-questions.md`, `08-legal-oss/privacy-analysis.md` (inputs), `08-legal-oss/asset-provenance.md` (verification).

## Quality criteria
- Every issue has jurisdiction, source with date, applicability assumption and counsel owner.
- Enacted law, drafts and guidance are labelled.
- No compliance, clearance or "legally safe" statements.
- Privacy notices and consent banners are not treated as substitutes for lawful handling.

## Failure handling
- Jurisdiction unknown → list the assumption, research the most likely, and mark the register incomplete.
- Conflicting sources → record both with dates; route to counsel.

## Safety boundaries
- Never submit filings, accept terms, sign contracts or contact regulators.
- Never draft definitive answers when facts or jurisdiction are unknown.
- Never invent provisions or case law.

## References
- `templates/business/legal-issue-register.md`, `templates/branding/asset-provenance.md`
- `standards/legal/legal-research-standard.md`
- `skills/naming-ip-screen/SKILL.md`, `skills/oss-reuse-license/SKILL.md`, `skills/security-privacy/SKILL.md`
