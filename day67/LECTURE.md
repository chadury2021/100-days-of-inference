# Day 67 — Lecture 67: Profile with Nsight Systems: identify kernel launch overhead

[Previous lecture](../day66/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day68/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 07](../day07/LECTURE.md), [Day 43](../day43/LECTURE.md).

## Learning objectives

- Identify launch gaps and synchronization.
- Validate a critical-path optimization.

## Lecture notes

A system timeline relates host activity, runtime calls, device kernels, and transfers. Focus capture on a warmed representative region to avoid drowning the question in initialization. Add stage markers so a cluster of kernels can be tied back to prefill, decode, or data movement. Observe both the host and device before blaming kernel duration.

Launch overhead matters when useful kernels are short and separated by host-side gaps. Synchronization can serialize otherwise independent work, but apparent empty device time may also reflect dependencies or missing instrumentation. A system profiler identifies where to investigate; detailed kernel efficiency may require another tool. Measure the final improvement without capture overhead.

## Board example

Suppose each step has 20 kernels of 5 microseconds plus 20 non-overlapped launch gaps of 5 microseconds. The simplified total is 200 microseconds, half in gaps. Removing half the kernels and gaps gives 100 microseconds only if the fused kernels retain the assumed total work behavior.

## Lab procedure

Capture a short decode loop with Nsight Systems on supported hardware. Identify one launch-bound or synchronization-heavy region. Compare a batched or compiled variant and remeasure normal execution outside the profiler.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit an annotated timeline, hypothesis, and unprofiled comparison.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

State which intervals overlap and which are serialized.

## Further reading

- [Nsight Systems user guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
