# Example: marketplace (illustrative)

Workflow: `idea-to-business` with two-sided specifics.

## Problem statements (01-research/problem-statements.md excerpt)

```
PS-1 (supply side, hypothesis): Independent <service providers> in <city> lose <share> of their week finding work
through word of mouth and spend <time> on unpaid quoting.
PS-2 (demand side, hypothesis): Households need a <service> within <time> and cannot judge provider reliability; they
fall back to <alternative>.
PS-3 (both sides, hypothesis): Payment disputes and no-shows erode trust; neither side has recourse.
Each labelled HYPOTHESIS until interviews (customer-research-plan.md) produce F- entries.
```

## Business model notes (02-product/business-model.md excerpt)

```
Options compared: take rate on completed jobs; provider subscription; lead fee; hybrid.
Unit = completed job. Variable costs include payment processing <range>, dispute handling <minutes>, SMS/WhatsApp
notifications <range>. Take rate <low>-<high>% gives gross margin <range> after variable costs.
Cold-start risk K-003: neither side joins without the other; mitigation hypothesis H-012 (seed supply in one
category and one locality first). Kill criterion: fewer than <n> completed jobs per provider per week after <weeks>.
```

## Design direction (04-design/design-rationale.md excerpt)

```
Category: marketplace (two-sided). Conventions kept: faceted search, provider verification signals, clear fees
before booking, separate provider dashboard. Direction: <adjective> and plain; trust is communicated through
specific verification facts and reviews with dates, not badges or gradients. Pattern-map comparison: competitors
<A>, <B> use <pattern>; this design does not.
Elements with a stated job: verification checklist (reduces booking hesitation per interview F-021); fee
breakdown before confirm (PS-3). Removed: decorative hero illustration (no job).
```

## Legal foundation (08-legal-oss/issue-register.md excerpt)

```
| L-004 | consumer | Marketplace liability for provider conduct | <jurisdiction> | <official source, date> | enacted |
Assumption: platform is an intermediary | Booking and dispute flows | H | Terms and dispute process to be drafted
by counsel | counsel: <name> | open |
Preliminary research, not legal advice.
```

What this example shows: both sides modelled separately, cold-start named as the main risk, a design direction justified against the pattern map, and legal questions routed to counsel.
