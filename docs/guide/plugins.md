# Plugins & the registry

RoboLens components register by name and resolve from strings — the mechanism the
CLI and `eval("...", "...", "...")` use. In-tree builtins register via decorators;
out-of-tree packages publish **entry points**, so an installed plugin appears in
`robolens list` without being imported first.

## Decorators

```python
from robolens.registry import embodiment, policy, scorer, task

@policy("my-vla")
class MyVLA: ...

@embodiment("my-arm")
class MyArm: ...

@scorer("smooth")
def smooth(): ...

@task("my-bench")
def my_bench(): ...
```

## Resolving

```python
from robolens.registry import registered, resolve

registered("policy")          # {"scripted": ..., "random": ..., "my-vla": ...}
policy = resolve("policy", "my-vla", checkpoint="...")   # constructor kwargs forwarded
```

## Shipping an out-of-tree plugin

Publish entry points from your package's `pyproject.toml`:

```toml
[project.entry-points."robolens.embodiments"]
maniskill = "robolens_maniskill:ManiSkillEmbodiment"

[project.entry-points."robolens.policies"]
openvla = "robolens_openvla:OpenVLAPolicy"
```

Groups: `robolens.tasks`, `robolens.policies`, `robolens.embodiments`,
`robolens.scorers`, `robolens.sinks`. After `pip install robolens-maniskill`, it
shows up in `robolens list` and resolves by name in `eval()` and the CLI.

This is how the ecosystem stays decoupled: this repository is the **framework**;
specific simulators, VLA weights, and benchmarks live in their own packages.
