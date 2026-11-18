# User flows

Role: ux-designer (T-002). Each flow lists entry points, steps, decisions, exits, errors and recovery. Text diagrams; `→` is a step, `?` a decision.

## D1 — Assign a job (dispatcher)
Entry: Today board/list, an unassigned job; or Job detail.
1. Open job (or tap its "Assign" chip) → 2. Technician picker shows technicians sorted by availability with today's load ("3 jobs, free from 14:00") and skill match → 3. ? technician has conflicting job in the window → warn "overlaps with Job #… at 14:00", allow or pick another → 4. Confirm → 5. Job status = assigned; technician notified; board updates.
Errors: network failure on confirm → "Not saved. Retry" with the choice preserved (no silent loss). Recovery: undo assignment within the toast for 10 s; later via Reassign.
Exit: board shows the job under the technician.

## D2 — Create a job from a call (dispatcher, phone)
Entry: New job (global).
1. Phone number field first → ? known customer → prefill name and last address; else new customer → 2. Service type (chips) → 3. Address (prefilled or new) → 4. Scheduled window (today / tomorrow / pick; slot chips) → 5. Optional: assign now (D1 picker) → 6. Save.
Errors: missing required field → inline message naming the field; duplicate job for same customer and window → warn with link. Recovery: form keeps values on error; draft kept if the app is backgrounded (phone call interrupts, A-001).
Exit: job detail with "Assign" prominent if unassigned.

## D3 — Spot and fix an overdue or unconfirmed job (dispatcher)
Entry: Today shows "Needs attention" group at top (overdue, unconfirmed, technician not moving).
1. Open item → 2. See reason and technician → 3. Actions: call technician, reassign (D1), reschedule, mark no-answer.
Errors: none specific. Recovery: each action is confirmable and undoable except call.

## T1 — Work through today's jobs (technician)
Entry: My jobs (default screen). Jobs ordered by window; the next job is visually first and larger.
1. Tap job → 2. Detail: customer first name, address, window, service, notes; buttons: Call, Navigate, Start → 3. Start → status "started"; Complete becomes primary → 4. Complete → ? add note or photo (optional) → done; next job surfaces.
Errors: offline → actions queue locally with "Will send when online" badge; conflicts resolved server-side by latest timestamp with dispatcher notified. Recovery: undo Complete for 10 minutes.
Exit: Done list shows the job.

## T2 — Customer not reachable (technician)
Entry: Technician job detail.
1. Tap "Customer not answering" → 2. Choose: wait 10 min / move to next / notify dispatcher → 3. Status "no-answer"; dispatcher's Needs attention updates.

## T3 — Change language (technician)
Entry: Profile → Language → choose → UI re-renders; labels never truncate (A-007; verified in design QA with longest strings).

## Permission boundaries
Technicians see only their jobs and customer first name, address and phone (phone only inside the job). Dispatchers see all. Owners manage settings. Expired session → re-login returns to the same screen with queued actions intact.
