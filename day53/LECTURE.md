# Day 53 — Lecture 53: Write a production Dockerfile for a vLLM inference server

[Previous lecture](../day52/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day54/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 22](../day22/LECTURE.md), [Day 46](../day46/LECTURE.md).

## Learning objectives

- Define image and model boundaries.
- Validate readiness and shutdown.

## Lecture notes

A serving image should identify the runtime, dependency versions, entrypoint, and expected model location. Pin a tested base image by digest for reproducibility and record the target architecture. A model stored outside the image speeds image iteration but makes artifact availability and revision checking part of startup. Never equate a process listening on a port with a loaded, usable model.

Readiness should verify that the service can accept its intended workload; liveness should detect an unrecoverable process failure without repeatedly killing a slow load. Signal handling must reach the serving process, stop admission, and allow active work to drain. Keep secrets out of image layers and build arguments that become image history.

## Board example

An image downloads in 20 seconds, model weights load in 45, and warmup takes 5. Sequential readiness is reached at 70 seconds, not at the first listening socket. If cached model artifacts reduce the measured weight-loading stage to 10 seconds, readiness moves to 35 seconds. Cached artifacts still need deserialization and device placement; measure these paths separately.

## Lab procedure

Write a Dockerfile and startup contract for the Day 46 server using its supported image. Build locally if available, inspect the resulting configuration, and test readiness during loading plus termination during a long request.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the image digest, model revision, startup timeline, and shutdown outcome.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how the same image can still behave differently when model or runtime configuration changes.

## Further reading

- [Docker build practices](https://docs.docker.com/build/building/best-practices/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
