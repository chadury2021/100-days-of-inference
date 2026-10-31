# Day 28 — Lecture 28: Observability: Metrics, Tracing & Dashboards

[Previous lecture](../day27/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day29/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 24](../day24/LECTURE.md), [Day 27](../day27/LECTURE.md).

## Learning objectives

- Choose useful metrics and spans.
- Diagnose an inference slowdown.

## Lecture notes

Metrics summarize behavior over time, traces show the stages of individual requests, and logs record discrete events. Use each for a question it can answer: a queue gauge shows backlog, a duration histogram shows distribution, and a trace locates waiting within a request. Counters must increase monotonically between restarts; gauges may rise or fall.

Observe arrival rate, completions, failures, queue depth, active requests, and stage durations together. A GPU can be busy while user-visible service deteriorates. Keep metric labels bounded: request IDs and full prompts belong neither in label sets nor routine telemetry. Histograms allow aggregation across replicas when bucket boundaries agree; averaging replica percentiles does not yield a fleet percentile.

## Board example

Two workers report p95 values of 20 ms and 200 ms but process 1,000 and 10 requests respectively. Their average, 110 ms, is not the fleet p95. Merge compatible histogram counts or raw observations before calculating the fleet statistic.

## Lab procedure

Instrument a simulated queue with arrivals, admissions, first-token events, completions, and failures. Introduce a slower service stage and draw the resulting queue-depth and latency curves on the same time axis.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a signal-to-question table and three incident diagnoses.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Identify which observation distinguishes slow model execution from slow admission.

## Further reading

- [Prometheus instrumentation](https://prometheus.io/docs/practices/instrumentation/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
