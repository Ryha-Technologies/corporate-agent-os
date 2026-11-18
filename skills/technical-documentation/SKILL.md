---
name: technical-documentation
description: Write and verify user documentation, installation guides, API references, runbooks, release notes and knowledge base articles against the shipped product by executing every documented command, keeping terminology consistent and listing known limitations. Use whenever documentation must match real behaviour.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: engineering
---
# Technical documentation

## Purpose
Documentation that a new user or operator can follow successfully, because every command, path and feature claim was checked against the product.

## When to use
- Any release; installation guides; API changes; runbooks; help centre content.

## Preconditions
- Access to the code, build and a clean environment to execute instructions.

## Inputs
- Code, tests, PRD, API contract, release scope, audience definition, terminology list.

## Procedure
1. **Audience and task** per document: who reads it, what they are trying to do, what they already know.
2. **Structure** by task: getting started, how-to, reference, concepts, troubleshooting; one purpose per page.
3. **Write from behaviour**, not intent: derive from code, tests and running the product. Do not document features that do not exist or are flagged off.
4. **Execute everything** you document: install steps in a clean environment, commands, examples, API calls; record the result and version. Fix the doc or file a defect when reality differs.
5. **Terminology** consistent with the PRD and UI; maintain a glossary.
6. **Accessibility of docs.** Headings, alt text, code blocks with language, readable tables.
7. **Known limitations and prerequisites** stated up front.
8. **Release notes.** What changed, why it matters, migration steps, breaking changes, fixes, with links to issues.
9. **Review** by the documentation auditor who re-executes a sample.

## Outputs
- `docs/**` in the product repository, `09-operations/docs/**`, `06-build/release-notes.md`, glossary.

## Quality criteria
- Every command and path was executed or verified; the verification record exists.
- No phantom features; limitations listed.
- Terminology matches product and PRD.

## Failure handling
- Cannot execute in a clean environment → mark the step as unverified in the review record, not in the user-facing doc; schedule verification.

## Safety boundaries
- Never include secrets, personal data or internal URLs in public docs.
- Public docs require human approval.

## References
- `standards/documentation/documentation-standard.md`
- `templates/engineering/release-notes.md`, `templates/operations/runbook.md`
