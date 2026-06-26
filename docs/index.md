---
sd_hide_title: true
---

# RoboLens

<div align="center" style="margin-top: 1rem; margin-bottom: 1.5rem;">

<h1 style="font-size: 3rem; margin-bottom: 0.25rem;">🤖 RoboLens</h1>

<p style="font-size: 1.35rem; font-weight: 500; margin-top: 0;">
The <strong>Inspect AI</strong> for robotics.
</p>

<p style="font-size: 1.1rem; max-width: 46rem; margin: 0 auto; color: var(--color-foreground-secondary);">
An open-source evaluation framework for <strong>physical AI</strong> and
<strong>VLA (vision-language-action)</strong> models. Define a robotics benchmark
once, then run <em>any</em> policy against <em>any</em> compatible embodiment —
a real robot or a simulator — with reproducible logs and first-class
<a href="https://github.com/rerun-io/rerun">Rerun</a> visualization.
</p>

</div>

```{button-ref} guide/quickstart
:ref-type: doc
:color: primary
:expand:
Get started →
```

[Concepts](guide/concepts.md) · [Write a benchmark](guide/writing-a-benchmark.md) · [GitHub ★](https://github.com/robocurve/robolens)

---

## One framework, two swappable inputs

LLM evals have a single swappable input: the model. **Robotics evals have two** —
and RoboLens makes both first-class and orthogonal.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 🧠 `Policy` — the VLA
The "brain". Maps an observation + a language instruction to an **action chunk**
(a horizon of actions executed open-loop, as π0 / ACT / diffusion policies do).
:::

:::{grid-item-card} 🦾 `Embodiment` — the robot or sim
The "body + world". Produces observations, executes actions, and owns the
action/observation spaces and control rate. Real-robot-first; sims are a stricter
special case.
:::
::::

A **`Task`** — a dataset of `Scene`s (initial conditions, instructions, success
targets) plus scorers — is defined *independently* of both. Before any rollout,
RoboLens verifies the `(policy, embodiment)` pair is **compatible** and fails fast
and loud if not.

---

## Quickstart

```{code-block} bash
pip install robolens            # core (numpy only)
pip install "robolens[rerun]"   # + Rerun visualization
```

No hardware or simulator required — the dependency-free `CubePick` mock world
exercises the whole stack:

```{code-block} python
from robolens import eval
from robolens.mock import CubePickEmbodiment, ScriptedPolicy
from robolens.scene import Scene
from robolens.scorer import success_at_end
from robolens.task import Task

task = Task(
    name="cubepick-reach",
    scenes=[Scene(id=f"layout-{i}", instruction="reach the cube", init_seed=i) for i in range(5)],
    scorer=success_at_end(),
    max_steps=80,
)

# The two swappable inputs: a policy (VLA) and an embodiment (robot/sim).
(log,) = eval(task, ScriptedPolicy(), CubePickEmbodiment())
print(log.status, log.results.metrics)   # success {'success_at_end': 1.0}
```

…or from the command line:

```{code-block} bash
robolens list                                   # registered components
robolens run --task cubepick-reach --policy scripted --embodiment cubepick
robolens inspect logs/cubepick-reach_*.json     # results table
```

---

## Why RoboLens

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} 🌍 Real-world first
Interfaces assume real-robot reality: human-in-the-loop reset, no privileged
success oracle, wall-clock control rate. Simulators just offer more.
:::

:::{grid-item-card} 🔁 Reproducible
Every run yields an immutable, schema-versioned `EvalLog` with the resolved
config, git revision, and package versions — re-readable across releases.
:::

:::{grid-item-card} 🪶 Light core
The core depends only on NumPy. Rerun and simulator/VLA backends are optional
extras and separately installable plugins.
:::

:::{grid-item-card} 🛑 Safe unattended
An explicit error taxonomy separates "record and continue" from "halt and require
a human", so a faulted robot never auto-advances overnight.
:::

:::{grid-item-card} 🎞️ Rerun visualization
Stream camera images, 3D poses, joint/action time-series, and success markers to
a [Rerun](https://github.com/rerun-io/rerun) recording.
:::

:::{grid-item-card} 🧩 Pluggable
Ship `robolens-maniskill` or `robolens-openvla` as separate packages — entry
points make them appear in `robolens list` automatically.
:::
::::

---

## How it maps to Inspect AI

If you know [Inspect AI](https://inspect.aisi.org.uk/), you already know RoboLens.

| Inspect AI | RoboLens |
|---|---|
| `Model` | `Policy` (VLA) **+** `Embodiment` *(two inputs)* |
| `Task = dataset + solver + scorer` | `Task = scenes + controller + scorer` |
| `Sample` | `Scene` |
| `Solver` chain | `Controller` middleware (chunking, ensembling, smoothing) |
| `eval()` → `EvalLog` | `eval()` → `EvalLog` |
| `@task`/`@solver`/`@scorer` + registry | `@task`/`@policy`/`@embodiment`/`@scorer` + entry points |

```{toctree}
:hidden:
:caption: Guide

guide/quickstart
guide/concepts
guide/writing-a-benchmark
guide/policies-and-embodiments
guide/scoring
guide/logging-and-rerun
guide/plugins
guide/cli
```

```{toctree}
:hidden:
:caption: Reference

api/index
For LLMs (llms.txt) <https://robocurve.github.io/robolens/llms.txt>
```

```{toctree}
:hidden:
:caption: Project

GitHub <https://github.com/robocurve/robolens>
Changelog <https://github.com/robocurve/robolens/blob/main/CHANGELOG.md>
```
