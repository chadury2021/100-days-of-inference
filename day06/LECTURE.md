# Day 06 — Lecture 06: Ops:Byte Ratio & Arithmetic Intensity

[Previous lecture](../day05/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day07/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 05](../day05/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Calculate arithmetic intensity.
- Use a roofline bound.

## Lecture notes

Arithmetic intensity divides operations by bytes moved at a specified memory boundary. A roofline model bounds achievable throughput by the lower of compute capacity and bandwidth times intensity. It is an upper bound, not a prediction that accounts for every launch, dependency, or communication cost.

## Board example

For hypothetical bandwidth 1 TB/s, compute ceiling 100 TFLOP/s, and intensity 10 FLOP/byte, the bandwidth ceiling is 10 TFLOP/s. The ridge point is 100 FLOP/byte. Raising intensity from 10 to 20 can improve the bound without changing peak compute.

## Notebook lab

- [ops-byte-ratio](./ops-byte-ratio.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Estimate FLOPs and transferred bytes for one matrix multiplication. Sweep batch size and compare measured performance with the bound. State whether you count weight, activation, and output traffic.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
