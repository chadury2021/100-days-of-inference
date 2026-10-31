# Day 71 — Lecture 71: GPU memory profiling: find where your memory budget goes

[Previous lecture](../day70/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day72/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 05](../day05/LECTURE.md), [Day 34](../day34/LECTURE.md), [Day 63](../day63/LECTURE.md).

## Learning objectives

- Reconcile weights, cache, and workspace.
- Distinguish live allocation from reservation.

## Lecture notes

A serving memory budget includes weights, KV state, activations, temporary workspaces, runtime allocations, and fragmentation or allocator reserves. These categories have different lifetimes and scaling rules. Measure at model load, after warmup, during peak prefill, and during steady decode; one idle snapshot cannot characterize the peak.

Framework allocated memory counts live managed tensors, while reserved memory includes allocator-held capacity. Device totals may also include allocations outside the framework. Releasing Python references and clearing allocator caches have different effects; neither proves that a genuine live-tensor leak is fixed. On shared-memory hardware, record the system accounting method as well.

## Board example

A hypothetical 24 GiB device holds 10 GiB weights, 8 GiB KV, and 4 GiB peak workspace, leaving only 2 GiB for other overhead. A 3 GiB prefill spike would exceed the nominal budget even though the idle model appears to fit comfortably.

## Lab procedure

Instrument staged allocations for a small model and sweep batch/context sizes. Compare analytical KV bytes with measured changes. Repeat request cycles and observe whether live allocations return to a stable baseline.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a memory waterfall and capacity boundary.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how reserved-but-unused memory differs from a persistent live allocation leak.

## Further reading

- [PyTorch CUDA memory management](https://docs.pytorch.org/docs/stable/notes/cuda.html#cuda-memory-management)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
