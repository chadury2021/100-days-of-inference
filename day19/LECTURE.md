# Day 19 — Lecture 19: GPU Architecture: SMs, Memory Hierarchy, HBM

[Previous lecture](../day18/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day20/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 18](../day18/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Trace the memory hierarchy.
- Distinguish capacity, bandwidth, and latency.

## Lecture notes

GPU execution distributes work across streaming multiprocessors. Registers and shared memory support local reuse, while larger memory levels serve broader access. Coalescing and locality change how much useful data is delivered. Occupancy can help hide latency but is not an optimization objective independent of actual throughput.

## Board example

Reading 1 GiB over a hypothetical sustained 500 GiB/s path takes at least 2 ms. Reading the same array twice doubles traffic if no cache reuse occurs. A kernel may still take longer because of dependencies, launch overhead, or inefficient accesses.

## Notebook lab

- [gpu-architecture-sms-hbm](./gpu-architecture-sms-hbm.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Profile contiguous and strided accesses at multiple sizes. Compare measured bandwidth and explain whether the working set fits a cache. Identify the memory system of the actual device instead of assuming every GPU uses HBM.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
