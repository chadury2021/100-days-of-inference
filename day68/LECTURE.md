# Day 68 — Lecture 68: Build a streaming inference client using SSE

[Previous lecture](../day67/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day69/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 29](../day29/LECTURE.md), [Day 65](../day65/LECTURE.md).

## Learning objectives

- Parse event framing across arbitrary reads.
- Handle completion and interruption.

## Lecture notes

Server-sent events use a text framing protocol whose event boundaries are independent of TCP chunks. Keep a byte/text buffer, decode UTF-8 incrementally, collect fields until a blank line, and dispatch the resulting event. Multiple data fields form one event payload. Comments may act as keepalives and should not become generated text.

The application defines how event payloads represent tokens, errors, and completion. A completion marker such as a sentinel string is application-specific, not a universal SSE rule. Distinguish a clean application terminal event from a transport close before completion. Automatic reconnect cannot safely resume arbitrary generation unless the service defines an explicit resume contract.

## Board example

A read may end with data: {"te and the next begin with xt":"hi"} followed by a blank line. Neither read is a complete JSON payload alone. Conversely, one read may contain several complete events that must all be processed.

## Lab procedure

Build a parser fixture that splits every byte boundary of a multibyte message, combines multiple events, includes comments, and closes mid-event. Measure first application-content arrival separately from the first network byte.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit parser tests and interruption behavior.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain how repeated events or reconnection would affect displayed output.

## Further reading

- [Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
