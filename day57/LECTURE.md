# Day 57 — Lecture 57: Implement round-robin and least-connections load balancers

[Previous lecture](../day56/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day58/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 24](../day24/LECTURE.md), [Day 29](../day29/LECTURE.md).

## Learning objectives

- Track active requests correctly.
- Compare round-robin and least-connections.

## Lecture notes

Round-robin assigns arrivals cyclically across eligible backends. Least-connections selects a backend with the fewest active requests, requiring accurate increments at admission and decrements on completion, failure, or cancellation. Tie-breaking should be deterministic for tests. Remove unhealthy backends from eligibility without losing accounting for their in-flight requests.

Connection count may differ from request count under persistent or multiplexed transports. Even accurate active-request counts ignore remaining work: a single long generation can exceed several short jobs. Therefore evaluate both policies on heterogeneous lengths and treat load estimates as approximations. A retry must not leave a phantom active request on the failed backend.

## Board example

If A has two jobs with one second remaining each and B has one ten-second job, least-active-request routing chooses B despite its larger outstanding work. Round-robin may choose either; neither policy uses the information needed to minimize estimated wait.

## Lab procedure

Implement both policies against mock workers with configurable durations. Inject failures and cancellations and assert every active count returns to zero. Compare per-worker assignments and request latency for uniform and mixed jobs.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit policy traces and accounting invariants.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how backend removal interacts with requests already running there.

## Further reading

- [aiohttp client guide](https://docs.aiohttp.org/en/stable/client_quickstart.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
