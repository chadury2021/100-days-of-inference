# Day 01 — Lecture 01: LLM Inference Mechanics: End-to-end text generation

[Course schedule](../LECTURES.md) · [Next lecture](../day02/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review Python arrays, matrix shapes, and conditional probability; read the [companion summary](./README.md).

## Learning objectives

- Trace prefill and decode.
- Distinguish latency from throughput.

## Lecture notes

An autoregressive model factors a sequence probability into conditional next-token probabilities. Tokenization supplies integer IDs, the forward pass produces logits, and a decoding rule chooses the next ID. Prefill processes the prompt; subsequent decode iterations extend its context. Time to first token includes more than model execution: queueing and tokenization also matter.

## Board example

For a request producing 11 tokens, suppose time to first token is 100 ms and each of the remaining 10 tokens takes 20 ms. End-to-end latency is 100 + 10 × 20 = 300 ms. Request throughput and aggregate token throughput cannot be inferred from this single latency measurement.

## Notebook lab

- [llm-inference-mechanics](./llm-inference-mechanics.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Derive p(x₁,…,xₙ) as a product of conditional probabilities. Compare greedy and temperature-based generation on three prompts. Submit a per-token latency plot and identify which work your timer includes.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
