"""RoboLens — the Inspect AI for robotics.

An evaluation framework for VLA (vision-language-action) models. A benchmark is
defined once as a [`Task`][robolens.task.Task] and run against any compatible
pairing of a [`Policy`][robolens.policy.Policy] (the VLA) and an
[`Embodiment`][robolens.embodiment.Embodiment] (a real robot or simulator).

The public API is everything exported here via ``__all__``. Anything not listed
(or prefixed with ``_``) is private and carries no stability guarantee.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("robolens")
except PackageNotFoundError:  # pragma: no cover - only hit in a non-installed tree
    __version__ = "0.0.0+unknown"

from robolens.embodiment import (
    Embodiment,
    EmbodimentBase,
    EmbodimentInfo,
)
from robolens.eval import eval, eval_set
from robolens.log import (
    EvalLog,
    EvalResults,
    EvalSpec,
    EvalStats,
    SceneResult,
    read_eval_log,
)
from robolens.policy import Policy, PolicyBase, PolicyConfig, PolicyInfo
from robolens.registry import embodiment, policy, registered, resolve, scorer, sink, task
from robolens.rollout import TrialRecord
from robolens.scene import Scene, Target
from robolens.scorer import (
    Score,
    Scorer,
    episode_length,
    min_distance_to_goal,
    operator_scorer,
    reached_goal_state,
    success_at_end,
)
from robolens.spaces import (
    ActionSemantics,
    Box,
    CameraSpec,
    ObservationSpace,
    StateField,
    StateSpec,
)
from robolens.task import Epochs, Task
from robolens.types import Action, ActionChunk, Observation, StepResult

# The public, stability-guaranteed API. Anything not listed here (or prefixed
# with ``_``) is private. Authoring a benchmark, policy, or embodiment should only
# need these names.
__all__ = [
    "Action",
    "ActionChunk",
    "ActionSemantics",
    "Box",
    "CameraSpec",
    "Embodiment",
    "EmbodimentBase",
    "EmbodimentInfo",
    "Epochs",
    "EvalLog",
    "EvalResults",
    "EvalSpec",
    "EvalStats",
    "Observation",
    "ObservationSpace",
    "Policy",
    "PolicyBase",
    "PolicyConfig",
    "PolicyInfo",
    "Scene",
    "SceneResult",
    "Score",
    "Scorer",
    "StateField",
    "StateSpec",
    "StepResult",
    "Target",
    "Task",
    "TrialRecord",
    "__version__",
    "embodiment",
    "episode_length",
    "eval",
    "eval_set",
    "min_distance_to_goal",
    "operator_scorer",
    "policy",
    "reached_goal_state",
    "read_eval_log",
    "registered",
    "resolve",
    "scorer",
    "sink",
    "success_at_end",
    "task",
]
