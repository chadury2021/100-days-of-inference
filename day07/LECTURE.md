# Day 07 — Lecture 07: CUDA Kernels, Kernel Selection & Kernel Fusion

[Previous lecture](../day06/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day08/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 06](../day06/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Explain kernel dispatch.
- Evaluate fusion against a baseline.

## Lecture notes

A kernel launches parallel work on the GPU. Separate elementwise operations can materialize intermediate arrays and incur multiple launches. Fusion can reduce those costs, but register pressure and resource use may offset the benefit. Shape, layout, and dtype influence which implementation performs well.

## Board example

For y=ReLU(ax+b), a simplified three-pass implementation reads and writes an N-element array three times: about 6N element transfers. One fused pass can approach 2N transfers, excluding scalar loads. This traffic ratio is not automatically the wall-clock speedup.

## Notebook lab

- [cuda-kernels](./cuda-kernels.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Profile an elementwise chain before and after compilation or fusion. Warm up both paths, verify outputs, and report launches, memory traffic assumptions, and elapsed time for small and large arrays.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
