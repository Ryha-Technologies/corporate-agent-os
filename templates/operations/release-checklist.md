# Release checklist

Filled by: devops-engineer. No production action without the final human approval line completed.

- [ ] Build provenance recorded (commit, artefact hash, pipeline run)
- [ ] All tests passed or failures disclosed with accepted-risk record
- [ ] Migration dry-run completed on realistic data; reversible
- [ ] Changelog and release notes written and verified
- [ ] Configuration and secrets reviewed; no secrets in artefacts
- [ ] Monitoring dashboards and alerts in place with owners
- [ ] Rollback procedure tested in staging
- [ ] Backup taken; restore tested (date, result)
- [ ] Support playbook and known issues published
- [ ] Privacy and legal gate verdicts attached
- [ ] Staged rollout plan with checkpoints and kill switch
- [ ] Human production approval: name, role, date, scope
