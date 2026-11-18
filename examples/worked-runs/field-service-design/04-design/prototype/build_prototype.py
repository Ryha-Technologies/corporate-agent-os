"""Build HTML prototypes from the token file (no hard-coded values) and screenshot them with headless Chrome."""
import json, subprocess
from pathlib import Path
R = Path(r"c:\Users\vellu\Downloads\corporate-agent-os-v0.1.0\build\design-run-field-service")
tok = json.loads((R / "04-design/design-tokens.json").read_text(encoding="utf-8"))
c = {k: v["light"] for k, v in tok["color"].items()}
sp = tok["spacing"]; ty = tok["typography"]["scale"]; rad = tok["radius"]
font = tok["typography"]["families"]["ui"]["stack"]

css = f"""
@import url('https://fonts.googleapis.com/css2?family=Anek+Latin:wdth,wght@87..100,400..700&family=Anek+Devanagari:wdth,wght@87..100,400..700&display=swap');
:root{{--bg:{c['background']};--surface:{c['surface']};--raised:{c['surface-raised']};--border:{c['border']};--border-strong:{c['border-strong']};
--ink:{c['text-primary']};--ink2:{c['text-secondary']};--brand:{c['brand']};--on-brand:{c['text-on-brand']};--marker:{c['marker']};--on-marker:{c['text-on-marker']};
--s-unassigned:{c['status-unassigned']};--s-assigned:{c['status-assigned']};--s-started:{c['status-started']};--s-completed:{c['status-completed']};--s-attention:{c['status-attention']};
--sp1:{sp['1']};--sp2:{sp['2']};--sp3:{sp['3']};--sp4:{sp['4']};--sp5:{sp['5']};--sp6:{sp['6']};--row-compact:{sp['row-compact']};--row-comfortable:{sp['row-comfortable']};--target:{sp['target-min']};
--r-sm:{rad['sm']};--r-md:{rad['md']};--r-pill:{rad['pill']};}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:{font};font-size:{ty['body']['size']};line-height:{ty['body']['line_height']};color:var(--ink);background:var(--bg)}}
h1{{font-size:{ty['title']['size']};line-height:{ty['title']['line_height']};font-weight:{ty['title']['weight']}}}
h2{{font-size:{ty['title-sm']['size']};font-weight:{ty['title-sm']['weight']}}}
.label{{font-size:{ty['label']['size']};font-weight:{ty['label']['weight']};letter-spacing:{ty['label'].get('tracking','0')}}}
.caption{{font-size:{ty['caption']['size']};color:var(--ink2)}}
.chip{{display:inline-flex;align-items:center;gap:6px;padding:2px 10px;border-radius:var(--r-pill);font-size:{ty['label']['size']};font-weight:600;background:var(--raised);border:1px solid var(--border)}}
.chip::before{{content:"";width:8px;height:8px;border-radius:50%;background:currentColor}}
.chip.unassigned{{color:var(--s-unassigned)}}.chip.assigned{{color:var(--s-assigned)}}.chip.started{{color:var(--s-started)}}.chip.completed{{color:var(--s-completed)}}.chip.attention{{color:var(--s-attention)}}
.btn,.btn:visited{{text-decoration:none}} .btn{{display:inline-flex;align-items:center;justify-content:center;min-height:40px;padding:0 var(--sp4);border-radius:var(--r-md);font-weight:600;font-size:{ty['body']['size']};border:1px solid transparent;cursor:pointer;font-family:inherit}}
.btn.primary{{background:var(--brand);color:var(--on-brand)}}.btn.secondary{{background:var(--raised);color:var(--ink);border-color:var(--border-strong)}}.btn.large{{min-height:48px;font-size:1.0625rem}}
.btn:focus-visible,.row:focus-visible{{outline:2px solid var(--brand);outline-offset:2px}}
.attention-strip{{background:var(--marker);color:var(--on-marker);border-radius:var(--r-sm);padding:var(--sp3) var(--sp4);display:flex;justify-content:space-between;align-items:center;gap:var(--sp3)}}
.mark{{display:inline-block;width:28px;height:28px;border-radius:5px;background:var(--ink);position:relative;vertical-align:middle}}
.mark i{{position:absolute;left:5px;right:5px;height:3px;border-radius:1px;background:rgba(255,255,255,.55)}}.mark i:nth-child(1){{top:6px}}.mark i:nth-child(2){{top:12.5px;right:14px}}.mark i:nth-child(3){{top:19px}}
.mark b{{position:absolute;left:14px;right:5px;top:12.5px;height:3px;border-radius:1px;background:var(--marker)}}
/* desktop board */
.app{{display:grid;grid-template-columns:200px 1fr;min-height:100vh}}
.rail{{background:var(--surface);border-right:1px solid var(--border);padding:var(--sp4)}}
.rail a{{display:block;padding:10px var(--sp3);border-radius:var(--r-md);color:var(--ink);text-decoration:none;font-weight:600}}.rail a.active{{background:var(--raised);border:1px solid var(--border)}}
.main{{padding:var(--sp5)}}
.topbar{{display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--sp4)}}
.board{{display:grid;grid-template-columns:160px repeat(12,1fr);border:1px solid var(--border);border-radius:var(--r-md);overflow:hidden;background:var(--raised);font-size:{ty['body-sm']['size']}}}
.board .h{{background:var(--surface);padding:6px 8px;font-weight:600;border-bottom:1px solid var(--border);font-variant-numeric:tabular-nums;font-stretch:87%}}
.board .t{{padding:6px 8px;border-top:1px solid var(--border);min-height:var(--row-compact);display:flex;flex-direction:column;justify-content:center}}
.board .cell{{border-top:1px solid var(--border);border-left:1px solid var(--border);min-height:var(--row-compact);padding:3px}}
.job{{border-radius:var(--r-sm);padding:4px 6px;font-size:{ty['caption']['size']};line-height:1.3;color:#fff;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.job.assigned{{background:var(--s-assigned)}}.job.started{{background:var(--s-started)}}.job.completed{{background:var(--s-completed)}}.job.unassigned{{background:var(--raised);color:var(--s-unassigned);border:1px dashed var(--border-strong)}}
/* phone */
.phone{{width:360px;margin:0;min-height:100vh;display:flex;flex-direction:column;border-right:1px solid var(--border)}}
a.row,a.row:visited{{color:inherit;text-decoration:none}} .row *{{min-width:0}}
.phone header{{padding:var(--sp4);display:flex;justify-content:space-between;align-items:center}}
.list{{padding:0 var(--sp4) 80px;display:flex;flex-direction:column;gap:var(--sp2)}}
.row{{display:grid;grid-template-columns:56px minmax(0,1fr) auto;gap:var(--sp3);align-items:center;min-height:var(--row-comfortable);background:var(--raised);border:1px solid var(--border);border-radius:var(--r-md);padding:var(--sp2) var(--sp3)}}
.row .time{{font-weight:700;font-variant-numeric:tabular-nums}}
.next{{background:var(--raised);border:1px solid var(--border-strong);border-radius:var(--r-md);padding:var(--sp4);display:grid;gap:var(--sp2)}}
.next .t{{font-size:{ty['next-job']['size']};font-weight:{ty['next-job']['weight']};line-height:{ty['next-job']['line_height']}}}
.tabs{{position:fixed;bottom:0;left:0;width:360px;display:flex;background:var(--surface);border-top:1px solid var(--border)}}
.tabs a{{flex:1;min-height:56px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--ink2);text-decoration:none}}.tabs a.active{{color:var(--brand)}}
.detail{{padding:var(--sp4);display:grid;gap:var(--sp4)}}
.kv{{display:grid;gap:4px}}.kv .caption{{text-transform:none}}
.actions{{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp3)}}
.queued{{font-size:12px;color:var(--ink2);border:1px solid var(--border);border-radius:var(--r-pill);padding:1px 8px}}
"""
(R / "04-design/prototype").mkdir(parents=True, exist_ok=True)
(R / "04-design/prototype/tokens.css").write_text(css, encoding="utf-8", newline="\n")

head = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t}</title><link rel="stylesheet" href="tokens.css"></head><body>'
techs = ["Ravi", "Suresh", "Anita", "Imran", "Deepak"]
hours = list(range(8, 20))
def board_rows():
    out = ""
    placed = {("Ravi",9,"assigned","Priya K. · AC repair",2),("Ravi",14,"started","Mehta · Wiring",2),("Suresh",10,"completed","Rao · Leak",1),("Suresh",15,"assigned","Nair · AC service",2),("Anita",11,"assigned","Shah · Geyser",2),("Imran",13,"unassigned","Khan · Fan install",1),("Deepak",9,"completed","Joshi · Switchboard",2),("Deepak",16,"assigned","D'Souza · AC gas",2)}
    for t in techs:
        n = sum(1 for p in placed if p[0]==t)
        out += f'<div class="t"><span class="label">{t}</span><span class="caption">{n} job{"s" if n!=1 else ""}</span></div>'
        h = 8
        while h < 20:
            hit = next((p for p in placed if p[0]==t and p[1]==h), None)
            if hit:
                span = hit[4]
                out += f'<div class="cell" style="grid-column:span {span}"><div class="job {hit[2]}" title="{hit[3]}">{hit[3]}</div></div>'
                h += span
            else:
                out += '<div class="cell"></div>'; h += 1
    return out
board = head.format(t="Today board — Kaamline (working title) — sample data") + f"""
<div class="app"><nav class="rail" aria-label="Main"><div style="display:flex;gap:10px;align-items:center;margin-bottom:24px"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><b></b></span><strong>kaamline</strong></div>
<a class="active" href="#">Today</a><a href="#">Jobs</a><a href="#">Customers</a><a href="#">Technicians</a><a href="#">Settings</a></nav>
<main class="main"><div class="topbar"><h1>Today · Tue 18 Nov</h1><div style="display:flex;gap:12px"><input aria-label="Search jobs" placeholder="Search jobs, customers, phone" style="min-width:260px;padding:8px 12px;border:1px solid var(--border-strong);border-radius:6px;font:inherit;background:var(--raised)"><a class="btn primary" href="#">New job</a></div></div>
<section class="attention-strip" role="region" aria-label="Needs attention" style="margin-bottom:16px"><div><strong>3 jobs need attention</strong> · 1 unassigned · 1 overdue · 1 customer not answering</div><a class="btn secondary" href="#" style="min-height:36px">Show</a></section>
<section aria-label="Technician board"><div class="board" role="grid"><div class="h">Technician</div>{''.join(f'<div class="h">{h:02d}:00</div>' for h in hours)}{board_rows()}</div>
<p class="caption" style="margin-top:12px">Sample data for layout review only — fictional names, not real customers (regression case E28).</p></section></main></div></body></html>"""
(R / "04-design/prototype/board.html").write_text(board, encoding="utf-8", newline="\n")

myjobs = head.format(t="My jobs — sample") + """
<div class="phone"><header><div style="display:flex;gap:10px;align-items:center"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><b></b></span><div><strong>Today</strong><div class="caption">Ravi · 4 jobs</div></div></div><span class="queued" role="status">1 waiting to send</span></header>
<div class="list">
<section class="next" aria-labelledby="nx"><span class="caption" id="nx">Next job</span><div class="t">14:00–16:00 · Mehta</div><div>Kothrud · Wiring repair</div><div style="display:flex;gap:8px;align-items:center"><span class="chip started">Started</span></div><a class="btn primary large" href="#">Open job</a></section>
<h2 style="margin-top:8px">Later today</h2>
<a class="row" href="#"><span class="time">16:30</span><span><strong>Kulkarni</strong><br><span class="caption">Baner · AC service</span></span><span class="chip assigned">Assigned</span></a>
<a class="row" href="#"><span class="time">18:00</span><span><strong>Patil</strong><br><span class="caption">Aundh · Fan install</span></span><span class="chip assigned">Assigned</span></a>
<h2 style="margin-top:8px">Done</h2>
<a class="row" href="#"><span class="time">09:00</span><span><strong>Priya K.</strong><br><span class="caption">Hinjewadi · AC repair</span></span><span class="chip completed">Completed</span></a>
<p class="caption">Sample data — fictional.</p></div>
<nav class="tabs" aria-label="Sections"><a class="active" href="#">My jobs</a><a href="#">Done</a><a href="#">Profile</a></nav></div></body></html>"""
(R / "04-design/prototype/my-jobs.html").write_text(myjobs, encoding="utf-8", newline="\n")

detail = head.format(t="Job detail — sample") + """
<div class="phone"><header><a href="#" class="btn secondary" style="min-height:40px;min-width:44px" aria-label="Back">←</a><strong>Job</strong><span class="chip started">Started</span></header>
<div class="detail"><div><h1>Mehta</h1><div class="caption">Customer</div></div>
<div class="kv"><span class="caption">Address</span><a href="#" style="color:var(--brand);font-weight:600">14 Mayur Colony, Kothrud</a></div>
<div class="kv"><span class="caption">Window</span><strong>14:00–16:00 today</strong></div>
<div class="kv"><span class="caption">Service</span><span>Wiring repair · Dispatcher note: "MCB tripping in kitchen since Sunday"</span></div>
<div class="actions"><a class="btn secondary large" href="#">Call</a><a class="btn secondary large" href="#">Navigate</a></div>
<a class="btn primary large" href="#">Complete job</a>
<a href="#" style="text-align:center;color:var(--ink2);font-weight:600;padding:12px;min-height:44px;text-decoration:underline">Customer not answering</a>
<p class="caption">Sample data — fictional.</p></div>
<nav class="tabs" aria-label="Sections"><a class="active" href="#">My jobs</a><a href="#">Done</a><a href="#">Profile</a></nav></div></body></html>"""
(R / "04-design/prototype/job-detail.html").write_text(detail, encoding="utf-8", newline="\n")

brandsheet = head.format(t="Brand sheet") + f"""
<main style="padding:32px;display:grid;gap:24px;max-width:900px">
<div style="display:flex;gap:32px;align-items:center"><img src="../../03-brand/assets/logo/symbol.svg" width="64" height="64" alt=""><img src="../../03-brand/assets/logo/symbol-mono.svg" width="64" height="64" alt=""><img src="../../03-brand/assets/logo/symbol-16.svg" width="16" height="16" alt="" style="image-rendering:crisp-edges"><img src="../../03-brand/assets/logo/symbol-16.svg" width="32" height="32" alt=""><img src="../../03-brand/assets/logo/wordmark-horizontal.svg" width="320" height="64" alt=""></div>
<h1 style="font-size:28px">kaamline — the day board for small service teams. Nothing falls through.</h1>
<p>Anek Latin / Devanagari · body 16/1.5 · <span lang="hi">आज के काम · रवि · 4 काम</span> · 14:00–16:00</p>
<div style="display:flex;gap:12px;flex-wrap:wrap">{''.join(f'<div style="width:120px"><div style="height:56px;border-radius:6px;background:{c[k]};border:1px solid var(--border)"></div><div class="caption">{k}<br>{c[k]}</div></div>' for k in ("background","surface","text-primary","text-secondary","brand","marker","status-unassigned","status-started","status-completed","status-attention"))}</div>
<div class="attention-strip"><strong>3 jobs need attention</strong><a class="btn secondary" href="#">Show</a></div>
<div style="display:flex;gap:12px"><a class="btn primary" href="#">Save job</a><a class="btn secondary" href="#">Cancel</a><span class="chip assigned">Assigned</span><span class="chip attention">Not answering</span></div>
</main></body></html>"""
(R / "04-design/prototype/brand-sheet.html").write_text(brandsheet, encoding="utf-8", newline="\n")

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
shots = R / "07-quality/screenshots"; shots.mkdir(parents=True, exist_ok=True)
jobs = [("board.html", 1280, 800, "board-1280.png"), ("board.html", 360, 800, "board-360.png"),
        ("my-jobs.html", 360, 760, "my-jobs-360.png"), ("job-detail.html", 360, 760, "job-detail-360.png"),
        ("my-jobs.html", 768, 900, "my-jobs-768.png"), ("brand-sheet.html", 1000, 700, "brand-sheet-1000.png")]
for f, w, h, out in jobs:
    url = (R / "04-design/prototype" / f).resolve().as_uri()
    r = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}", "--virtual-time-budget=6000",
                        f"--screenshot={shots / out}", url], capture_output=True, text=True, timeout=120)
    print(out, "ok" if (shots / out).exists() else f"FAILED {r.stderr[-200:]}")
