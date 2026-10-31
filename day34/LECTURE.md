# Day 34 — Lecture 34: Profile attention memory growth across sequence lengths

[Previous lecture](../day33/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day35/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 05](../day05/LECTURE.md), [Day 33](../day33/LECTURE.md).

## Learning objectives

- Separate quadratic scores from linear KV storage.
- Measure peak memory correctly.

## Lecture notes

Dense score materialization uses B×H×S×S elements, while KV storage grows with B×L×S×Hkv×d. These are different tensors with different lifetimes. An efficient attention backend can avoid a full score matrix but still needs keys and values. Model weights add a largely sequence-independent baseline.

Measure allocated and reserved memory separately, reset peak statistics for each run, and release tensors between configurations. Backend selection, dtype, and gradients affect results. A memory slope is meaningful only when those conditions remain fixed. Unified-memory systems require additional care because physical memory is shared and device accounting may differ from a discrete GPU.

## Board example

For batch 1, 8 heads, S=2,048, and two-byte scores, the score tensor alone is 64 MiB. Doubling S produces 256 MiB. A fixed-architecture KV cache instead doubles when sequence length doubles.

## Lab procedure

Sweep sequence lengths with the dense reference and tiled implementation. Record predicted score bytes, peak allocation, reserved memory, and selected backend. If no GPU is available, report analytical tensor sizes and CPU measurements separately.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a log-log plot and explain any discontinuities.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Identify which measurements include weights, temporary buffers, and allocator reserves.

## Further reading

- [PyTorch CUDA memory management](https://docs.pytorch.org/docs/stable/notes/cuda.html#cuda-memory-management)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
