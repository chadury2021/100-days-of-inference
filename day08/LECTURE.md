# Day 08 — Lecture 08: PyTorch, Model File Formats, ONNX & TensorRT

[Previous lecture](../day07/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day09/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 07](../day07/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Distinguish weights, graphs, and engines.
- Separate compile cost from execution.

## Lecture notes

A weight container stores tensors. A graph representation describes operations, and an optimized engine specializes execution for supported hardware and shapes. Exporting a model does not guarantee that every operation or dynamic shape works on the destination runtime. Validate numerical behavior after each conversion.

## Board example

Suppose compilation costs 30 seconds, eager execution costs 20 ms per call, and compiled execution costs 10 ms. Break-even is 30/(0.020−0.010)=3,000 calls, ignoring other costs. A short job can lose overall time despite faster steady-state execution.

## Notebook lab

- [pytorch-model-formats](./pytorch-model-formats.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Inspect one saved weight file and compare eager with compiled execution where supported. Report setup time separately from warm latency. Test at least two input shapes and record conversion or graph-break limitations.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
