"""design_gate.py blocks until the research record is complete; template_signature_android.py flags a stock template."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "skills/ui-ux-design/scripts/design_gate.py"
ANDROID = ROOT / "skills/ui-ux-design/scripts/template_signature_android.py"
TEMPLATE = ROOT / "templates/design/research-record.md"


def run(script, *args):
    return subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True)


def test_gate_closed_without_record(tmp_path):
    r = run(GATE, tmp_path)
    assert r.returncode == 1 and "DESIGN GATE CLOSED" in r.stdout


def test_gate_closed_on_unfilled_template(tmp_path):
    (tmp_path / "04-design").mkdir()
    (tmp_path / "04-design/research-record.md").write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
    r = run(GATE, tmp_path)
    assert r.returncode == 1
    assert "capture date" in r.stdout or "AWAITING_APPROVAL" in r.stdout or "no URL" in r.stdout


def test_gate_opens_on_complete_record(tmp_path):
    rows = "\n".join(
        f"| {n} | {role} | a | b | c | d | e | f | g | h | https://x.test/{n} | 2026-11-18 |"
        for n, role in [("c1", "direct"), ("c2", "direct"), ("c3", "direct"), ("a1", "adjacent"), ("a2", "adjacent"), ("paper", "non-digital")])
    psych = "\n".join(f"| P{i} | why | implication |" for i in range(4))
    fams = ["Material", "Time", "Inversion"]
    dirs = "\n".join(
        f"### Direction {d}: name\n- Lens: the instrument, family: {fams[i]} (fits gloves and glance)\n- First-screen sentence: the next job and minutes to it\n- Signature element: the route strip\n- Concept: x\n- Deliberate departure from the category template: y\n- What this direction gives up: browsing\n- Motion table: none\n- Risk: z\n" for i, d in enumerate("ABC"))
    dirs += """
### Distance table
| Direction | vs c1 | vs c2 | vs c3 | vs a1 | vs a2 | vs platform default | Min |
|---|---|---|---|---|---|---|---|
| A | 12 | 11 | 10 | 12 | 13 | 11 | 10 |
| B | 11 | 12 | 12 | 10 | 11 | 12 | 10 |
| C | 13 | 12 | 11 | 11 | 12 | 13 | 11 |

### Sibling check
| Pair | Score /14 |
|---|---|
| A vs B | 11 |
| A vs C | 12 |
| B vs C | 10 |

### Provocations
- Remove the nav bar: the route strip carries wayfinding; keep.
- Exaggerate the route strip x3: works to 60% height; keep at 40%.
- Swap the medium to print: a departure board; taught us to right-align times.
"""
    rec = f"""# Research record
## Job
A field technician on a 6-inch phone, outdoors, dispatching the next job while a customer waits, deciding in five seconds whether the job card is theirs and what to do first.
## Category research
| Reference | Role | Layout | Type | Colour | Imagery | Motion | Voice | Well | Badly | Source | Captured |
|---|---|---|---|---|---|---|---|---|---|---|---|
{rows}
## Pattern map
- Category template: cards. Keep: back nav. Free to change: bottom bar. Nobody does: show the route.
## Psychology
| Principle | Why | Implication |
|---|---|---|
{psych}
## Directions
{dirs}
| Criterion | A | B | C |
|---|---|---|---|
| Total | 20 | 15 | 12 |
## Approved direction
Approved by Velluraju C on 2026-11-18: Direction A.
"""
    (tmp_path / "04-design").mkdir()
    (tmp_path / "04-design/research-record.md").write_text(rec, encoding="utf-8")
    r = run(GATE, tmp_path)
    assert r.returncode == 0, r.stdout
    assert "DESIGN GATE OPEN" in r.stdout


def test_gate_rejects_cousin_direction(tmp_path):
    """A direction whose minimum distance to a reference is under 8/14 closes the gate."""
    test_gate_opens_on_complete_record(tmp_path)
    rec = tmp_path / "04-design/research-record.md"
    s = rec.read_text(encoding="utf-8").replace("| A | 12 | 11 | 10 | 12 | 13 | 11 | 10 |", "| A | 5 | 11 | 10 | 12 | 13 | 11 | 5 |")
    rec.write_text(s, encoding="utf-8")
    r = run(GATE, tmp_path)
    assert r.returncode == 1 and "cousin" in r.stdout, r.stdout


def test_android_template_is_common(tmp_path):
    src = tmp_path / "app/src/main/java/com/example/app"
    src.mkdir(parents=True)
    (src / "Color.kt").write_text("val Purple80 = Color(0xFFD0BCFF)\nval PurpleGrey80 = Color(0xFFCCC2DC)\nval Pink80 = Color(0xFFEFB8C8)\n", encoding="utf-8")
    (src / "Theme.kt").write_text("@Composable fun AppTheme(darkTheme: Boolean = isSystemInDarkTheme(), dynamicColor: Boolean = true, content: @Composable () -> Unit) { MaterialTheme(colorScheme = lightColorScheme(), typography = Typography, content = content) }\n", encoding="utf-8")
    (src / "Type.kt").write_text("val Typography = Typography(bodyLarge = TextStyle(fontFamily = FontFamily.Default))\n", encoding="utf-8")
    (src / "MainActivity.kt").write_text(
        "@Composable fun Greeting(name: String) { Text(text = \"Hello $name!\") }\n@Composable fun Home() { Scaffold(bottomBar = { NavigationBar { } }, floatingActionButton = { FloatingActionButton(onClick = {}) { Icon(Icons.Default.Add, null) } }) { LazyColumn { items(10) { Card { Text(\"Welcome to the app\") } } } } }\n"
        + "\n".join(f"@Composable fun S{i}() {{ Card {{ Text(\"Get started\") }} }}" for i in range(6)), encoding="utf-8")
    res = tmp_path / "app/src/main/res/mipmap-anydpi-v26"
    res.mkdir(parents=True)
    (res / "ic_launcher.xml").write_text("<adaptive-icon/>", encoding="utf-8")
    d = tmp_path / "app/src/main/res/drawable"
    d.mkdir()
    (d / "ic_launcher_foreground.xml").write_text('<vector><path android:fillColor="#3DDC84" android:pathData="M0,0"/></vector>', encoding="utf-8")
    r = run(ANDROID, tmp_path)
    assert r.returncode == 1 and "COMMON" in r.stdout, r.stdout
    assert "template colours" in r.stdout and "launcher icon" in r.stdout
