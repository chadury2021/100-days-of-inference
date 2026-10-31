# Day 37 — Lecture 37: Sweep quantization bit widths and plot perplexity vs compression

[Previous lecture](../day36/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day38/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 35](../day35/LECTURE.md), [Day 36](../day36/LECTURE.md).

## Learning objectives

- Compute token-weighted perplexity.
- Compare measured storage across bit widths.

## Lecture notes

Perplexity is exp of mean negative log-likelihood over evaluated target tokens. Keep tokenizer, held-out corpus, context windows, stride, and padding policy fixed. Quantize each candidate from the same original checkpoint rather than repeatedly quantizing already rounded weights. Exclude calibration examples from evaluation.

Compression should use actual artifact bytes or a clearly labeled theoretical estimate that includes scale overhead. A quality curve is not a serving-speed curve. Weight-only quantization may use floating-point activations and different kernels at different precisions. Report failures such as unsupported bit widths rather than interpolating invented results.

## Board example

If two batches have total negative log-likelihood 20 over 10 tokens and 90 over 30 tokens, the corpus mean is 110/40=2.75 and perplexity is exp(2.75)≈15.64. Averaging the two batch perplexities gives the wrong token weighting.

## Lab procedure

Evaluate one small model at its reference precision and two supported lower precisions on the same corpus. Save total loss and valid-token count per batch, artifact bytes, and a few task-specific examples.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit perplexity-versus-bytes and task-quality tables.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why perplexity comparisons across different tokenizers require special care.

## Further reading

- [Perplexity evaluation](https://huggingface.co/docs/transformers/en/perplexity)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
