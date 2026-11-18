"""Measure horizontal overflow of each site page at a given viewport width using headless Chrome.

Headless Chrome clamps the window to >= 500px, so each page is loaded in an iframe of the
requested width inside a wider host page.
"""
import pathlib, subprocess, sys, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
WIDTH = int(sys.argv[1]) if len(sys.argv) > 1 else 360

HOST = """<!doctype html><html><head><meta charset="utf-8"></head><body>
<iframe id="f" src="%(src)s" style="width:%(w)dpx;height:900px;border:0"></iframe>
<pre id="MEASURE">pending</pre>
<script>
function measure() {
  const d = document.getElementById('f').contentDocument;
  if (!d || !d.body || d.readyState !== 'complete') { setTimeout(measure, 100); return; }
  const w = d.documentElement.clientWidth, sw = d.documentElement.scrollWidth;
  const wide = [];
  d.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    const sc = el.closest('.table-scroll, pre');
    const inScroller = sc && sc !== el;
    const cls = typeof el.className === 'string' ? el.className : '';
    if (r.right > w + 1 && !inScroller) wide.push(el.tagName + '.' + cls + ' right=' + Math.round(r.right));
  });
  document.getElementById('MEASURE').textContent = 'clientWidth=' + w + ' scrollWidth=' + sw + ' bodyScroll=' + d.body.scrollWidth + '\\n' + wide.slice(0, 20).join('\\n');
}
setTimeout(measure, 300);
</script></body></html>"""

for page in ["index.html", "skills.html", "agents.html", "docs.html"]:
    tmp = ROOT / f"_measure_host.html"
    tmp.write_text(HOST % {"src": page, "w": WIDTH}, encoding="utf-8")
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                          "--window-size=1000,900", "--virtual-time-budget=5000",
                          "--dump-dom", tmp.as_uri()], capture_output=True, text=True, encoding="utf-8").stdout
    tmp.unlink()
    m = re.search(r'<pre id="MEASURE">(.*?)</pre>', out, re.S)
    print(f"== {page} @ {WIDTH}px")
    print(m.group(1) if m else "  (no measurement captured)")
