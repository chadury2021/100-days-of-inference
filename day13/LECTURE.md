# Day 13 — Lecture 13: Quantization: Number Formats (FP8, INT8, INT4, NVFP4)

[Previous lecture](../day12/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day14/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 12](../day12/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Calculate packed weight storage.
- Quantify rounding and clipping error.

## Lecture notes

Quantization maps values to a smaller representable set. For affine integer quantization, q=clip(round(x/s)+z), and reconstruction is x̂=s(q−z). Floating-point and block-scaled formats have different representations. Storage savings depend on metadata and packing; speed also depends on available kernels and workload.

## Board example

A model with 7 billion parameters has 14 GB of raw two-byte weights and 3.5 GB of ideally packed four-bit weights. Scales, padding, and non-quantized tensors add overhead. With s=0.1 and z=0, x=0.26 rounds to q=3 and reconstructs to 0.3, an absolute error of 0.04.

## Notebook lab

- [quantization-number-formats](./quantization-number-formats.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Quantize a tensor at two precisions and report mean and maximum reconstruction error, clipping count, and actual stored bytes. Explain why a fourfold weight reduction does not guarantee fourfold speedup.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
