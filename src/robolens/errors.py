"""RoboLens error taxonomy.

The split below resolves the "fail fast vs never-crash-overnight" tension:

- [`ConfigError`][robolens.errors.ConfigError] /
[`CompatibilityError`][robolens.errors.CompatibilityError] are raised *before* any
  rollout — bad configuration should fail loudly and immediately.
- [`PolicyError`][robolens.errors.PolicyError] is recorded as a failed trial; whether it aborts the
eval
  is governed by ``fail_on_error`` (Inspect semantics).
- [`EmbodimentFault`][robolens.errors.EmbodimentFault] and
[`SafetyAbort`][robolens.errors.SafetyAbort] *always* halt the eval
  regardless of ``fail_on_error`` — a faulted or unsafe robot must never
  auto-advance to the next scene unattended.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from robolens.rollout import TrialRecord


class RoboLensError(Exception):
    """Base class for all RoboLens errors.

    When an error is raised from inside a running trial, the rollout engine
    attaches the partial [`TrialRecord`][robolens.rollout.TrialRecord] — the
    steps walked and the transcript events up to the failure — as ``record``,
    so the orchestrator can preserve it in logs. ``record`` is ``None`` for
    errors raised outside a rollout (configuration, compatibility, ...).
    """

    record: TrialRecord | None = None


class ConfigError(RoboLensError):
    """Invalid task / policy / embodiment configuration. Fail fast."""


class CompatibilityError(RoboLensError):
    """A policy and embodiment are not compatible. Fail fast, before any rollout."""


class PolicyError(RoboLensError):
    """The policy raised during inference. Recorded as a failed trial."""


class EmbodimentFault(RoboLensError):
    """The embodiment/robot faulted. Always halts the eval and requires a human."""


class SafetyAbort(RoboLensError):
    """An approver vetoed an action / e-stop. Always halts the eval."""
