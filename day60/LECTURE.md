# Day 60 — Lecture 60: MIG capability checks and partition planning on supported GPUs

[Previous lecture](../day59/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day61/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 21](../day21/LECTURE.md), [Day 55](../day55/LECTURE.md).

## Learning objectives

- Check explicit hardware support.
- Evaluate service placement under partition limits.

## Lecture notes

MIG partitions supported GPUs into hardware instances with defined resource profiles. Support is product-specific; compute capability or the word Blackwell alone is insufficient. The original roadmap’s instruction to configure MIG on Spark is replaced with capability discovery and supported-device practice. DGX Spark GB10 is not listed in the cited MIG supported-products table; use a simulator unless the actual product is explicitly supported.

Model each partition as a capacity and compute allocation rather than a fraction of the parent’s advertised throughput. Profiles constrain feasible combinations. Partition reconfiguration affects running workloads and belongs in a controlled lab procedure. On unsupported hardware, process-level concurrency experiments are not equivalent to MIG isolation.

## Board example

A service needs 10 GiB of weights, 5 GiB of cache, and 2 GiB of workspace: 17 GiB before extra headroom. It cannot fit a 10 GiB profile. Two 10 GiB instances do not transparently supply one 20 GiB address space.

## Lab procedure

Record the exact device identity and compare it with the official support table. Simulate placing three services into candidate profiles. Only on a dedicated supported device, follow the vendor setup procedure and compare isolation under concurrent load.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit capability evidence, feasible placements, and simulated or measured latency.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why memory fit alone does not prove sufficient compute capacity.

## Further reading

- [NVIDIA MIG supported products](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
