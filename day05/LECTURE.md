# Day 05 — Lecture 05: KV Cache

[Previous lecture](../day04/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day06/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 04](../day04/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Implement incremental attention.
- Calculate KV-cache storage.

## Lecture notes

Cached decoding stores past keys and values so they do not need to be projected again. Each new query still attends to the preceding context; caching does not make attention independent of context length. Cache positions, masks, and layer identity must remain consistent with the uncached computation.

## Board example

KV bytes = 2 × layers × batch × sequence length × KV heads × head dimension × bytes per element. With 12 layers, batch 1, length 1,024, 12 KV heads, head dimension 64, and FP16 storage, the result is 37,748,736 bytes = 36 MiB. Grouped-query attention uses KV-head count here, not query-head count.

## Notebook lab

- [kv-cache](./kv-cache.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Compare cached and uncached logits within a stated tolerance. Sweep context length and plot latency plus allocated cache bytes. Explain both the memory increase and the computation avoided.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
