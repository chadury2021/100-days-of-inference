# Day 54 — Lecture 54: NVIDIA NIM deployment and custom serving-container contracts

[Previous lecture](../day53/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day55/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 22](../day22/LECTURE.md), [Day 53](../day53/LECTURE.md).

## Learning objectives

- Distinguish a vendor NIM from a custom service.
- Version deployment artifacts.

## Lecture notes

NVIDIA NIM packages a supported inference stack with model- and platform-specific deployment requirements. Matching a familiar HTTP endpoint does not turn an arbitrary image into a NIM. Choose either a documented NIM deployment on supported hardware or a custom container with an explicitly documented API contract. Describe that choice accurately in the artifact name and report.

For a NIM path, record the selected image, supported model profile, host requirements, and model-cache location from the official guide. For a custom path, define endpoint compatibility and test it rather than asserting vendor certification. Registry publication is a separate lifecycle step: a tag is mutable, while a digest identifies the pushed image content.

## Board example

If tag course-server:latest points to digest A today and B tomorrow, repeating the tag does not reproduce the deployment. Recording digest A plus the model revision and configuration makes the intended artifact set unambiguous.

## Lab procedure

Prepare a deployment manifest for a documented NIM or the Day 53 custom image. Validate health and one inference request, then document the registry push/pull procedure for a lab registry. Publication is an exercise, not an action performed by these notes.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit the compatibility checklist, digest manifest, and smoke-test result.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

State exactly which contract was tested and whether an actual NVIDIA NIM was used.

## Further reading

- [NVIDIA NIM deployment playbook](https://build.nvidia.com/playbooks/nim-llm/instructions)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
