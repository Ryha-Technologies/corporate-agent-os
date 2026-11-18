# Engineering rubric

| Dimension | 0 | 1 | 2 | 3 | Evidence to cite |
|---|---|---|---|---|---|
| Architecture fit | Complexity without requirement | Some justification | Simplest option with ADRs | Simplest option, ADRs, failure modes, cost model, threat model | Architecture, ADRs |
| Contracts and data | None | Partial | Auth, errors, idempotency defined | Full contract, constraints, justified indexes, reversible migrations | API contract, data model |
| Code quality | Does not build | Builds, poor structure | Clean, within scope | Clean, scoped, secure defaults, documented | Code review findings |
| Tests | None | Happy path | Negative and boundary | All layers appropriate, honest results, traceability complete | Test report, matrix |
| Verification honesty | Claims without runs | Partial commands | Commands and output recorded | Commands, output, NOT_RUN disclosed, reviewer re-ran | CHECKS_ACTUALLY_RUN |
| Dependencies | Unknown licences | Partial register | Register complete | Register with use-mode obligations, scans, provenance | Component register |
| Documentation | Absent or wrong | Describes intent | Matches behaviour | Matches behaviour, commands executed, limitations listed | Documentation audit |
