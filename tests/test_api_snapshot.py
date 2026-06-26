"""Guard the public API surface against accidental growth/shrinkage.

If you intend to change the public API, update ``EXPECTED`` here and note it in
the changelog. Everything not in ``robolens.__all__`` (or prefixed ``_``) is
private and carries no stability guarantee.
"""

from __future__ import annotations

import robolens

EXPECTED = {
    "EvalLog",
    "EvalResults",
    "EvalSpec",
    "EvalStats",
    "SceneResult",
    "__version__",
    "eval",
    "eval_set",
    "read_eval_log",
}


def test_public_api_snapshot() -> None:
    assert set(robolens.__all__) == EXPECTED


def test_public_names_are_importable() -> None:
    for name in robolens.__all__:
        assert hasattr(robolens, name), f"{name} declared in __all__ but missing"
