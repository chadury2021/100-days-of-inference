# Day 62 — Lecture 62: Blue-green deployment: zero-downtime model version swap

[Previous lecture](../day61/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day63/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 26](../day26/LECTURE.md), [Day 53](../day53/LECTURE.md), [Day 57](../day57/LECTURE.md).

## Learning objectives

- Gate traffic on readiness.
- Preserve streaming requests during cutover.

## Lecture notes

Blue-green deployment prepares a complete new serving pool before changing routing. Validate model identity, readiness, and representative inference results before sending ordinary traffic. A successful health response alone does not establish model quality. Record the old and new artifact sets so rollback restores a known configuration.

Routing changes affect new admissions; existing streams should finish on their original worker where the infrastructure permits. Drain old workers by stopping admission and tracking active requests until completion or an explicit deadline. A rollback can redirect future requests but cannot erase text already streamed to a client. Test that limitation rather than promising perfect invisibility.

## Board example

Suppose the old pool has 12 active streams and accepts no new work after cutover. Ten finish within 20 seconds and two need 80 seconds. A 30-second drain deadline interrupts two requests unless the deployment keeps those workers alive or defines an explicit recovery behavior.

## Lab procedure

Use mock pools or an available lab server to roll from model version A to B. Include a readiness failure, a bad quality canary, and a long stream. Record admission decisions, version identity, and active counts throughout.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the cutover and rollback timeline plus interruption counts.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain the temporary capacity cost and the meaning of zero downtime for streams.

## Further reading

- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
