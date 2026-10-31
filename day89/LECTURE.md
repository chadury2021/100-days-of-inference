# Day 89 — Lecture 89: Medusa: multi-head speculative decoding, measure speedup

[Previous lecture](../day88/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day90/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 15](../day15/LECTURE.md), [Day 38](../day38/LECTURE.md), [Day 73](../day73/LECTURE.md).

## Learning objectives

- Explain multi-head proposals and tree verification.
- Separate greedy and stochastic claims.

## Lecture notes

Medusa adds prediction heads that propose multiple future tokens from a shared model representation. Candidate combinations form a tree that can be verified with an attention arrangement preserving each path’s context. Heads and verification settings must match the base model. More candidates increase potential accepted progress but also verification work and memory.

Acceptance policies differ in their guarantees. A greedy path check and a typical-acceptance heuristic should not be described as exact target-distribution sampling without proof for the chosen policy. Record which variant is used and evaluate quality accordingly. Include target-only execution and the extra heads’ overhead in the comparison.

## Board example

If a candidate tree has 20 nodes but only four tokens on its chosen accepted path, the verifier processed 20 candidate positions for four committed tokens. Increasing to 40 nodes is beneficial only if additional progress or parallel efficiency compensates for the added work.

## Lab procedure

Draw a depth-three proposal tree and its causal visibility rules. Simulate pruning and path selection. With a compatible model and implementation, measure verification time, candidate count, committed tokens, quality, and memory.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the tree, acceptance-policy statement, and cost/progress comparison.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why equal draft depth does not imply equal verification cost.

## Further reading

- [Medusa paper](https://arxiv.org/abs/2401.10774)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
