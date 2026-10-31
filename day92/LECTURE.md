# Day 92 — Lecture 92: Dynamic disaggregation with NVIDIA Dynamo

[Previous lecture](../day91/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day93/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 49](../day49/LECTURE.md), [Day 55](../day55/LECTURE.md), [Day 91](../day91/LECTURE.md).

## Learning objectives

- Model worker-role transitions.
- Account for migration and warmup costs.

## Lecture notes

Dynamic allocation changes the balance between prefill and decode resources as workload composition changes. The controller must observe queue pressure, estimate capacity, and account for transition time. A worker cannot be reassigned as though active requests and model state disappear instantly. Draining, loading, cache movement, and readiness belong in the state machine.

Use hysteresis or minimum residence time to avoid repeatedly paying transition cost in response to noisy demand. Backend capabilities determine which transitions are supported; consult the pinned Dynamo release before implementing a real controller. A static split is the baseline, and a zero-cost transition simulator is only an optimistic bound.

## Board example

Moving a worker costs 30 seconds, and the new role saves 2 seconds of aggregate waiting per second during a sustained phase. A simple payback estimate is 15 seconds of useful operation after transition, but if the workload switches back immediately, the migration produces no useful return.

## Lab procedure

Simulate alternating prompt-heavy and decode-heavy intervals with nonzero transition delay. Compare fixed allocation, instantaneous reallocation, and a draining-aware controller. Track active, draining, loading, and ready worker states.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit queue curves, role timelines, and transition cost.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how the controller prevents capacity from being counted in both roles at once.

## Further reading

- [Dynamo documentation and release selection](https://docs.nvidia.com/dynamo/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
