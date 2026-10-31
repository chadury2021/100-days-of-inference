# Day 43 — Lecture 43: CUDA profiling: profile a PyTorch model with `torch.profiler`

[Previous lecture](../day42/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day44/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 07](../day07/LECTURE.md), [Day 27](../day27/LECTURE.md).

## Learning objectives

- Capture a representative trace.
- Map operators to a critical-path hypothesis.

## Lecture notes

Profiling introduces overhead and can alter scheduling. Use a short representative window after warmup, include CPU and supported device activities, and label request stages. Operator self time excludes child operations; total time can overlap across threads or streams, so summing all durations does not necessarily equal elapsed wall time.

Begin with a question such as whether repeated small launches dominate decode. Examine shapes and call counts, then locate synchronization and gaps. A high-duration operator is a candidate, not proof of the system bottleneck. Confirm the hypothesis by changing one cause and measuring the unprofiled workload again.

## Board example

Suppose a 40 ms request includes 10 ms of CPU preparation overlapping 8 ms of GPU work, followed by 30 ms of serialized GPU work. Summed CPU-plus-GPU duration is 48 ms, while the critical path is 40 ms. Overlap explains the discrepancy.

## Lab procedure

Capture a short trace of the Day 31 decode loop with labeled prefill and decode regions. Compare uncached and cached operation counts. If GPU activity is unavailable, perform the CPU trace and state that limitation.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a trace screenshot or exported trace plus a before/after measurement.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why profiling a cold first call would answer a different question.

## Further reading

- [PyTorch profiler recipe](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
