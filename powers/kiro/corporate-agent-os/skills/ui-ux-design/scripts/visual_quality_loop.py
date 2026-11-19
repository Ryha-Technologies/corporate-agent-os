"""Visual quality loop: render, screenshot, measure, score 0-100, and decide whether another pass is needed.

The score is of the *rendered* page, not the code. It combines the measurable half of quality (what a
script can see: template signature, overflow, contrast, targets, type and spacing discipline, motion
presence and restraint, states, performance proxies) with a slot for the human-judged half (swap test,
psychology fit, copy specificity) that a reviewer fills in from the screenshots the script produces.

Usage:
    python visual_quality_loop.py <url-or-html-file> [--out evidence/pass-01] [--target 90]
                                  [--reviewer-json review.json] [--widths 360,768,1280]

Outputs in --out: <name>-<width>.png screenshots, measurements.json, score.md (per-criterion table).
Exit code 0 when score >= target, else 1 (another pass is needed).

Loop protocol (used by ui-ux-design Phase 4 and product-overhaul-orchestrator):
  pass N: build -> run this script -> read score.md and LOOK at the screenshots -> fix the lowest
  criteria -> pass N+1. Stop when score >= target for two consecutive passes with the reviewer slot
  filled by someone who did not make the design, or when two passes produce no change (then escalate).
  100 means every measured criterion is at its ceiling and the reviewer awarded full marks; it is rare
  and the script never reports it from measurements alone.

Reviewer JSON (optional):
  {"swap_test": 0-10, "psychology": 0-10, "copy_specificity": 0-5, "notes": "..."}
If absent, those 25 points are reported as NOT_RUN and the maximum achievable score is 75.
"""
from __future__ import annotations
import json, os, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.dont_write_bytecode = True  # keep skills/ free of __pycache__ (the Power validator compares trees)
sys.path.insert(0, str(HERE))
import template_signature as ts  # noqa: E402

MEASURE_JS = r"""
(() => {
  const cs = e => getComputedStyle(e);
  const all = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
  const vw = document.documentElement.clientWidth;
  const lum = c => { const m = c.match(/\d+(\.\d+)?/g); if (!m) return null; const [r,g,b] = m.slice(0,3).map(Number).map(v => { v/=255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); }); return 0.2126*r+0.7152*g+0.0722*b; };
  const bgOf = e => { let n = e; while (n && n !== document.documentElement) { const b = cs(n).backgroundColor; if (b && b !== 'rgba(0, 0, 0, 0)' && b !== 'transparent') return b; n = n.parentElement; } return cs(document.body).backgroundColor || 'rgb(255, 255, 255)'; };
  const texts = all.filter(e => e.children.length === 0 && e.innerText && e.innerText.trim().length > 1);
  let minContrast = 21, failing = 0;
  texts.forEach(e => { const l1 = lum(cs(e).color), l2 = lum(bgOf(e)); if (l1 === null || l2 === null) return; const c = (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05); const large = parseFloat(cs(e).fontSize) >= 24 || (parseFloat(cs(e).fontSize) >= 18.66 && parseInt(cs(e).fontWeight) >= 700); if (c < (large ? 3 : 4.5)) failing++; minContrast = Math.min(minContrast, c); });
  const inter = all.filter(e => ['A','BUTTON','INPUT','SELECT','TEXTAREA'].includes(e.tagName) || e.getAttribute('role') === 'button');
  const targets = inter.map(e => { const r = e.getBoundingClientRect(); return Math.min(r.width, r.height); }).filter(x => x > 0);
  const smallTargets = targets.filter(t => t < 24).length;
  const sizes = new Set(), pads = new Set(), gaps = new Set();
  texts.forEach(e => sizes.add(cs(e).fontSize));
  all.forEach(e => { const s = cs(e); [s.paddingTop, s.paddingBottom, s.marginTop, s.marginBottom, s.gap].forEach(v => { if (v && v !== '0px' && v !== 'normal') pads.add(v); }); });
  const h1 = document.querySelector('h1');
  const ctas = all.filter(e => /btn|button|cta/i.test(e.className || '') && e.getBoundingClientRect().top < 900);
  const primary = ctas.filter(e => { const s = cs(e); return s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== bgOf(e.parentElement); });
  const focusable = inter.filter(e => e.tabIndex >= 0).length;
  const imgsNoAlt = [...document.images].filter(i => !i.hasAttribute('alt')).length;
  const unlabeled = [...document.querySelectorAll('input,select,textarea')].filter(i => !i.labels?.length && !i.getAttribute('aria-label') && !i.getAttribute('aria-labelledby')).length;
  const landmarks = ['main','nav','header','footer'].filter(t => document.querySelector(t)).length;
  const reduced = [...document.styleSheets].some(s => { try { return [...s.cssRules].some(r => r.media && /prefers-reduced-motion/.test(r.media.mediaText)); } catch (e) { return false; } });
  const anim = all.filter(e => cs(e).animationName !== 'none').length;
  const trans = all.filter(e => cs(e).transitionDuration !== '0s' && cs(e).transitionDuration !== '').length;
  const longest = Math.max(0, ...[...document.querySelectorAll('p,li')].map(p => Math.round(p.getBoundingClientRect().width / (parseFloat(cs(p).fontSize) * 0.5))));
  const consoleErrors = window.__errs ? window.__errs.length : null;
  return { vw, scrollWidth: document.documentElement.scrollWidth, minContrast: +minContrast.toFixed(2), contrastFailures: failing, textNodes: texts.length,
    interactive: inter.length, smallTargets, smallestTarget: targets.length ? Math.min(...targets) : null,
    fontSizes: sizes.size, spacingValues: pads.size, h1Count: document.querySelectorAll('h1').length, hasH1: !!h1,
    ctasAboveFold: ctas.length, primaryCtasAboveFold: primary.length, focusable, imgsNoAlt, unlabeledInputs: unlabeled, landmarks,
    reducedMotionRule: reduced, animated: anim, transitions: trans, longestLine: longest, bytes: document.documentElement.outerHTML.length };
})()
"""

def render(target: str, width: int, out_png: pathlib.Path, chrome: str) -> dict | None:
    """Screenshot at the true width (iframe trick below 500 px) and return measurements for that width."""
    is_url = re.match(r"^https?://", target) is not None
    src = pathlib.Path(target).resolve() if not is_url else None
    html = src.read_text(encoding="utf-8", errors="replace") if src else None
    inject = f'<script>window.__errs=[];window.addEventListener("error",e=>window.__errs.push(String(e.message)));window.addEventListener("load",()=>{{const o={MEASURE_JS};const p=document.createElement("pre");p.id="__VQ__";p.style.display="none";p.textContent=JSON.stringify(o);document.body.appendChild(p);}});</script>'
    tmp = None
    if html is not None:
        tmp = src.with_name(f"_vq_{src.name}")
        tmp.write_text(html.replace("</body>", inject + "</body>") if "</body>" in html else html + inject, encoding="utf-8")
        page_url = tmp.as_uri()
    else:
        page_url = target
    host = None
    shot_url = page_url
    if width < 500:
        host = (src.parent if src else pathlib.Path.cwd()) / f"_vq_host_{width}.html"
        host.write_text(f'<!doctype html><html><body style="margin:0"><iframe id="f" src="{page_url}" style="width:{width}px;height:1200px;border:0;display:block"></iframe></body></html>', encoding="utf-8")
        shot_url = host.as_uri()
    try:
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                        f"--window-size={max(width, 500)},1200", "--virtual-time-budget=4000", f"--screenshot={out_png}", shot_url],
                       capture_output=True, text=True, timeout=120)
        dom = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                              f"--window-size={max(width, 500)},1200", "--virtual-time-budget=4000", "--dump-dom", page_url],
                             capture_output=True, text=True, encoding="utf-8", timeout=120).stdout
    finally:
        for f in (tmp, host):
            if f and f.exists():
                f.unlink()
    if width < 500 and out_png.exists():
        try:
            from PIL import Image
            im = Image.open(out_png); im.crop((0, 0, width, im.height)).save(out_png)
        except Exception:
            pass
    m = re.search(r'<pre id="__VQ__"[^>]*>(.*?)</pre>', dom, re.S)
    if not m:
        return None
    txt = m.group(1).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"')
    return json.loads(txt)

def score(meas: dict[int, dict], tsig: dict, reviewer: dict | None) -> tuple[int, int, list[tuple[str, int, int, str]]]:
    rows: list[tuple[str, int, int, str]] = []  # criterion, points, max, evidence
    def add(name, pts, mx, why): rows.append((name, max(0, min(mx, round(pts))), mx, why))
    # 1 Template signature (20): 0 at >=60, 20 at <=10
    s = tsig["score"]; add("Template signature (distinct from the category centre)", 20 * (60 - s) / 50 if s < 60 else 0, 20, f"template_signature {s}/100 -> {tsig['verdict']}; " + "; ".join(r.strip() for r in tsig["reasons"][:4]))
    # 2 Overflow (8)
    ov = [w for w, m in meas.items() if m and m["scrollWidth"] > m["vw"] + 1]
    add("No horizontal overflow at any width", 8 if not ov else 0, 8, f"overflow at {ov}" if ov else "none at " + ",".join(map(str, meas)))
    # 3 Contrast (10)
    m1280 = meas.get(1280) or next(iter(meas.values()))
    cf = m1280["contrastFailures"]; add("Text contrast (WCAG AA)", 10 if cf == 0 else max(0, 10 - 2 * cf), 10, f"{cf} failing text nodes, min ratio {m1280['minContrast']}")
    # 4 Targets (6)
    st = min(m["smallTargets"] for m in meas.values() if m); add("Interactive targets >= 24 px", 6 if st == 0 else max(0, 6 - st), 6, f"{st} targets under 24 px; smallest {m1280['smallestTarget']} px")
    # 5 Type discipline (7)
    fs = m1280["fontSizes"]; add("Type scale (<= 6 sizes)", 7 if fs <= 6 else max(0, 7 - (fs - 6)), 7, f"{fs} distinct font sizes; longest line {m1280['longestLine']} chars")
    # 6 Spacing discipline (5)
    sp = m1280["spacingValues"]; add("Spacing scale (<= 8 values)", 5 if sp <= 8 else max(0, 5 - (sp - 8) // 2), 5, f"{sp} distinct spacing values")
    # 7 Hierarchy (6): one h1, one primary CTA above fold
    h = 3 if m1280["h1Count"] == 1 else 0; p = 3 if m1280["primaryCtasAboveFold"] == 1 else (1 if m1280["primaryCtasAboveFold"] in (0, 2) else 0)
    add("Hierarchy: one h1, one primary action above the fold", h + p, 6, f"h1={m1280['h1Count']}, primary CTAs above fold={m1280['primaryCtasAboveFold']}, all CTAs={m1280['ctasAboveFold']}")
    # 8 Motion (7): present but restrained, reduced-motion honoured
    an = m1280["animated"] + m1280["transitions"]; mo = 0
    if an == 0: mo = 2; why = "no motion or feedback states"
    elif an > 40: mo = 2; why = f"{an} animated/transitioning elements (decorative)"
    else: mo = 5; why = f"{an} animated/transitioning elements"
    if m1280["reducedMotionRule"]: mo += 2; why += "; prefers-reduced-motion rule present"
    else: why += "; no prefers-reduced-motion rule"
    add("Motion: purposeful, restrained, reduced-motion honoured", mo, 7, why)
    # 9 Semantics (6)
    sem = 0; sem += 2 if m1280["landmarks"] >= 3 else 0; sem += 2 if m1280["imgsNoAlt"] == 0 else 0; sem += 2 if m1280["unlabeledInputs"] == 0 else 0
    add("Semantics: landmarks, alt text, labelled inputs", sem, 6, f"landmarks={m1280['landmarks']}, imgs without alt={m1280['imgsNoAlt']}, unlabeled inputs={m1280['unlabeledInputs']}")
    measured_total = sum(r[1] for r in rows); measured_max = sum(r[2] for r in rows)  # 75
    # Reviewer slot (25)
    if reviewer:
        add("Reviewer: swap test (could a stranger pick this out among competitors?)", reviewer.get("swap_test", 0), 10, reviewer.get("notes", ""))
        add("Reviewer: psychology fit (principles visibly implemented)", reviewer.get("psychology", 0), 10, "")
        add("Reviewer: copy specificity (no generic phrases, real numbers)", reviewer.get("copy_specificity", 0), 5, "")
    else:
        rows.append(("Reviewer: swap test / psychology / copy (NOT_RUN: provide --reviewer-json)", 0, 25, "NOT_RUN"))
    total = sum(r[1] for r in rows)
    return total, 100, rows

def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    def opt(name, default):
        return argv[argv.index(name) + 1] if name in argv else default
    target = args[0]
    out = pathlib.Path(opt("--out", "evidence/pass-01")); out.mkdir(parents=True, exist_ok=True)
    goal = int(opt("--target", "90"))
    widths = [int(w) for w in opt("--widths", "360,768,1280").split(",")]
    rev = opt("--reviewer-json", None)
    reviewer = json.loads(pathlib.Path(rev).read_text(encoding="utf-8")) if rev else None
    chrome = ts.find_chrome()
    if not chrome:
        print("Chrome/Chromium not found: the visual loop needs a renderer (set CHROME). Nothing scored."); return 2
    name = re.sub(r"[^a-z0-9]+", "-", pathlib.Path(target).stem.lower()) or "page"
    meas: dict[int, dict] = {}
    for w in widths:
        m = render(target, w, out / f"{name}-{w}.png", chrome)
        if m is None:
            print(f"render failed at {w}px"); return 2
        meas[w] = m
    tsm = ts.render(target, 1280, chrome)
    tscore, treasons = ts.score(tsm) if tsm else (100, ["render failed"])
    tsig = {"score": tscore, "verdict": "COMMON" if tscore >= 40 else "MIXED" if tscore >= 20 else "DISTINCT", "reasons": treasons}
    total, mx, rows = score(meas, tsig, reviewer)
    (out / "measurements.json").write_text(json.dumps({"target": target, "widths": meas, "template_signature": tsig, "reviewer": reviewer}, indent=2), encoding="utf-8")
    lines = [f"# Visual quality score: {total}/{mx} (target {goal})", "", f"Target: `{target}`  Screenshots: " + ", ".join(f"`{name}-{w}.png`" for w in widths), "",
             "| Criterion | Points | Max | Evidence |", "|---|---|---|---|"]
    for c, p, m_, e in rows:
        lines.append(f"| {c} | {p} | {m_} | {e} |")
    lines += ["", "## Next pass", "Fix the criteria with the largest gap first. LOOK at every screenshot before deciding; the numbers do not see composition.",
              "Stop when the score meets the target on two consecutive passes with the reviewer slot filled by someone who did not make the design."]
    (out / "score.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if total >= goal else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
