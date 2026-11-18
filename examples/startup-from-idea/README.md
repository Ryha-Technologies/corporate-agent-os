# Example: startup from idea (illustrative)

Workflow: `business-validation`, then `idea-to-business` if the decision is pursue or test first.

## 00-intake/brief.md (excerpt)

```
Request as stated: "I want to build a scheduling tool for small field-service businesses in India
(plumbers, electricians, AC repair) that coordinate technicians over WhatsApp."
Problem: (F) Owners coordinate jobs by WhatsApp messages and phone calls. (A) This causes missed and
double-booked jobs. (A) Owners would pay a monthly fee to reduce it.
Constraints: Geography India (F); validation budget INR <amount> (F); timeline six weeks (F).
Chosen workflow: business-validation (D-001).
Blocking question: none; proceeding on assumptions A-001..A-003.
```

## 10-decisions/memory-ledger.jsonl (first lines)

```
{"id":"F-001","type":"fact","statement":"Founder runs a two-person company in Pune.","provenance":{"kind":"user_statement","source":"00-intake/brief.md"},"confidence":"high","recorded_by":"corporate-orchestrator","recorded_at":"<ts>","status":"active"}
{"id":"A-001","type":"assumption","statement":"Missed and double-booked jobs are frequent enough to matter to owners.","provenance":{"kind":"agent_inference","limitation":"No customer evidence yet."},"confidence":"low","recorded_by":"corporate-orchestrator","recorded_at":"<ts>","status":"active","review_by":"<date>"}
{"id":"H-001","type":"hypothesis","statement":"Incumbent tools under-serve WhatsApp-first dispatch.","provenance":{"kind":"agent_inference"},"confidence":"low","recorded_by":"research-lead","recorded_at":"<ts>","status":"active","review_by":"<date>"}
```

## 10-decisions/tasks/T-003.json

See `core/task-management/examples/T-003-competitor-map.json` for the complete contract shape used at this stage.

## 07-quality/gate-discovery-<date>.md (excerpt)

```
GATE: discovery   STAGE: synthesis   REVIEWER: research-auditor   VERDICT: PASS_WITH_ACCEPTED_RISK
Evidence checked: research-brief.md present; evidence-ledger.md present (N rows, 5 opened, all supported);
problem-statement.md present; competitor-map.md present with substitutes and "do nothing".
Findings:
 - medium: two consequential claims rest on a single source type (industry association report only).
   Fix: add a second source type or downgrade to hypothesis. Retest: re-open ledger rows E-014, E-021.
Accepted risk: medium finding accepted by human:founder pending interviews (review <date>).
```

## 10-decisions/opportunity-decision.md (excerpt)

```
Recommendation: TEST FIRST. Confidence: low-medium.
Evidence: problem frequency supported by owner interviews (<n> sessions, F-010..F-014); willingness to pay
untested (A-002); competitor map shows <n> direct tools, none WhatsApp-first in India (H-001 partially
supported, E-030..E-034); base-case SAM <range> built from <inputs>.
Assumption that matters most: A-002 (price INR <low>-<high> per technician per month).
Kill criteria: fewer than <n> of <m> owners complete a paid pilot sign-up by <date>; or interviews show
dispatch is not a top-three pain for most owners.
Next: six-week validation plan within budget (02-product/validation-plan.md). Human approval: <name>, <date>.
```

What this example shows: the first run can end in "test first" with a concrete plan. Nothing here is a real figure; every `<...>` would be filled from actual evidence with ledger ids.
