# Day 82 — Lecture 82: Image generation: diffusion model inference and kernel optimization

[Previous lecture](../day81/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day83/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 07](../day07/LECTURE.md), [Day 27](../day27/LECTURE.md), [Day 72](../day72/LECTURE.md).

## Learning objectives

- Decompose iterative generation cost.
- Evaluate quality when reducing work.

## Lecture notes

Diffusion generation repeatedly updates a noisy state using a learned denoising model and a chosen sampling schedule. End-to-end work can also include text encoding, image decoding, safety or quality processing, and serialization. Keep the model, scheduler, seed policy, resolution, and guidance settings explicit when comparing configurations.

Reducing denoising steps changes the inference algorithm and may change quality; it is not equivalent to optimizing the same computation. Compilation, precision changes, and memory-efficient attention can improve execution, but effects depend on shapes and support. Image batches can increase throughput while increasing memory and single-image latency. Use multiple prompts and seeds rather than selecting one attractive output.

## Board example

With 30 denoising steps at 20 ms each plus 100 ms fixed overhead, total time is 700 ms. Reducing step time to 15 ms gives 550 ms. Reducing the count to 15 gives 400 ms under the original timing, but requires a separate quality evaluation.

## Lab procedure

Benchmark a supported small diffusion pipeline across two step counts and two execution settings. Hold prompt/seed fixtures fixed and record image quality judgments, total time, denoiser time, and peak memory.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a quality/latency grid and identify which changes alter the algorithm.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain the limit imposed by fixed overhead.

## Further reading

- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
