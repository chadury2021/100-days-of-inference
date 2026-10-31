# Day 85 — Lecture 85: Embedding similarity search pipeline: embed → index → query

[Previous lecture](../day84/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day86/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 03](../day03/LECTURE.md), [Day 79](../day79/LECTURE.md).

## Learning objectives

- Separate embedding and index errors.
- Evaluate recall against an exact baseline.

## Lecture notes

A retrieval pipeline chunks documents, embeds them, builds an index, embeds a query, and retrieves candidates. Store the embedding model revision, normalization rule, chunking policy, and document IDs with the index. Query and document representations must follow the checkpoint’s compatible conventions; changing the model generally requires rebuilding or migrating the index.

An exact dot-product or distance search provides a reference for approximate indexing. Measure recall@k relative to that reference and separately measure relevance against human or task labels. Approximate-search recall is not the same as semantic usefulness. Include index build time, memory, query latency, and update behavior in the system evaluation.

## Board example

If exact top-5 neighbors are {A,B,C,D,E} and approximate top-5 are {A,C,E,F,G}, recall@5 is 3/5=0.6. This says three exact neighbors were retained; it does not establish that any of the five are relevant to the user’s question.

## Lab procedure

Build exact search over a small embedded corpus, then add an available approximate index. Sweep its search-effort setting, and test a document update plus a model-version mismatch. Keep stable document IDs through the pipeline.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit latency/recall curves and a relevance sample.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how stale index metadata can produce plausible but invalid comparisons.

## Further reading

- [Faiss getting started](https://github.com/facebookresearch/faiss/wiki/Getting-started)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
