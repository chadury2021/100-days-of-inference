# Day 75 — Lecture 75: Tensor parallelism scaling: throughput and latency vs GPU count

[Previous lecture](../day74/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day76/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 17](../day17/LECTURE.md), [Day 59](../day59/LECTURE.md), [Day 72](../day72/LECTURE.md).

## Learning objectives

- Distinguish strong scaling from capacity scaling.
- Report communication overhead.

## Lecture notes

Strong scaling fixes the workload and increases devices, measuring speedup and efficiency. Capacity scaling asks what larger models or workloads additional devices make possible. Keep these experiments separate. Tensor parallelism may improve memory fit while increasing latency for small batches because collectives and smaller local operations dominate.

Record topology, rank placement, dtype, sequence lengths, and batch policy. Compare one, two, and more devices only when the model fits each configuration. Where it does not, state the missing baseline. Device cost and power rise with device count, so the fastest point may not minimize cost under a latency target.

## Board example

If one device takes 100 ms and four take 40 ms, speedup is 2.5× and parallel efficiency is 2.5/4=62.5%. Four times the hardware has not produced four times the speed. A 25 ms ideal reference ignores communication and serial work.

## Lab procedure

Run supported device counts or simulate local compute plus collective costs from Day 59. Sweep batch size at each count and record p95 latency, throughput, memory, and communication time.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit scaling and efficiency plots with explicit baseline availability.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which operating point fits the model and satisfies the service target at lowest modeled cost.

## Further reading

- [PyTorch distributed execution](https://docs.pytorch.org/docs/stable/distributed.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
