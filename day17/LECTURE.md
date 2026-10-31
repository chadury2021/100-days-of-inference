# Day 17 — Lecture 17: Model Parallelism: Tensor, Expert, Pipeline & Data

[Previous lecture](../day16/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day18/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 16](../day16/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Distinguish tensor, pipeline, expert, and data parallelism.
- Model communication.

## Lecture notes

Tensor parallelism partitions tensor operations; pipeline parallelism places layer groups on different workers; expert parallelism distributes mixture-of-experts computation; data parallelism replicates the model across independent requests. Splitting computation introduces communication and coordination, so ideal scaling is an upper bound.

## Board example

If 90% of execution scales perfectly across four devices and 10% remains serial, Amdahl’s bound is 1/(0.1+0.9/4)≈3.08×. Communication lowers this further. Four full replicas can increase serving capacity without lowering the latency of an individual request.

## Notebook lab

- [model-parallelism](./model-parallelism.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Choose a parallelism strategy for a model that exceeds one device’s memory and another that fits. Estimate per-device memory and identify communications. Explain how expert imbalance or pipeline bubbles affect utilization.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
