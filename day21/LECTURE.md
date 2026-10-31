# Day 21 — Lecture 21: Multi-GPU Instances & Multi-Instance GPU (MIG)

[Previous lecture](../day20/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day22/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 20](../day20/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Distinguish partitioning from sharding.
- Assess isolation and interconnects.

## Lecture notes

Multi-device execution connects separate accelerators. Hardware partitioning divides a supported device into isolated instances with constrained resources. These solve different problems. Supported partition profiles and interconnect capabilities are device-specific; a lab plan must first establish which features exist on the available hardware.

## Board example

A service requiring 18 GiB for weights plus 8 GiB for cache and workspace needs at least 26 GiB before additional headroom. It cannot fit a partition with only 20 GiB even if the parent device has ample memory. Two partitions do not automatically combine into one larger allocation.

## Notebook lab

- [multi-gpu-instances-mig](./multi-gpu-instances-mig.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Inventory device capability and available memory. Design placements for two differently sized services. If hardware partitioning is unsupported, simulate placement and clearly report that no partition was created.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
