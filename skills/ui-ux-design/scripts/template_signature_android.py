"""Template-signature score for an Android project (Jetpack Compose and/or XML views).

Scans source for the signals that make an app look like the Android Studio "Empty Activity" template
plus stock Material 3 with nothing decided: default template colours and typography, default shapes,
Scaffold + BottomNavigation + FAB with cards for everything, placeholder strings, default launcher icon,
no motion specification, generic copy. Prints a 0-100 score with per-point evidence.

Usage:
    python template_signature_android.py <android-project-root> [--json]

Verdict: COMMON (>= 40) means redesign is mandatory; MIXED (20-39) targeted changes; DISTINCT (< 20).
Exit code 1 when COMMON. Heuristic: every point lists its evidence so a reviewer can disagree with reasons.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

TEMPLATE_COLOURS = {  # Android Studio Compose template (Color.kt) and legacy purple_500 set
    "FFD0BCFF": "Purple80", "FFCCC2DC": "PurpleGrey80", "FFEFB8C8": "Pink80",
    "FF6650A4": "Purple40", "FF625B71": "PurpleGrey40", "FF7D5260": "Pink40",
    "FF6200EE": "purple_500", "FF3700B3": "purple_700", "FFBB86FC": "purple_200",
    "FF03DAC5": "teal_200", "FF018786": "teal_700",
}
GENERIC_PHRASES = ["welcome to", "get started", "lorem", "hello world", "hello android", "sample text", "placeholder",
                   "supercharge", "seamless", "effortless", "all-in-one", "unlock", "elevate", "empower", "next-gen",
                   "your journey", "coming soon", "todo", "tbd"]
SKIP_DIRS = {"build", ".gradle", ".idea", "node_modules", ".git", "generated"}

def files(root: Path, exts: tuple[str, ...]):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in exts and not any(part in SKIP_DIRS for part in p.parts):
            yield p

def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""

def analyse(root: Path) -> dict:
    kt = [(p, read(p)) for p in files(root, (".kt", ".java"))]
    xml = [(p, read(p)) for p in files(root, (".xml",))]
    ui_kt = [(p, s) for p, s in kt if "@Composable" in s or "androidx.compose" in s]
    strings = [(p, s) for p, s in xml if p.name.startswith("strings")]
    layouts = [(p, s) for p, s in xml if "layout" in p.parts]
    m: dict = {"project": str(root), "composeFiles": len(ui_kt), "xmlLayouts": len(layouts)}
    allkt = "\n".join(s for _, s in kt)
    allxml = "\n".join(s for _, s in xml)
    everything = allkt + "\n" + allxml

    # 1. Template colours still defined/used
    hexes = {h.upper() for h in re.findall(r"0x([0-9A-Fa-f]{8})", allkt)} | {("FF" + h.upper()) for h in re.findall(r"#([0-9A-Fa-f]{6})\b", allxml)} | {h.upper() for h in re.findall(r"#([0-9A-Fa-f]{8})\b", allxml)}
    m["templateColours"] = sorted(TEMPLATE_COLOURS[h] for h in hexes if h in TEMPLATE_COLOURS)
    # 2. Typography: default Typography() untouched, or no custom font family
    m["customFontFamily"] = bool(re.search(r"FontFamily\(\s*Font\(", allkt)) or bool(re.search(r"android:fontFamily=\"@font/", allxml)) or any("font" in p.parts for p, _ in xml)
    m["typographyOverridden"] = bool(re.search(r"Typography\(\s*\n?\s*\w+\s*=", allkt)) and not bool(re.search(r"bodyLarge\s*=\s*TextStyle\(\s*fontFamily\s*=\s*FontFamily\.Default", allkt))
    m["textStylesDeclared"] = len(re.findall(r"TextStyle\(", allkt)) + len(re.findall(r"<style name=\"[^\"]*Text", allxml))
    # 3. Shapes
    m["shapesOverridden"] = bool(re.search(r"Shapes\(", allkt)) or bool(re.search(r"shapeAppearance", allxml))
    m["cardCount"] = len(re.findall(r"\b(Elevated|Outlined)?Card\s*\(", allkt)) + len(re.findall(r"<(com\.google\.android\.material\.card\.MaterialCardView|androidx\.cardview\.widget\.CardView)", allxml))
    m["lazyColumnOfCards"] = len(re.findall(r"LazyColumn[\s\S]{0,400}?\bCard\s*\(", allkt))
    # 4. Stock scaffold: Scaffold + NavigationBar/BottomNavigation + FloatingActionButton
    m["scaffold"] = bool(re.search(r"\bScaffold\s*\(", allkt))
    m["bottomNav"] = bool(re.search(r"\b(NavigationBar|BottomNavigation)\s*\(", allkt)) or "BottomNavigationView" in allxml
    m["fab"] = bool(re.search(r"\b(Extended)?FloatingActionButton\s*\(", allkt)) or "FloatingActionButton" in allxml
    m["topAppBarDefault"] = bool(re.search(r"\b(CenterAligned|Medium|Large)?TopAppBar\s*\(", allkt)) and not re.search(r"TopAppBar\s*\([\s\S]{0,300}?(colors|scrollBehavior)", allkt)
    # 5. Motion
    m["animationCalls"] = len(re.findall(r"\b(animate\w*AsState|AnimatedVisibility|AnimatedContent|Crossfade|animateContentSize|updateTransition|rememberInfiniteTransition|sharedElement|animateItem(Placement)?|MotionLayout|ObjectAnimator|TransitionManager)\b", everything))
    m["navTransitionsCustom"] = bool(re.search(r"(enterTransition|exitTransition|popEnterTransition)\s*=", allkt))
    m["infiniteAnimations"] = len(re.findall(r"rememberInfiniteTransition", allkt))
    m["reducedMotionHandled"] = bool(re.search(r"(ANIMATOR_DURATION_SCALE|isReduceMotion|areAnimatorsEnabled|LocalAccessibilityManager|animatorDurationScale)", everything))
    # 6. Strings and copy
    allstrings = "\n".join(s for _, s in strings)
    texts = re.findall(r"<string[^>]*>([^<]{3,})</string>", allstrings) + re.findall(r"Text\(\s*(?:text\s*=\s*)?\"([^\"]{3,})\"", allkt)
    lower = " ".join(texts).lower()
    m["hardcodedTextInCompose"] = len(re.findall(r"Text\(\s*(?:text\s*=\s*)?\"[^\"]{3,}\"", allkt))
    m["genericPhrases"] = sorted({g for g in GENERIC_PHRASES if g in lower})
    m["emptyStatesDefined"] = bool(re.search(r"(empty|no_items|nothing_here|no_results)", lower + allkt.lower()))
    m["errorStatesDefined"] = bool(re.search(r"(error|retry|offline|try_again)", lower + allkt.lower()))
    # 7. Icons / launcher
    launcher = [p for p in files(root, (".xml", ".png", ".webp")) if "ic_launcher" in p.name]
    fg = [p for p in launcher if "foreground" in p.name and p.suffix == ".xml"]
    m["defaultLauncherIcon"] = any("android:fillColor=\"#3DDC84\"" in read(p) or "M31,63.928c0,0 6.4-11 12.1-13.1" in read(p) for p in fg) or (bool(launcher) and not fg and not any(p.suffix in (".png", ".webp") and "foreground" in p.name for p in launcher))
    m["customVectorIcons"] = len([p for p in files(root, (".xml",)) if "drawable" in p.parts and "<vector" in read(p) and "ic_launcher" not in p.name])
    m["materialIconsOnly"] = bool(re.search(r"Icons\.(Default|Filled|Outlined|Rounded)\.", allkt)) and m["customVectorIcons"] == 0
    # 8. Theme: dynamicColor template default, dark theme
    m["dynamicColorTemplateDefault"] = bool(re.search(r"dynamicColor:\s*Boolean\s*=\s*true", allkt))
    m["darkThemeDefined"] = bool(re.search(r"darkColorScheme\(", allkt)) or "values-night" in everything or any("values-night" in p.parts for p, _ in xml)
    # 9. Spacing: distinct dp values
    dps = re.findall(r"\b(\d+(?:\.\d+)?)\.dp\b", allkt) + re.findall(r"\"(\d+)dp\"", allxml)
    m["distinctDp"] = len(set(dps))
    m["spacingTokensFile"] = bool(re.search(r"object\s+(Spacing|Dimens|Space)\b", allkt)) or bool(re.search(r"<dimen name=", allxml))
    # 10. Template leftovers
    m["greetingComposable"] = bool(re.search(r"fun Greeting\(", allkt))
    m["templatePreviewOnly"] = bool(re.search(r"GreetingPreview", allkt))
    return m

def score(m: dict) -> tuple[int, list[str]]:
    pts: list[tuple[int, str]] = []
    if m["templateColours"]:
        pts.append((15, "Android Studio template colours still present: " + ", ".join(m["templateColours"])))
    if not m["customFontFamily"]:
        pts.append((10, "No custom font family: default Roboto/system typography (no typographic voice)"))
    if not m["typographyOverridden"] and m["textStylesDeclared"] < 3:
        pts.append((6, "Material Typography() left at defaults; fewer than 3 TextStyles declared"))
    if not m["shapesOverridden"]:
        pts.append((4, "Shapes left at Material defaults"))
    if m["cardCount"] >= 6 or m["lazyColumnOfCards"] >= 1:
        pts.append((10, f"{m['cardCount']} Card() usages, {m['lazyColumnOfCards']} LazyColumn-of-Cards: cards as the unit of layout"))
    elif m["cardCount"] >= 3:
        pts.append((5, f"{m['cardCount']} Card() usages"))
    if m["scaffold"] and m["bottomNav"] and m["fab"]:
        pts.append((8, "Stock Scaffold + bottom navigation bar + FAB (the default app skeleton)"))
    if m["topAppBarDefault"]:
        pts.append((3, "TopAppBar with default colours and no scroll behaviour"))
    if m["animationCalls"] == 0:
        pts.append((8, "No animation or transition API used anywhere (no feedback, no continuity)"))
    elif m["infiniteAnimations"] >= 2:
        pts.append((5, f"{m['infiniteAnimations']} infinite animations (decorative motion)"))
    if m["animationCalls"] > 0 and not m["reducedMotionHandled"]:
        pts.append((3, "Motion present but reduced-motion / animator duration scale not respected"))
    if m["composeFiles"] >= 3 and not m["navTransitionsCustom"]:
        pts.append((3, "Navigation uses default transitions"))
    if m["genericPhrases"]:
        pts.append((min(10, 3 * len(m["genericPhrases"])), "Placeholder or generic copy: " + ", ".join(m["genericPhrases"])))
    if m["hardcodedTextInCompose"] >= 10:
        pts.append((3, f"{m['hardcodedTextInCompose']} hard-coded strings in Compose (no localisation, often placeholder text)"))
    if not m["emptyStatesDefined"] or not m["errorStatesDefined"]:
        pts.append((5, "Empty and/or error states not found in strings or code"))
    if m["defaultLauncherIcon"]:
        pts.append((8, "Default Android launcher icon (green robot) still shipped"))
    if m["materialIconsOnly"]:
        pts.append((4, "Only stock Material icons; no custom vector drawables"))
    if m["dynamicColorTemplateDefault"]:
        pts.append((4, "dynamicColor = true template default: the app's palette is whatever the wallpaper decides"))
    if not m["darkThemeDefined"]:
        pts.append((3, "No dark theme defined"))
    if m["distinctDp"] >= 14 and not m["spacingTokensFile"]:
        pts.append((5, f"{m['distinctDp']} distinct dp values and no spacing token object (spacing drift)"))
    if m["greetingComposable"] or m["templatePreviewOnly"]:
        pts.append((6, "Template `Greeting` composable/preview still in the project"))
    return min(100, sum(p for p, _ in pts)), [f"+{p:2d}  {why}" for p, why in pts]

def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    root = Path(args[0]).resolve()
    if not root.exists():
        print(f"{root} does not exist"); return 2
    m = analyse(root)
    total, reasons = score(m)
    verdict = "COMMON" if total >= 40 else "MIXED" if total >= 20 else "DISTINCT"
    if "--json" in argv:
        print(json.dumps({"score": total, "verdict": verdict, "reasons": reasons, "measurements": m}, indent=2))
    else:
        print(f"== {root}  (compose files: {m['composeFiles']}, xml layouts: {m['xmlLayouts']})")
        for r in reasons:
            print("   " + r)
        print(f"   score {total}/100  ->  {verdict}" + ("  (redesign mandatory)" if verdict == "COMMON" else ""))
    return 1 if total >= 40 else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
