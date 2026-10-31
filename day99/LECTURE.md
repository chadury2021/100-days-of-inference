# Day 99 — Lecture 99: Build: FastAPI + vLLM inference server with health checks and metrics

[Previous lecture](../day98/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day100/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 53](../day53/LECTURE.md), [Day 63](../day63/LECTURE.md), [Day 68](../day68/LECTURE.md), [Day 98](../day98/LECTURE.md).

## Learning objectives

- Build a minimal request path.
- Expose readiness, metrics, and bounded admission.

## Lecture notes

Implement the designed service using a small API layer and a supported inference runtime. Keep model execution ownership clear: an API wrapper should not accidentally load a second model copy or block its event loop with synchronous heavy work. Validate input limits and map runtime failures into a documented response contract.

Add readiness, liveness, bounded admission, timeouts, and streaming cancellation as part of the request lifecycle. Metrics should reconcile arrivals, terminal outcomes, and in-flight work. Use a mock runtime adapter to test failure behavior without requiring expensive model execution. A successful endpoint demo does not establish load capacity or rollout safety yet.

## Board example

With a queue limit of 20 and two active slots, the twenty-third simultaneous request cannot be silently accepted into an unbounded internal queue. Define whether it receives a retryable rejection or another documented response, and include it in metrics.

## Lab procedure

Build the API and runtime adapter, then exercise success, oversized input, queue saturation, timeout, cancellation, and unavailable-model cases. Run a small inference smoke fixture when the supported runtime is available.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit source, launch instructions, API examples, and lifecycle test results.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how disconnecting a streaming client releases server-side work.

## Further reading

- [FastAPI asynchronous execution](https://fastapi.tiangolo.com/async/)
- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
