# Day 70 — Lecture 70: Multi-cloud routing: geo-aware latency-based request routing

[Previous lecture](../day69/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day71/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 25](../day25/LECTURE.md), [Day 57](../day57/LECTURE.md), [Day 61](../day61/LECTURE.md).

## Learning objectives

- Combine network and queue estimates.
- Preserve constraints during failover.

## Lecture notes

The nearest region by geography is not necessarily the fastest available route. Estimate network delay, queue delay, execution time, and any required artifact or cache transfer. Apply eligibility constraints before scoring regions, including supported model revision and required data placement. A low predicted latency does not override an incompatible backend.

Use health signals with hysteresis so transient failures do not cause rapid oscillation. Stale queue estimates can send many routers to the same apparently idle destination; consider dampening and admission feedback. Failover capacity must be ready or its cold-start delay belongs in the recovery estimate. Keep cross-region transfer costs in the service cost model.

## Board example

Region A has 20 ms network delay and 100 ms queue wait; B has 70 ms network delay and 10 ms wait. With equal execution time, B is 40 ms faster despite being farther away. If B is an incompatible model version, it is ineligible regardless of that score.

## Lab procedure

Simulate two regions with time-varying queues and one outage. Compare nearest-region routing with predicted completion time and constrained failover. Include delayed health updates and cold standby startup.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit per-region assignments, p95 latency, and recovery time.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain a case where stale state reverses the policy ranking.

## Further reading

- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
