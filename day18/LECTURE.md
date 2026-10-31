# Day 18 — Lecture 18: Disaggregation: Prefill/Decode Split

[Previous lecture](../day17/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day19/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 17](../day17/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Compare colocated and split serving.
- Locate the crossover point.

## Lecture notes

Prefill and decode have different resource profiles, but these vary with batch size, context length, and hardware. Disaggregation helps when better scheduling and resource allocation outweigh transfer and coordination. Evaluate time to first token and inter-token latency separately; average throughput can hide an interactive regression.

## Board example

A colocated configuration has 80 ms of contention overhead. Splitting removes 60 ms but adds 25 ms transfer and 10 ms coordination. Net improvement is 25 ms. If transfer grows to 70 ms, the same design becomes 20 ms slower.

## Notebook lab

- [disaggregation-prefill-decode](./disaggregation-prefill-decode.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Build a crossover plot over prompt length and effective network bandwidth. Compare colocated and split policies at equal total resources. State the workload region where your result changes sign.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
