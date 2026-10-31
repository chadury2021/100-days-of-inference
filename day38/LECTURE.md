# Day 38 — Lecture 38: Simulate draft-target speculative decoding with acceptance sampling

[Previous lecture](../day37/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day39/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 15](../day15/LECTURE.md), [Day 31](../day31/LECTURE.md).

## Learning objectives

- Implement acceptance and residual sampling.
- Verify the target distribution empirically.

## Lecture notes

For a draft distribution q and target p, sample x from q and accept it with probability min(1,p(x)/q(x)). On rejection, sample from the normalized positive residual max(p−q,0). In a sequence, stop verification at the first rejection; later draft tokens conditioned on the rejected history cannot be committed. Handle all-accepted proposals with the algorithm’s next-token step.

The correction is essential. A rule that accepts only matching argmax tokens describes a different, greedy procedure. For a toy categorical simulation, estimate output frequencies across many draws and compare them with p. Distribution agreement is statistical, so report sample count and uncertainty rather than expecting identical sampled sequences.

## Board example

Let p=[0.8,0.2] and q=[0.5,0.5]. Token A is always accepted; B is accepted with probability 0.4. Accepted mass is [0.5,0.2], and the rejected mass 0.3 goes entirely to A through the residual. Output probabilities are exactly [0.8,0.2].

## Lab procedure

Implement the two-token case using Python’s random module, then add three-token distributions. Test p=q, disjoint support, and near-zero probabilities. Compare empirical frequencies and rejected mass with hand calculations.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit distribution checks and a cost model with draft and verification overhead.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why acceptance rate alone cannot establish speedup.

## Further reading

- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
