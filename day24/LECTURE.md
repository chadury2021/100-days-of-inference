# Day 24 — Lecture 24: Routing, Load Balancing & Queueing

[Previous lecture](../day23/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day25/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 23](../day23/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Compare work-aware routing policies.
- Analyze fairness and stability.

## Lecture notes

Request count is a weak proxy for remaining work when prompt and output lengths vary. Routing can consider queue estimates, prefix reuse, or adapter locality. Priority policies need an explicit starvation response. Queueing models are useful only when their arrival, service, and stationarity assumptions are stated.

## Board example

Worker A has two requests with estimated remaining work 1 second each; B has one with 10 seconds remaining. Least-connections selects B, while least-estimated-work selects A. Estimates may be wrong, so compare policies under prediction error rather than assuming perfect information.

## Notebook lab

- [routing-load-balancing-queueing](./routing-load-balancing-queueing.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Replay mixed short and long jobs through FIFO and a work-aware policy. Report p50/p95 latency for each class and maximum wait. Inject estimation errors and show whether the policy still improves the result.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
