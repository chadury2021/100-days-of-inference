# Day 64 — Lecture 64: Build a Grafana dashboard: TTFT, TBT, queue depth, GPU utilization

[Previous lecture](../day63/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day65/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 28](../day28/LECTURE.md), [Day 63](../day63/LECTURE.md).

## Learning objectives

- Build panels around diagnostic questions.
- Aggregate distributions correctly.

## Lecture notes

A useful dashboard starts with user-visible service health and then shows likely causes. Pair request rate, error rate, and latency with queue depth, active work, cache behavior, and device telemetry. Use consistent time windows and units so correlated changes remain interpretable. An empty panel should distinguish missing telemetry from a genuine zero.

Fleet percentiles require aggregation of compatible histogram buckets before quantile estimation. Do not average replica p95 values. A rate increase can explain a queue rise without any model slowdown, while flat arrivals with rising execution duration suggests a different cause. Annotate deployments and configuration changes to test these hypotheses.

## Board example

Worker A handles 900 fast requests and worker B handles 100 slow ones. Weighting their p95 values by request counts still does not reconstruct the fleet p95; quantiles are nonlinear. The underlying bucket counts or observations are needed.

## Lab procedure

Create a Grafana dashboard specification or local dashboard from Day 63 metrics. Include TTFT, inter-token gaps, completion latency, queue depth, error rate, and device utilization. Replay a burst, a slow worker, and a failed scrape.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit panel definitions and three annotated incident views.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which panels distinguish demand growth from reduced service capacity.

## Further reading

- [Grafana dashboard practices](https://grafana.com/docs/grafana/latest/visualizations/dashboards/build-dashboards/best-practices/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
