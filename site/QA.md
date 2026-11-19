# QA report: Corporate Agent OS showcase site

Scope: `site/index.html`, `skills.html`, `agents.html`, `docs.html`, `assets/style.css`, `assets/filter.js`, `assets/banner.png`.
Verdict: **GO_WITH_ACCEPTED_RISKS for a human-reviewed preview. Not a release approval.** Several checks below are `NOT_RUN`, and the author of the site also ran this self-check (no independent reviewer ran).

Delegation: the host's sub-agent feature was not used. The roles (discovery, IA, design, build, accessibility, documentation, anti-slop) were performed as sequential passes by one agent.

## What was checked, how, result

| # | Check | Method | Result |
|---|---|---|---|
| 1 | 39 skills, none invented | Generator read `.kiro/skills/*/SKILL.md` frontmatter; threw if count != 39 or any skill was ungrouped or duplicated; description = first sentence of each file's `description` | PASS |
| 2 | 58 agents in five tiers (1/8/10/28/11) | Generator read `.kiro/agents/*.json`; tier and autonomy parsed from `welcomeMessage`; threw if count != 58. Tier counts shown on the page are computed. | PASS (counts of 1/8/10/28/11 were confirmed in a listing before generation) |
| 3 | 22 departments, 9 workflows, 12 gates | Counted `departments/`, `workflows/`, `core/quality-gates/gates.yaml` in the local repo copy | PASS |
| 4 | Other brief facts (110 roles, 58 templates, 11 standards, 63 tests, 28 regression cases, 5 golden benchmarks, 10 validators, v0.2.0) | Copied from `BRIEF.md` as supplied. `VERSION` file in the local repo reads 0.2.0. The other counts were **not recounted**. | NOT_RUN (taken from brief) |
| 5 | External links | HTTP HEAD on all 55 unique external URLs | 54 return 200. `linkedin.com/in/velluraju` returns 405 (LinkedIn rejects HEAD); not verified. |
| 6 | Docs links resolve in the repo | Each linked path tested with `Test-Path` in the local repo copy, then fetched on GitHub (`main`) | PASS |
| 7 | Internal anchors, duplicate ids, one `h1` per page, heading order | Regex scan of the generated HTML | PASS (no duplicate ids, no broken anchors, no skipped heading levels) |
| 8 | Alt text | Scan: every `<img>` has `alt`; banner alt transcribes its text and describes the diagram | PASS |
| 9 | No horizontal scroll at 360, 768, 1280 | Headless Edge, each page in an iframe at each width, compared `scrollWidth` to `clientWidth` | PASS, all 12 combinations |
| 10 | Visual check at 1280 | Headless Edge screenshot of `index.html`, viewed | PASS (found and fixed: missing space in the brand name, orphaned count tile) |
| 11 | Placeholder text <!-- slop-ignore: describes the search itself --> | Search for lorem, TODO, TBD, placeholder. The only hit is the word "placeholders" inside the `anti-slop-quality-gate` skill description, quoted from the repo. | PASS |
| 12 | Fake metrics, testimonials, logos, user counts, readiness claims | Manual read of all copy. Numbers shown are repo counts from the brief. Only Kiro CLI 3.3.0 is described as live-verified. | PASS |
| 13 | Third-party requests | No external CSS, fonts, scripts or images. System font stack, so no font licence applies. | PASS |

## Contrast (WCAG 2.x relative luminance, computed)

| Foreground on background | Ratio | Requirement |
|---|---|---|
| Text #F4F6F8 on #15181C | 16.44:1 | 4.5:1 |
| Muted #AEB7C2 on #15181C | 8.78:1 | 4.5:1 |
| Accent #2EE6C5 on #15181C (links) | 11.23:1 | 4.5:1 |
| #15181C on accent #2EE6C5 (primary button, step numbers) | 11.23:1 | 4.5:1 |
| Text #F4F6F8 on panel #1D2227 | 14.79:1 | 4.5:1 |
| Muted #AEB7C2 on panel #1D2227 | 7.90:1 | 4.5:1 |
| Accent #2EE6C5 on panel #1D2227 | 10.11:1 | 4.5:1 |
| Border #6E7A87 on #15181C / on #1D2227 | 4.07:1 / 3.66:1 | 3:1 (non-text) |

The banner image contains small text (about 11 to 12 px at native size) that is part of the supplied brand asset; its content is repeated in the alt text and in page text.

## WCAG 2.2 AA, criterion level (partial)

- 1.1.1, 1.3.1, 2.4.1 (skip link), 2.4.2 (titles), 3.1.1 (`lang="en"`), 1.4.3, 1.4.11 (colour values above), 2.4.7 and 2.4.11 (visible 3px focus outline defined in CSS, header is sticky but only 2 rows high), 2.5.8 (nav links, buttons, inputs and footer links set to min-height 44px), 2.3.3 and reduced motion (the site has no animation; a `prefers-reduced-motion` rule is present anyway): **PASS by code inspection**.
- 4.1.2 / 1.3.1 for the filter: labelled input, polite live-region status: **PASS by code inspection**, not exercised.
- Scrollable regions (`pre`, table wrapper) have `tabindex="0"` and an accessible name so keyboard users can scroll them: PASS by code inspection.

## NOT_RUN

- Interactive keyboard walk-through of every page in a browser (tab order, focus visibility actually rendered).
- Screen reader testing (NVDA, JAWS, VoiceOver).
- Automated accessibility scanner (axe, Lighthouse, WAVE).
- Executing `filter.js` (typing in the filter and checking counts and hidden groups). Code is 25 lines; unexercised.
- Viewing the 360 px and 768 px renderings (only overflow was measured; a 360 px screenshot was captured but not inspected).
- Firefox, Safari, and real mobile devices. Only Chromium-based Edge was used.
- HTML validation with the W3C validator.
- Independent review by a `design-qa-auditor`, `documentation-auditor` or `test-auditor` agent.
- Verification of the brief's facts against the upstream repository beyond the local copy and the link checks above.
- Deployment to GitHub Pages (not permitted by the brief).
- Zoom to 200 % and 400 % reflow, forced-colours mode, print.

## Anti-slop self-check

- Every section has a stated job. No gradients, shadows or decorative imagery. Teal is used for links, focus, the primary button and step numbers only.
- The one image is the project's own banner, not stock imagery.
- Claims are limited to the supplied facts and to text read from the repo. The "How it works" five-step list and the SVG are this site's summary of the orchestrator rules; they are labelled as a general pattern.
- The grouping of skills into seven areas is the site's own organisation, and the skills page says so.
- Known weakness: the layout is a conventional dark card grid. It is plain by intent, but it is not a strongly distinctive design.

## Independent check (Velluraju C, after generation)
Tooling: headless Chrome (not Edge), `qa/measure.py` and `qa/shoot.py` (screenshots `qa/index-360.png`, `qa/index-1280.png`).
- Overflow re-measured on all four pages at 360, 768 and 1280 px: `scrollWidth == clientWidth` in all 12 cases, and no element outside the `pre` / `.table-scroll` scrollers extends past the viewport. Check 9 above **confirmed**.
- 360 px and 768 px renderings were viewed this time (the generator's QA listed this as NOT_RUN): header wraps to two rows at 360 px, counts grid collapses to two columns, no clipping.
- False alarm recorded for honesty: a first screenshot with `--window-size=360,900` appeared to clip the hero and counts. Headless Chrome clamps its window to a minimum of 500 px, so that image was a 500 px layout cropped to 360 px, not a site defect. The rerun loads each page in a 360 px iframe (with `--allow-file-access-from-files`) and crops the iframe region.
- Still NOT_RUN: everything in the NOT_RUN list above except the 360/768 visual check.

## Open issues to accept or fix

1. NOT_RUN items above, especially keyboard and screen-reader checks.
2. The LinkedIn link is unverified by tooling.
3. Counts not recounted: 110 roles, 58 templates, 11 standards, 63 tests, 28 regression cases, 5 golden benchmarks, 10 validators.
