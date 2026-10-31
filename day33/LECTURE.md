# Day 33 — Lecture 33: Implement Flash Attention (simplified, tiling in Python)

[Previous lecture](../day32/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day34/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 06](../day06/LECTURE.md), [Day 32](../day32/LECTURE.md).

## Learning objectives

- Derive an online softmax update.
- Avoid materializing the full score matrix.

## Lecture notes

Tiling processes score blocks while maintaining per-query running statistics. Store a running maximum m, exponential sum l, and unnormalized weighted-value sum u. For a new block with scores s and values V, set m′=max(m,max(s)), rescale old l and u by exp(m−m′), and add exp(s−m′) and its value-weighted sum. The final output is u/l.

This is exact attention algebra up to floating-point roundoff; it does not approximate attention by dropping keys. A Python implementation teaches the recurrence but cannot claim the GPU memory traffic or speed of a fused FlashAttention kernel. Apply causal masks within each tile, and skip fully masked tiles so the initial negative-infinity state does not create NaNs.

## Board example

Two scalar score blocks [0] and [ln(3)] with values [2] and [6] give m=ln(3), l=1/3+1=4/3, and u=2/3+6=20/3. Dividing gives 5, matching the dense calculation from Day 32.

## Lab procedure

Implement tiled forward attention with running statistics. Compare several tile sizes against the Day 32 reference, including extreme logits and a non-divisible sequence length. Track the largest temporary score tensor.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the update derivation, correctness results, and temporary-memory estimate.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a slower Python implementation can still demonstrate a better memory algorithm.

## Further reading

- [FlashAttention paper](https://arxiv.org/abs/2205.14135)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
