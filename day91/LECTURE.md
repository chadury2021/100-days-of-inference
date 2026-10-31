# Day 91 — Lecture 91: Expert parallelism: simulate routing across N expert shards

[Previous lecture](../day90/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day92/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 41](../day41/LECTURE.md), [Day 90](../day90/LECTURE.md).

## Learning objectives

- Route tokens to expert owners.
- Model all-to-all communication and stragglers.

## Lecture notes

Expert parallelism places different experts on different workers. Token representations travel to the selected expert owners, are processed, and return for weighted combination. Preserve token identity and gate weights across packing, exchange, and reordering; a fast implementation with permuted outputs is incorrect.

Communication volume depends on selected experts, hidden width, dtype, and locality. Worker completion is constrained by the busiest expert shard, not average work. Expert replication or placement can improve balance but consumes additional memory and routing complexity. A simulator should expose these tradeoffs without claiming hardware speed from Python timing.

## Board example

If three workers receive 10, 10, and 40 equal-cost expert assignments, the compute makespan is proportional to 40 rather than the mean 20. Even before communication, utilization under a synchronized step is 60/(3×40)=50%.

## Lab procedure

Extend Day 90 with expert-to-worker placement, packetized token IDs, configurable network cost, and gather/reorder. Compare balanced versus skewed routing and replicate one hot expert under a fixed memory budget.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit correctness against the single-worker reference and a makespan breakdown.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain when communication outweighs the benefit of additional expert workers.

## Further reading

- [Switch Transformers paper](https://arxiv.org/abs/2101.03961)
- [PyTorch distributed execution](https://docs.pytorch.org/docs/stable/distributed.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
