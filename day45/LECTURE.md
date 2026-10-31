# Day 45 — Lecture 45: Build a PyTorch custom op with CUDA backend

[Previous lecture](../day44/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day46/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 08](../day08/LECTURE.md), [Day 44](../day44/LECTURE.md).

## Learning objectives

- Specify an operator contract.
- Integrate CUDA execution with dispatch.

## Lecture notes

A custom operator needs a public contract before a kernel: supported ranks, shapes, dtypes, devices, strides, mutation, and output layout. Its registration must reflect those semantics. Reject unsupported inputs explicitly instead of interpreting arbitrary tensor memory as contiguous. A CPU reference is useful for correctness even when production use is GPU-only.

Device guards and the framework’s current stream matter for composability. Register appropriate metadata behavior when using compilation, and state whether autograd is supported. An inference-only operator should not silently produce incorrect gradients. Packaging must account for compiler and framework compatibility; record the tested environment rather than claiming universal binary portability.

## Board example

An operator that computes z=x+y for two length-N tensors must reject shapes [N] and [N,1] if broadcasting is not in its contract. Accepting both and returning a flat N-element array would disagree with standard broadcast semantics.

## Lab procedure

Build a small operator from the official example, document its supported subset, and compare against a reference for valid inputs. Test noncontiguous views, mixed devices, mismatched shapes, and compilation metadata if supported.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the contract, correctness cases, and installation instructions for the tested environment.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain one failure that numerical happy-path tests alone would miss.

## Further reading

- [PyTorch custom C++ and CUDA operators](https://docs.pytorch.org/tutorials/advanced/cpp_custom_ops.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
