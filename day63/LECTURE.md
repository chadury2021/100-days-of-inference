# Day 63 — Lecture 63: Emit Prometheus metrics from an inference server

[Previous lecture](../day62/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day64/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 28](../day28/LECTURE.md), [Day 53](../day53/LECTURE.md).

## Learning objectives

- Choose counters, gauges, and histograms.
- Keep metrics internally consistent.

## Lecture notes

Instrument arrivals, completions, and errors as counters; current queue depth and in-flight requests as gauges; and durations as histograms. Decide whether completion counters include failures and keep names or labels consistent with that definition. Time units should be explicit. Observe latency at a lifecycle boundary that occurs on all relevant outcomes.

Bound label cardinality with a small set of model versions, outcomes, or service classes. User IDs, request IDs, and prompt text produce unbounded series and are unsuitable metric labels. On cancellation or exception, decrement gauges in a guaranteed cleanup path. In a multiprocess service, configure collection according to the client library’s documented process model.

## Board example

Over an interval, 100 requests arrive, 90 succeed, 5 fail, and 5 remain active. If the system began empty, arrivals minus terminal completions equals 5 in flight. A counter that counts only successes cannot be used alone to reconcile active work.

## Lab procedure

Instrument a mock server and send a known sequence of successful, failed, and cancelled requests. Scrape its metrics and reconcile arrivals, terminal outcomes, and current gauges. Check that each request observes duration once.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the metric schema, sample exposition, and lifecycle reconciliation.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain what a restart does to counters and how rate calculations should handle it.

## Further reading

- [Prometheus instrumentation](https://prometheus.io/docs/practices/instrumentation/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
