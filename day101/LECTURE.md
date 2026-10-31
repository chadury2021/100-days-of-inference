# Day 101 — Lecture 101: Optimize: run the benchmark harness, find the bottleneck, fix it

[Previous lecture](../day100/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day102/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 52](../day52/LECTURE.md), [Day 71](../day71/LECTURE.md), [Day 77](../day77/LECTURE.md), [Day 100](../day100/LECTURE.md).

## Learning objectives

- Choose a bottleneck from evidence.
- Validate a single controlled improvement.

## Lecture notes

Use the benchmark harness and traces to identify the dominant constraint under the capstone workload. Optimize one cause at a time: scheduling, prefix reuse, quantization, kernel execution, or client behavior. State the expected effect before running the experiment. Keep the original baseline and preserve quality, workload, and resource accounting across comparisons.

Evaluate the whole service after a local improvement. A faster kernel may move the bottleneck to tokenization or networking, and a larger batch may improve throughput while violating latency. Repeat measurements and inspect failures. Reject a change that improves one headline metric by changing the task or hiding bad outcomes.

## Board example

If model execution accounts for 60% of end-to-end time and an optimization halves it, the ideal overall speedup is 1/(0.4+0.6/2)=1.43×. A claimed 2× end-to-end gain needs an additional explanation beyond that kernel improvement.

## Lab procedure

Select one bottleneck, predict its maximum benefit, implement one change, and rerun the frozen acceptance workload. Compare quality, p95 TTFT, throughput, peak memory, cost model, and failures with the baseline.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the hypothesis, patch, raw results, and retain-or-revert decision.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain the next bottleneck and whether another optimization is worthwhile.

## Further reading

- [PyTorch benchmarking](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
