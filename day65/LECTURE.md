# Day 65 — Lecture 65: Add distributed tracing (OpenTelemetry) to an inference request

[Previous lecture](../day64/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day66/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 28](../day28/LECTURE.md), [Day 63](../day63/LECTURE.md).

## Learning objectives

- Propagate request context.
- Interpret overlapping spans.

## Lecture notes

A trace links spans across client, router, scheduler, model worker, and response transport. Propagate the context through queued work and asynchronous tasks; otherwise the slow stage may appear as an unrelated root trace. Record stage names, timing, bounded attributes, and terminal status without copying prompt content into routine traces.

Parent-child duration is not additive when children overlap. Trace sampling can omit rare slow requests, so select a strategy consistent with the diagnostic goal and record its limits. Cross-host wall clocks can skew apparent order; use per-process monotonic durations and treat distributed timestamps carefully. A span around an async launch may not measure completed device work.

## Board example

Two child operations lasting 40 and 60 ms start together, and the parent waits for both. Their combined critical-path contribution is 60 ms, not 100 ms. A further 10 ms of serialized response work yields a 70 ms parent duration.

## Lab procedure

Trace a mock router-to-worker request with a queue stage and a streaming response. Inject a delayed worker and a cancelled client. Verify context propagation and that spans end on both normal and exceptional paths.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit two trace timelines and a critical-path explanation.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Identify which timing still requires device-level instrumentation.

## Further reading

- [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
