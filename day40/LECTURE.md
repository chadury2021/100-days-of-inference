# Day 40 — Lecture 40: Implement prefix caching with hash-based deduplication

[Previous lecture](../day39/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day41/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 16](../day16/LECTURE.md), [Day 39](../day39/LECTURE.md).

## Learning objectives

- Construct context-sensitive cache keys.
- Define collision and invalidation behavior.

## Lecture notes

A prefix block’s identity depends on both its token contents and the preceding prefix. Hashing only the current block wrongly equates identical local tokens that follow different histories. Include model revision and other execution-affecting state in the namespace. A lookup must also honor any isolation policy between callers.

Use a chained hash or explicit prefix key and keep enough metadata to validate identity under the chosen collision model. Deduplication affects ownership: shared physical blocks need reference counting, and appending to a partial shared block may require copying. Invalidation must make old-version entries unavailable without corrupting active requests still using them.

## Board example

Prefixes [1,2,7,8] and [3,4,7,8] have the same final two-token block [7,8], but different preceding context. Their final block keys must differ. Prefixes [1,2,7,8] and [1,2,7,8,9] may reuse the common complete blocks.

## Lab procedure

Extend Day 39 with chained keys and namespaces. Test equal prefixes, equal suffixes with different histories, model-version changes, and an injected hash collision using a deliberately weak test hash.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit hit/miss traces and memory savings.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which entries survive invalidation and how active readers finish safely.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
