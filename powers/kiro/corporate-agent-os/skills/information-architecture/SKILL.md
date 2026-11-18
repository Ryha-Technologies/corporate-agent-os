---
name: information-architecture
description: Design navigation hierarchy, content models, page hierarchy, task flows and interaction models from user goals and content relationships, including error, empty, loading and responsive behaviour. Use before wireframes or visual design for any product with more than a handful of screens.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: design
---
# Information architecture

## Purpose
Organise the product around what users are trying to do and how content relates, so that navigation, labels and flows are findable and predictable before any pixel is placed.

## When to use
- After PRD and research; before wireframes.
- When navigation confusion or findability problems are reported.

## Preconditions
- PRD with user roles, scenarios and content/data entities; research on user goals and language.

## Inputs
- PRD, customer findings, content inventory (existing products), platform constraints.

## Procedure
1. **User goals and tasks.** List top tasks per role with frequency and importance.
2. **Content model.** Entities, attributes, relationships, ownership, lifecycle states. Note which entities users think of as the "things" in the product.
3. **Navigation hierarchy.** Global, local and contextual navigation; depth limits; labels in user language (test with card sorts or label tests where possible).
4. **Page hierarchy and templates.** Page types, their purpose, primary action, content blocks; which pages share a template.
5. **Task flows.** For each top task: entry points, steps, decisions, exits, error and recovery paths, permission boundaries.
6. **Interaction models.** Patterns for create/edit/delete, search and filter, bulk actions, confirmation and undo, destructive actions.
7. **States.** Error, empty, loading, offline, permission denied, expired session for each page type (feeds `states-matrix.md`).
8. **Responsive behaviour.** How navigation and hierarchy adapt across breakpoints; what is deprioritised on small screens and why.
9. **Validate.** Walk the flows as each role; tree-test labels where tools permit; record issues.

## Outputs
- `04-design/information-architecture.md`, `04-design/user-flows.md`, inputs to `04-design/states-matrix.md`

## Quality criteria
- Labels use user language from research, not internal jargon.
- Every top task has a flow with error and recovery paths.
- Navigation depth and structure are justified by goals, not org chart.
- Responsive adaptations are stated per breakpoint.

## Failure handling
- No content inventory → derive from PRD entities and mark as provisional.
- Conflicting mental models between roles → separate navigation per role or document the trade-off.

## Safety boundaries
- Do not invent user research; label untested labels and hierarchies as hypotheses.

## References
- `templates/design/information-architecture.md`, `templates/design/states-matrix.md`
- `standards/design/design-standard.md`
