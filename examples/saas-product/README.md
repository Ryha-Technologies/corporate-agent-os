# Example: SaaS product (illustrative)

Workflows: `product-discovery` → `product-design` → `software-development` → `security-review`.

## 02-product/prd.md (excerpt)

```
Goal: teachers at small language schools record attendance for a class in under 30 seconds on a phone
(metric: median time in usability test; target <n>s by <date>).
Non-goals: billing, grading, parent chat.
Story S-004: As a teacher I want to mark attendance so that parents are notified of absences.
  AC-004a Given a scheduled class today, When I open it, Then I see the roster with every student defaulted to present.
  AC-004b Given I mark a student absent and tap Save, When the save succeeds, Then the parent notification job is queued and I see confirmation.
  AC-004c Given the network drops during Save, When I retry, Then no duplicate notification is sent (idempotency key).
  AC-004d Given a keyboard-only user, When focus moves through the roster, Then every control is reachable and labelled.
Data: student name and attendance = personal data of minors → retention <n> months, deletion on withdrawal,
lawful-basis question Q-007 for legal.
```

## 04-design/states-matrix.md (row)

```
| Attendance roster | specified | specified (skeleton rows) | specified (no students enrolled) | specified | specified (unsaved changes) | specified (save failed, retry) | specified (offline queue) | specified (not the class teacher) | specified | specified (saved) | n/a (no destructive action) |
```

## 05-architecture/adr/ADR-001.md (excerpt)

```
Decision: single deployable web service with a relational database and a background job table for notifications.
Options: (a) as decided; (b) separate notification microservice with a message broker; (c) serverless functions.
Rationale: stated scale <n> schools, <n> notifications/day; (b) adds operational surface without a requirement;
(c) complicates local development for a one-developer team. Reversibility: high; the job table is an interface.
Revisit trigger: sustained notification backlog > <n> minutes or > <n> schools.
```

## 07-quality/gate-build-slice-1.md (excerpt)

```
GATE: build   REVIEWER: code-reviewer   VERDICT: FAIL → (after rework) PASS
Re-ran: `npm ci && npm run lint && npm test` → lint 0 errors; tests <n> passed, 0 failed (<duration>).
Findings (first pass):
 - high: attendance save endpoint lacked tenant check on class id (src/routes/attendance.ts:<line>). Fix added, test
   `rejects save for class outside tenant` added. Retest: PASS.
 - medium: migration 0003 not reversible (missing down). Fixed. Retest: PASS.
 - low: debug logging of request body included student names. Removed. Retest: PASS.
```

What this example shows: a narrow slice, every state specified, an ADR that refuses unneeded complexity, and a build gate that fails first and passes after real rework with re-run commands.
