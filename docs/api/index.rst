API reference
=============

The API reference is generated automatically from the source docstrings. The
public, stability-guaranteed surface is everything exported by
``robolens.__all__`` (``eval``, ``eval_set``, ``read_eval_log``, ``EvalLog`` and
the other log dataclasses); the submodules below document the full framework.

Core types & spaces
-------------------

.. automodule:: robolens.types

.. automodule:: robolens.spaces

Policy & embodiment
-------------------

.. automodule:: robolens.policy

.. automodule:: robolens.embodiment

Tasks & scenes
--------------

.. automodule:: robolens.scene

.. automodule:: robolens.task

Scoring
-------

.. automodule:: robolens.scorer

Rollout, controllers & safety
-----------------------------

.. automodule:: robolens.rollout

.. automodule:: robolens.controller

.. automodule:: robolens.approver

.. automodule:: robolens.frames

.. automodule:: robolens.transcript

Compatibility & errors
----------------------

.. automodule:: robolens.compat

.. automodule:: robolens.errors

Evaluation & logs
-----------------

.. automodule:: robolens.eval
   :members: eval, eval_set

.. automodule:: robolens.log

Logging sinks
-------------

.. automodule:: robolens.logging.sink

.. automodule:: robolens.logging.json_log

.. automodule:: robolens.logging.rerun_sink

Registry & CLI
--------------

.. automodule:: robolens.registry

.. automodule:: robolens.cli

Mock world
----------

.. automodule:: robolens.mock.cubepick

.. automodule:: robolens.mock.policies
