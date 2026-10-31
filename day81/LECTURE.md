# Day 81 — Lecture 81: TTS: streaming real-time text-to-speech

[Previous lecture](../day80/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day82/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 29](../day29/LECTURE.md), [Day 68](../day68/LECTURE.md), [Day 80](../day80/LECTURE.md).

## Learning objectives

- Separate first-audio latency from synthesis speed.
- Manage chunk and playback buffers.

## Lecture notes

Text-to-speech may include text normalization, acoustic generation, and waveform synthesis. A streaming service emits playable audio chunks before the whole utterance is complete. Measure time to first audio, total synthesis time, and playback underruns separately. Audio duration provides the denominator for real-time factor, while chunk scheduling determines interactivity.

Small text chunks can reduce initial delay but deprive the model of context needed for pronunciation and prosody. Large chunks improve context at the cost of waiting. Preserve sample rate, channel count, and codec framing across chunks. A playback buffer absorbs jitter but adds latency; define what happens when a client cancels mid-utterance.

## Board example

If synthesizing 10 seconds of audio takes 2 seconds, real-time factor is 0.2. Yet if the first playable chunk arrives after 1.5 seconds, the interaction still has a noticeable initial wait. A 200 ms playback buffer can absorb smaller production jitter but adds 200 ms to first playback.

## Lab procedure

Use an available streaming TTS engine or a timed audio-chunk simulator. Sweep chunk sizes and buffer depth, then measure first playback, underruns, and total duration. For a real model, listen for boundary artifacts using the same text.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit latency and continuity results.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why faster-than-real-time average generation can still produce audible stalls.

## Further reading

- [Text-to-speech task guide](https://huggingface.co/docs/transformers/en/tasks/text-to-speech)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
