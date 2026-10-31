# Day 02 — Lecture 02: Inference from Scratch: Model internals & tokenization

[Previous lecture](../day01/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day03/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 01](../day01/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Inspect tensor shapes and parameter counts.
- Explain BPE encoding.

## Lecture notes

Weights encode learned arrays; architecture code defines how those arrays are used. A tokenizer supplies a separate mapping between text and IDs. BPE training learns merge rules, while encoding applies the learned rules in priority order. The model configuration, tokenizer, and weights must agree on vocabulary and dimensions.

## Board example

An embedding table with vocabulary 50,000 and hidden width 768 contains 38,400,000 parameters. At two bytes per parameter it occupies 76.8 MB in decimal units, before metadata. Tied input and output weights share storage; counting both as separate parameters would overestimate the model.

## Notebook lab

- [02-a-whats-inside-a-model](./02-a-whats-inside-a-model.ipynb)
- [02-b-tokenization](./02-b-tokenization.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Count parameters by tensor group without double-counting shared tensors. Trace the merges for one string and test encode/decode round trips on whitespace and Unicode. Explain why fewer tokens alone does not establish better task quality.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
