# Day 93 — Lecture 93: Cache-aware routing: route requests to maximize KV cache hits

[Previous lecture](../day92/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day94/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 16](../day16/LECTURE.md), [Day 40](../day40/LECTURE.md), [Day 57](../day57/LECTURE.md), [Day 74](../day74/LECTURE.md).

## Learning objectives

- Optimize completion time rather than hits alone.
- Test stale routing estimates.

## Lecture notes

Cache locality can reduce prefill work, but routing also changes queues and future cache contents. Score eligible workers using estimated waiting, uncached prefill work, decode load, and transfer costs where applicable. Use model and tenant compatibility as eligibility rules before optimization. A high hit rate is a means to lower cost or latency, not the sole objective.

Routing feedback can concentrate traffic on one popular-prefix worker. Include queue pressure and consider bounded replication or spillover. Test the policy under stale cache and load information, because perfect-state simulations overestimate routing quality. Eviction can invalidate a previously advertised hit between decision and admission.

## Board example

Worker A offers a 50 ms cache saving with 100 ms queue wait; B offers no saving and 20 ms queue wait. Relative to uncached compute, A adds 50 ms and B adds 20, so B is preferable by 30 ms despite its miss.

## Lab procedure

Replay mixed repeated and unique prompts using Day 40’s cache and Day 57’s router. Compare round-robin, hit-maximizing, and queue-aware policies. Inject delayed state updates and measure both hit fractions and completion latency.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit policy tradeoffs and one adversarial trace.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how fallback works when the advertised cache entry has been evicted.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
