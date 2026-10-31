# Day 41 — Lecture 41: Simulate tensor parallelism: split a matmul across N workers

[Previous lecture](../day40/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day42/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 17](../day17/LECTURE.md), [Day 32](../day32/LECTURE.md).

## Learning objectives

- Derive row and column partitioning.
- Identify required collectives.

## Lecture notes

For Y=XW, splitting W by output columns produces independent output slices that can be concatenated. Splitting the contracted dimension instead requires matching slices of X and summing partial products. These are different communication patterns. A distributed model alternates compatible layouts to avoid unnecessary gathering between every operation.

A CPU or single-process simulation verifies algebra but does not measure network scaling. Real costs include launch synchronization, collective latency, transfer volume, and imbalance. Keep a reference matrix multiplication and compare outputs within tolerance because different reduction orders may change floating-point rounding.

## Board example

For X=[2,3] and W=[[1,4],[5,6]], Y=[17,26]. Column shards return [17] and [26]. Contracted-dimension shards produce [2,8] and [15,18], whose sum is [17,26]. Concatenating the latter would be incorrect.

## Lab procedure

Implement both decompositions for random matrices, including dimensions not divisible by the worker count. Record shard shapes and the bytes needed for each gather or reduction. Add a configurable communication delay model.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit equality checks and predicted speedup versus workers.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why smaller local matrix multiplications can reduce compute efficiency.

## Further reading

- [PyTorch distributed execution](https://docs.pytorch.org/docs/stable/distributed.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
