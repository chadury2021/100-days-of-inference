# Day 35 — Lecture 35: Build an INT8 quantization pipeline: quantize → dequantize → measure error

[Previous lecture](../day34/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day36/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 13](../day13/LECTURE.md), [Day 32](../day32/LECTURE.md).

## Learning objectives

- Implement symmetric quantize/dequantize.
- Diagnose clipping and scale granularity.

## Lecture notes

For a symmetric signed INT8 teaching scheme, choose s=max(abs(x))/127, round x/s, and clamp to [−127,127]. Reconstruct with x̂=sq. Use a defined scale such as 1 for an all-zero group. This convention deliberately leaves −128 unused and must match the chosen implementation.

Per-tensor scaling shares one scale across all values; per-channel scaling can preserve small channels in the presence of outliers. Reconstruction error is only a local proxy: downstream output error also depends on activation directions. Storing integer weights and dequantizing before an ordinary floating-point operation demonstrates compression error, not accelerated INT8 inference.

## Board example

With maximum magnitude 12.7, s=0.1. Values [−0.26,0,0.24] quantize to [−3,0,2] and reconstruct to [−0.3,0,0.2]. The maximum absolute error is 0.04. A zero tensor should reconstruct exactly without division by zero.

## Lab procedure

Implement both scale granularities, then inject one large outlier. Measure storage including scales, mean-square error, maximum error, and the error of a small linear layer on held-out inputs.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the pipeline and a granularity comparison.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why dtype storage and kernel arithmetic are separate claims.

## Further reading

- [GPTQ: quantization and reconstruction objectives](https://arxiv.org/abs/2210.17323)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
