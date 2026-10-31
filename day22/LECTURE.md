# Day 22 — Lecture 22: Containerization: Docker & NVIDIA NIMs

[Previous lecture](../day21/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day23/LECTURE.md)

**Session:** 90 minutes plus assignment. **Preparation:** Review [Day 21](../day21/LECTURE.md) and the [companion summary](./README.md).

## Learning objectives

- Separate image, model, and runtime configuration.
- Define readiness.

## Lecture notes

An inference container packages application dependencies, while model artifacts may be bundled or supplied separately. A running process is not necessarily ready to serve: weights must load and the request path must work. Reproducibility requires recording the image digest, model revision, runtime version, and configuration.

## Board example

A container starts its process after 5 seconds but finishes loading weights after 60 seconds. Routing traffic at process start exposes a 55-second failure window. A readiness probe should gate admission until the serving path is usable; liveness answers a different question.

## Notebook lab

- [containerization-docker-nim](./containerization-docker-nim.ipynb)

Read the notebook’s setup and assumptions, then use its relevant demonstrations to investigate the assignment below. Record the baseline before changing one variable. Label simulated and measured results separately; use the [course measurement conventions](../LECTURES.md#measurement-and-submission-conventions).

## Problem set and deliverable

Review the notebook container example and document image/model boundaries. Define readiness, liveness, and a minimal inference smoke check. Measure image download, model loading, and warmup as separate startup stages if execution is available.

## Check your understanding

Explain the worked example without looking at the notes. Name one assumption that would change its conclusion and describe an experiment that could test it.
