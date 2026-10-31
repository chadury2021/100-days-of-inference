# Day 47 — Lecture 47: Deploy SGLang, benchmark structured output latency

[Previous lecture](../day46/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day48/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 10](../day10/LECTURE.md), [Day 29](../day29/LECTURE.md), [Day 46](../day46/LECTURE.md).

## Learning objectives

- Evaluate schema and semantic correctness.
- Measure grammar-related overhead.

## Lecture notes

Structured decoding restricts the output space, but schema validity and task success remain different objectives. Specify the exact schema, validation policy, and semantic rubric before benchmarking. Compare against an unconstrained baseline on the same prompts and model; a different output length or retry policy can otherwise explain the observed latency difference.

Schema processing may introduce setup work, and repeated schemas may benefit from reuse. Separate first-use and warm-schema measurements. Include difficult cases such as empty arrays, optional fields, escapes, and truncated generations. A generation stopped by a token budget may remain incomplete even when the decoding process enforced valid prefixes.

## Board example

Out of 100 outputs, suppose 98 pass JSON parsing, 95 pass the schema, and 80 contain the correct answer. Report 98%, 95%, and 80% separately. Calling this 95% task accuracy would conflate structure with meaning.

## Lab procedure

Serve a supported model with SGLang using the documented structured-output interface. Evaluate a fixed extraction task with constrained and unconstrained generation, measuring cold/warm schema latency, completion rate, and semantic correctness.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the schema, fixtures, three correctness metrics, and latency distributions.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how you score truncated or missing responses.

## Further reading

- [SGLang structured outputs](https://docs.sglang.io/docs/advanced_features/structured_outputs)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
