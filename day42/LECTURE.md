# Day 42 — Lecture 42: Benchmark ops:byte ratio in practice across matrix sizes

[Previous lecture](../day41/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day43/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 06](../day06/LECTURE.md), [Day 41](../day41/LECTURE.md).

## Learning objectives

- Estimate matrix traffic.
- Explain deviations from roofline predictions.

## Lecture notes

For a dense M×K by K×N product, count about 2MKN floating-point operations. A simple single-read traffic model is b(MK+KN+MN) bytes, where b is bytes per element and the output is written once. This is a lower-bound model; cache behavior, repeated reads, and implementation details change actual traffic.

Sweep shapes independently rather than treating matrix size as one scalar. Skinny decode-like products can have low reuse despite large weights. Align dtype and arithmetic conventions with the compute ceiling: counting sparse or mixed-precision peak rates against a different operation produces misleading efficiency claims.

## Board example

For M=1, K=N=1,024 and b=2, FLOPs are 2,097,152 and ideal traffic is 2,101,248 bytes, about 1 FLOP/byte. Increasing M allows the same weight matrix to serve more rows, raising reuse if the implementation can exploit it.

## Lab procedure

Benchmark a grid of M, K, and N values with warmup and synchronized timing. Plot achieved FLOP/s against estimated intensity and annotate shapes that perform poorly relative to neighboring points.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the operation/byte derivation and measured plot.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain whether the traffic estimate represents cache, device memory, or an analytical lower bound.

## Further reading

- [PyTorch benchmarking](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
