# Command-line interface

The `robolens` CLI wraps the registry and [`eval`][robolens.eval.eval].

## `robolens list`

Show registered components (builtins + installed plugins):

```bash
robolens list                 # all kinds
robolens list policies        # just one kind
robolens list embodiments
```

## `robolens run`

Resolve a task/policy/embodiment from the registry and run an eval. Pass
constructor arguments with `-T` (task), `-P` (policy), and `-E` (embodiment) as
`key=value` (parsed as bool/int/float/None/str):

```bash
robolens run --task cubepick-reach --policy scripted --embodiment cubepick
robolens run --task cubepick-reach -T num_scenes=10 --policy scripted -P chunk_size=8 \
             --embodiment cubepick --log-dir logs --seed 0
```

The exit code is `0` on a successful eval, `1` otherwise.

## `robolens inspect`

Print a summary of a saved [`EvalLog`][robolens.log.EvalLog]:

```bash
robolens inspect logs/cubepick-reach_xxxx.json
```

```text
task:        cubepick-reach
policy:      scripted
embodiment:  cubepick
status:      success
scenes:      5   trials: 5
metrics:
  success_at_end: 1
scenes:
  [success] scene-0: success_at_end=1
  ...
```

## `robolens --version`

```bash
robolens --version
```
