# Day 46 — Lecture 46: Deploy vLLM on spark-01, benchmark TTFT and throughput

[Previous lecture](../day45/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day47/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 09](../day09/LECTURE.md), [Day 27](../day27/LECTURE.md), [Day 29](../day29/LECTURE.md).

## Learning objectives

- Establish a reproducible serving baseline.
- Measure latency under controlled load.

## Lecture notes

A serving benchmark includes frontend parsing, scheduling, model execution, and transport. Record the exact runtime and model revision, available memory, numerical format, and request distribution. Check the selected model and runtime against the actual Spark software stack before installation; a CPU-only analytical exercise cannot establish GPU throughput.

Begin with one request to establish correctness and a low-load baseline. Then increase offered concurrency while keeping prompt and output distributions fixed. Report failures and queue growth alongside successful throughput. Time-to-first-token and inter-token gaps must be measured from the stream, accounting for possible event buffering.

## Board example

If 100 successful requests each produce 50 output tokens over a 10-second measurement interval, aggregate output throughput is 500 tokens/s. This does not imply that each request receives a token every 2 ms; concurrency and scheduling determine individual gaps.

## Lab procedure

On an available supported host, follow the pinned runtime’s official serving guide, load a small model, and replay a fixed fixture at concurrency 1, 2, 4, and 8. Save startup logs, configuration, and raw per-request events.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit correctness samples and latency/throughput curves. If execution is unavailable, submit the launch manifest and analytical capacity worksheet without reporting a measured benchmark.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Which assumption in the vllm serving experiment example most strongly affects its conclusion?

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
