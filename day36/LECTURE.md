# Day 36 — Lecture 36: Curvature-aware quantization: scale search and GPTQ distinctions

[Previous lecture](../day35/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day37/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 14](../day14/LECTURE.md), [Day 35](../day35/LECTURE.md).

## Learning objectives

- Derive an activation-weighted error objective.
- Distinguish a teaching approximation from GPTQ.

## Lecture notes

Let X contain calibration activation rows and W be a linear layer’s weights. Reconstruction loss is ||X(W−Ŵ)||²_F. Its curvature depends on XᵀX, so errors in frequently activated directions matter more than errors in rarely used directions. Correlations also matter: dropping off-diagonal terms changes the objective.

A diagonal weighting alone does not change independent nearest-grid rounding when every weight keeps the same fixed grid: multiplying a coordinate’s squared error by a positive scalar preserves its minimizer. To make weighting consequential, compare candidate scales or allocate precision across coordinates. Full GPTQ additionally uses sequential error compensation and curvature structure; do not label a diagonal experiment as a full implementation.

## Board example

For activation covariance diag(100,1), weight error [0.1,0] costs 1, while error [0,0.1] costs 0.01. Equal raw weight errors can therefore produce a hundredfold difference in the calibration objective.

## Lab procedure

Compare ordinary rounding with a scale search minimizing activation-weighted reconstruction loss. Use a damped covariance estimate and a separate evaluation set. Show a case where calibration distribution shift reverses the ranking.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the objective, scale choices, and held-out error.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Identify which GPTQ steps are absent and why independent weighted rounding on a fixed grid is insufficient.

## Further reading

- [GPTQ paper](https://arxiv.org/abs/2210.17323)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
