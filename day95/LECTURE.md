# Day 95 — Lecture 95: Fine-tuning a small model for inference quality vs a large quantized one

[Previous lecture](../day94/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day96/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 37](../day37/LECTURE.md), [Day 61](../day61/LECTURE.md), [Day 72](../day72/LECTURE.md).

## Learning objectives

- Define a fair task-specific comparison.
- Include adaptation and serving costs.

## Lecture notes

Compare models on a concrete use case with fixed acceptance criteria. A small adapted model may specialize well, while a larger quantized model may retain broader capability. Neither parameter count nor quantization bit width alone predicts task performance. Keep training, validation, and held-out evaluation data separate, and freeze the decision rule before final evaluation.

Measure latency, useful throughput, memory, and quality using each model’s appropriate tokenizer and documented prompt format. Token counts may not be directly comparable across tokenizers, so also report request-level outcomes and end-to-end latency. Training cost is amortized over future usage; include it when claiming economic advantage.

## Board example

If adaptation costs a hypothetical $100 and saves $0.001 per accepted request, simple break-even is 100,000 accepted requests, excluding maintenance. If the adapted model fails the quality floor, that cost calculation does not make it eligible.

## Lab procedure

Choose a narrow classification or extraction fixture. Compare an unadapted small model, a small adapted model if training is available, and a supported larger quantized model. Use a mock cost analysis when training cannot be performed.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a quality/latency/memory table and amortization assumptions.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain one out-of-domain test that could reveal excessive specialization.

## Further reading

- [Parameter-efficient fine-tuning](https://huggingface.co/docs/peft/en/index)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
