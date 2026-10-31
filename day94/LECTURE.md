# Day 94 — Lecture 94: Long context without context parallelism: chunked prefill

[Previous lecture](../day93/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day95/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 05](../day05/LECTURE.md), [Day 50](../day50/LECTURE.md), [Day 87](../day87/LECTURE.md).

## Learning objectives

- Schedule long prompts incrementally.
- Distinguish temporary work from total KV capacity.

## Lecture notes

Chunked prefill divides prompt processing across scheduling iterations, allowing decode work or other requests to run between chunks. Each chunk must attend to the appropriate preceding context and update positions and cache state consistently. It is a scheduling and workspace technique, not permission to drop parts of the prompt.

Smaller chunks can reduce decode stalls but add scheduling overhead or reduce compute efficiency. They do not by themselves reduce the final full-context KV requirement. Compare output equivalence with an unchunked reference and evaluate both the long prompt’s TTFT and other users’ inter-token gaps. A mean throughput number can hide either regression.

## Board example

A 4,096-token prompt split into 512-token chunks requires eight prefill admissions. If each chunk creates a 10 ms uninterruptible interval, it may replace one larger blocking interval with eight smaller ones, but total work and scheduling overhead must still be measured.

## Lab procedure

Extend Day 50 with prompt chunks and decode-priority scheduling. Sweep chunk size and token budget using one long prompt mixed with short interactive jobs. If supported, repeat with a real runtime and verify outputs.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit TTFT, decode-gap, throughput, and peak-memory curves.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why chunking can improve responsiveness without making a model fit less KV memory.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
