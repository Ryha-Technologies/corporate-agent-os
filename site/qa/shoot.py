"""Render true 360px-wide screenshots (headless Chrome clamps windows to >=500px, so the page
is loaded in a 360px iframe inside a 1000px host and the iframe region is cropped out)."""
import pathlib, subprocess
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def shoot(page, width, height=900):
    name = f"{page[:-5]}-{width}.png"
    if width >= 500:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={width},{height}", "--virtual-time-budget=3000",
                        f"--screenshot={HERE / name}", (ROOT / page).as_uri()], capture_output=True)
        return name
    host = ROOT / "_shot_host.html"
    host.write_text(f'<!doctype html><html><body style="margin:0"><iframe src="{page}" '
                    f'style="width:{width}px;height:{height}px;border:0;display:block"></iframe></body></html>',
                    encoding="utf-8")
    tmp = HERE / "_host.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    f"--window-size=1000,{height}", "--virtual-time-budget=3000",
                    f"--screenshot={tmp}", host.as_uri()], capture_output=True)
    host.unlink()
    Image.open(tmp).crop((0, 0, width, height)).save(HERE / name)
    tmp.unlink()
    return name

for page in ["index.html", "skills.html", "agents.html", "docs.html"]:
    for w in (360, 768, 1280):
        print(shoot(page, w))
