---
name: naming-ip-screen
description: Generate distinctive company or product names from strategic territories and run preliminary linguistic, domain, social-handle, company-registry and trademark screening across the user's target jurisdictions (India, US, EU and WIPO starting points) with an explicit status per candidate. Use before any name, logo or public launch; never as legal clearance.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: naming-ip
---
# Naming and preliminary IP screening

## Purpose
Produce a ranked shortlist of names that fit the brand strategy and have been screened as thoroughly as public tools allow, with honest statuses and a clear hand-off to qualified trademark counsel.

## When to use
- A company, product, feature or campaign needs a name.
- An existing name is about to be used in a new territory or category.
- A logo or design mark needs a similarity screen.

## Preconditions
- Brand strategy (positioning, personality, audience, geography) exists.
- Goods/services description and target jurisdictions are stated by the user; if not, ask once, then assume India, US and EU and label the assumption.

## Inputs
- Brand strategy, category audit, competitor pattern map.
- Goods/services, launch territories, languages of the audience.

## Procedure
1. **Generate from strategy.** Develop naming territories (invented, suggestive, metaphorical, descriptive-compound, founder/heritage where real) and explain the semantic logic of each candidate. Avoid random syllables and generator output.
2. **First-pass screen.** Score distinctiveness, pronounceability, spelling clarity, memorability, meaning and connotation in the audience's languages, category fit, extension potential, domain feasibility, undesirable meanings. Check pronunciation with speakers of the target languages when possible.
3. **Preliminary clearance per serious candidate** (see `references/trademark-offices.md`):
   1. Search exact term, spacing, plural, phonetic, spelling variants, transliterations, similar-sounding marks.
   2. Search the trademark databases of every launch territory (IP India public search, USPTO, EUIPO/TMview, WIPO Global Brand Database) in the relevant Nice classes and adjacent classes.
   3. Search company registries, app stores, domains, social handles, package registries and general web results.
   4. Check unregistered/common-law use, marketplace use and local-language meanings.
   5. Record for each hit: mark text, owner, territory, status, filing/priority dates, goods/services, similarity reason, source URL, access date.
   6. For logos, icons, slogans or borrowed elements, run copyright/originality checks separately; a logo search does not clear a name and vice versa.
4. **Assign status** from the allowed set only: `NOT_SCREENED`, `PRELIMINARY_LOW_CONFLICT_SIGNAL`, `POTENTIAL_CONFLICT`, `INSUFFICIENT_DATA`, `COUNSEL_REVIEW_REQUIRED`.
5. **Rank and report** using `templates/branding/naming-clearance.md`: rationale, pronunciation, meanings, negative associations, variants searched, domain/handle status, jurisdiction/class scope, results, confidence, unresolved issues, recommended next step. Keep screenshots or exports where databases permit.
6. **Hand off.** Recommend qualified IP counsel in each target jurisdiction before filing, investment, major spend or launch.

## Outputs
- `03-brand/naming-report.md`
- `03-brand/naming-screens/<candidate>.md` per serious candidate
- Ledger entries: `K-` for conflicts, `Q-` for counsel questions.

## Quality criteria
- Each candidate has a territory logic and scores.
- Every serious candidate has records for every target jurisdiction and class, or an explicit `INSUFFICIENT_DATA` with the missing jurisdiction.
- Statuses use the allowed set; no clearance language anywhere.
- Every search result has URL and access date.
- Limitations section lists databases not searched and reasons.

## Failure handling
- Database unreachable → `INSUFFICIENT_DATA` with the database name and date; never infer availability.
- Many conflicts → return to territories and generate new candidates; record rejected names with the conflict reason.
- User asks for "trademark safe" confirmation → refuse the wording, explain territorial and common-law limits, provide the status and the counsel step.

## Safety boundaries
- Never say "trademark safe", "copyright free", "available worldwide", "legally cleared".
- Never register, purchase, file or publish anything.
- Do not imitate a competitor's name with a one-letter change or phonetic twin.

## References
- `references/trademark-offices.md` — databases, classes, search tips, limitations per jurisdiction
- `templates/branding/naming-clearance.md`
- `standards/legal/legal-research-standard.md`
