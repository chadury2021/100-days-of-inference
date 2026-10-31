# Day 10 — Lecture 10: SGLang: RadixAttention & Structured Outputs

[Previous lecture](../day09/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day11/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 09](../day09/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Trace prefix-tree reuse.
- Distinguish output syntax from correctness.

## Lecture notes

A radix tree represents shared token prefixes compactly. Reusing a compatible prefix can avoid repeated prefill computation. Constrained decoding narrows valid token choices according to a grammar or schema, but syntactic validity does not establish factual accuracy or useful task completion.

## Board example

Requests with token sequences [1,2,3,4] and [1,2,3,9] share a three-token prefix. A cache hit can reuse those prefix states when execution configuration matches. A valid JSON object containing an incorrect answer still fails a factual evaluation.

## Notebook lab

- [sglang-radix-attention](./sglang-radix-attention.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Construct a small prefix tree and measure reusable tokens for repeated and unique prompts. Evaluate structured outputs using both schema validation and a task-specific correctness check. Report these metrics separately.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
