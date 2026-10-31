# Day 04 — Lecture 04: Transformer Blocks & Attention Deep Dive

[Previous lecture](../day03/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day05/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 03](../day03/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Derive scaled dot-product attention.
- Apply a causal mask.

## Lecture notes

Queries compare each position with keys; softmax turns the scores into weights used to combine values. Scaling by √dₖ moderates score magnitude. A causal mask excludes future positions before softmax. Residual connections, normalization, and feed-forward layers complete the block; attention alone is not the entire transformer.

## Board example

Attention(Q,K,V) = softmax(QKᵀ/√dₖ + M)V. For three tokens, the allowed key positions are {1}, {1,2}, and {1,2,3}. A first-position row of scores [2,1,0] becomes [2,−∞,−∞] and therefore weights [1,0,0].

## Notebook lab

- [attention](./attention.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Compute a two-token attention example by hand. Verify row sums and masked probabilities numerically. Change a future token and check that an earlier output stays unchanged in deterministic evaluation mode.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
