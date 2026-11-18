"""Shared fixtures for the Corporate Agent OS test suite."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "validate"))
sys.path.insert(0, str(ROOT / "scripts" / "package"))
sys.path.insert(0, str(ROOT / "scripts" / "install"))


@pytest.fixture(scope="session")
def root() -> Path:
    return ROOT


@pytest.fixture
def project_dir(tmp_path: Path) -> Path:
    """An empty target project directory."""
    p = tmp_path / "project"
    p.mkdir()
    return p
