# Day 72 — Lecture 72: Benchmark quantization levels on real throughput: FP16 vs INT8 vs INT4

[Previous lecture](../day71/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day73/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 13](../day13/LECTURE.md), [Day 37](../day37/LECTURE.md), [Day 46](../day46/LECTURE.md).

## Learning objectives

- Compare supported precisions fairly.
- Enforce quality and latency constraints.

## Lecture notes

Precision changes affect weight traffic, activation processing, dequantization, kernel choice, and numerical behavior. A smaller checkpoint does not guarantee faster execution. Verify that each runtime path actually uses the intended optimized kernels; a floating-point fallback may preserve output while defeating the expected acceleration.

Hold model family, input/output distribution, and serving resources fixed. Evaluate a reference, INT8, and INT4 only where supported, recording any non-quantized layers and scale overhead. Keep a task-quality floor and latency objective so performance is not improved by accepting unusable results. Report both single-request latency and saturated useful throughput.

## Board example

Suppose FP16 delivers 1,000 useful tokens/s and INT4 delivers 900 despite smaller weights. If INT4 adds dequantization overhead or selects a less efficient kernel for the tested shape, the result is plausible. Storage compression alone cannot override that measurement.

## Lab procedure

Run a fixed fixture across supported precisions with warmup and repeated trials. Capture artifact size, peak memory, quality pass rate, p95 TTFT, and useful output tokens/s. Inspect the selected runtime path when a result is surprising.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a precision Pareto table and one causal explanation supported by profiling. Mark unsupported configurations rather than filling their cells with projections.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Which assumption in the real quantized throughput example most strongly affects its conclusion?

## Further reading

- [GPTQ: quantization and reconstruction objectives](https://arxiv.org/abs/2210.17323)
- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
