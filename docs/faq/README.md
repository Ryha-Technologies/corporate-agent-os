# FAQ

**Does this replace a company or a professional team?**
No. It models how a well-run team divides work and checks it, so a model can follow that discipline. Research, legal, financial and security conclusions still need qualified humans; the system is built to route those questions to them.

**Why is the version 0.2.0 and not 1.0.0?**
Because no model-driven benchmark run exists for this build and platform formats are still moving. The repository's own validators and tests pass; the behaviour of a model following these skills on real tasks is unmeasured. 1.0.0 would claim stability we cannot show.

**Which parts are actual software?**
`scripts/` (validators, installer, builders), `tests/`, the schemas in `core/` and `evaluations/run_evals.py`. Everything else is instruction and specification for a model to follow.

**Can I use only a few skills?**
Yes. `install.py --skills a,b,c` installs a subset. Skills reference each other by path for context but each is self-contained enough to run alone.

**Can I add my own departments or agents?**
Yes. Edit `departments/*/roles.yaml` and `agents/**/*.yaml`, run the validators, rebuild adapters and the Power, reinstall.

**Why do reviewers have no write tool?**
So a reviewer cannot quietly fix the thing it is judging. Findings go back to the owner as a rework task.

**Why does the orchestrator refuse to say "production-ready"?**
Because the label requires every gate to be PASS with no critical findings open. Until then it is a claim without evidence.

**What happens on a host without sub-agents (Codex)?**
The same roles run one at a time as sequential passes and the report says so. Independence comes from running the reviewer role in a fresh session.

**Is the trademark screening legal clearance?**
No. It is preliminary screening with explicit statuses and limitations; the skill tells you to engage counsel in each target jurisdiction before commercial use.

**Can the agents deploy, publish or spend?**
Not without a recorded human approval. The permission policy lists those actions, every adapter instructs agents to pause, and Kiro agents carry deny rules for destructive shell patterns.

**Where do I report a problem?**
Validator or script defects: open an issue with the command and output. Behaviour defects: attach the transcript and add it as a regression case. Security issues: see `SECURITY.md`.
