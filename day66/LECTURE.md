# Day 66 — Lecture 66: Load test with Locust: ramp traffic, find saturation point

[Previous lecture](../day65/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day67/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 27](../day27/LECTURE.md), [Day 52](../day52/LECTURE.md), [Day 63](../day63/LECTURE.md).

## Learning objectives

- Measure offered and completed load.
- Locate a sustainable operating point.

## Lecture notes

Load testing should reveal where the service stops meeting its objectives. Define request mix, duration, ramp steps, maximum load, and stop conditions. A closed-loop user model can reduce arrival rate as latency grows, hiding the degree of overload. Report actual offered requests per second alongside configured user count and successful completion rate.

Streaming HTTP success does not guarantee successful generation. Parse terminal events and validate output so truncated streams count as failures. The load generator itself can saturate CPU, sockets, or network; inspect its resource use before attributing the plateau to the server. Include a drain period to account for queued requests after arrivals stop.

## Board example

At offered load 100 requests/s and completion capacity 80/s, backlog grows by about 20/s. A 60-second steady overload creates roughly 1,200 queued requests under a fluid model. Reporting only successful completions conceals that accumulating debt.

## Lab procedure

Create a Locust workload or equivalent fixture-aware generator with staged load. Track offered load, completions, failed streams, p95 TTFT, and queue slope. Stop when a predefined error or latency threshold is exceeded in the lab.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the saturation curve and sustainable load recommendation.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how you verified the generator was not the bottleneck.

## Further reading

- [Locust workload authoring](https://docs.locust.io/en/stable/writing-a-locustfile.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
