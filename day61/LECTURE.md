# Day 61 — Lecture 61: GPU cost model: $/token across instance types at different utilizations

[Previous lecture](../day60/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day62/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 26](../day26/LECTURE.md), [Day 52](../day52/LECTURE.md).

## Learning objectives

- Define a consistent cost denominator.
- Analyze utilization without double counting.

## Lecture notes

Cost per million useful tokens equals total cost over the observation window divided by delivered useful tokens, multiplied by one million. Include all replicas, idle capacity, and relevant infrastructure if claiming total service cost. Define input versus output accounting and how failed, retried, or discarded tokens are treated.

A prospective model can multiply peak throughput by an assumed effective utilization. An observed average throughput already includes the measured idle time, so multiplying it by utilization again double-counts the loss. Keep hypothetical prices labeled and date any live quotes. Compare cost only among configurations that meet the same quality and latency constraints.

## Board example

A fleet costs $18 during one hour and delivers 3.6 million useful output tokens. Cost is $5 per million output tokens. If raw execution produced 4 million but 0.4 million were discarded, dividing by 4 million understates cost per useful output.

## Lab procedure

Build a worksheet with hourly fleet cost, observed token count, quality pass rate, and latency eligibility. Sweep utilization only in the prospective model. Compare warm-reserve and scale-to-zero scenarios using explicitly hypothetical prices.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit sensitivity plots and an accounting boundary.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how retries can increase both billed compute and apparent raw token throughput while worsening useful cost.

## Further reading

- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
