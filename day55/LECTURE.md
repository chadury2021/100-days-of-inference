# Day 55 — Lecture 55: Simulate an autoscaling policy: requests per second → replica count

[Previous lecture](../day54/LECTURE.md) · [Course schedule](../LECTURES.md) · [Next lecture](../day56/LECTURE.md)

**Session:** 90 minutes plus an implementation assignment. **Preparation:** [Day 23](../day23/LECTURE.md), [Day 50](../day50/LECTURE.md).

## Learning objectives

- Model delayed capacity.
- Compare hysteresis and warm reserves.

## Lecture notes

Start with a discrete-time queue model: backlog at the next step is max(0, backlog + arrivals − service capacity). New replicas contribute capacity only after startup completes. The controller observes a lagged signal and selects a desired replica count subject to minimum, maximum, and cooldown constraints. Scheduling a replica is not the same as making it ready.

Compare policies on identical arrival traces. A target utilization below one provides headroom but costs idle capacity. Scale-down must account for draining work and a minimum stable observation window. Prevent duplicate scale-up requests from repeatedly counting the same pending replica, a common error in simplified controllers.

## Board example

At 30 arrivals/s and 20 service completions/s, backlog grows by 10 requests/s. A new 10-request/s replica arriving after 20 seconds finds 200 queued requests. Matching arrivals then stops growth but does not clear that backlog without additional spare capacity.

## Lab procedure

Implement fixed-capacity, reactive, and warm-reserve policies. Include startup delay, a short burst, a sustained step, and a quiet period. Plot pending versus ready replicas, backlog, and approximate wait time.

Use the [measurement and submission conventions](../LECTURES.md#measurement-and-submission-conventions). This is a student exercise specification; reference implementations and recorded GPU measurements are not bundled for this day.

## Problem set and deliverable

Submit total replica-seconds and latency-target violations.

1. Reproduce the board calculation and state its units and assumptions.
2. Complete the lab comparison, keeping its baseline and raw observations.
3. Describe one failure case and how your implementation or analysis handles it.

## Check your understanding

Explain why a policy can stabilize the queue while leaving users waiting too long.

## Further reading

- [Kubernetes horizontal autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)

For runtime APIs and hardware support, use documentation matching the version in your experiment manifest. The numerical example is illustrative, not a reported benchmark.
