# Day 80 — Lecture 80: ASR (Whisper): single-chunk and long-file latency optimization

[Previous lecture](../day79/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day81/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 27](../day27/LECTURE.md), [Day 29](../day29/LECTURE.md).

## Learning objectives

- Measure real-time factor and transcription error.
- Handle long-audio boundaries.

## Lecture notes

ASR inference includes audio decoding, channel handling, resampling, feature extraction, and model execution. Preserve the expected sample rate and preprocessing contract. Duration is a natural workload unit, but speech density, language, silence, and noise also affect decoding behavior. Record these properties for evaluation fixtures.

Long recordings may require windows or chunks, with overlap or context to preserve words near boundaries. Independent chunk transcription can duplicate or omit boundary text. Word error rate counts substitutions, deletions, and insertions relative to the reference; punctuation and normalization policies affect the score. Report real-time factor together with first-result delay for streaming-like workflows.

## Board example

Processing 60 seconds of audio in 12 seconds gives real-time factor 0.2. If the reference has 100 words and the transcript has 5 substitutions, 3 deletions, and 2 insertions, WER=(5+3+2)/100=10%. Faster execution alone says nothing about that error rate.

## Lab procedure

Use a small supported Whisper checkpoint and short licensed or self-recorded clips. Compare whole-clip and chunked transcription, keeping preprocessing fixed. Inspect words crossing chunk boundaries and include a silence segment.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit duration, runtime, WER policy, and boundary examples.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a low average real-time factor does not guarantee low interactive delay.

## Further reading

- [Whisper reference implementation](https://github.com/openai/whisper)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
