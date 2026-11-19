# Overhaul run plan (existing repository to released product)

Status: plan for the next live run. Written 2026-11-18 after two live runs of `product-overhaul-orchestrator` on Kiro CLI 3.3.0 and 3.5.0. Every step has a command and a pass/fail check; nothing is called done on opinion.

## Principles
1. **Two phases, one gate between them.** Audit changes nothing. Build starts only from approvals the owner wrote down.
2. **Delegate for real.** Every deliverable names its maker (`Made by:`), the maker owns the folder, and a reviewer who is not the maker signs off.
3. **Evidence on disk, not in chat.** A finding that exists only in a log does not count.
4. **Measured, then looked at.** Scripts score; a reviewer opens the screenshots; both are required.
5. **Honest status.** Every unrun check is `NOT_RUN` with the reason.

## Sequence

| # | Step | Command or action | Pass condition | Owner |
|---|---|---|---|---|
| 0 | Answer the owner questions | Copy `templates/business/owner-answers.md` to `<project>/00-intake/owner-answers.md` and fill it | File exists; unknowns written as `UNKNOWN` | You |
| 1 | Preflight | `python scripts/run/run_overhaul.py --project <p> --phase audit --preflight` | No `FAIL` on kiro-cli, install (58 agents, 52 skills) or project folder; Chrome present or visual checks marked `NOT_RUN` | Script |
| 2 | Audit run | `python scripts/run/run_overhaul.py --project <p> --phase audit --request "<your words>"` | Script exit 0: 6 core files exist; all 10 department audits on disk; proposal says `AWAITING_APPROVAL`; no project source file changed; ownership check passes (no stray folders); copy check passes; at least 3 delegation calls | Orchestrator and 10 specialists |
| 3 | Read and decide | Open `10-decisions/overhaul-proposal.md`; for each item write a line in `10-decisions/approvals.md`: `- M-2: approved by <name> on YYYY-MM-DD`. Skip items you reject | At least one approved item; each approval names you | You |
| 4 | Direction choice | The audit run presents three researched directions in `04-design/research-record.md`; pick one and write `Approved by <name> on <date>` under `## Approved direction` | `design_gate.py` prints `DESIGN GATE OPEN` | You |
| 5 | Build run | `python scripts/run/run_overhaul.py --project <p> --phase build` | Refuses to start without steps 3 and 4. Script exit 0 afterwards: design gate OPEN; `visual_quality_loop.py` DONE (two reviewed passes at 90 or more by a non-maker); ownership and copy checks pass; `release-readiness.md` exists | Orchestrator and specialists |
| 6 | Independent verification | Run the three scorers yourself on the result: `template_signature.py`, `visual_quality_loop.py --reviewer-json <your review>`, `copy_slop_check.py` | Template signature `DISTINCT`, or `MIXED` with a written reason per remaining point; your own swap test passes (below) | You |
| 7 | Release | You merge `overhaul/<date>`, deploy by the runbook, switch payments live only by your written word | `release-record.md` written; rollback point recorded | You, devops-engineer |
| 8 | Post-launch review | On the dates in the executive review | Real metrics read against the model's assumptions; confirm, adjust or stop | You, ceo-strategy |

## Acceptance criteria for the whole run
- Every page in `00-intake/page-map.md` has a keep, change, merge, remove or add decision with a reason.
- Every approved item maps to a finding id; no unapproved change appears in the diff (`git diff main..overhaul/<date>` reviewed against `approvals.md`).
- Template signature of every built page: before and after in `04-design/evidence/`.
- Visual quality loop: final pass at or above 90 on every main page, twice in a row, reviewer is not the maker, reviewer lists every screenshot as viewed.
- Security findings of severity High or above: zero open, each retested by a different agent.
- Contrast, overflow at 360/768/1280, targets of at least 24 px: all pass in the loop output.
- Swap test: show three anonymised screenshots (yours and two references) to at least three people who did not work on it; record how many pick yours out. A page that two of three can pick out is distinct; none picking it out is the target; all picking it out is a fail.
- Every library used is in `08-legal-oss/component-register.md` with its licence.

## Kill criteria
- Step 2 fails twice in a row for the same reason: stop and fix the system, not the run.
- Template signature stays `COMMON` after two design passes: stop and ask whether the constraints (stack, must-not-change) are the cause.
- Loop returns ESCALATE (exit 3): show both passes to the owner.
- Counsel or the executive review finds a legal or economic blocker: stop; do not polish what should not ship.

## Known risks and how the plan handles them
| Risk | Evidence | Handling |
|---|---|---|
| Host behaviour changes between Kiro CLI versions | Delegation, trust flags and write rules were probed on 3.3.0 and again on 3.5.0 | Launcher records the version in every run summary and warns on unverified versions; re-run the one-delegation probe after an upgrade |
| Orchestrator does specialist work itself | First live run: audits written directly, no delegation | Launcher fails the run when fewer than 3 delegation calls; `ownership_check.py` fails any file made by the orchestrator outside its two folders |
| Agents write outside the defined folders | Live run created `06-security/` | `ownership_check.py` fails on any stray numbered folder |
| Audits exist only as chat text | Five audits of the first run were blocked from disk | Launcher checks all ten department audits exist on disk |
| Reviewer slot filled by the maker | Possible by design | Loop rejects a maker, a missing reviewer id, or screenshots not listed as viewed |
| Scores reward the wrong thing | Heuristics miss composition | A human opens the screenshots and runs the swap test; scripts are floors, not verdicts |
| Long runs time out or stop midway | Background run took about 25 minutes for the audit | Results persist on disk; rerun the same phase; `--check` re-evaluates without running |

## What this plan does not cover (state before relying on it)
- No model-driven benchmark exists; quality of model behaviour on these skills across many projects is unmeasured. Until a benchmark of at least five repositories and five empty-folder prompts is run, the system stays labelled 0.2.0 beta.
- Android: the template scorer reads source; there is no rendered screenshot score for Compose yet.
- Windows, macOS and Linux CI run the validators and tests, not a full overhaul.
- Legal, tax and payments output is research and questions for professionals, not advice.

## Next improvements after one clean run, in order
1. Run the plan on a second, different repository (an app, not a site) to separate system faults from project quirks.
2. Build the benchmark set and publish the scores for template signature, copy slop and loop passes, before and after.
3. Add a rendered Android score (emulator or Compose preview screenshots) to the loop.
4. Replace the agent reviewer's swap test with the outside-people swap test as the default.
