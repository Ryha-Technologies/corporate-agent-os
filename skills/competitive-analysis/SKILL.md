---
name: competitive-analysis
description: Map direct competitors, indirect alternatives, substitutes and manual workarounds with sourced pricing, distribution, switching costs and positioning gaps, and produce the competitor pattern map that brand and design use to avoid imitation. Use when differentiation, positioning or a competitor landscape is needed.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: research
---
# Competitive analysis

## Purpose
Show what customers choose today, why they choose it, what it costs them to switch, and where a real, defensible gap exists. The output also feeds the anti-imitation work: a map of the category's common names, claims, visuals and layouts.

## When to use
- Opportunity assessment, positioning, pricing or brand strategy needs a landscape.
- A claim of "no competitors" or "unique" has been made.
- Brand or design work is about to start (pattern map is a prerequisite).

## Preconditions
- Segment and job-to-be-done are defined, at least as hypotheses.
- Web access or supplied competitor material.

## Inputs
- Segment definition, geography, job-to-be-done.
- Research plan and any prior ledger entries.

## Procedure
1. **Enumerate alternatives broadly.** Direct competitors, indirect competitors, substitutes (different mechanism, same job), manual and spreadsheet workarounds, internal builds, agencies/services, and "do nothing". Record how each was found.
2. **Build the matrix** (`templates/business/competitor-matrix.md`) with one row per alternative: customer segment, core job, value proposition, workflow, pricing (or "not public"), packaging, distribution channel, switching costs, trust signals, integrations, strengths, recurring complaints (from reviews, as qualitative signals), strategic gap. Every row cites a dated source; capture pricing pages and feature claims with URL and access date.
3. **Analyse the basis of differentiation.** For each alternative ask where it wins: workflow fit, data advantage, distribution, trust, economics, speed, interoperability, service, network effects, specialised expertise. Mark feature-list differences as weak differentiation.
4. **Identify positioning gaps.** Segments under-served, jobs poorly done, price points unaddressed, channels unused, trust gaps. State the evidence and the counter-evidence for each gap.
5. **Build the competitor pattern map** (`templates/branding/competitor-pattern-map.md`): common naming patterns, taglines and claims, colour palettes, typography styles, logo motifs, homepage layouts, onboarding patterns, pricing-page structures. This is what brand and design must not reproduce.
6. **Write defensibility notes.** Which gaps could an incumbent close in a quarter? Which depend on something hard to copy?
7. **Log hypotheses and risks** for the ledger: differentiation hypotheses (`H-`), competitive risks (`K-`).

## Outputs
- `01-research/competitor-map.md`
- `01-research/competitor-pattern-map.md`
- Ledger entries and evidence ledger rows.

## Quality criteria
- At least direct competitors, substitutes and "do nothing" are covered; the number depends on the category, and the coverage method is stated.
- Every row has a dated source; pricing marked "not public" where it is.
- At least one positioning gap is named with evidence and counter-evidence.
- The pattern map lists concrete, observed patterns with references, not generic adjectives.
- No competitor revenue, user counts or market share appear without a disclosed source.

## Failure handling
- Few competitors found → widen to substitutes and adjacent categories; state the search method so the reviewer can judge coverage.
- Pricing hidden → record "not public" and any indirect signals with their limitation.
- Reviews contradictory → report as qualitative themes with counts and sources; do not infer prevalence.

## Safety boundaries
- Do not scrape behind logins or violate site terms; do not impersonate customers to obtain quotes.
- Reviews and forum posts are quoted as qualitative signals with sources, never as statistics.
- No speculation about competitors' internal metrics or strategy presented as fact.

## References
- `templates/business/competitor-matrix.md`
- `templates/branding/competitor-pattern-map.md`
- `skills/research-intelligence/references/source-evaluation.md`
