# Day 29 — Lecture 29: Client Code: Streaming, Async & Protocol Support

[Previous lecture](../day28/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day30/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 01](../day01/LECTURE.md), [Day 24](../day24/LECTURE.md), [Day 28](../day28/LECTURE.md).

## Learning objectives

- Implement streaming lifecycle handling.
- Bound asynchronous request concurrency.

## Lecture notes

A streaming client receives incremental events, not necessarily one token per network read. Network chunks may split an event or contain several events. Parsing must retain incomplete data, decode text incrementally, and distinguish ordinary data from terminal or error events. Time to first byte, first event, and first generated token are different measurements.

Client concurrency can saturate connection pools, server queues, or memory. Set an explicit bound and timeouts for connection, inactivity, and overall request duration. Cancellation should release the connection and notify the server when supported. Retrying after partial output can repeat computation and duplicate text; make that behavior explicit rather than silently appending a new generation.

## Board example

At concurrency 8 and average request time 2 seconds, an ideal closed-loop client completes about 4 requests/s. Raising concurrency to 80 does not imply 40 requests/s if the server is already saturated; it may mainly lengthen queues.

## Lab procedure

Build a mock stream that splits a multibyte character and an event across reads. Exercise success, timeout, disconnect, and cancellation. Then run ten mock requests through a concurrency limit of three and record peak in-flight work.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the parser state diagram and lifecycle tests.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which errors can be retried before output and which require exposing an interrupted result.

## Further reading

- [Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)
- [aiohttp client guide](https://docs.aiohttp.org/en/stable/client_quickstart.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
