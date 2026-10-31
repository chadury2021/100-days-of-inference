# Day 51 — Lecture 51: Visualize PagedAttention block layout and fragmentation

[Previous lecture](../day50/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day52/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 09](../day09/LECTURE.md), [Day 39](../day39/LECTURE.md), [Day 50](../day50/LECTURE.md).

## Learning objectives

- Distinguish logical and physical blocks.
- Quantify internal fragmentation.

## Lecture notes

A request’s tokens occupy logical positions, while a page table maps those positions to physical blocks. Logical adjacency does not require physical adjacency. This permits reuse of freed blocks and sharing of compatible prefixes. Tail slots within a partially occupied block are internal fragmentation; free whole blocks are available capacity, not internal waste.

Draw the page table separately from physical storage. Visuals that place every request contiguously can obscure the reason for paging. Reference counts and copy-on-write must be visible when a shared partial block changes. Increasing block size reduces mapping overhead but may increase tail waste, so neither extreme is universally best.

## Board example

For block size 8 and request lengths 9, 16, and 3, allocation is 2+2+1=5 blocks or 40 token slots. Useful occupancy is 28 tokens and internal waste is 12 slots, a 30% allocation waste fraction.

## Lab procedure

Extend the Day 39 allocator with a text grid or plotted physical-block diagram. Animate or snapshot allocation, sharing, completion, and reallocation. Sweep block sizes 4, 8, and 16 on the same length distribution.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit diagrams and useful/allocated/free capacity counts.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a large free region is not itself evidence of fragmentation.

## Further reading

- [vLLM documentation](https://docs.vllm.ai/en/latest/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
