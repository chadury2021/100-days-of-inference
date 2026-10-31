# Day 30 — Lecture 30: Implement a BPE tokenizer from scratch

[Previous lecture](../day29/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day31/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 02](../day02/LECTURE.md), [Day 29](../day29/LECTURE.md).

## Learning objectives

- Train a deterministic toy BPE vocabulary.
- Distinguish training from encoding.

## Lecture notes

Start from a defined alphabet and a corpus represented as symbol sequences. Count adjacent pairs within each training sequence, select the most frequent pair, merge its non-overlapping occurrences, and repeat until reaching a merge budget. Deterministic tie-breaking makes training reproducible. Boundaries and preprocessing are part of the tokenizer definition.

Encoding uses the learned merge ranks, not fresh corpus counts. A toy character tokenizer demonstrates the algorithm but is not automatically compatible with GPT-2’s byte mapping, preprocessing, or special tokens. Decoding should invert the symbol mapping for supported input. Unknown-symbol behavior and Unicode handling need explicit tests rather than assumptions.

## Board example

For sequences [a,b,a,b] and [a,b], pair (a,b) occurs three times. Merging it into X gives [X,X] and [X]. One merge rule reduces the corpus from six symbols to three. Subsequent encoding must apply this learned rule consistently.

## Lab procedure

Implement pair counting, stable tie-breaking, non-overlapping merging, encoding, and decoding in a small Python module. Test empty input, repeated symbols, overlapping pairs such as aaa, and an unseen character. Compare your trace with the Day 02 notebook.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit merge rules, round-trip cases, and corpus token counts before and after training.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why token compression alone does not measure language-model quality.

## Further reading

- [Tokenization pipeline](https://huggingface.co/docs/tokenizers/en/pipeline)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
