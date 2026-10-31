# Day 69 — Lecture 69: Async batch inference client using `asyncio` + `aiohttp`

[Previous lecture](../day68/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day70/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 29](../day29/LECTURE.md), [Day 68](../day68/LECTURE.md).

## Learning objectives

- Reuse connections.
- Preserve per-request results under partial failure.

## Lecture notes

Use a shared client session and an explicit concurrency limit to avoid opening a new connection pool for every request. Bound the number of queued tasks as well as active network operations for large datasets. A semaphore around network work does not by itself prevent allocating millions of pending coroutine objects.

Give each input a stable index and store its outcome independently of completion order. Timeouts, cancellations, and parsing failures should produce structured results rather than silently disappearing. Retry only according to a stated policy, with bounded attempts and backoff; an ambiguous timeout may already have consumed server work. Cleanup must close responses and release permits on every path.

## Board example

With 1,000 inputs, concurrency 10, and 0.5-second mean service time, an ideal no-overhead lower bound is about 50 seconds. A worker-pool design can keep only ten active requests plus a bounded input queue instead of 1,000 live tasks.

## Lab procedure

Implement a producer and fixed worker pool against a mock HTTP endpoint. Inject latency, HTTP errors, malformed payloads, and cancellation. Verify output order by input ID and that active requests never exceed the configured bound.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit result records and peak concurrency/memory observations.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how you prevent retries from duplicating final results.

## Further reading

- [aiohttp client guide](https://docs.aiohttp.org/en/stable/client_quickstart.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
