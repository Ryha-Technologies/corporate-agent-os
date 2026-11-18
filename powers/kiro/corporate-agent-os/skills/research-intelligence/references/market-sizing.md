# Bottom-up market sizing

Top-down sizing ("the global X market is $Y billion") is acceptable only as a sanity check and only when the report's methodology was read. The primary estimate is bottom-up.

## Method

```
TAM = (number of potential buyers in the broadest sensible definition) × (annual spend per buyer on this job)
SAM = TAM × (share reachable with the product's segment, geography, language, channel and regulatory constraints)
SOM = SAM × (share obtainable in the planning horizon given conversion, capacity and competition)
```

Each factor is a ledger row with its source. Where a factor is estimated, the estimate is labelled and given a low/base/high value.

## Required table

| Factor | Low | Base | High | Source or reasoning | Confidence |
|---|---|---|---|---|---|
| Buyers in segment (count) | | | | e.g. national registry, census, industry body | |
| Share with the problem (%) | | | | customer research, surveys with sample size | |
| Annual spend per buyer | | | | observed prices, interviews on current spend | |
| Reachable share (%) | | | | channel analysis | |
| Obtainable share in N years (%) | | | | conversion assumptions, capacity | |

Compute TAM/SAM/SOM for low, base and high. Report all three; never a single number.

## Common errors

- Counting companies that cannot buy (wrong size, geography, regulation).
- Using list price when customers pay discounted or bundled prices.
- Confusing adjacent-category spend with spend on this job.
- Treating competitor funding or valuation as demand evidence.
- Hiding assumptions in a spreadsheet cell with no source.

## What to write in the brief

"Base-case SAM is X, built from A buyers × B% with the problem × C annual spend × D% reachable. The most influential assumption is B (confidence low; based on N interviews). A ±50% change in B moves SAM to [range]. Next experiment: survey N more buyers in segment S."
