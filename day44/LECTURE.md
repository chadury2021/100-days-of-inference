# Day 44 — Lecture 44: Write a custom elementwise CUDA kernel via Triton

[Previous lecture](../day43/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day45/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 07](../day07/LECTURE.md), [Day 19](../day19/LECTURE.md), [Day 42](../day42/LECTURE.md).

## Learning objectives

- Map program IDs to array offsets.
- Mask tail loads and stores.

## Lecture notes

An elementwise kernel partitions a flat array into blocks. Program ID selects a block, local offsets select elements within it, and a mask excludes offsets at or beyond the array length. Guard both loads and stores; a correct result for divisible sizes does not prove tail safety. Establish input dtype, device, contiguity, and aliasing assumptions.

Use a simple affine or vector-add operation first. Compare against a library reference, then tune block size across small and large arrays. JIT compilation belongs to startup cost and should be excluded from warm measurements. A custom kernel is useful only if its correctness and measured behavior justify maintaining it.

## Board example

For N=1,000 and block size 256, launch four programs. The last covers offsets 768–1,023, of which only 232 are valid. Its mask must reject the remaining 24 positions. For N=0, define an empty-result path without an invalid launch.

## Lab procedure

Implement a vector-add kernel following the official tutorial, then adapt it to y=ax+b. Test N=0,1,255,256,257, and 1,000, plus multiple dtypes. Report compilation and warm execution separately.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit tail tests and a bandwidth plot.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why increasing block size indefinitely may worsen performance.

## Further reading

- [Triton vector-add tutorial](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
