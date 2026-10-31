# Day 03 — Lecture 03: Embeddings: From integers to vectors

[Previous lecture](../day02/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day04/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 02](../day02/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Compute embedding lookups.
- Track position and output projection shapes.

## Lecture notes

An embedding layer selects rows from a learned matrix. GPT-2 adds learned position embeddings before the transformer blocks. Later architectures may represent position differently, so this example is architecture-specific. Similarity between raw token embeddings is a geometric observation, not a guarantee of semantic equivalence in context.

## Board example

With vocabulary V=10,000 and width d=64, E has shape [10,000,64]. IDs [7,2,7] produce a [3,64] tensor. Rows one and three initially match; adding different position vectors can make their transformer inputs different. Projection through Eᵀ maps a hidden vector back to 10,000 logits when weights are tied.

## Notebook lab

- [embeddings](./embeddings.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Manually gather three embedding rows and check equality with the library lookup. Compare repeated tokens before and after position addition. Report tensor shapes at each step and explain the output projection.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
