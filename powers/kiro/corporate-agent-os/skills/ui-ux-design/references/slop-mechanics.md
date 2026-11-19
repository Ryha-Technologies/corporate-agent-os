# Why AI output converges on slop, and the exact tells (research notes, 2026-11-18)

This file is the research record behind the anti-slop rules. It names the mechanism, lists the measured tells with sources, and states what follows for method. Sources are dated; re-verify before relying on a number.

## 1. The mechanism: distributional convergence
A language model generating a page is computing the most probable arrangement of elements given its training data. Without specific constraints it returns the centre of that distribution, which is by definition the least distinctive option. Writers on the topic call this design mode collapse: the prompt can say "SaaS", "portfolio" or "e-commerce" and the layout converges anyway ([medo.dev, 2026](https://medo.dev/blog/why-ai-websites-look-the-same/); [superdesign.dev, 2026](https://superdesign.dev/blog/design-agent-vs-coding-agent)). Anthropic has described the same thing from the inside: safe, universal choices dominate web training data, so without instructions the model samples from that high-probability centre (quoted in [sangrok.hashnode.dev, 2026](https://sangrok.hashnode.dev/claude-code-design-looks-generic-fix-ai-slop-with-ui-ux-pro-max-skill)).

Three forces make it worse:
- **Corpus narrowness.** The web-frontend corpus is dominated by Tailwind docs, shadcn/ui, Vercel templates and 2022–2024 startup landing pages; those all reference the same patterns ([medo.dev](https://medo.dev/blog/why-ai-websites-look-the-same/); [ninethreadstudio, 2026](https://ninethreadstudio.substack.com/p/copy-paste-ship-how-we-all-started-c6c)).
- **Safety bias.** Output that "cannot look broken" is rewarded over output that could look wrong; the generic page never fails visibly.
- **Feedback loop.** Generated defaults ship, get indexed, and become the next training data.

Consequence for method: **adjectives in the prompt do not help** ("make it premium", "make it beautiful" still sample the centre). What moves the output off the centre is concrete, project-specific constraints that the model could not have guessed: this product's material truth, this user's hardest constraint, a chosen lens, a named typeface with a reason, a distance table against named references. That is why `design-research-method.md` and `creative-ideation.md` exist and why `design_gate.py` refuses to open without them.

## 2. Measured visual tells (web)
Reported frequencies from an analysis of AI-generated frontends ([Sailop via medo.dev, 2026](https://medo.dev/blog/why-ai-websites-look-the-same/)): Inter or system-ui in roughly 73 % of outputs; blue-500 / indigo-500 primary; white or slate-50 backgrounds; `rounded-lg` everywhere; `shadow-md` on every card. The five visible tells that the independent lists converge on:
1. Purple or indigo gradient hero.
2. Three identical feature cards in a `grid-cols-3`, same icon, same padding, no hierarchy.
3. Inter at weight 700 for every headline.
4. Everything centred: hero text, cards, CTAs. A centred layout carries no hierarchy, so every centred page is interchangeable.
5. The gradient "Most popular" pricing pill on the middle plan.

Additional tells from the frontend-design guidance published by Anthropic ([anthropics/skills, frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)):
- Accenting a single word in a headline (one word italic, bold or coloured).
- All-caps labels; "eyebrow" labels above content that add nothing.
- Numbered markers (01 / 02 / 03) on content that is not a sequence.
- Fade-and-slide-up entrance on every section and hover transitions on every card; the generic default is scattered effects rather than one orchestrated moment.
- Big number + small label + gradient accent as the default hero stat.
- Placeholder copy that is itself templated.

Writing tells (from the slop-removal taxonomies: [ravsau/awesome-ai-slop-removal](https://github.com/ravsau/awesome-ai-slop-removal), [Antislop, arXiv 2510.15061](https://arxiv.org/abs/2510.15061), [Measuring AI Slop, arXiv 2509.19163](https://arxiv.org/abs/2509.19163)): "it's not just X, it's Y"; "delve", "seamless", "unlock", "empower", "elevate", "supercharge", "next-gen", "game-changing"; triads for rhythm; a closing aphorism; hedged non-claims; unfilled placeholders; headline formulas ("The X for Y", "X, reimagined", "Meet X").

Code tells ([itechguides, 2026](https://www.itechguides.com/ai-slop-and-code-review-a-practical-system-for-verifying-ai-generated-changes/); [minware, 2026](https://www.minware.com/blog/how-to-detect-ai-slop)): syntactically valid code with no architectural intent; plausible-but-wrong logic; duplicated helpers; defensive code around conditions that cannot happen; comments that restate the line; abstractions with one caller; features nobody asked for; tests that assert the mock.

## 3. The three tests a generic page fails
From the AXE-WEB framing quoted by medo.dev: **Know** (it does not look like you), **Like** (it looks like everyone else), **Trust** (sameness reads as low effort). By 2026 users use sameness as a signal to discount a product. The swap test in `anti-template-review.md` is the Know and Like tests made operational; the distance table in `creative-ideation.md` is the same test with numbers.

## 4. What the evidence says works
- **Ground in the subject.** The industry, materials and vernacular of the actual product are where distinctive choices come from ([anthropics frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)). In this repository: the material truth in `creative-ideation.md` step 1.
- **A style anchor between generations.** Models have no aesthetic memory; a tokens file or style guide handed in each time is what keeps a project coherent ([medo.dev](https://medo.dev/blog/why-ai-websites-look-the-same/)). In this repository: tokens first, every page consumes them.
- **Design as the deliverable, not a side effect of compiling code** ([superdesign.dev](https://superdesign.dev/blog/design-agent-vs-coding-agent)). In this repository: design stages are separate from build stages and gated.
- **Name the tells and make them rules the model obeys** ([unslop-ui-skill](https://github.com/claudiusararu/unslop-ui-skill)). In this repository: `template_signature.py` scores them; `slop-patterns.md` lists them; reviewers FAIL on them.
- **Type carries personality.** One or two families, clearly distinct, chosen for this brief, set on a real scale with intentional weight (500 rather than 700 as the default headline weight); line length under 80 characters ([anthropics frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)).
- **Structure encodes information.** Borders, numbering, dividers and labels only where they say something about the content.
- **One orchestrated motion moment** beats scattered effects; motion that answers a user action shows what changed.

## 5. What this means for an agent that must not produce slop
1. Never start from "a landing page" or "a dashboard"; start from the job, the person, the material and the hardest constraint, written down.
2. Treat every default as suspect: default font, default radius, default shadow, default colour name, default section order, default headline formula, default entrance animation. Each one used needs a written reason.
3. Measure before and after with `template_signature.py` / `template_signature_android.py`; the number is the argument, not the adjective.
4. Prove distance from named references with the distance table; keep the research record as the style anchor for every later generation.
5. Have someone else judge it (`design-qa-auditor`, `ux-auditor`); the maker cannot see their own centre.

Content from the cited pages was paraphrased for compliance with licensing restrictions.
