# Day 74 — Lecture 74: Measure KV cache hit rates across real traffic patterns

[Previous lecture](../day73/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day75/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 16](../day16/LECTURE.md), [Day 40](../day40/LECTURE.md), [Day 63](../day63/LECTURE.md).

## Learning objectives

- Separate request and token hit rates.
- Account for cold state and eviction.

## Lecture notes

A request-level hit metric asks whether any prefix was reused; a token-level metric measures how much prefill work may have been avoided. Both are useful but answer different questions. Weighting by reused tokens better reflects prefix length, while actual saved time also depends on device and scheduling. Always define the denominator.

Replay workloads in timestamp order because cache capacity, arrival patterns, and eviction change outcomes. Separate cold-start, warming, and steady intervals. Include model-version changes and tenant namespace rules. A high hit rate can coexist with poor latency if cache-aware routing concentrates demand on overloaded workers.

## Board example

Two requests have prompt lengths 10 and 1,000. The first reuses all 10 tokens; the second reuses none. Request hit rate is 50%, but reused-token fraction is 10/1,010≈0.99%. Reporting only the first number exaggerates the likely saved work.

## Lab procedure

Replay repeated-template, chat-history, and unique-prompt traces through Day 40’s cache. Sweep capacity and eviction policy. Record request hits, reused tokens, evictions, and estimated or measured prefill time saved.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit cold/warm time series and hit-rate definitions.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a version change should affect reuse even for identical token IDs.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
