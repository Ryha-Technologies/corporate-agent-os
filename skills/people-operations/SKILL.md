---
name: people-operations
description: Plan lean organisation structures, role charters with decision rights, workload-based capacity, fair job-related hiring criteria, secure onboarding and offboarding, operating rituals and human ownership of agent-augmented work. Use when roles, hiring, team process or org design are planned.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: people
---
# People and organisational operations

## Purpose
Give the company the roles, rituals and people processes it needs at its stage, fairly and securely, without pretending agents are employees or that a startup is a large enterprise.

## When to use
- Planning the first hires or a reorganisation; defining role charters; setting operating cadence; introducing agents into a team.

## Preconditions
- Strategy and operating plan exist; capacity constraints known.

## Inputs
- Strategy memo, operating plan, workload estimates, existing team, legal jurisdiction for employment questions.

## Procedure
1. **Organisation around outcomes.** Design from capabilities and accountable outcomes, not impressive department names. Combine functions at small scale; use `departments/*/roles.yaml → startup_stage` guidance; never imply one person is a department.
2. **Role charters.** Responsibilities, decision rights, success measures, skills, experience, interfaces; separate accountable owner from contributors and reviewers with a RACI/DACI for high-impact decisions.
3. **Capacity.** From actual workload, service levels and skills gaps; compare hire, contractor, partner, automation and process simplification.
4. **Hiring.** Structured, fair, job-related criteria and interviews; no discriminatory criteria or unsupported personality inferences; offers are human decisions.
5. **Onboarding.** Access controls, security and privacy training, documentation, first-week outcomes, mentor and manager check-ins.
6. **Operating rituals.** Planning, async updates, review, retrospectives, incident learning, decision logs; minimise meetings without removing accountability.
7. **Agent-augmented teams.** Assign a human owner for every outcome produced with agents; monitor quality, review burden, tool access, auditability and escalation; agents carry no legal responsibility.
8. **Performance.** Feedback on observable outcomes, craft, collaboration, learning, safety and customer impact; avoid surveillance-heavy metrics.
9. **Continuity.** Succession, knowledge continuity, access offboarding, credential rotation.

## Outputs
- `09-operations/org-model.md`, `09-operations/role-charters/**`, `09-operations/decision-matrix.md`, `09-operations/hiring-plan.md`, `09-operations/onboarding-plan.md`, operating cadence.

## Quality criteria
- Org model matches stage; roles combined where appropriate.
- Charters have decision rights and interfaces.
- Hiring criteria job-related; employment-law questions flagged for local professionals.
- Every agent-produced outcome has a human owner.

## Failure handling
- Workload unknown → plan with ranges and a review date.

## Safety boundaries
- Employment decisions are human; no legal conclusions on employment law.
- No collection of sensitive personal data beyond what hiring lawfully needs.

## References
- `templates/operations/role-charter.md`, `templates/operations/raci.md`
- `departments/README.md`
