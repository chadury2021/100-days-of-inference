# Day 77 — Lecture 77: Build a reusable inference benchmark harness

[Previous lecture](../day76/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day78/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 27](../day27/LECTURE.md), [Day 66](../day66/LECTURE.md), [Day 76](../day76/LECTURE.md).

## Learning objectives

- Define a stable experiment schema.
- Preserve raw results and failures.

## Lecture notes

A benchmark harness separates workload specification, transport adapter, execution scheduling, event recording, and analysis. Keep these boundaries small and concrete rather than building a general orchestration framework. Store enough metadata to reproduce the experiment: model revision, runtime, hardware, configuration, input IDs, timing conventions, and source revision.

Raw per-request events should remain immutable inputs to summaries. Record requested and actual token counts, terminal outcome, and timing fields with units. The analyzer should reject incompatible comparisons or missing required metadata. Timeouts and malformed streams are results, not reasons to silently shrink the denominator. Seed synthetic workloads and save the generated fixture.

## Board example

If run A uses 100 requests with 100 output tokens each and run B uses 100 requests with 20 tokens each, comparing requests/s alone favors a different task. A harness can flag the mismatch before drawing a speed conclusion.

## Lab procedure

Combine the Day 69 client, Day 68 parser, and Day 27 analysis into a small command-line experiment runner. Add a mock transport for deterministic failure and timing fixtures, then run one real supported endpoint if available.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a sample manifest, raw result file, summary, and reproduction command.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Demonstrate that partial failures survive into the final report.

## Further reading

- [PyTorch benchmarking](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
