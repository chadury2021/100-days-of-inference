# Day 52 — Lecture 52: Benchmark TTFT vs throughput tradeoff across batch sizes

[Previous lecture](../day51/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day53/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 27](../day27/LECTURE.md), [Day 46](../day46/LECTURE.md), [Day 50](../day50/LECTURE.md).

## Learning objectives

- Construct a Pareto frontier.
- Choose a configuration under an explicit latency target.

## Lecture notes

Batching can improve aggregate throughput while increasing waiting time or per-step latency. Sweep concurrency, scheduling limits, and batch policy one at a time. Distinguish the client’s request batch from the runtime’s internal token batch. Keep prompt and output distributions fixed and include failed or unfinished work in the experiment report.

A point is dominated if another configuration improves one objective without worsening the other. The useful frontier depends on service targets and quality constraints. A throughput maximum that violates an interactive latency target may be unsuitable, even if its utilization is impressive. Report repeated runs because frontier membership may be uncertain near measurement noise.

## Board example

Configurations A, B, and C deliver (100 tokens/s, 50 ms p95 TTFT), (150,70), and (120,90). C is dominated by B. Under a 60 ms target, only A is eligible; under 80 ms, B becomes the higher-throughput eligible choice.

## Lab procedure

Use the Day 46 fixture or Day 50 simulator to sweep at least four load levels. Plot aggregate useful output throughput against p95 TTFT, annotate errors, and mark the latency target before selecting a point.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the frontier and chosen configuration with uncertainty.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why comparing different output-length mixes would invalidate the selection.

## Further reading

- [PyTorch benchmarking](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
