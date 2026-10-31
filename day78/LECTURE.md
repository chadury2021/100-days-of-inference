# Day 78 — Lecture 78: Vision Language Model (VLM) inference: image preprocessing and batching

[Previous lecture](../day77/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day79/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 04](../day04/LECTURE.md), [Day 27](../day27/LECTURE.md), [Day 52](../day52/LECTURE.md).

## Learning objectives

- Account for image preprocessing and visual tokens.
- Batch by actual multimodal cost.

## Lecture notes

A vision-language request often includes image decoding, resizing or tiling, a vision encoder, projection into language-model inputs, and text generation. The exact sequence depends on the architecture. Use the model’s own processor and record its configuration; arbitrary resizing can alter both token count and answer quality. Image count alone is a weak workload descriptor.

Batching may require padding visual and textual sequences, which wastes work when resolutions or tile counts differ. Bucket by compatible processing shapes and total token budget. Measure preprocessing separately so a CPU image bottleneck is not misdiagnosed as slow language decoding. Include corrupt images and unsupported dimensions in the input contract.

## Board example

In a hypothetical patch encoder with 16×16 patches and no extra tokens, a 224×224 image gives 14²=196 patches. A 448×448 image gives 28²=784, four times as many. Actual models may add tokens, tile images, or compress features, so verify the processor output.

## Lab procedure

Use a supported small VLM on the same image at two resolutions. Record processor output shapes, preprocessing time, encoder time where observable, TTFT, and answer quality. Compare mixed-resolution with bucketed batches.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the shape trace and cost/quality comparison.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why lowering resolution may improve speed while losing small-text or fine-detail accuracy.

## Further reading

- [Image-text-to-text inference](https://huggingface.co/docs/transformers/en/tasks/image_text_to_text)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
