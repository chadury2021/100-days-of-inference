# Day 23 — Lecture 23: Autoscaling: Concurrency, Batching & Cold Starts

[Previous lecture](../day22/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day24/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 22](../day22/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Relate arrival rate to concurrency.
- Account for provisioning lag.

## Lecture notes

Autoscaling reacts to observed or predicted demand, but replicas need time to become useful. Queue length, in-flight work, and service-time distributions often convey more than utilization alone. Hysteresis and cooldowns reduce oscillation; capacity targets also need headroom for bursts and long requests.

## Board example

Little’s law gives L=λW in a stable system with consistent boundaries. At 10 requests/s and mean residence time 2 seconds, mean in-system concurrency is 20. If demand jumps to 20 requests/s while capacity remains 10 requests/s for 30 seconds, backlog grows by roughly 300 requests under this fluid approximation.

## Notebook lab

- [autoscaling-concurrency-cold-starts](./autoscaling-concurrency-cold-starts.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Simulate a burst with nonzero cold-start delay. Compare a reactive policy with a warm reserve. Plot queue length, active replicas, and latency; explain the cost of the reserve and the risk of scaling down too early.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
