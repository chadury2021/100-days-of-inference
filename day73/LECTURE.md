# Day 73 — Lecture 73: Measure speculative decoding acceptance rates by draft model size

[Previous lecture](../day72/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day74/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 15](../day15/LECTURE.md), [Day 38](../day38/LECTURE.md), [Day 72](../day72/LECTURE.md).

## Learning objectives

- Measure acceptance and committed progress.
- Include draft overhead and memory.

## Lecture notes

A larger draft model may agree with the target more often but also cost more to execute and store. Measure acceptance by position and prompt class, then measure committed tokens per complete verification cycle. Rejections truncate accepted prefixes, so a single marginal token agreement rate does not fully determine useful progress.

Keep target, sampling policy, prompt distribution, and draft length controlled. The draft can compete for memory or bandwidth with the target; compare total serving resources and concurrency. Include the case where target-only generation is faster. An exact-sampling implementation needs the correction rules from Day 38, not only a match-rate heuristic.

## Board example

Draft A costs 2 ms plus 10 ms verification and commits 2 tokens on average: 6 ms/token. Draft B costs 6 ms plus 10 ms verification and commits 3: about 5.33 ms/token. If B commits only 2.5, it becomes 6.4 ms/token and loses to A.

## Lab procedure

Compare at least two available draft sizes or a labeled cost simulation. Record per-position acceptance, committed tokens/cycle, draft time, verification time, total memory, and target-only latency.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the size-versus-effective-latency curve.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why the draft with the highest acceptance may not be the best system choice.

## Further reading

- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
