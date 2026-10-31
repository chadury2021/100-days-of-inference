# Day 56 — Lecture 56: Measure cold start latency: model load times at different sizes

[Previous lecture](../day55/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day57/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 22](../day22/LECTURE.md), [Day 27](../day27/LECTURE.md), [Day 53](../day53/LECTURE.md).

## Learning objectives

- Decompose startup latency.
- Compare genuinely cold and cached conditions.

## Lecture notes

Cold start consists of several possible stages: scheduling, image transfer, process initialization, model artifact transfer, deserialization, device placement, compilation, and warmup. Some overlap and some disappear on a cached host. Record each boundary rather than attributing the whole interval to model loading.

Define cold precisely. Restarting a process while the model remains in the filesystem cache is not an uncached download test. Repeat trials, record cache conditions, and avoid clearing shared caches merely to obtain a measurement. Use isolated test directories or fresh workers where available. A startup succeeds only when the documented readiness contract is met.

## Board example

If download takes 40 seconds and initialization takes 10 after download, readiness cannot precede 50 seconds. If a later run uses cached weights and takes 12 seconds, the apparent 4.17× improvement describes cache state, not necessarily a faster loader.

## Lab procedure

Measure a small and larger available model under process-cold and artifact-cached conditions. Collect stage timestamps and first successful inference. If the hardware cannot fit a model, report that constraint rather than extrapolating a load time.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit stacked timelines and a startup definition.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which optimizations reduce image, artifact, and device initialization costs respectively.

## Further reading

- [PyTorch benchmarking](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
