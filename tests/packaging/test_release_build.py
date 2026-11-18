"""Packaging tests: power build into a temp dir, release zips open and contain the expected content."""
import json
import zipfile
from pathlib import Path

import build_power
import build_release
import validate_power
from common import Report


def test_build_power_into_temp(tmp_path: Path):
    out = tmp_path / "corporate-agent-os"
    build_power.build(out)
    assert (out / "plugin.json").exists() and (out / "LICENSE").exists()
    skills = [d for d in (out / "skills").iterdir() if d.is_dir()]
    assert len(skills) == len([d for d in (build_power.SKILLS).iterdir() if d.is_dir()])
    r = Report("p")
    validate_power.validate_power(out, r)
    assert r.ok, r.errors


def test_release_build_and_verify(tmp_path: Path):
    code = build_release.main(["--out", str(tmp_path), "--skip-validate"])
    assert code == 0
    repo_zip = tmp_path / "corporate-agent-os-final.zip"
    power_zip = tmp_path / "corporate-agent-os-kiro-power.zip"
    assert repo_zip.exists() and power_zip.exists()
    manifest = json.loads((tmp_path / "release-manifest.json").read_text(encoding="utf-8"))
    sums = (tmp_path / "SHA256SUMS.txt").read_text(encoding="utf-8")
    for name, art in manifest["artifacts"].items():
        assert art["corrupt_member"] is None
        assert art["entries"] == art["files_written"]
        assert art["sha256"] in sums
    with zipfile.ZipFile(repo_zip) as zf:
        names = zf.namelist()
        assert "corporate-agent-os/README.md" in names
        assert "corporate-agent-os/skills/corporate-orchestrator/SKILL.md" in names
        assert "corporate-agent-os/powers/kiro/corporate-agent-os/plugin.json" in names
        assert not any("/dist/" in n or "__pycache__" in n for n in names)
    with zipfile.ZipFile(power_zip) as zf:
        names = zf.namelist()
        assert "corporate-agent-os/plugin.json" in names
        assert manifest["artifacts"]["corporate-agent-os-kiro-power.zip"]["skills"] >= 39
        assert all(n.startswith("corporate-agent-os/") for n in names)
