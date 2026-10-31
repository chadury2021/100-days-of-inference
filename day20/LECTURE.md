# Day 20 — Lecture 20: GPU Generations: Hopper, Ada, Blackwell, Rubin

[Previous lecture](../day19/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day21/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 19](../day19/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Compare hardware using workload constraints.
- Separate projections from measurements.

## Lecture notes

A device comparison must include usable memory, bandwidth, supported numerical formats, interconnect, software support, and power or acquisition cost. Peak arithmetic rates describe a particular operation and precision. They cannot establish end-to-end performance for an arbitrary model.

## Board example

Suppose device A sustains 1 TB/s and device B sustains 2 TB/s, while B has four times the peak compute. A purely weight-bandwidth-bound workload has an ideal 2× bandwidth-based improvement, not 4×. Real gains require measurement with matching model, precision, and workload.

## Notebook lab

- [gpu-generations-hopper-blackwell](./gpu-generations-hopper-blackwell.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Create a dated comparison using official specifications for the devices you can access. Label notebook forecasts and hypothetical values explicitly. Predict the bottleneck and test one prediction; do not present projected generations as measured hardware.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
