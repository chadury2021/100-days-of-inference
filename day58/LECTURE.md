# Day 58 — Lecture 58: Build a priority request queue with batch formation

[Previous lecture](../day57/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day59/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 24](../day24/LECTURE.md), [Day 50](../day50/LECTURE.md), [Day 57](../day57/LECTURE.md).

## Learning objectives

- Combine priorities with token budgets.
- Prevent starvation.

## Lecture notes

A batch scheduler chooses eligible requests under capacity limits. A request-count limit alone may admit too many prompt tokens or too much KV state. Track an estimated token or memory budget and reserve room for ongoing decoding. Priority can reflect service class, but lower-priority work still needs an explicit progress policy.

Aging increases effective priority with wait time; weighted fair scheduling assigns shares across classes. Neither is interchangeable with FIFO. Stable ordering within a class makes behavior predictable. Large jobs that never fit the current residual budget need an explicit path, such as a dedicated slot or rejection with a documented limit.

## Board example

With a 100-token admission budget, queued prompts of 70, 40, and 20 tokens cannot all enter. Selecting 70 and 20 uses 90; selecting 40 and 20 uses 60. A greedy fill rule changes fairness and may repeatedly postpone the 70-token request.

## Lab procedure

Extend Day 50 with two priorities, stable arrival ordering, aging, and a token budget. Replay a continuous high-priority stream plus occasional large low-priority requests. Include one request larger than the total budget.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit wait-time distributions by class and a starvation trace before and after aging.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how overload differs from unfair scheduling.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
