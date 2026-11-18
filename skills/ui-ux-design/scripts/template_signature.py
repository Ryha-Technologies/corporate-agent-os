"""Template-signature score for a rendered web page.

Measures how closely a page matches the common "AI-generated landing/dashboard template" and
prints a score (0-100) with the evidence for each point. Used twice by `ui-ux-design`: on the
existing UI (to decide whether a redesign is mandatory) and on the result (to prove it passed).

Usage:
    python template_signature.py <url-or-html-file> [--width 1280] [--json]
    python template_signature.py site/index.html site/skills.html

Needs Chrome/Chromium for a rendered measurement (set CHROME env var or let the script find it).
Without Chrome, a static-HTML fallback runs and is labelled as such.

Verdict: COMMON (>= 40), MIXED (20-39), DISTINCT (< 20). COMMON means redesign is mandatory.
Scores are heuristics; every point lists its evidence so a reviewer can disagree with reasons.
"""
from __future__ import annotations
import json, os, pathlib, re, shutil, subprocess, sys, tempfile

GENERIC_PHRASES = [
    "build ai agents", "supercharge", "unlock", "seamless", "next-gen", "next generation",
    "all-in-one", "powerful", "effortless", "revolutioni", "game-chang", "10x", "elevate",
    "empower", "transform your", "the future of", "trusted by", "loved by", "join thousands",
    "get started for free", "start your journey", "welcome to", "cutting-edge", "state-of-the-art",
]

JS = r"""
(() => {
  const cs = e => getComputedStyle(e);
  const all = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
  const vw = document.documentElement.clientWidth;
  const out = {};
  // 1. Hero: h1 + paragraph + >=2 buttons, centred
  const h1 = document.querySelector('h1');
  let hero = { present: !!h1, centred: false, buttons: 0, sub: false };
  if (h1) {
    const box = h1.closest('header, section, div') || h1.parentElement;
    const ctr = cs(h1).textAlign === 'center' || Math.abs((h1.getBoundingClientRect().left + h1.getBoundingClientRect().right) / 2 - vw / 2) < 40 && h1.getBoundingClientRect().left > vw * 0.15;
    const btns = box ? box.querySelectorAll('a[class*="btn"], button, a[class*="button"], a[class*="cta"]').length : 0;
    hero = { present: true, centred: ctr, buttons: btns, sub: !!(box && box.querySelector('p')) };
  }
  out.hero = hero;
  out.chipRows = all.filter(e => e.children.length >= 3 && [...e.children].every(k => (k.innerText||'').trim().length < 40 && cs(k).borderTopWidth !== '0px' && cs(k).display !== 'block')).length;
  // 2. Cards: boxed elements with radius >= 6 and own background or border, containing a heading or >1 child
  const cards = all.filter(e => { const s = cs(e); const r = parseFloat(s.borderTopLeftRadius) || 0; const hasBox = (s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== cs(document.body).backgroundColor) || s.borderTopWidth !== '0px' || s.boxShadow !== 'none'; const siblingsAlike = e.parentElement && [...e.parentElement.children].filter(k => k.tagName === e.tagName && k.className === e.className).length >= 2; return hasBox && siblingsAlike && e.children.length >= 1 && e.getBoundingClientRect().width > 140 && e.getBoundingClientRect().height > 60 && !['BUTTON','A','INPUT','PRE','CODE','TABLE','TR','TD','TH','LI'].includes(e.tagName) || (hasBox && siblingsAlike && e.tagName === 'LI' && e.children.length >= 2 && e.getBoundingClientRect().height > 60); });
  out.cards = cards.length;
  // 3. Section rhythm: signature of each section's child tag sequence
  const sections = [...document.querySelectorAll('section, main > div, body > div > section')];
  const sig = s => [...s.children].map(c => c.tagName + (c.children.length > 2 ? '*' : '')).join('>');
  const sigs = sections.map(sig).filter(Boolean);
  const freq = {}; sigs.forEach(s => freq[s] = (freq[s] || 0) + 1);
  out.sections = sections.length; out.mostRepeatedSectionSignature = Math.max(0, ...Object.values(freq));
  // 4. Grids of 3-4 equal items with an icon/svg/img and heading
  let featureRows = 0;
  all.forEach(e => { const s = cs(e); if ((s.display === 'grid' || s.display === 'flex') && e.children.length >= 3 && e.children.length <= 4) { const kids = [...e.children]; const w = kids.map(k => Math.round(k.getBoundingClientRect().width)); const equal = Math.max(...w) - Math.min(...w) < 12; const iconic = kids.filter(k => k.querySelector('svg, img, [class*="icon"]') && k.querySelector('h2,h3,h4')).length >= 3; if (equal && iconic) featureRows++; } });
  out.iconFeatureRows = featureRows;
  // 5. Gradients, shadows, blur glows
  out.gradients = all.filter(e => cs(e).backgroundImage.includes('gradient')).length;
  out.shadows = all.filter(e => cs(e).boxShadow !== 'none').length;
  out.glows = all.filter(e => { const s = cs(e); return (s.filter && s.filter.includes('blur')) || (s.boxShadow !== 'none' && /\d{2,3}px/.test(s.boxShadow) && parseFloat(s.boxShadow.split(' ')[3] || '0') >= 24); }).length;
  // 6. Type: distinct sizes, families
  const sizes = new Set(), fams = new Set();
  all.forEach(e => { if (e.innerText && e.innerText.trim() && e.children.length === 0) { sizes.add(cs(e).fontSize); fams.add(cs(e).fontFamily.split(',')[0].replace(/["']/g, '').trim()); } });
  out.fontSizes = sizes.size; out.fontFamilies = [...fams]; out.bodyFontStack = cs(document.body).fontFamily;
  // 7. Logo wall / trusted-by
  out.logoWall = !!all.find(e => /trusted by|loved by|used by|as seen|our customers|backed by/i.test(e.innerText || '') && e.children.length < 4);
  // 8. Emoji bullets / icon soup
  out.emoji = (document.body.innerText.match(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/gu) || []).length;
  // 9. Motion presence and volume
  out.animated = all.filter(e => cs(e).animationName !== 'none').length;
  out.transitions = all.filter(e => cs(e).transitionDuration !== '0s').length;
  // 10. Layout: everything centred, single column, max-width container
  const mains = [...document.querySelectorAll('main, .container, .wrap, .wrapper, [class*="container"]')];
  out.centredContainer = mains.some(m => { const s = cs(m); return s.marginLeft === s.marginRight && s.marginLeft !== '0px' && s.maxWidth !== 'none'; });
  const rows = sections.map(s => [...s.children].filter(c => cs(c).display === 'grid').length);
  out.gridSections = rows.filter(n => n > 0).length;
  // 11. Text
  out.text = document.body.innerText.slice(0, 20000);
  out.h1 = h1 ? h1.innerText.trim() : '';
  out.statTiles = all.filter(e => e.children.length >= 4 && [...e.children].filter(k => /^\s*\d{1,4}\b/.test(k.innerText||'') && parseFloat(cs(k.querySelector('strong,b,span,h3,div')||k).fontSize) >= 24).length >= 4).length;
  out.width = vw;
  return out;
})()
"""

def find_chrome() -> str | None:
    env = os.environ.get("CHROME")
    if env and pathlib.Path(env).exists():
        return env
    for c in ["chrome", "google-chrome", "chromium", "chromium-browser", "msedge"]:
        p = shutil.which(c)
        if p:
            return p
    for p in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]:
        if pathlib.Path(p).exists():
            return p
    return None

def render(target: str, width: int, chrome: str) -> dict | None:
    if re.match(r"^https?://", target):
        html = None
        url = target
    else:
        src = pathlib.Path(target).resolve()
        html = src.read_text(encoding="utf-8", errors="replace")
        url = None
    inject = f'<script>window.addEventListener("load",()=>{{const o={JS};const p=document.createElement("pre");p.id="__TS__";p.textContent=JSON.stringify(o);document.body.appendChild(p);}});</script>'
    if html is not None:
        tmp = src.with_name(f"_ts_{src.name}")
        tmp.write_text(html.replace("</body>", inject + "</body>") if "</body>" in html else html + inject, encoding="utf-8")
        url = tmp.as_uri()
    else:
        tmp = None
    try:
        out = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                              f"--window-size={max(width, 500)},1200", "--virtual-time-budget=4000",
                              "--dump-dom", url], capture_output=True, text=True, encoding="utf-8", timeout=90).stdout
    finally:
        if tmp and tmp.exists():
            tmp.unlink()
    m = re.search(r'<pre id="__TS__">(.*?)</pre>', out, re.S)
    if not m:
        if url and url.startswith("http"):
            # remote page cannot be injected via file; evaluate with a bookmarklet-style wrapper is not possible with dump-dom.
            return None
        return None
    txt = m.group(1).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"')
    return json.loads(txt)

def static_fallback(target: str) -> dict:
    html = pathlib.Path(target).read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"<[^>]+>", " ", html)
    cls = lambda pat: len(re.findall(r"class=[\"'][^\"']*" + pat, html, re.I))
    sections = re.findall(r"<section\b.*?</section>", html, re.S | re.I)
    sig = lambda s: ">".join(re.findall(r"<(h2|h3|p|ul|ol|div|table|figure|pre)\b", s, re.I)[:4]).lower()
    sigs = [sig(s) for s in sections]
    rep = max([sigs.count(x) for x in set(sigs)] or [0])
    grid_secs = sum(1 for s in sections if re.search(r"class=[\"'][^\"']*(grid|cards|row|columns)", s, re.I))
    hero_html = sections[0] if sections else html[:4000]
    return {
        "hero": {"present": "<h1" in html.lower(), "centred": bool(re.search(r"text-align:\s*center", hero_html, re.I)) or bool(re.search(r"class=[\"'][^\"']*hero", hero_html, re.I)),
                 "buttons": len(re.findall(r"class=[\"'][^\"']*(btn|button|cta)", hero_html, re.I)), "sub": "<p" in hero_html.lower()},
        "cards": cls("card"),
        "sections": len(sections), "mostRepeatedSectionSignature": rep,
        "iconFeatureRows": 0, "gradients": len(re.findall(r"gradient\(", html)), "shadows": len(re.findall(r"box-shadow", html)), "glows": 0,
        "fontSizes": len(set(re.findall(r"font-size:\s*([^;}]+)", html))), "fontFamilies": [],
        "logoWall": bool(re.search(r"trusted by|loved by", text, re.I)), "emoji": len(re.findall(r"[\U0001F300-\U0001FAFF]", text)),
        "animated": len(re.findall(r"@keyframes|animation:", html)), "transitions": len(re.findall(r"transition:", html)),
        "centredContainer": bool(re.search(r"margin:\s*0\s+auto", html)),
        "gridSections": grid_secs, "text": text[:20000], "h1": "", "width": 0, "static": True,
    }

def score(m: dict) -> tuple[int, list[str]]:
    pts: list[tuple[int, str]] = []
    h = m["hero"]
    if h["present"] and h["centred"] and h["buttons"] >= 2:
        pts.append((15, f"Centred hero with headline, subhead and {h['buttons']} buttons (the category default)"))
    elif h["present"] and h["buttons"] >= 2:
        pts.append((10, f"Hero = headline, subhead and {h['buttons']} equally weighted buttons (category default, left-aligned variant)"))
    if m.get("chipRows", 0) >= 1:
        pts.append((4, f"{m['chipRows']} badge/chip row(s)"))
    secs = max(m["sections"], 1)
    if m["cards"] >= 12 or m["cards"] / secs >= 3:
        pts.append((15, f"{m['cards']} card boxes across {m['sections']} sections: cards used as the unit of layout"))
    elif m["cards"] >= 6:
        pts.append((7, f"{m['cards']} card boxes"))
    if m["mostRepeatedSectionSignature"] >= 3:
        pts.append((12, f"{m['mostRepeatedSectionSignature']} sections share an identical child structure (same rhythm down the page)"))
    if m["gridSections"] >= 3:
        pts.append((6, f"{m['gridSections']} sections are a heading plus a grid"))
    if m.get("statTiles", 0) >= 1:
        pts.append((6, "Row of big-number stat tiles with equal weight"))
    if m["iconFeatureRows"] >= 1:
        pts.append((10, f"{m['iconFeatureRows']} three/four-column icon feature row(s)"))
    if m["gradients"] >= 2:
        pts.append((8, f"{m['gradients']} gradient backgrounds"))
    if m["glows"] >= 1:
        pts.append((6, f"{m['glows']} blur/glow effects"))
    if m["shadows"] >= 8:
        pts.append((4, f"{m['shadows']} drop shadows"))
    if m["fontSizes"] >= 8:
        pts.append((5, f"{m['fontSizes']} distinct font sizes (no scale)"))
    fams = [f.lower() for f in m.get("fontFamilies", [])]
    stack = (m.get("bodyFontStack") or "").lower()
    defaults = ("inter", "roboto", "system-ui", "-apple-system", "blinkmacsystemfont", "segoe ui", "arial", "helvetica", "helvetica neue", "ui-sans-serif", "sans-serif", "ui-monospace", "monospace", "consolas", "menlo", "sfmono-regular", "liberation mono", "courier new")
    if (fams and all(f in defaults for f in fams)) or (stack and all(x.strip().strip('"\'') in defaults for x in stack.split(","))):
        pts.append((6, "Only default/system typefaces (no typographic voice)"))
    if m["logoWall"]:
        pts.append((6, "'Trusted by' / logo-wall section"))
    if m["emoji"] >= 3:
        pts.append((5, f"{m['emoji']} emoji used as decoration or bullets"))
    text = (m.get("text") or "").lower()
    hits = sorted({p for p in GENERIC_PHRASES if p in text})
    if hits:
        pts.append((min(12, 3 * len(hits)), "Generic marketing phrases: " + ", ".join(hits)))
    if m["animated"] == 0 and m["transitions"] == 0:
        pts.append((4, "No motion or feedback states at all"))
    elif m["animated"] + m["transitions"] > 40:
        pts.append((6, f"{m['animated'] + m['transitions']} animated/transitioning elements (motion as decoration)"))
    total = min(100, sum(p for p, _ in pts))
    return total, [f"+{p:2d}  {why}" for p, why in pts]

def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    width = 1280
    if "--width" in argv:
        width = int(argv[argv.index("--width") + 1]); args = [a for a in args if a != str(width)]
    as_json = "--json" in argv
    if not args:
        print(__doc__); return 2
    chrome = find_chrome()
    worst = 0
    results = []
    for target in args:
        m = render(target, width, chrome) if chrome else None
        mode = "rendered"
        if m is None:
            if re.match(r"^https?://", target):
                print(f"{target}: remote URLs need a local copy for rendered measurement (save the page first)."); continue
            m = static_fallback(target); mode = "static (Chrome not available or render failed)"
        total, reasons = score(m)
        verdict = "COMMON" if total >= 40 else "MIXED" if total >= 20 else "DISTINCT"
        worst = max(worst, total)
        results.append({"target": target, "score": total, "verdict": verdict, "mode": mode, "reasons": reasons,
                        "measurements": {k: v for k, v in m.items() if k != "text"}})
        if not as_json:
            print(f"== {target}  [{mode}]")
            for r in reasons: print("   " + r)
            print(f"   score {total}/100  ->  {verdict}" + ("  (redesign mandatory)" if verdict == "COMMON" else ""))
    if as_json:
        print(json.dumps(results, indent=2))
    return 1 if worst >= 40 else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
