"""Smoke-test the example scripts so they never silently rot."""

from __future__ import annotations

import os
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


def test_quickstart_runs(tmp_path: Path, capsys: object) -> None:
    import runpy

    cwd = os.getcwd()
    os.chdir(tmp_path)  # write logs/ into the temp dir, not the repo
    try:
        runpy.run_path(str(_EXAMPLES / "quickstart.py"), run_name="__main__")
    finally:
        os.chdir(cwd)
    assert (tmp_path / "logs").exists()
