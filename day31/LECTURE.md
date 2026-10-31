# Day 31 — Lecture 31: Build a bare autoregressive decoder loop in PyTorch

[Previous lecture](../day30/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day32/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 01](../day01/LECTURE.md), [Day 04](../day04/LECTURE.md), [Day 05](../day05/LECTURE.md).

## Learning objectives

- Write an explicit decode loop.
- Preserve stopping and cache semantics.

## Lecture notes

Separate tokenization, model execution, token selection, and stopping into inspectable steps. A minimal greedy decoder takes the final-position logits, selects their argmax, appends that ID, and repeats until EOS or a generation budget. Use evaluation mode and an inference context; dropout or gradient tracking changes the experiment.

An uncached implementation provides a correctness reference. The cached variant initially processes the prompt and then only the new token, passing the returned cache forward. Attention masks and position indices must reflect the entire logical sequence even when the latest input contains one token. Batch padding and per-sequence completion require more bookkeeping than a single-prompt loop.

## Board example

If a prompt has 5 tokens and generation is capped at 3, the uncached forward input lengths are 5, 6, and 7. With a correctly initialized cache, they are 5, 1, and 1. Both should select the same greedy IDs within the effects of numerical precision.

## Lab procedure

Use a small local model to implement the uncached path first. Add a cached path and compare logits and token IDs on three prompts. Exercise immediate EOS, maximum-length stopping, and an empty-input policy.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit both traces and a latency comparison with warmup excluded.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why changing sampling RNG consumption can prevent token-for-token agreement even when distributions match.

## Further reading

- [PyTorch inference and CUDA semantics](https://docs.pytorch.org/docs/stable/notes/cuda.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
