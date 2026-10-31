# Day 15 — Lecture 15: Speculative Decoding: Draft-Target, Medusa, EAGLE

[Previous lecture](../day14/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day16/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 14](../day14/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Explain draft-and-verify decoding.
- Evaluate acceptance and overhead.

## Lecture notes

A draft model proposes tokens and the target verifies them in parallel. Exact speculative sampling uses acceptance and correction rules to preserve the target distribution; simply accepting similar-looking tokens does not provide that guarantee. Benefit depends on accepted progress relative to drafting and verification costs.

## Board example

Suppose a cycle costs 4 ms of drafting and 12 ms of verification and yields an average of three committed tokens. Its effective time is 16/3≈5.33 ms per token. Against an 8 ms target-only baseline, speedup is 1.5×. At only one committed token per cycle, it is slower than the baseline.

## Notebook lab

- [speculative-decoding](./speculative-decoding.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Sweep draft length and measure committed tokens per cycle, total latency, and quality. Explain acceptance and rejection for the notebook method. Separate greedy verification from claims about exact stochastic sampling.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
