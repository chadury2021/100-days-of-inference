# Day 12 — Lecture 12: NVIDIA Dynamo: Disaggregated Serving

[Previous lecture](../day11/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day13/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 11](../day11/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Trace disaggregated request flow.
- Estimate KV-transfer cost.

## Lecture notes

Disaggregated serving assigns prompt processing and token generation to separate worker pools. The decoder needs the correct KV state before continuing the request. Routing, transfer, admission, and failure handling are part of the design; extra communication can consume the benefit of independent scaling.

## Board example

For a 512 MiB cache and effective transfer bandwidth 25 GiB/s, the ideal transfer time is 0.5/25=0.02 seconds, or 20 ms. Allocation, serialization, coordination, and contention add to that bound. A 10 ms compute saving cannot repay even the ideal transfer cost in this example.

## Notebook lab

- [nvidia-dynamo](./nvidia-dynamo.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Trace one request from admission through prefill, transfer, and decode. Sweep cache size and effective bandwidth in the notebook model. Explain what happens if the prefill worker fails before transfer completes.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
