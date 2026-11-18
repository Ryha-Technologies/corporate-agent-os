## What this changes
<One paragraph. Link the issue.>

## Layer(s) touched
- [ ] core  - [ ] skills  - [ ] agents  - [ ] departments  - [ ] workflows  - [ ] adapters / power  - [ ] standards / templates  - [ ] evaluations  - [ ] scripts / tests  - [ ] docs

## Checks actually run (paste output)
```
python scripts/validate/run_all.py
python -m pytest -q
```
- [ ] Generated files regenerated (`build_adapters.py`, `build_power.py`, `render_roles.py`) — no hand edits to generated files
- [ ] Regression case added or updated if a failure mode was addressed
- [ ] CHANGELOG entry added
- [ ] Platform claims cite `research/source-register.md` with an access date
- [ ] No placeholders, secrets, fabricated results or quality labels without evidence

## Needs a second reviewer?
- [ ] Yes — this touches orchestrator policy, permissions, agent tools/scopes, gates, installer or destructive actions
