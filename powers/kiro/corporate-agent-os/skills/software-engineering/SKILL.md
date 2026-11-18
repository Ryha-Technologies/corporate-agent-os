---
name: software-engineering
description: "Implement application features in small, maintainable, secure, tested increments following repository conventions: inspect first, vertical slices, validation at boundaries, tests with negative cases, formatter/linter/type/test/build runs with recorded output, reviewed diffs. Use for any implementation task."
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: engineering
---
# Software engineering execution

## Purpose
Ship working, tested, secure code inside the assigned scope, with evidence of what was run, so reviewers and operators can trust it.

## When to use
- Any task that changes code, configuration, migrations or infrastructure definitions.

## Preconditions
- Task contract with file ownership and acceptance criteria; architecture and API/data contracts for the slice; repository access.

## Inputs
- Task contract, PRD slice, design package (for UI), API contract, data model, repository conventions.

## Procedure
1. **Inspect before editing.** Language, package manager, structure, conventions, tests, CI, existing components, changelog, open issues. Do not replace the stack.
2. **Slice.** Translate the requirement into one vertical slice with acceptance tests; confirm interfaces and ownership with the orchestrator or lead.
3. **Reuse.** Prefer existing abstractions; avoid new dependencies, broad rewrites, duplication and speculative abstraction. New dependencies go through `oss-reuse-license`.
4. **Implement one coherent change.** Focused functions, explicit types where the language supports them, handled errors, validated input at trust boundaries, clear module boundaries.
5. **Security defaults.** Treat external input and model output as untrusted; parameterised queries; output encoding; secure session handling; least privilege; secrets from environment or vault, never in code or logs.
6. **Tests.** Unit, integration, contract and end-to-end as appropriate; include negative, boundary and failure cases. Tests must fail for the right reasons.
7. **Run everything.** Formatter, linter, type checker, tests, build. Record exact commands and outputs. Fix regressions; never silence failures with broad ignores or skipped tests without disclosure.
8. **Inspect the diff.** Unrelated changes, secrets, dead code, debug output, accidental API changes, generated files, scope violations.
9. **Docs.** Update docs, examples, migrations, changelog and operational notes when behaviour changes.
10. **Report.** Files changed, commands and results, limitations, risks. "Works" requires evidence.

### UI implementation
Semantic HTML, accessible forms, real loading/error/empty states, responsive layouts, robust state handling, tokens from the design system; verify in a browser at representative sizes; no fake data in production flows.

### Database changes
Reversible migrations, explicit constraints, indexes justified by queries, safe rollout for large tables, backup/restore awareness, integrity tests; no destructive production migrations without approval.

### Git
Small commits, clear messages, scoped changes. No force-push, history rewriting, branch deletion, resets of others' work, or edits outside assigned scope without permission.

## Outputs
- Code within file ownership; tests; `06-build/<area>-notes.md` with commands and results; changelog entry.

## Quality criteria
- Build and tests pass, or failures are disclosed with cause.
- Diff limited to task scope; no secrets or debug output.
- Validation, error handling and authorisation present at boundaries.
- Tests include negative and failure cases.

## Failure handling
- Specification gap → ask the lead or record the assumption as `A-` with `review_by`; do not guess silently on behaviour.
- Tests cannot run in the environment → mark `NOT_RUN` with reason.
- Conflicting file ownership → stop and report; never overwrite another agent's files.

## Safety boundaries
- No destructive commands, force pushes or production actions without approval.
- No execution of untrusted scripts; no secrets committed.

## References
- `standards/engineering/engineering-standard.md`, `standards/security/secure-development.md`
- `skills/code-review/SKILL.md`, `skills/test-strategy/SKILL.md`, `skills/oss-reuse-license/SKILL.md`
