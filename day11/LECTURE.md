# Day 11 — Lecture 11: TensorRT-LLM: Compilation & Plugin System

[Previous lecture](../day10/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day12/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 10](../day10/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Explain engine specialization.
- Evaluate build and runtime tradeoffs.

## Lecture notes

An optimized inference runtime can select specialized implementations and execution plans for supported workloads. Plugins supply operations that need custom handling. Optimization requires an explicit support envelope: model architecture, precision, shapes, device, and runtime version all affect whether an execution path is usable.

## Board example

If one execution plan covers sequence lengths up to 2,048, a 4,096-token request needs an explicitly supported alternative. Silently truncating it changes the task. If a build costs 120 seconds and saves 5 ms per call, amortization requires 24,000 calls.

## Notebook lab

- [tensorrt-llm](./tensorrt-llm.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Describe a supported model/shape/precision configuration using the notebook. Compare build cost and warm execution where hardware permits; otherwise use its simulation and label results as simulated. Specify behavior for unsupported requests.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
