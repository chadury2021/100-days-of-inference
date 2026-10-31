# Day 26 — Lecture 26: Zero-Downtime Deployment & Cost Estimation

[Previous lecture](../day25/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day27/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 25](../day25/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Design rollout gates and draining.
- Calculate cost per useful token.

## Lecture notes

A rollout must validate readiness, preserve in-flight requests where possible, and define rollback behavior. Canary evaluation needs both system metrics and task-quality checks. Cost comparisons must use consistent accounting: measured throughput already reflects observed utilization and should not be discounted a second time.

## Board example

For a fleet costing $12/hour and delivering 1,000 useful tokens/s averaged over that hour, cost per million tokens is 12×10⁶/(1,000×3,600)≈$3.33. Include the entire fleet and define whether the denominator counts input, output, or both. A second identical fleet during rollout increases temporary cost.

## Notebook lab

- [zero-downtime-deployment](./zero-downtime-deployment.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Specify a canary schedule, readiness gate, rollback thresholds, and drain timeout. Simulate long-lived requests during cutover. Calculate cost from observed delivered tokens and identify any excluded infrastructure expenses.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
