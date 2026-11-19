"""copy_slop_check flags writing tells; template_signature flags the researched visual tells (static mode);
visual_quality_loop rejects a maker-as-reviewer and enforces DONE / CONTINUE / ESCALATE (when Chrome exists)."""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COPY = ROOT / "skills/anti-slop-quality-gate/scripts/copy_slop_check.py"
TS = ROOT / "skills/ui-ux-design/scripts/template_signature.py"
VQ = ROOT / "skills/ui-ux-design/scripts/visual_quality_loop.py"


def run(*args, env=None):
    return subprocess.run([sys.executable, "-B", *map(str, args)], capture_output=True, text=True, env=env)


def test_copy_slop_flags_tells(tmp_path):
    f = tmp_path / "landing.md"
    f.write_text("# Meet Nova\nIt's not just a tool, it's a revolution. Unlock your potential with seamless, cutting-edge AI.\n"
                 "In today's fast-paced world, trusted by thousands.\n[Your Name]\n", encoding="utf-8")
    r = run(COPY, f)
    assert r.returncode == 1, r.stdout
    for pid in ("placeholder", "not-just", "slop-verb", "slop-adjective", "landscape", "headline-formula", "social-proof-fake"):
        assert f"[{pid}]" in r.stdout, (pid, r.stdout)


def test_copy_slop_passes_plain_specific_copy(tmp_path):
    f = tmp_path / "page.md"
    f.write_text("# Dispatch the next job in one tap\nTechnicians see the address, the customer's name and minutes until arrival.\n"
                 "The list refreshes every 30 seconds and works offline for 8 hours.\n", encoding="utf-8")
    r = run(COPY, f)
    assert r.returncode == 0, r.stdout


def test_copy_slop_ignore_marker(tmp_path):
    f = tmp_path / "qa.md"
    f.write_text("| 11 | Placeholder text, TODO, TBD searched | PASS | <!-- slop-ignore -->\n", encoding="utf-8")
    assert run(COPY, f).returncode == 0


def test_template_signature_static_flags_researched_tells(tmp_path):
    html = tmp_path / "t.html"
    html.write_text("<html><body><section><h1>Ship <span class='text-gradient'>faster</span></h1>"
                    "<p class='uppercase'>NEW</p><a class='btn bg-indigo-600'>Start</a><a class='btn bg-indigo-500'>Demo</a></section>"
                    "<section><div>01</div><div>02</div><div>03</div></section>"
                    "<section><span>Most popular</span></section>"
                    + "".join(f"<section data-aos='fade-up'><h2>S{i}</h2></section>" for i in range(5)) + "</body></html>", encoding="utf-8")
    env = dict(os.environ, TEMPLATE_SIGNATURE_STATIC="1")
    r = run(TS, html, env=env)
    out = r.stdout
    assert "numbered markers" in out and "indigo" in out and "pricing pill" in out and "fade-up" in out, out


CHROME = None
for c in (os.environ.get("CHROME"), shutil.which("chrome"), shutil.which("google-chrome"), shutil.which("chromium"),
          r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
    if c and Path(c).exists():
        CHROME = c
        break


@pytest.mark.skipif(CHROME is None, reason="needs Chrome/Chromium")
def test_visual_loop_rejects_maker_review_and_enforces_status(tmp_path):
    page = tmp_path / "index.html"
    page.write_text("<!doctype html><html lang=en><head><style>@media (prefers-reduced-motion: reduce){*{transition:none}}"
                    "body{font-family:Georgia,serif;margin:0;padding:2rem;color:#111;background:#fff}a{display:inline-block;padding:14px}</style></head>"
                    "<body><header><nav><a href=#>Home</a></nav></header><main><h1>Dispatch the next job</h1>"
                    "<p>Technicians see the address and minutes to arrival.</p><a class=btn style='background:#0b5;color:#fff'>Open queue</a></main>"
                    "<footer>Velluraju C</footer></body></html>", encoding="utf-8")
    shots = ["index-360.png", "index-768.png", "index-1280.png"]
    rev_maker = tmp_path / "rev-maker.json"
    rev_maker.write_text(json.dumps({"reviewer": "frontend-engineer", "screenshots_viewed": shots, "swap_test": 10, "psychology": 10, "copy_specificity": 5}), encoding="utf-8")
    p1 = run(VQ, page, "--out", tmp_path / "ev/pass-01", "--maker", "frontend-engineer", "--reviewer-json", rev_maker, "--target", "60")
    assert "is the maker" in p1.stdout, p1.stdout
    assert p1.returncode == 1
    rev = tmp_path / "rev.json"
    rev.write_text(json.dumps({"reviewer": "design-qa-auditor", "screenshots_viewed": shots, "swap_test": 8, "psychology": 8, "copy_specificity": 5}), encoding="utf-8")
    run(VQ, page, "--out", tmp_path / "ev/pass-02", "--maker", "frontend-engineer", "--reviewer-json", rev, "--target", "60")
    p3 = run(VQ, page, "--out", tmp_path / "ev/pass-03", "--maker", "frontend-engineer", "--reviewer-json", rev, "--target", "60")
    assert p3.returncode == 0 and "DONE" in p3.stdout, p3.stdout
    assert "identical to the previous pass" in p3.stdout
