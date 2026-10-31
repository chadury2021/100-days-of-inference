# Day 84 — Lecture 84: Multi-modal batching: mixing text and image requests

[Previous lecture](../day83/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day85/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 50](../day50/LECTURE.md), [Day 58](../day58/LECTURE.md), [Day 78](../day78/LECTURE.md).

## Learning objectives

- Estimate multimodal request work.
- Preserve fairness across request types.

## Lecture notes

A mixed workload may combine text-only requests, one-image requests, and requests with multiple high-resolution images. Scheduling solely by request count can place radically different workloads in the same batch. Use processor-derived visual token counts and text lengths where available, along with modality-specific encoder limits.

Separate encoding and language-model work in the scheduling model. Bucketing can improve padding efficiency but delay uncommon request types. Preserve a fairness or maximum-wait policy so efficiency does not starve large visual jobs. The shared language decoder still needs consistent masks and positions for each modality’s input representation.

## Board example

A text request has 100 tokens while an image request adds 900 visual tokens to the same 100-token prompt. Treating both as one equal-size admission understates the second’s prefill footprint by a factor of ten in this simplified token model.

## Lab procedure

Extend Day 50’s simulator with text and image-encoder stages, different token budgets, and length bucketing. Compare count-based admission against cost-based admission under the same arrival trace. Include a rare large-image class.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit padding waste, per-class p95 latency, and maximum wait.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain a case where better average utilization worsens one class’s experience.

## Further reading

- [Image-text-to-text inference](https://huggingface.co/docs/transformers/en/tasks/image_text_to_text)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
