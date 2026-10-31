# Day 88 — Lecture 88: EAGLE speculative decoding: feature-level draft vs token-level

[Previous lecture](../day87/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day89/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 15](../day15/LECTURE.md), [Day 38](../day38/LECTURE.md), [Day 73](../day73/LECTURE.md).

## Learning objectives

- Explain feature-based proposals.
- Evaluate a compatible draft mechanism.

## Lecture notes

EAGLE explores drafting from target-model features rather than treating the draft as only an independent smaller language model. Its proposal mechanism must be paired with compatible target features, token conditioning, and verification. A generic small model is not an interchangeable EAGLE adapter. Pin the method version because variants change implementation details.

Separate the proposal mechanism from the acceptance procedure. Preserving the target sampling distribution requires the appropriate verification and correction, not merely high feature prediction accuracy. Evaluate end-to-end time, committed progress, and extra memory on a fixed target and workload. Learned adapters introduce their own training and compatibility costs.

## Board example

Suppose feature drafting costs 3 ms and verification 9 ms, with an average of three committed tokens per cycle. Effective cost is 4 ms/token. Against a 6 ms/token target-only baseline, speedup is 1.5×. At two committed tokens, the same configuration only breaks even.

## Lab procedure

Read the original method and draw the feature/token dependencies. If a compatible supported checkpoint is available, benchmark it against target-only decoding; otherwise simulate the cost model across committed lengths and label the result analytical.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the dependency diagram, compatibility assumptions, and speedup curve.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why feature prediction error and accepted-token progress are different metrics.

## Further reading

- [EAGLE paper](https://arxiv.org/abs/2401.15077)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
