#!/usr/bin/env python3
"""Build the distributable archives and checksums.

Steps:
  1. Rebuild generated artefacts (adapters, power, rendered docs).
  2. Run every validator; abort on failure.
  3. Zip the repository (excluding dist/, caches, .git) to dist/corporate-agent-os-final.zip.
  4. Zip the Kiro Power to dist/corporate-agent-os-kiro-power.zip.
  5. Re-open both archives, list entries, verify plugin.json and skill count, write SHA-256 sums and a manifest.

Usage: python scripts/package/build_release.py [--out DIR] [--skip-validate]
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", "dist", "node_modules", ".venv", ".worktrees"}
EXCLUDE_SUFFIX = {".pyc"}


def _iter_files(base: Path):
    for p in sorted(base.rglob("*")):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(base).parts
        if any(part in EXCLUDE_DIRS for part in rel_parts) or p.suffix in EXCLUDE_SUFFIX:
            continue
        yield p


def _zip(base: Path, out: Path, prefix: str) -> int:
    count = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in _iter_files(base):
            arc = f"{prefix}/{p.relative_to(base).as_posix()}"
            info = zipfile.ZipInfo(arc, date_time=(2026, 1, 1, 0, 0, 0))  # reproducible timestamps
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with p.open("rb") as fh:
                zf.writestr(info, fh.read())
            count += 1
    return count


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _verify(zip_path: Path, expect_prefix: str) -> dict:
    with zipfile.ZipFile(zip_path) as zf:
        bad = zf.testzip()
        names = zf.namelist()
        skills = sorted({n.split("/")[2] for n in names if n.startswith(f"{expect_prefix}/skills/") and n.endswith("/SKILL.md")})
        manifest = None
        for cand in (f"{expect_prefix}/plugin.json", f"{expect_prefix}/powers/kiro/corporate-agent-os/plugin.json"):
            if cand in names:
                manifest = json.loads(zf.read(cand))
                break
    return {"entries": len(names), "corrupt_member": bad, "skills": len(skills), "plugin_json": manifest is not None,
            "plugin_version": manifest.get("version") if manifest else None}


def main(argv: list[str]) -> int:
    out_dir = ROOT / "dist"
    if "--out" in argv:
        out_dir = Path(argv[argv.index("--out") + 1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    py = sys.executable
    print("1/5 regenerating adapters, power and rendered docs")
    for script in ("scripts/package/build_adapters.py", "scripts/package/build_power.py", "scripts/package/render_roles.py"):
        subprocess.run([py, str(ROOT / script)], check=True, cwd=ROOT)
    if "--skip-validate" not in argv:
        print("2/5 running validators")
        res = subprocess.run([py, str(ROOT / "scripts/validate/run_all.py"), "--json", str(out_dir / "validation-report.json")], cwd=ROOT)
        if res.returncode != 0:
            print("Validation failed; release not built.")
            return res.returncode
    else:
        print("2/5 validators skipped (--skip-validate)")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    print("3/5 zipping repository")
    repo_zip = out_dir / "corporate-agent-os-final.zip"
    n_repo = _zip(ROOT, repo_zip, "corporate-agent-os")
    print("4/5 zipping Kiro Power")
    power_zip = out_dir / "corporate-agent-os-kiro-power.zip"
    n_power = _zip(ROOT / "powers/kiro/corporate-agent-os", power_zip, "corporate-agent-os")
    print("5/5 verifying archives")
    manifest = {
        "version": version,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": {},
    }
    for z, prefix, n in ((repo_zip, "corporate-agent-os", n_repo), (power_zip, "corporate-agent-os", n_power)):
        v = _verify(z, prefix)
        v.update({"files_written": n, "sha256": _sha256(z), "bytes": z.stat().st_size})
        manifest["artifacts"][z.name] = v
        if v["corrupt_member"]:
            print(f"CORRUPT member in {z.name}: {v['corrupt_member']}")
            return 1
        if v["entries"] != n:
            print(f"Entry count mismatch in {z.name}: wrote {n}, read {v['entries']}")
            return 1
        print(f"  {z.name}: {v['entries']} entries, {v['skills']} skills, sha256={v['sha256'][:16]}..., plugin.json={v['plugin_json']} v{v['plugin_version']}")
    (out_dir / "SHA256SUMS.txt").write_text("".join(f"{a['sha256']}  {name}\n" for name, a in manifest["artifacts"].items()), encoding="utf-8")
    (out_dir / "release-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Release {version} written to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
