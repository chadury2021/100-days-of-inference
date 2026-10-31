# Day 16 — Lecture 16: KV Cache: Prefix Caching & Cache-Aware Routing

[Previous lecture](../day15/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day17/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 15](../day15/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Define valid prefix reuse.
- Balance cache locality against queueing.

## Lecture notes

Prefix reuse requires matching token history and compatible model execution state. Cache identity should account for model version and relevant adapters or configuration. A route with a cache hit may still be slow if its queue is long. Cache eviction and invalidation are therefore part of request scheduling.

## Board example

Worker A has a reusable prefix saving 40 ms but a 100 ms queue. Worker B has no hit and a 10 ms queue. Holding other costs equal, A adds 100−40=60 ms relative to uncached compute, while B adds 10 ms. Cache locality alone would select the slower worker.

## Notebook lab

- [kv-cache-prefix-caching](./kv-cache-prefix-caching.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Compare round-robin with a policy that considers both cache savings and waiting time. Include repeated prompts, unique prompts, and a model-version change. Explain how stale cache reuse is prevented.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
