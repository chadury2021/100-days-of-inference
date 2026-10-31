# Day 90 — Lecture 90: MoE routing from scratch: top-K gating, load balancing loss

[Previous lecture](../day89/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day91/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 04](../day04/LECTURE.md), [Day 17](../day17/LECTURE.md).

## Learning objectives

- Implement top-k dispatch and combination.
- Quantify expert imbalance.

## Lecture notes

A router scores experts for each token, selects a subset, and combines their outputs using gate weights. Define whether selected weights are renormalized and how ties are handled. The dense reference computes selected expert outputs explicitly and provides a correctness target before optimizing dispatch.

Sparse activation reduces the number of experts used per token, but all expert weights still need storage or an offloading plan. Capacity constraints can force dropping, rerouting, or delaying tokens; each changes behavior. A load-balancing training loss encourages distribution but does not guarantee uniform inference traffic, especially under domain-specific prompts.

## Board example

For router probabilities [0.6,0.3,0.1] and top-2 selection, renormalized gates are [2/3,1/3]. If the two expert outputs are 3 and 9, the combined scalar output is 5. Without renormalization the result would be 4.5, a different convention.

## Lab procedure

Implement a toy router and three linear experts. Test top-1 and top-2, ties, and capacity overflow. Compare vectorized dispatch with an explicit per-token reference and plot assignments per expert for skewed inputs.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit gate/output checks and an imbalance metric.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain the chosen overflow policy and its effect on output equivalence.

## Further reading

- [Switch Transformers paper](https://arxiv.org/abs/2101.03961)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
