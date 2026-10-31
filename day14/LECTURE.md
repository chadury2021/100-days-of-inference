# Day 14 — Lecture 14: Quantization Algorithms: GPTQ, AWQ, SmoothQuant

[Previous lecture](../day13/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day15/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 13](../day13/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Compare calibration objectives.
- Evaluate output error on held-out inputs.

## Lecture notes

Weight-only and weight-and-activation quantization address different bottlenecks. GPTQ-style methods use curvature information to guide weight approximation; AWQ uses activation information to guide scaling; SmoothQuant redistributes scaling between activations and weights. A simplified demonstration is not a complete implementation of these algorithms.

## Board example

For row-vector activations X and weights W, introducing invertible diagonal D gives XW=(XD⁻¹)(DW). The unquantized product is unchanged, but the ranges of the two factors change. After quantization, their errors can differ greatly, which makes calibration and evaluation necessary.

## Notebook lab

- [quantization-gptq-awq-smoothquant](./quantization-gptq-awq-smoothquant.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Verify the scaling identity numerically. Compare a rounding baseline with the notebook demonstrations on separate calibration and evaluation inputs. Report output error and describe exactly which algorithmic steps your implementation omits.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
