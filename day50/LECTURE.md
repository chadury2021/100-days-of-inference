# Day 50 — Lecture 50: Simulate continuous batching: queue arrivals, dynamic batch formation

[Previous lecture](../day49/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day51/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 09](../day09/LECTURE.md), [Day 23](../day23/LECTURE.md), [Day 24](../day24/LECTURE.md).

## Learning objectives

- Model arrivals and token-step scheduling.
- Evaluate admission and completion behavior.

## Lecture notes

A discrete-event simulator can represent request arrival, prefill, decode steps, and completion. A static batch waits for its members according to a chosen policy; continuous batching admits new work as capacity becomes available. Define capacity in both active requests and token or memory budget, because equal request counts may represent very different work.

The scheduler needs explicit ordering for simultaneous events and a deterministic random seed. Keep service-time assumptions visible: fixed time per token is a simplification, while real step duration depends on batch and context. Include cancellation and exhausted token budgets so the simulation does not accumulate immortal requests.

## Board example

With two active slots, A needs two decode steps and B needs five. If C arrives after step one, a continuous scheduler can admit C after A completes at step two. A static scheduler that waits for the whole batch delays C until B finishes at step five.

## Lab procedure

Implement a small event loop and compare static admission with per-step admission on the same arrival trace. Record first service, first token, completion, and active batch size. Add one burst and one long-output outlier.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit scheduler timelines, queue lengths, and p95 latency by request class.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which conclusions depend on the assumed batch service-time function.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
