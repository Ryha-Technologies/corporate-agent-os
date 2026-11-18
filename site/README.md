# Corporate Agent OS showcase site

A static site for [Corporate Agent OS](https://github.com/Ryha-Technologies/corporate-agent-os). Plain HTML, CSS and one small JavaScript file. No framework, no build step, no dependencies, no third-party requests.

## Files

| Path | Purpose |
|---|---|
| `index.html` | Home: hero, why, departments, how it works, platforms, quick start, status, author |
| `skills.html` | The 39 skills, grouped, with a filter |
| `agents.html` | The 58 agents in five tiers, with a filter |
| `docs.html` | Links into the repository docs on GitHub |
| `assets/style.css` | Styles, with contrast ratios in the header comment |
| `assets/filter.js` | Filter for the skills and agents pages. Pages work without it. |
| `assets/banner.png` | Project banner copied from `docs/assets/banner.png` in the repository |
| `QA.md` | What was checked and what was not run |
| `qa/` | Overflow measurement and screenshot scripts (headless Chrome) plus two reference renders |

Fonts: system font stack only, so there is no font licence to record.

## Preview locally

From this `site/` folder:

```
python -m http.server 8000
```

Open <http://localhost:8000/>. Stop with Ctrl+C. Opening `index.html` directly from disk also works.

## Deploy to GitHub Pages

Deployment needs a person's approval. These are the steps for the person who owns the repository.

Option A, from a branch:
1. Put the contents of `site/` at the root of a branch (for example `gh-pages`), or in a `/docs` folder on `main`.
2. In the repository, open Settings, then Pages.
3. Under Build and deployment, set Source to "Deploy from a branch", pick the branch and folder, and save.
4. Wait for the Pages build, then open the URL shown on that settings page.

Option B, with GitHub Actions: `.github/workflows/pages.yml` in this repository uploads `site/` with `actions/upload-pages-artifact` and deploys it with `actions/deploy-pages` on every push to `main` that touches `site/`. It needs Pages set to "GitHub Actions" as the source once (Settings, Pages).

All links between pages and to assets are relative, so the site works under a project path such as `/corporate-agent-os/`.

## Updating content

The skill and agent pages were generated from `.kiro/skills/*/SKILL.md` and `.kiro/agents/*.json`, and the department cards from `docs/organization/*.md` in the repository. The generator is not part of this folder. If the repository changes, update the HTML by hand or regenerate it, then re-check the counts on the pages.

## Status

Describes version 0.2.0, a beta. See `QA.md` for the checks that were not run.
