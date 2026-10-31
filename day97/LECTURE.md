# Day 97 — Lecture 97: Intelligence evaluation: build an eval harness for a deployed model

[Previous lecture](../day96/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day98/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 37](../day37/LECTURE.md), [Day 47](../day47/LECTURE.md), [Day 77](../day77/LECTURE.md).

## Learning objectives

- Build task-grounded evaluation cases.
- Distinguish quality regressions from harness failures.

## Lecture notes

An evaluation harness needs a task definition, representative inputs, expected behavior or scoring rubric, and a stable execution record. Include normal, boundary, and failure cases. Version prompts, model settings, and fixtures so a score change can be attributed. Structural validity, factual correctness, and user usefulness may require separate scores.

Use deterministic checks where possible and blinded human or model-assisted rubrics where necessary. A model judge is itself fallible and should be calibrated against reviewed examples. Keep timeouts and malformed responses in the report. Repeated stochastic trials and confidence intervals help distinguish small apparent gains from noise; avoid tuning repeatedly on the final held-out set.

## Board example

Model A passes 90 of 100 cases and B passes 92. The two-point difference alone does not establish a reliable improvement. Inspect paired outcomes: which cases changed, whether failures cluster, and how repeated trials affect the comparison.

## Lab procedure

Build a 30-case fixture spanning at least three categories with explicit scoring. Run a reference and candidate endpoint or mock adapters. Record raw responses, parse failures, rubric scores, latency, and exact configuration.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a per-category comparison and release recommendation.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how you would detect a harness bug that mistakenly treats missing outputs as passes.

## Further reading

- [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
