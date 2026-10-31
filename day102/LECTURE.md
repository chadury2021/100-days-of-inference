# Day 102 — Lecture 102: Reflect: what I learned, what I'd do differently, what's next

[Previous lecture](../day101/LECTURE.md) · [Course schedule](../LECTURES.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 97](../day97/LECTURE.md), [Day 98](../day98/LECTURE.md), [Day 101](../day101/LECTURE.md).

## Learning objectives

- Present reproducible evidence.
- Distinguish demonstrated results from future work.

## Lecture notes

A final report should make the system understandable and its claims auditable. Restate the use case and targets, describe the implemented design, and present baseline versus final results under the same workload. Include failed experiments when they explain a tradeoff or prevent repeated mistakes. Separate measured outcomes, analytical estimates, and unimplemented ideas.

Reproducibility requires artifact versions, environment details, fixtures, commands, and result files. A reader should be able to locate the evidence behind each claim. Discuss limitations such as small evaluation sets, unavailable hardware, simulated failure behavior, or narrow prompt distributions. Use these limits to prioritize the next experiment rather than promising unsupported generality.

## Board example

If throughput improves from 100 to 140 tokens/s while p95 TTFT rises from 80 to 130 ms against a 100 ms target, the final configuration fails that target. A balanced defense reports the 40% throughput gain and the latency regression, then chooses a compliant operating point.

## Lab procedure

Prepare a ten-minute defense with problem, architecture, experiment design, results, failures, and next steps. Re-run the documented smoke path from a clean environment or have a peer follow it. Archive the exact manifests and evaluation outputs.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the final report, reproduction guide, and evidence index.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain the strongest conclusion supported by your experiments and one attractive claim the evidence does not support.

## Further reading

- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
