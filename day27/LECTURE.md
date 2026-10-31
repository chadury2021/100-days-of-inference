# Day 27 — Lecture 27: Performance Benchmarking: Tooling & Profiling

[Previous lecture](../day26/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day28/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 06](../day06/LECTURE.md), [Day 07](../day07/LECTURE.md), [Day 26](../day26/LECTURE.md).

## Learning objectives

- Define a reproducible workload.
- Distinguish device time from user-visible latency.

## Lecture notes

A benchmark answers a specific question under a specified workload. Fix prompt lengths, generated lengths, arrival process, model revision, precision, and stopping rules before comparing implementations. Warmup changes the experiment by excluding initialization; keep a separate cold-start measurement. GPU execution is asynchronous, so a host timer around a launch can measure submission rather than completion.

Latency percentiles describe a distribution, while aggregate throughput counts completed work over a common interval. A closed-loop client waits for responses before issuing more work and can hide overload by reducing its own arrival rate. An open-loop generator schedules arrivals independently and must retain failures and unfinished requests in its report. Use profiling to explain a measured effect, then repeat performance measurements without heavy tracing.

## Board example

For sorted request latencies [10,11,12,13,100] ms, the mean is 29.2 ms and the median is 12 ms. Under the nearest-rank convention, p95 is 100 ms. State your percentile convention and sample count; five requests cannot establish a stable production tail.

## Lab procedure

Create a fixed 20-prompt fixture with short and long groups. Run warmup separately, collect at least 100 measured requests per configuration, and record timestamps and outcomes. Compare one configuration change using repeated runs; preserve timeouts rather than dropping them.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the workload manifest, raw timings, percentile table, and one profiler hypothesis.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a lower median with more failed requests might be a regression.

## Further reading

- [PyTorch benchmarking](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
