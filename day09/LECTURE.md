# Day 09 — Lecture 09: vLLM: PagedAttention & Continuous Batching

[Previous lecture](../day08/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day10/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 08](../day08/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Explain block-based kv allocation.
- Simulate continuous batching.

## Lecture notes

Paged KV storage maps logical token blocks onto physical memory blocks. Continuous batching admits new requests as others finish, improving utilization when lengths differ. Memory allocation and scheduling are related but distinct mechanisms: one reduces wasted capacity while the other changes when requests execute.

## Board example

With block size 16 and lengths 17 and 31, the requests each need two blocks. There are 64 allocated token slots and 48 occupied slots, leaving 16 unused. A static batch with output lengths 2 and 8 cannot replace the short request unless its scheduler permits new admission.

## Notebook lab

- [vllm-paged-attention](./vllm-paged-attention.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Simulate block allocation for mixed lengths and compare waste with a fixed reservation per request. Trace a scheduler timeline with arrivals and completions. Report useful tokens per second alongside time-to-first-token percentiles.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
