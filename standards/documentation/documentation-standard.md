# Documentation standard

Applies to product documentation, API references, runbooks, release notes, help centre content and this repository's own docs.

| # | Requirement | Verified by |
|---|---|---|
| DOC1 | Each document names its audience and the task it supports; one purpose per page. | Reviewer |
| DOC2 | Content is written from actual behaviour (code, tests, running product), not from intent or roadmap. Features that do not exist are not documented. | Documentation audit |
| DOC3 | Every command, path, option and example was executed or verified in a clean environment; the verification record exists. | Documentation audit |
| DOC4 | Terminology matches the PRD and UI; a glossary exists for products with domain terms. | Reviewer |
| DOC5 | Prerequisites and known limitations are stated up front. | Reviewer |
| DOC6 | Install instructions match the actual scripts and their options. | Documentation audit (executes them) |
| DOC7 | Compatibility and platform claims are evidence-based and dated. | Compatibility matrix, source register |
| DOC8 | Documents are accessible: heading hierarchy, alt text, code blocks with language, readable tables. | Reviewer |
| DOC9 | No secrets, personal data or internal URLs in public docs. | Secret scan |
| DOC10 | Release notes list changes, breaking changes, migration steps, fixes and verification. | Reviewer |
| DOC11 | Component type is labelled where it matters: specification / playbook vs implemented and tested software. | Reviewer |
