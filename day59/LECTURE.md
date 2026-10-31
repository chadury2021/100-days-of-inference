# Day 59 — Lecture 59: Multi-GPU tensor parallel benchmark across spark-01 and spark-02

[Previous lecture](../day58/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day60/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 17](../day17/LECTURE.md), [Day 21](../day21/LECTURE.md), [Day 41](../day41/LECTURE.md).

## Learning objectives

- Verify network topology.
- Separate model-fit gains from speedup.

## Lecture notes

Two physical hosts communicate over their actual interconnect, not an assumed same-board GPU link. Inventory device architecture, network interface, transport support, runtime version, and collective backend before attempting distributed execution. Both workers need compatible model and tokenizer artifacts. Failure to form the distributed group is a setup result, not a zero-throughput benchmark.

Establish a single-device reference when the model fits. If it does not fit, compare model capacity separately from speed: the two-device run enables a previously impossible configuration but has no measured one-device latency baseline. Record communication and compute overlap, plus rank imbalance. Use fixed workloads and equivalent numerical formats.

## Board example

If each decode step spends 6 ms on local compute and 4 ms on non-overlapped communication, step time is 10 ms. Reducing compute to 3 ms with more shards yields 7 ms only if communication stays constant; doubling communication instead gives 11 ms.

## Lab procedure

Prepare and, where supported, execute a two-host run on spark-01 and spark-02. Save topology, startup diagnostics, and a small correctness fixture before load testing. Otherwise simulate communication costs using the Day 41 decomposition.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit speedup or capacity-enablement results with their distinct baselines.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a faster network may matter more than another compute shard.

## Further reading

- [PyTorch distributed execution](https://docs.pytorch.org/docs/stable/distributed.html)
- [DGX Spark user guide](https://docs.nvidia.com/dgx/dgx-spark/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
