# Day 100 — Lecture 100: Deploy: ship it to the home lab cluster with load balancing

[Previous lecture](../day99/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day101/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 57](../day57/LECTURE.md), [Day 62](../day62/LECTURE.md), [Day 99](../day99/LECTURE.md).

## Learning objectives

- Deploy reproducible artifacts.
- Demonstrate routing and recovery.

## Lecture notes

Deploy the capstone into the available lab with explicit model, image, and configuration versions. Keep service discovery and routing simple enough to inspect. Readiness should prevent traffic reaching unloaded workers, and the load balancer should stop new admissions to unhealthy ones while accounting for existing streams. Document the hardware topology and resource allocation actually used.

Exercise recovery rather than inferring it from a successful startup. Restart a worker, interrupt a stream, and roll back a version in a controlled lab. Verify whether requests fail, retry, or finish on their original workers, and report the user-visible result. A single-host setup can demonstrate lifecycle behavior but cannot prove multi-host fault tolerance.

## Board example

Two workers each sustain 4 requests/s and serve a total 6 requests/s. Losing one leaves a deficit of 2 requests/s. Over a 15-second restart, about 30 requests accumulate unless admission rejects excess work or spare capacity is available.

## Lab procedure

Deploy the Day 99 artifacts, run the acceptance smoke suite, and execute one worker restart plus one rollback. Collect readiness events, routing decisions, queue depth, error counts, and model-version responses.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the deployment manifest, recovery timeline, and observed limitations.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain whether the design meets its target under one-worker failure.

## Further reading

- [Docker build practices](https://docs.docker.com/build/building/best-practices/)
- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
