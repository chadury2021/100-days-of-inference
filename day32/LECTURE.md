# Day 32 — Lecture 32: Implement scaled dot-product attention (SDPA) with masking

[Previous lecture](../day31/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day33/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 04](../day04/LECTURE.md), [Day 31](../day31/LECTURE.md).

## Learning objectives

- Implement a numerically stable attention reference.
- Test mask alignment.

## Lecture notes

Compute scores QKᵀ/√d, apply the causal and padding masks, subtract each row’s maximum, exponentiate, and normalize before multiplying by V. For full-sequence self-attention, the causal mask is lower triangular. Cached decoding requires absolute position alignment; a one-row local triangle is not a sufficient specification of which past keys are visible.

Define behavior for fully masked rows before coding. Softmax of a row consisting entirely of negative infinity produces undefined arithmetic in a naive implementation. Padding outputs can be zeroed under an explicit policy. Keep dropout disabled in the reference, and compare both outputs and shapes with a library implementation under the same mask convention.

## Board example

For scores [0, ln(3)], softmax is [1/4,3/4]. With values [2,6], the weighted result is 5. If the second key is masked, the result becomes 2. Adding the same finite constant to both unmasked scores leaves the probabilities unchanged.

## Lab procedure

Implement the reference in NumPy or PyTorch. Test full attention, causal attention, padding, cached-query offsets, and a fully masked row. Compare against hand calculations before using larger random tensors.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit numerical error and mask tests.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Demonstrate that modifying a future value cannot affect an earlier causal output.

## Further reading

- [PyTorch scaled dot-product attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
