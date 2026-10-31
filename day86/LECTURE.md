# Day 86 — Lecture 86: Speech-to-speech pipeline: ASR → LLM → TTS end-to-end latency

[Previous lecture](../day85/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day87/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 68](../day68/LECTURE.md), [Day 80](../day80/LECTURE.md), [Day 81](../day81/LECTURE.md).

## Learning objectives

- Trace first audible response.
- Manage partial transcripts and cancellation.

## Lecture notes

A speech pipeline combines endpoint detection, ASR, language-model generation, TTS, and playback. These stages can overlap only when their interfaces accept incremental results. A partial transcript may change, so sending every unstable fragment directly to generation can create repeated or contradictory work. Define when text becomes committed for downstream use.

Measure latency from the user’s end of speech to first audible response, along with full-turn duration. Endpoint detection and buffering often dominate perceived delay. Interruption should cancel obsolete generation and queued audio consistently; otherwise the system may continue speaking after a new turn begins. Keep transcript quality and response quality in the same evaluation.

## Board example

If endpoint detection takes 300 ms, final ASR 150 ms, LLM TTFT 250 ms, TTS first audio 200 ms, and playback buffering 100 ms sequentially, first response is 1,000 ms after speech ends. Overlap can reduce this only where dependencies allow it.

## Lab procedure

Connect mock incremental stages first, recording timestamps and turn IDs. Inject a revised transcript and a user interruption. With available models, replace one mock at a time and measure the changed critical path.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit a turn timeline, cancellation trace, and quality examples.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain which stage you would optimize first and why.

## Further reading

- [Whisper reference implementation](https://github.com/openai/whisper)
- [Text-to-speech task guide](https://huggingface.co/docs/transformers/en/tasks/text-to-speech)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
