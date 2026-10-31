# Day 25 — Lecture 25: Multi-Cloud Capacity Management

[Previous lecture](../day24/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day26/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 24](../day24/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Plan capacity across failure domains.
- Account for network and recovery costs.

## Lecture notes

Multiple providers can offer alternative capacity, but failover requires more than a routing rule. Compatible serving images, accessible model artifacts, data placement, quotas, and warm capacity affect recovery. Geographic placement also changes request latency and transfer costs.

## Board example

Two regions each sustain 60 requests/s and jointly serve 80. Losing one leaves only 60 requests/s, a deficit of 20. Over a 30-second recovery interval, roughly 600 requests accumulate unless traffic is shed or spare capacity becomes available.

## Notebook lab

- [multi-cloud-capacity](./multi-cloud-capacity.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Design a two-region capacity plan with a stated recovery target. Simulate loss of one region and include startup delay. Compare warm redundancy with cold recovery, documenting transfer costs as assumptions rather than live price quotes.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
