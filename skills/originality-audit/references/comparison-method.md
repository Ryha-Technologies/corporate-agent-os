# Comparison method for originality audits

The scorecard asks "is it differentiated?". This method makes the answer reproducible: another auditor with the same references should reach the same verdict.

## Step 1 — Fix the reference set before reading the deliverable

| Reference type | Where from | Record |
|---|---|---|
| Competitor artefacts of the same kind (names, taglines, narratives, palettes, logos, screens, copy) | `01-research/competitor-pattern-map.md`, `03-brand/category-audit.md` | id, URL, access date, screenshot path |
| Category default | One-sentence description of what most of the category does for this artefact type | sentence |
| Generic-output patterns | `evaluations/originality/slop-patterns.md` | pattern ids used |

No reference set → differentiation is `NOT_ASSESSABLE`; say so and request the pattern map. Never compare from memory of "what brands usually do".

## Step 2 — Element-by-element table

Split the deliverable into its decisive elements (for a brand: name, tagline, narrative arc, personality words, palette logic, type character, mark motif; for a UI: see `skills/ui-ux-design/references/anti-template-review.md`; for a strategy or research document: framing, segment, claimed differentiation, evidence pattern, structure).

| Element | Ours (quote or describe) | Closest competitor (ref) | Closest generic pattern (slop id) | Relation: same / variant / different | Evidence for our choice (ledger id, brief, rationale) | Verdict |
|---|---|---|---|---|---|---|

Relation definitions:
- **same** — a reader would mistake one for the other or the text could be swapped without loss;
- **variant** — same idea with surface changes (synonyms, colour, order);
- **different** — a different idea that a reader would notice.

## Step 3 — Apply verdict rules

| Situation | Verdict | Severity |
|---|---|---|
| Same as a competitor's distinctive asset (name root, mark motif, signature phrase, named layout) | FAIL | high (route to legal review as well) |
| Same as generic pattern with no evidence | FAIL on specificity | medium |
| Variant presented as an alternative direction | FAIL on direction diversity | medium |
| Same as category convention with a stated, evidenced reason | PASS (convention kept) | — |
| Different with traceable reason | PASS | — |
| Different with no reason | finding: arbitrary; needs rationale | low |

## Step 4 — Whole-artefact tests

- **Swap test:** replace the company name with a competitor's. Does the artefact still read as theirs? If yes, it is generic.
- **Claim test:** for each claim, is there a ledger id or a labelled hypothesis? Unsupported claims fail evidence quality regardless of originality.
- **Three-directions test:** were at least three directions compared, differing in idea rather than surface? Check `rejected-concepts.md`.

## Step 5 — Convert findings to rework tasks

Each failing row becomes a task-contract line: the element, the reference it resembles, the strategic gap from the pattern map it should use instead, the acceptance criterion ("a new direction for element X that is *different* on the comparison table with a traceable reason"). The auditor does not propose the new creative content; the creator does.

## Step 6 — Record limits

State which references were used and which were unavailable, and that similarity judgements here are editorial, not legal. Automated similarity (text or image embeddings, reverse image search) may be cited as a signal with the tool named; it never changes a verdict on its own.
