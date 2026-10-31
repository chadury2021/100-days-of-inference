# Inference Engineering — Daily Lecture Series

An independent course organized around the existing inference-engineering notebooks. The format takes inspiration from [Stanford CS229’s public course materials](https://see.stanford.edu/Course/CS229/): a numbered schedule, lecture notes, practical work, and problem sets. This is original course organization, with no Stanford affiliation.

## Course guide

**Prerequisites:** Python, basic NumPy/PyTorch, matrix multiplication, probability, and basic command-line use. CUDA experience is useful from Day 07 onward. Review tensor shapes before starting Day 01.

**Outcome:** Explain the generation pipeline, derive memory and performance estimates, evaluate serving optimizations, and design an inference service with measurable latency, quality, and cost targets.

**Pace:** One numbered session per study day; day labels are sequence numbers rather than calendar dates. Allow 90 minutes for each taught session, plus 30–60 minutes for its assignment. Implementation projects later in the course may span several study sessions.

**Coverage:** All 102 days include lecture notes, worked examples, lab instructions, and problem sets. Days 01–26 link the existing notebooks. Days 27–102 provide complete written lessons and student implementation assignments; they do not include prebuilt lab notebooks or claimed GPU benchmark results. The repository’s “100 Days” title is a challenge name: its existing roadmap contains 102 topics.

## Daily lecture format

| Time | Activity |
|---|---|
| 0–10 min | Review prerequisites and state the problem |
| 10–35 min | Develop the core model and equations |
| 35–50 min | Work through the numerical example |
| 50–75 min | Explore the linked notebook or simulation |
| 75–90 min | Discuss results and attempt the problem set |

Each lecture gives learning objectives, theory notes, a worked example, a notebook lab or written lab procedure, a problem set, and a comprehension check. Existing day READMEs remain companion summaries. Notebook demonstrations may use simulations or require specific hardware; identify which before interpreting results.

## Measurement and submission conventions

For every lab, submit the executed notebook or clearly labeled simulation, a short interpretation, and the requested plot or table. Record model revision, device, software versions, dtype, batch size, input/output lengths, warmup, and repetition count. Separate setup time from steady-state timing. State measurement boundaries and synchronize asynchronous GPU work when timing it; consult the [PyTorch benchmarking guide](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html).

Use numerical tolerances and quality checks before claiming an optimization works. Report failed runs and unsupported features explicitly. Hypothetical examples in the lecture notes illustrate arithmetic; they are not hardware benchmarks or price quotations.

## Assessment

- Daily problem sets and lab reports: 40%.
- Day 18 checkpoint: 15%. Compare an uncached baseline with two optimizations, including correctness, latency, memory, and tradeoffs.
- Day 26 systems review: 15%. Defend a capacity and deployment plan against a burst, a failed worker, and a model rollback.
- Days 98–102 capstone: 30%. Design, build, deploy in an available lab environment, evaluate, and document a serving stack.

Assess reports for correctness (40%), reproducible evidence (30%), interpretation of tradeoffs (20%), and clarity (10%). Hardware access is not required for conceptual exercises; simulated results must remain clearly distinguished from measurements.

## Daily schedule

### Phase 1 — Runtime: Single-Instance Optimization

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 01 — Lecture 01 | LLM Inference Mechanics: End-to-end text generation | [Notes](./day01/LECTURE.md) · [Companion](./day01/README.md) |
| Day 02 — Lecture 02 | Inference from Scratch: Model internals & tokenization | [Notes](./day02/LECTURE.md) · [Companion](./day02/README.md) |
| Day 03 — Lecture 03 | Embeddings: From integers to vectors | [Notes](./day03/LECTURE.md) · [Companion](./day03/README.md) |
| Day 04 — Lecture 04 | Transformer Blocks & Attention Deep Dive | [Notes](./day04/LECTURE.md) · [Companion](./day04/README.md) |
| Day 05 — Lecture 05 | KV Cache | [Notes](./day05/LECTURE.md) · [Companion](./day05/README.md) |
| Day 06 — Lecture 06 | Ops:Byte Ratio & Arithmetic Intensity | [Notes](./day06/LECTURE.md) · [Companion](./day06/README.md) |
| Day 07 — Lecture 07 | CUDA Kernels, Kernel Selection & Kernel Fusion | [Notes](./day07/LECTURE.md) · [Companion](./day07/README.md) |
| Day 08 — Lecture 08 | PyTorch, Model File Formats, ONNX & TensorRT | [Notes](./day08/LECTURE.md) · [Companion](./day08/README.md) |
| Day 09 — Lecture 09 | vLLM: PagedAttention & Continuous Batching | [Notes](./day09/LECTURE.md) · [Companion](./day09/README.md) |
| Day 10 — Lecture 10 | SGLang: RadixAttention & Structured Outputs | [Notes](./day10/LECTURE.md) · [Companion](./day10/README.md) |
| Day 11 — Lecture 11 | TensorRT-LLM: Compilation & Plugin System | [Notes](./day11/LECTURE.md) · [Companion](./day11/README.md) |
| Day 12 — Lecture 12 | NVIDIA Dynamo: Disaggregated Serving | [Notes](./day12/LECTURE.md) · [Companion](./day12/README.md) |
| Day 13 — Lecture 13 | Quantization: Number Formats (FP8, INT8, INT4, NVFP4) | [Notes](./day13/LECTURE.md) · [Companion](./day13/README.md) |
| Day 14 — Lecture 14 | Quantization Algorithms: GPTQ, AWQ, SmoothQuant | [Notes](./day14/LECTURE.md) · [Companion](./day14/README.md) |
| Day 15 — Lecture 15 | Speculative Decoding: Draft-Target, Medusa, EAGLE | [Notes](./day15/LECTURE.md) · [Companion](./day15/README.md) |
| Day 16 — Lecture 16 | KV Cache: Prefix Caching & Cache-Aware Routing | [Notes](./day16/LECTURE.md) · [Companion](./day16/README.md) |
| Day 17 — Lecture 17 | Model Parallelism: Tensor, Expert, Pipeline & Data | [Notes](./day17/LECTURE.md) · [Companion](./day17/README.md) |
| Day 18 — Lecture 18 | Disaggregation: Prefill/Decode Split | [Notes](./day18/LECTURE.md) · [Companion](./day18/README.md) |

### Phase 2 — Infrastructure: Scaling Across Clusters

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 19 — Lecture 19 | GPU Architecture: SMs, Memory Hierarchy, HBM | [Notes](./day19/LECTURE.md) · [Companion](./day19/README.md) |
| Day 20 — Lecture 20 | GPU Generations: Hopper, Ada, Blackwell, Rubin | [Notes](./day20/LECTURE.md) · [Companion](./day20/README.md) |
| Day 21 — Lecture 21 | Multi-GPU Instances & Multi-Instance GPU (MIG) | [Notes](./day21/LECTURE.md) · [Companion](./day21/README.md) |
| Day 22 — Lecture 22 | Containerization: Docker & NVIDIA NIMs | [Notes](./day22/LECTURE.md) · [Companion](./day22/README.md) |
| Day 23 — Lecture 23 | Autoscaling: Concurrency, Batching & Cold Starts | [Notes](./day23/LECTURE.md) · [Companion](./day23/README.md) |
| Day 24 — Lecture 24 | Routing, Load Balancing & Queueing | [Notes](./day24/LECTURE.md) · [Companion](./day24/README.md) |
| Day 25 — Lecture 25 | Multi-Cloud Capacity Management | [Notes](./day25/LECTURE.md) · [Companion](./day25/README.md) |
| Day 26 — Lecture 26 | Zero-Downtime Deployment & Cost Estimation | [Notes](./day26/LECTURE.md) · [Companion](./day26/README.md) |

### Phase 3 — Tooling: Productivity & Observability

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 27 — Lecture 27 | Performance Benchmarking: Tooling & Profiling | [Notes](./day27/LECTURE.md) · [Day overview](./day27/README.md) |
| Day 28 — Lecture 28 | Observability: Metrics, Tracing & Dashboards | [Notes](./day28/LECTURE.md) · [Day overview](./day28/README.md) |
| Day 29 — Lecture 29 | Client Code: Streaming, Async & Protocol Support | [Notes](./day29/LECTURE.md) · [Day overview](./day29/README.md) |

### Phase 4 — Deep Implementation: Build It from Scratch

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 30 — Lecture 30 | Implement a BPE tokenizer from scratch | [Notes](./day30/LECTURE.md) · [Day overview](./day30/README.md) |
| Day 31 — Lecture 31 | Build a bare autoregressive decoder loop in PyTorch | [Notes](./day31/LECTURE.md) · [Day overview](./day31/README.md) |
| Day 32 — Lecture 32 | Implement scaled dot-product attention (SDPA) with masking | [Notes](./day32/LECTURE.md) · [Day overview](./day32/README.md) |
| Day 33 — Lecture 33 | Implement Flash Attention (simplified, tiling in Python) | [Notes](./day33/LECTURE.md) · [Day overview](./day33/README.md) |
| Day 34 — Lecture 34 | Profile attention memory growth across sequence lengths | [Notes](./day34/LECTURE.md) · [Day overview](./day34/README.md) |
| Day 35 — Lecture 35 | Build an INT8 quantization pipeline: quantize → dequantize → measure error | [Notes](./day35/LECTURE.md) · [Day overview](./day35/README.md) |
| Day 36 — Lecture 36 | Curvature-aware quantization: scale search and GPTQ distinctions | [Notes](./day36/LECTURE.md) · [Day overview](./day36/README.md) |
| Day 37 — Lecture 37 | Sweep quantization bit widths and plot perplexity vs compression | [Notes](./day37/LECTURE.md) · [Day overview](./day37/README.md) |
| Day 38 — Lecture 38 | Simulate draft-target speculative decoding with acceptance sampling | [Notes](./day38/LECTURE.md) · [Day overview](./day38/README.md) |
| Day 39 — Lecture 39 | Build a simple KV cache manager (block allocator, eviction policy) | [Notes](./day39/LECTURE.md) · [Day overview](./day39/README.md) |
| Day 40 — Lecture 40 | Implement prefix caching with hash-based deduplication | [Notes](./day40/LECTURE.md) · [Day overview](./day40/README.md) |
| Day 41 — Lecture 41 | Simulate tensor parallelism: split a matmul across N workers | [Notes](./day41/LECTURE.md) · [Day overview](./day41/README.md) |
| Day 42 — Lecture 42 | Benchmark ops:byte ratio in practice across matrix sizes | [Notes](./day42/LECTURE.md) · [Day overview](./day42/README.md) |
| Day 43 — Lecture 43 | CUDA profiling: profile a PyTorch model with `torch.profiler` | [Notes](./day43/LECTURE.md) · [Day overview](./day43/README.md) |
| Day 44 — Lecture 44 | Write a custom elementwise CUDA kernel via Triton | [Notes](./day44/LECTURE.md) · [Day overview](./day44/README.md) |
| Day 45 — Lecture 45 | Build a PyTorch custom op with CUDA backend | [Notes](./day45/LECTURE.md) · [Day overview](./day45/README.md) |
| Day 46 — Lecture 46 | Deploy vLLM on spark-01, benchmark TTFT and throughput | [Notes](./day46/LECTURE.md) · [Day overview](./day46/README.md) |
| Day 47 — Lecture 47 | Deploy SGLang, benchmark structured output latency | [Notes](./day47/LECTURE.md) · [Day overview](./day47/README.md) |
| Day 48 — Lecture 48 | TensorRT-LLM: compile a model and compare with eager PyTorch | [Notes](./day48/LECTURE.md) · [Day overview](./day48/README.md) |
| Day 49 — Lecture 49 | NVIDIA Dynamo: run a disaggregated prefill experiment | [Notes](./day49/LECTURE.md) · [Day overview](./day49/README.md) |
| Day 50 — Lecture 50 | Simulate continuous batching: queue arrivals, dynamic batch formation | [Notes](./day50/LECTURE.md) · [Day overview](./day50/README.md) |
| Day 51 — Lecture 51 | Visualize PagedAttention block layout and fragmentation | [Notes](./day51/LECTURE.md) · [Day overview](./day51/README.md) |
| Day 52 — Lecture 52 | Benchmark TTFT vs throughput tradeoff across batch sizes | [Notes](./day52/LECTURE.md) · [Day overview](./day52/README.md) |

### Phase 5 — Production Systems: From Notebook to Cluster

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 53 — Lecture 53 | Write a production Dockerfile for a vLLM inference server | [Notes](./day53/LECTURE.md) · [Day overview](./day53/README.md) |
| Day 54 — Lecture 54 | NVIDIA NIM deployment and custom serving-container contracts | [Notes](./day54/LECTURE.md) · [Day overview](./day54/README.md) |
| Day 55 — Lecture 55 | Simulate an autoscaling policy: requests per second → replica count | [Notes](./day55/LECTURE.md) · [Day overview](./day55/README.md) |
| Day 56 — Lecture 56 | Measure cold start latency: model load times at different sizes | [Notes](./day56/LECTURE.md) · [Day overview](./day56/README.md) |
| Day 57 — Lecture 57 | Implement round-robin and least-connections load balancers | [Notes](./day57/LECTURE.md) · [Day overview](./day57/README.md) |
| Day 58 — Lecture 58 | Build a priority request queue with batch formation | [Notes](./day58/LECTURE.md) · [Day overview](./day58/README.md) |
| Day 59 — Lecture 59 | Multi-GPU tensor parallel benchmark across spark-01 and spark-02 | [Notes](./day59/LECTURE.md) · [Day overview](./day59/README.md) |
| Day 60 — Lecture 60 | MIG capability checks and partition planning on supported GPUs | [Notes](./day60/LECTURE.md) · [Day overview](./day60/README.md) |
| Day 61 — Lecture 61 | GPU cost model: $/token across instance types at different utilizations | [Notes](./day61/LECTURE.md) · [Day overview](./day61/README.md) |
| Day 62 — Lecture 62 | Blue-green deployment: zero-downtime model version swap | [Notes](./day62/LECTURE.md) · [Day overview](./day62/README.md) |
| Day 63 — Lecture 63 | Emit Prometheus metrics from an inference server | [Notes](./day63/LECTURE.md) · [Day overview](./day63/README.md) |
| Day 64 — Lecture 64 | Build a Grafana dashboard: TTFT, TBT, queue depth, GPU utilization | [Notes](./day64/LECTURE.md) · [Day overview](./day64/README.md) |
| Day 65 — Lecture 65 | Add distributed tracing (OpenTelemetry) to an inference request | [Notes](./day65/LECTURE.md) · [Day overview](./day65/README.md) |
| Day 66 — Lecture 66 | Load test with Locust: ramp traffic, find saturation point | [Notes](./day66/LECTURE.md) · [Day overview](./day66/README.md) |
| Day 67 — Lecture 67 | Profile with Nsight Systems: identify kernel launch overhead | [Notes](./day67/LECTURE.md) · [Day overview](./day67/README.md) |
| Day 68 — Lecture 68 | Build a streaming inference client using SSE | [Notes](./day68/LECTURE.md) · [Day overview](./day68/README.md) |
| Day 69 — Lecture 69 | Async batch inference client using `asyncio` + `aiohttp` | [Notes](./day69/LECTURE.md) · [Day overview](./day69/README.md) |
| Day 70 — Lecture 70 | Multi-cloud routing: geo-aware latency-based request routing | [Notes](./day70/LECTURE.md) · [Day overview](./day70/README.md) |
| Day 71 — Lecture 71 | GPU memory profiling: find where your memory budget goes | [Notes](./day71/LECTURE.md) · [Day overview](./day71/README.md) |
| Day 72 — Lecture 72 | Benchmark quantization levels on real throughput: FP16 vs INT8 vs INT4 | [Notes](./day72/LECTURE.md) · [Day overview](./day72/README.md) |
| Day 73 — Lecture 73 | Measure speculative decoding acceptance rates by draft model size | [Notes](./day73/LECTURE.md) · [Day overview](./day73/README.md) |
| Day 74 — Lecture 74 | Measure KV cache hit rates across real traffic patterns | [Notes](./day74/LECTURE.md) · [Day overview](./day74/README.md) |
| Day 75 — Lecture 75 | Tensor parallelism scaling: throughput and latency vs GPU count | [Notes](./day75/LECTURE.md) · [Day overview](./day75/README.md) |
| Day 76 — Lecture 76 | End-to-end latency breakdown: tokenization → TTFT → TBT → detokenization | [Notes](./day76/LECTURE.md) · [Day overview](./day76/README.md) |
| Day 77 — Lecture 77 | Build a reusable inference benchmark harness | [Notes](./day77/LECTURE.md) · [Day overview](./day77/README.md) |

### Phase 6 — Modalities: Beyond Text

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 78 — Lecture 78 | Vision Language Model (VLM) inference: image preprocessing and batching | [Notes](./day78/LECTURE.md) · [Day overview](./day78/README.md) |
| Day 79 — Lecture 79 | Embedding model inference: batching and throughput optimization | [Notes](./day79/LECTURE.md) · [Day overview](./day79/README.md) |
| Day 80 — Lecture 80 | ASR (Whisper): single-chunk and long-file latency optimization | [Notes](./day80/LECTURE.md) · [Day overview](./day80/README.md) |
| Day 81 — Lecture 81 | TTS: streaming real-time text-to-speech | [Notes](./day81/LECTURE.md) · [Day overview](./day81/README.md) |
| Day 82 — Lecture 82 | Image generation: diffusion model inference and kernel optimization | [Notes](./day82/LECTURE.md) · [Day overview](./day82/README.md) |
| Day 83 — Lecture 83 | Video generation: context parallelism and attention optimization | [Notes](./day83/LECTURE.md) · [Day overview](./day83/README.md) |
| Day 84 — Lecture 84 | Multi-modal batching: mixing text and image requests | [Notes](./day84/LECTURE.md) · [Day overview](./day84/README.md) |
| Day 85 — Lecture 85 | Embedding similarity search pipeline: embed → index → query | [Notes](./day85/LECTURE.md) · [Day overview](./day85/README.md) |
| Day 86 — Lecture 86 | Speech-to-speech pipeline: ASR → LLM → TTS end-to-end latency | [Notes](./day86/LECTURE.md) · [Day overview](./day86/README.md) |
| Day 87 — Lecture 87 | Long context: RoPE scaling, context parallelism across GPUs | [Notes](./day87/LECTURE.md) · [Day overview](./day87/README.md) |

### Phase 7 — Advanced Techniques

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 88 — Lecture 88 | EAGLE speculative decoding: feature-level draft vs token-level | [Notes](./day88/LECTURE.md) · [Day overview](./day88/README.md) |
| Day 89 — Lecture 89 | Medusa: multi-head speculative decoding, measure speedup | [Notes](./day89/LECTURE.md) · [Day overview](./day89/README.md) |
| Day 90 — Lecture 90 | MoE routing from scratch: top-K gating, load balancing loss | [Notes](./day90/LECTURE.md) · [Day overview](./day90/README.md) |
| Day 91 — Lecture 91 | Expert parallelism: simulate routing across N expert shards | [Notes](./day91/LECTURE.md) · [Day overview](./day91/README.md) |
| Day 92 — Lecture 92 | Dynamic disaggregation with NVIDIA Dynamo | [Notes](./day92/LECTURE.md) · [Day overview](./day92/README.md) |
| Day 93 — Lecture 93 | Cache-aware routing: route requests to maximize KV cache hits | [Notes](./day93/LECTURE.md) · [Day overview](./day93/README.md) |
| Day 94 — Lecture 94 | Long context without context parallelism: chunked prefill | [Notes](./day94/LECTURE.md) · [Day overview](./day94/README.md) |
| Day 95 — Lecture 95 | Fine-tuning a small model for inference quality vs a large quantized one | [Notes](./day95/LECTURE.md) · [Day overview](./day95/README.md) |
| Day 96 — Lecture 96 | Distillation for inference: teacher-student latency/quality tradeoffs | [Notes](./day96/LECTURE.md) · [Day overview](./day96/README.md) |
| Day 97 — Lecture 97 | Intelligence evaluation: build an eval harness for a deployed model | [Notes](./day97/LECTURE.md) · [Day overview](./day97/README.md) |

### Phase 8 — Capstone: A Production Inference Stack

| Day / lecture | Topic | Materials |
|---|---|---|
| Day 98 — Lecture 98 | Design: sketch the full inference stack for a real use case | [Notes](./day98/LECTURE.md) · [Day overview](./day98/README.md) |
| Day 99 — Lecture 99 | Build: FastAPI + vLLM inference server with health checks and metrics | [Notes](./day99/LECTURE.md) · [Day overview](./day99/README.md) |
| Day 100 — Lecture 100 | Deploy: ship it to the home lab cluster with load balancing | [Notes](./day100/LECTURE.md) · [Day overview](./day100/README.md) |
| Day 101 — Lecture 101 | Optimize: run the benchmark harness, find the bottleneck, fix it | [Notes](./day101/LECTURE.md) · [Day overview](./day101/README.md) |
| Day 102 — Lecture 102 | Reflect: what I learned, what I'd do differently, what's next | [Notes](./day102/LECTURE.md) · [Day overview](./day102/README.md) |

## Reference shelf

- Course foundation: *Inference Engineering*, Philip Kiely; chapter mappings are retained in the [original roadmap](./README.md).
- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/) for GPU concepts and device-specific support.
- [vLLM documentation](https://docs.vllm.ai/en/latest/) for supported serving features and version-specific configuration.
- Each existing notebook’s references provide topic-specific follow-up reading. Verify current runtime and hardware support before executing version-sensitive examples.

## Maintaining the course

The [complete lecture PDF](./output/pdf/inference-engineering-complete-lectures.pdf) contains the course guide and all 102 lectures. Rebuild it with `python3 scripts/build_lecture_pdf.py` after installing Pandoc, XeLaTeX (TeX Live), and the STIX Two Text and STIX Two Math fonts; the current layout also uses Helvetica and Menlo. The script writes temporary typesetting files under `tmp/pdfs/` and the final document under `output/pdf/`. PDF compilation does not execute the student labs.

Run `python3 scripts/validate_lectures.py` from the repository root after editing lessons. The check verifies all 102 day labels, schedule titles, required sections, adjacent navigation, and local Markdown links and anchors. It does not execute student assignments or validate external websites.

The roadmap now distinguishes a curvature-aware teaching experiment from full GPTQ, a custom serving image from NVIDIA NIM, and supported MIG hardware from the Spark lab. These distinctions also appear in the corresponding lectures.
