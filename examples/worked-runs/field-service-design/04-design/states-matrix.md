# States matrix

Role: ux-designer (T-002). Every cell is specified, or n/a with reason. No cell is 'missing'.

| Screen / component | Initial | Loading | Empty | Populated | Error (validation) | Error (system) | Offline | Permission denied | Expired session | Success | Destructive confirmation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Today board (desktop) | specified | specified: skeleton rows per technician | specified: 'No jobs today' + New job | specified | n/a: no input | specified: banner 'Could not load, retry', last data shown greyed | specified: banner, read-only | specified: 'You need dispatcher access' | specified: re-login, return here | n/a | n/a |
| Today list (phone) | specified | specified: skeleton | specified | specified | n/a | specified | specified | specified | specified | n/a | n/a |
| Needs attention group | specified | specified | specified: 'Nothing needs attention' (positive) | specified | n/a | specified | specified | n/a | specified | n/a | n/a |
| Job detail (dispatcher) | specified | specified | n/a | specified | specified: inline on edits | specified | specified: actions disabled with reason | specified | specified | specified: assigned / rescheduled toast with undo | specified: Cancel job confirm |
| Technician picker | specified | specified | specified: 'No technician with this skill today' + show all | specified | n/a | specified: 'Not saved. Retry' keeps choice | specified: cannot assign offline, explain | n/a | specified | specified: undo 10 s | n/a |
| New job form | specified: phone field focused | n/a | n/a | specified | specified: field-level messages | specified: save failed, values kept | specified: save as draft locally | n/a | specified: draft kept | specified: job created | n/a |
| Jobs list | specified | specified | specified: 'No jobs match' + clear filters | specified | n/a | specified | specified: cached list, badge | specified | specified | n/a | n/a |
| Customer detail | specified | specified | specified: no history yet | specified | specified | specified | specified | specified | specified | specified: saved | specified: archive confirm |
| Technician detail | specified | specified | n/a | specified | specified | specified | specified | specified | specified | specified | specified: deactivate confirm |
| My jobs (technician) | specified | specified | specified: 'No jobs today' + contact dispatcher | specified | n/a | specified | specified: last list, queued badge | n/a | specified | n/a | n/a |
| Technician job detail | specified | specified | n/a | specified | specified: note length | specified | specified: actions queue with badge | specified: 'Not your job' | specified | specified: started / completed with undo | specified: none (no destructive action) |
| Done list (technician) | specified | specified | specified: 'Nothing completed yet today' | specified | n/a | specified | specified | n/a | specified | n/a | n/a |
| Profile / language | specified | n/a | n/a | specified | n/a | specified | specified: language change works offline | n/a | specified | specified: language changed | n/a |
| Login | specified | specified | n/a | specified | specified: wrong code | specified | specified: cannot log in offline, explain | n/a | n/a | specified | n/a |
