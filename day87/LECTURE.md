# Day 87 — Lecture 87: Long context: RoPE scaling, context parallelism across GPUs

[Previous lecture](../day86/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day88/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 04](../day04/LECTURE.md), [Day 17](../day17/LECTURE.md), [Day 34](../day34/LECTURE.md).

## Learning objectives

- Distinguish position extrapolation from memory capacity.
- Evaluate long-context quality.

## Lecture notes

Rotary position embeddings rotate query/key coordinate pairs according to position. Their relative-position behavior does not guarantee reliable inference at arbitrary lengths. Context extension methods change positional scaling or training behavior and must be evaluated for both short- and long-context tasks. A larger configured maximum length is not evidence of preserved quality.

Memory and compute remain constraints even if position encoding accepts the index. KV storage grows with context, and attention work can grow substantially. Context parallelism distributes sequence work but requires correct global attention semantics and communication. Chunked prefill, covered later, changes scheduling without automatically partitioning total cache capacity across devices.

## Board example

For 32 layers, 8 KV heads, dimension 128, FP16, and batch 1, KV storage is 131,072 bytes per token. At 32,768 tokens this is 4 GiB; at 131,072 tokens it is 16 GiB, before weights and workspace.

## Lab procedure

Compute capacity for a chosen model, then test retrieval of facts placed at several positions and distances within supported contexts. Compare a documented extension configuration only if available, retaining short-context controls.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit memory estimates and quality by position/length.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why passing a single needle-retrieval example does not establish general long-context reasoning.

## Further reading

- [RoFormer: rotary position embeddings](https://arxiv.org/abs/2104.09864)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
