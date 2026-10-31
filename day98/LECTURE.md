# Day 98 — Lecture 98: Design: sketch the full inference stack for a real use case

[Previous lecture](../day97/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day99/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 61](../day61/LECTURE.md), [Day 77](../day77/LECTURE.md), [Day 97](../day97/LECTURE.md).

## Learning objectives

- Translate a use case into measurable requirements.
- Select a defensible serving design.

## Lecture notes

Choose one concrete application such as document extraction, a local assistant, or embedding retrieval. Define workload distributions, quality acceptance, latency targets, maximum concurrency, and available hardware. Scope the first version tightly enough to measure. A design is incomplete if it lists components without explaining why their capacities and interfaces fit the workload.

Draw the request path from client through admission, serving, and observation. Estimate weight, KV, and workspace memory, then forecast capacity using measured baselines or clearly labeled assumptions. Define overload, timeout, cancellation, and rollback behavior. Identify the largest uncertainty and design a small experiment to resolve it before adding complexity.

## Board example

If expected arrivals are 5 requests/s and mean time in system is 2 seconds, stable mean concurrency is 10. A design targeting only two concurrent requests cannot satisfy that workload without changing service time, queueing, or rejection behavior.

## Lab procedure

Write a two-page design using results from earlier lectures. Include a component diagram, capacity worksheet, model/runtime manifest, three failure scenarios, and an acceptance table with numeric targets.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the design and a prioritized implementation plan.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which choice you would revisit first if prompt lengths doubled.

## Further reading

- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
