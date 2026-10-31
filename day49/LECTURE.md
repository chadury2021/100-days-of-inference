# Day 49 — Lecture 49: NVIDIA Dynamo: run a disaggregated prefill experiment

[Previous lecture](../day48/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day50/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 12](../day12/LECTURE.md), [Day 18](../day18/LECTURE.md), [Day 46](../day46/LECTURE.md).

## Learning objectives

- Measure KV-transfer overhead.
- Compare equal-resource serving layouts.

## Lecture notes

Separate prefill and decode workers only after establishing a colocated reference. Keep total device count and workload fixed when comparing layouts; adding hardware changes the question. Instrument admission, prefill execution, transfer readiness, decode admission, and first-token delivery so the transfer is visible rather than buried in one aggregate timer.

Cache handoff must identify the request, model state, and correct token positions. Test a worker failure during transfer and define whether the request is retried, recomputed, or failed. Use the installed Dynamo backend’s documented configuration; support varies with backend and hardware. A network estimate is not a measured transport benchmark.

## Board example

Suppose splitting saves 45 ms of contention but adds 18 ms transfer and 12 ms coordination. The predicted improvement is 15 ms. If transfer doubles under load to 36 ms, the same layout becomes 3 ms slower than the reference.

## Lab procedure

Run or design two equal-resource layouts using a fixed mix of short and long prompts. Sweep network bandwidth in a simulator if physical deployment is unavailable. Produce stage timelines and inspect one interrupted handoff.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the crossover plot, resource accounting, and failure outcome.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which workload change makes separation less attractive.

## Further reading

- [Dynamo documentation and release selection](https://docs.nvidia.com/dynamo/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
