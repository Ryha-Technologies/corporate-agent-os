# Wireframes (low fidelity, text)

Role: ux-designer (T-003). Regions listed top to bottom. One primary action per screen. Widths: phone 360 px, desktop 1280 px. These are structural specifications; no rendering exists yet.

## W1 — Today board (desktop ≥ 1024)
```
[Left rail: Today · Jobs · Customers · Technicians · Settings]   [Header: date, search, NEW JOB (primary)]
[Needs attention strip: 3 overdue · 2 unconfirmed  → opens list]
[Board: rows = technicians (name, load "4 jobs"); columns = hours 08–20; job blocks show customer first name, service, status colour + text]
[Unassigned lane at top of board]
```
States covered: initial, loading (skeleton rows), empty, populated, system error (banner), offline (read-only banner), permission denied.

## W2 — Today list (phone dispatcher, 360)
```
[Header: Today ▾ | search]
[Needs attention card (collapsed count, tap to expand)]
[Group: Unassigned — job rows: time · customer · service · [Assign]]
[Group: per technician — name, load; job rows with status chip + text]
[Bottom tabs: Today · Jobs · (+ New job, primary, centre) · More]
```

## W3 — Technician picker (sheet)
```
[Title: Assign "Customer F., AC repair, 14:00–16:00"]
[List: technician rows — name · skill match ✓ · "3 jobs, free from 13:30" · conflict warning if any]
[CONFIRM (primary, disabled until selection)]
```

## W4 — New job (phone)
```
[Header: New job · Cancel]
[Phone number (focused, numeric)] → known customer banner with prefilled name/address
[Service type chips]  [Address]  [Window: Today | Tomorrow | Pick; slot chips]
[Assign now (optional, opens W3)]  [Notes]
[SAVE JOB (primary, sticky bottom)]
```

## W5 — My jobs (technician, 360)
```
[Header: Today, name, offline badge if any]
[Next job card (large): time window · customer first name · area · service · [OPEN]]
[Later today: compact rows]
[Bottom tabs: My jobs · Done · Profile]
```

## W6 — Technician job detail
```
[Header: ← Job · status chip + text]
[Customer first name · address (tap to navigate) · window · service · notes from dispatcher]
[Row: CALL (secondary) · NAVIGATE (secondary)]
[START (primary) → after start: COMPLETE (primary) ; "Customer not answering" (tertiary)]
[Photos / note (after start)]
[Queued badge when offline]
```

Checks: every screen fits 360 px without horizontal scroll (structural); every primary action is in thumb reach on phone (bottom third); icons always paired with text.
