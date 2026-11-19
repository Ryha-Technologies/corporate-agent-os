"""Copy slop check: scan the words a product or document actually shows for the writing tells of generated text.

Usage:
    python copy_slop_check.py <file-or-dir-or-url> [...] [--json] [--max 10]

A line containing `slop-ignore` is skipped (for text that quotes the patterns on purpose).
URLs are rendered with headless Chrome first so JavaScript-rendered copy is scanned.

Reads .md, .txt, .html, .htm, .jsx, .tsx, .vue, .svelte, .astro and Android strings.xml. For markup and
components it extracts visible text (tag content, alt/title/aria-label/placeholder attributes, string
literals inside JSX text). Prints each hit with file:line and the suggested fix, and a density score
(hits per 1,000 words). Exit 1 when the weighted hit count exceeds --max (default 10) or any
placeholder is found.

Sources for the patterns: skills/ui-ux-design/references/slop-mechanics.md section 2.
A hit is a signal to rewrite, not proof that a model wrote it; humans produce these too.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PATTERNS: list[tuple[str, str, int, str]] = [
    # (id, regex, weight, fix)
    ("placeholder", r"\blorem ipsum\b|\[(your|company|product) ?name\]|\bTODO\b|\bTBD\b|\bplaceholder text\b|\bXXX\b", 5, "Fill with real content or remove the element."),
    ("not-just", r"\b(it'?s|this is|we'?re|isn'?t) not (just|only|merely) [^.,;]{2,40}[,;:-]+\s*(it'?s|but|this is)\b", 3, "State the one claim directly."),
    ("not-x-its-y", r"\bnot [a-z]+(?: [a-z]+){0,3}[,;] (but|it'?s) [a-z]+", 2, "Negative parallelism: say what it is."),
    ("slop-verb", r"\b(delve|delves|delving|leverag(e|es|ing)|harness(es|ing)? the power|unlock(s|ing)? (the|your)|elevat(e|es|ing) your|empower(s|ing)?|supercharg(e|es|ing)|revolutioni[sz](e|es|ing)|streamlin(e|es|ing) your|embark|unleash(es|ing)?)\b", 2, "Use the concrete verb for what the product does."),
    ("slop-adjective", r"\b(seamless(ly)?|robust|cutting[- ]edge|state[- ]of[- ]the[- ]art|next[- ]gen(eration)?|game[- ]chang(er|ing)|world[- ]class|best[- ]in[- ]class|all[- ]in[- ]one|effortless(ly)?|powerful|innovative|holistic|pivotal|transformative|unparalleled|bespoke)\b", 1, "Replace with a number, a name or a specific property."),
    ("landscape", r"\b(in today'?s (fast[- ]paced |digital |ever[- ]changing )?(world|landscape|era)|ever[- ]evolving landscape|digital landscape|tapestry|realm of)\b", 2, "Cut the scene-setting; start with the point."),
    ("headline-formula", r"(?m)^\s*(#+\s*)?([Mm]eet [A-Z]\w+|[A-Z][\w ]{1,30}, reimagined|[Tt]he [\w-]+ (platform|tool|app|way) for [\w ]{2,30}|([Bb]uild|[Ss]hip|[Cc]reate) [\w ]{1,20} (faster|10x|in minutes))\b", 2, "Headline from the product's specific job, not a formula."),
    ("hype", r"\b(10x|blazing(ly)? fast|lightning[- ]fast|magic(al)?ly|like never before|take (it|your \w+) to the next level|the future of)\b", 2, "Give the measured number or drop it."),
    ("hedge-stack", r"\b(may potentially|could possibly|might perhaps|arguably|it is important to note that|it'?s worth noting that|needless to say)\b", 1, "Commit to the claim or remove it."),
    ("closing-aphorism", r"(?m)(^|\. )(in (the end|conclusion|summary)|ultimately|at the end of the day)[, ]", 1, "End on the last fact, not a summary."),
    ("social-proof-fake", r"\b(trusted by (thousands|millions|teams|leading)|loved by|join (thousands|millions)|#1 (rated|choice))\b", 3, "Only real, sourced proof; otherwise remove."),
    ("urgency", r"\b(limited time|act now|don'?t miss out|only \d+ (left|spots))\b", 3, "Remove fake urgency."),
    ("emoji-bullet", r"(?m)^\s*[-*]?\s*[\u2705\u2728\U0001F680\U0001F525\U0001F4A1\U0001F3AF\u26A1\U0001F4C8\U0001F31F\U0001F389]\s", 1, "Bullets without decorative emoji."),
]
EM_DASH_LIMIT_PER_100_WORDS = 1.0
EXTS = {".md", ".txt", ".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".xml", ".mdx"}
SKIP = {"node_modules", ".git", "dist", "build", ".next", "out", "coverage", "__pycache__", "vendor"}

def visible_lines(path: Path) -> list[tuple[int, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    suf = path.suffix.lower()
    if suf == ".xml" and "<resources" not in raw:
        return []
    out: list[tuple[int, str]] = []
    in_script = in_code = False
    for i, line in enumerate(raw.splitlines(), 1):
        if suf in (".md", ".mdx", ".txt"):
            if line.strip().startswith("```"):
                in_code = not in_code; continue
            if in_code:
                continue
            out.append((i, re.sub(r"`[^`]*`|\]\([^)]*\)", " ", line)))
            continue
        if re.search(r"<(script|style)\b", line, re.I):
            in_script = True
        if in_script:
            if re.search(r"</(script|style)>", line, re.I):
                in_script = False
            continue
        attrs = " ".join(re.findall(r"\b(?:alt|title|aria-label|placeholder|content)=[\"']([^\"']{3,})[\"']", line))
        if suf in (".jsx", ".tsx", ".vue", ".svelte", ".astro"):
            text = " ".join(re.findall(r">([^<>{}]{3,})<", line)) + " " + " ".join(re.findall(r"(?:title|label|description|heading|text|cta)\s*[:=]\s*[\"'`]([^\"'`]{6,})[\"'`]", line))
        elif suf == ".xml":
            text = " ".join(re.findall(r"<string[^>]*>([^<]+)</string>", line))
        else:
            text = re.sub(r"<[^>]+>", " ", line)
        t = (text + " " + attrs).strip()
        if t:
            out.append((i, re.sub(r"&[a-z]+;|&#\d+;", " ", t)))
    return out

def fetch_rendered(url: str) -> Path | None:
    """Render a live URL with headless Chrome and save its visible text, so JS-rendered copy is scanned."""
    import os, shutil, subprocess, tempfile
    chrome = os.environ.get("CHROME") or next((shutil.which(c) for c in ("chrome", "google-chrome", "chromium", "msedge") if shutil.which(c)), None)
    for c in (r"C:\Program Files\Google\Chrome\Application\chrome.exe", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if not chrome and Path(c).exists():
            chrome = c
    if not chrome:
        print(f"{url}: Chrome not found; save the page's text and scan the file instead"); return None
    try:
        dom = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--virtual-time-budget=8000", "--dump-dom", url],
                             capture_output=True, text=True, encoding="utf-8", timeout=120).stdout
    except subprocess.TimeoutExpired:
        print(f"{url}: render timed out after 120 s; NOT_RUN for this URL"); return None
    dom = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", dom)
    text = re.sub(r"(?s)<[^>]+>", "\n", dom)
    text = "\n".join(l.strip() for l in text.splitlines() if l.strip())
    out = Path(tempfile.gettempdir()) / ("copy_slop_" + re.sub(r"[^a-z0-9]+", "_", url.lower())[:60] + ".txt")
    out.write_text(text, encoding="utf-8")
    return out

def scan(paths: list[Path]) -> dict:
    hits, words, dashes = [], 0, 0
    files = []
    for p in paths:
        if isinstance(p, str):  # live URL
            f = fetch_rendered(p)
            if f:
                files.append(f)
            continue
        if p.is_dir():
            files += [f for f in p.rglob("*") if f.is_file() and f.suffix.lower() in EXTS and not any(s in f.parts for s in SKIP)]
        elif p.is_file():
            files.append(p)
    raw_lines: dict[Path, list[str]] = {}
    for f in files:
        raw_lines[f] = f.read_text(encoding="utf-8", errors="replace").splitlines()
        for ln, text in visible_lines(f):
            if ln <= len(raw_lines[f]) and "slop-ignore" in raw_lines[f][ln - 1]:
                continue  # line quotes the patterns on purpose (e.g. a QA report describing its own search)
            words += len(re.findall(r"[A-Za-z']+", text))
            dashes += text.count("\u2014")
            for pid, rx, w, fix in PATTERNS:
                for m in re.finditer(rx, text, re.I if pid != "headline-formula" else 0):
                    hits.append({"file": str(f), "line": ln, "pattern": pid, "weight": w, "match": m.group(0).strip()[:80], "fix": fix})
    weighted = sum(h["weight"] for h in hits)
    dash_rate = (dashes / words * 100) if words else 0.0
    if dash_rate > EM_DASH_LIMIT_PER_100_WORDS:
        hits.append({"file": "(all)", "line": 0, "pattern": "em-dash-density", "weight": 2, "match": f"{dashes} em dashes in {words} words ({dash_rate:.1f}/100)", "fix": "Use periods and commas; keep em dashes rare."})
        weighted += 2
    return {"files": len(files), "words": words, "hits": hits, "weighted": weighted,
            "per_1000_words": round(weighted / words * 1000, 1) if words else 0.0,
            "placeholders": sum(1 for h in hits if h["pattern"] == "placeholder")}

def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    mx = int(argv[argv.index("--max") + 1]) if "--max" in argv else 10
    args = [a for a in args if a != str(mx)]
    r = scan([a if re.match(r"^https?://", a) else Path(a) for a in args])  # type: ignore[misc]
    if "--json" in argv:
        print(json.dumps(r, indent=2))
    else:
        for h in r["hits"]:
            print(f"{h['file']}:{h['line']}  [{h['pattern']}] \"{h['match']}\"  -> {h['fix']}")
        verdict = "FAIL" if (r["weighted"] > mx or r["placeholders"]) else "PASS"
        print(f"\n{r['files']} files, {r['words']} words, weighted hits {r['weighted']} ({r['per_1000_words']}/1000 words), placeholders {r['placeholders']}  ->  {verdict} (max {mx})")
    return 1 if (r["weighted"] > mx or r["placeholders"]) else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
