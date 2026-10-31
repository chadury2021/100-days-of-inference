# Day 76 — Lecture 76: End-to-end latency breakdown: tokenization → TTFT → TBT → detokenization

[Previous lecture](../day75/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day77/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 27](../day27/LECTURE.md), [Day 65](../day65/LECTURE.md), [Day 68](../day68/LECTURE.md).

## Learning objectives

- Define disjoint stage intervals.
- Reconcile client and server clocks.

## Lecture notes

Client-observed latency includes transport, queueing, tokenization, prefill, token selection, decode, serialization, and delivery. Some stages overlap, so a decomposition must identify disjoint intervals or explicitly model a critical path. Time to first token already contains earlier stages and must not be added to them again as an independent component.

Use a consistent client monotonic clock for send, first content, and terminal event. Server spans explain internal time but may use different clocks. Separate time to first byte from first generated content, and note that a stream event can contain multiple tokens. Average token time inferred from totals is not a full distribution of inter-token gaps.

## Board example

For a request with TTFT 120 ms and four further token gaps [20,30,20,30] ms, terminal content arrives at 220 ms, excluding any later completion metadata. If tokenization took 10 ms inside TTFT, adding it again would incorrectly report 230 ms.

## Lab procedure

Instrument a mock or lab request with client events and server stage spans. Reconcile the timeline, mark overlap, and explain any unaccounted interval. Repeat with network buffering and one queue delay.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a latency waterfall and clock-boundary definitions.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why per-token averages can hide a long pause in the middle of a response.

## Further reading

- [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
