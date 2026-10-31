# Day 39 — Lecture 39: Build a simple KV cache manager (block allocator, eviction policy)

[Previous lecture](../day38/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day40/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 05](../day05/LECTURE.md), [Day 09](../day09/LECTURE.md).

## Learning objectives

- Maintain allocation invariants.
- Handle shared blocks and exhaustion.

## Lecture notes

A paged cache manager maps each request’s logical blocks to physical block IDs. A free list tracks unused blocks, and reference counts track blocks shared by multiple requests. Allocation and release must preserve the invariant that a block is either free or referenced, never both. Partial final blocks need special treatment when requests append tokens.

Eviction is safe only for cache entries whose use is governed by the manager’s lifecycle; active execution cannot lose its KV data silently. Under exhaustion, admission can wait, reject, or explicitly preempt and later recompute. Define this policy before implementing allocation. Reusing a freed ID must not leave a stale request mapping pointing at new content.

## Board example

With four physical blocks, request A owns [0,1] and B owns [2]. The free set is {3}. If C shares A’s block 0, its reference count becomes two. Releasing A frees block 1 but not block 0, which C still needs.

## Lab procedure

Implement allocate, retain, release, and append operations using a small in-memory simulator. Drive random request lifecycles and verify no duplicate free IDs, no negative references, and no use of released blocks.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit lifecycle traces for sharing, exhaustion, cancellation, and reuse.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how copy-on-write protects a partially filled shared block.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
