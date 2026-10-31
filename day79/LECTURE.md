# Day 79 — Lecture 79: Embedding model inference: batching and throughput optimization

[Previous lecture](../day78/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day80/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 03](../day03/LECTURE.md), [Day 27](../day27/LECTURE.md), [Day 52](../day52/LECTURE.md).

## Learning objectives

- Choose pooling and normalization deliberately.
- Optimize token-aware batching.

## Lecture notes

Embedding models convert token sequences into fixed-size vectors using a model-specific pooling and normalization policy. Padding must be excluded where the pooling rule requires it. CLS pooling, mean pooling, and normalized embeddings are not interchangeable choices; use the checkpoint’s documented inference contract before experimenting.

Batch by total tokens or length buckets to reduce padding overhead. Report vectors per second and input tokens per second because request lengths vary. A throughput improvement is useful only if retrieval or similarity quality remains adequate. Tokenization, host-device transfer, and vector serialization may dominate smaller models, so include them in end-to-end measurements.

## Board example

For sequence lengths 8, 8, and 64 in one padded batch, 192 token positions are processed for 80 real tokens: only 41.7% are useful under this simplified count. Grouping the short pair separately can reduce padding without changing their contents.

## Lab procedure

Embed a fixed corpus using sequential, fixed-count batched, and length-bucketed execution. Verify output dimensions, normalization, and similarity rankings against a reference. Measure end-to-end throughput and peak memory.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit padding efficiency and retrieval-quality checks.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why comparing vectors/s across different length distributions can mislead.

## Further reading

- [Sentence Transformers inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
