# Day 96 — Lecture 96: Distillation for inference: teacher-student latency/quality tradeoffs

[Previous lecture](../day95/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day97/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 31](../day31/LECTURE.md), [Day 95](../day95/LECTURE.md).

## Learning objectives

- Distinguish soft-target and sequence distillation.
- Evaluate student quality and speed.

## Lecture notes

Distillation transfers behavior from a teacher to a student through training targets. Soft-target distillation can compare probability distributions over a compatible output space; sequence distillation trains on teacher-generated outputs. Different tokenizers complicate token-level logit matching, so do not assume arbitrary teacher and student vocabularies align.

A common classification objective mixes label cross-entropy with temperature-scaled KL divergence between teacher and student distributions. The temperature changes probability softness, and the loss weighting determines how much the student follows labels versus teacher behavior. Generated examples can contain errors; reserve independent evaluation data and inspect failure patterns rather than treating the teacher as ground truth.

## Board example

For matching two-class probabilities p=[0.8,0.2] and q=[0.6,0.4], KL(p||q)=0.8 ln(0.8/0.6)+0.2 ln(0.2/0.4)≈0.0915 nats. Matching only the argmax discards this confidence information.

## Lab procedure

Implement a small classifier distillation experiment or a sequence-target dataset pipeline. Compare the same student with and without distillation, using identical held-out examples. Measure student inference latency separately from teacher data-generation and training costs.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the target-generation method, loss definition, quality changes, and deployment cost model.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how teacher mistakes can propagate into the student.

## Further reading

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
