# Day 48 — Lecture 48: TensorRT-LLM: compile a model and compare with eager PyTorch

[Previous lecture](../day47/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day49/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 08](../day08/LECTURE.md), [Day 11](../day11/LECTURE.md), [Day 27](../day27/LECTURE.md).

## Learning objectives

- Separate engine preparation from steady-state inference.
- Test the supported shape envelope.

## Lecture notes

Compilation and runtime optimization trade preparation work for reusable execution plans. TensorRT-LLM has version-dependent execution paths; identify the documented path for your installed version and hardware instead of assuming every model follows one engine-build command. Use the same weights, tokenizer, sampling policy, and quality checks as the reference.

Record conversion, build, load, and warmup separately. Test shapes near the configured limits and define the response to an unsupported request. Numerical changes should be evaluated on logits or task quality as appropriate, not hidden by choosing only easy prompts. Compare total job time as well as warm latency.

## Board example

An optimization requiring 180 seconds of setup and saving 6 ms per request breaks even after 30,000 requests, ignoring other differences. For a 1,000-request job, the warm saving is only 6 seconds, far below the setup cost.

## Lab procedure

Choose a small supported model and build or configure the documented optimized path. Measure preparation time, warm latency, memory, and quality against eager execution at two prompt lengths. Record unsupported paths explicitly.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit an amortization curve and compatibility table.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which result would justify this approach for a long-running service but not a short batch job.

## Further reading

- [TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
