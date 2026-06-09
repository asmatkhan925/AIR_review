# Block A Seed Set

## Purpose

Block A establishes the first literature spine for the AIR review before deeper method-specific collection begins. It is benchmark-heavy by design: three survey anchors, seven dataset or benchmark anchors, and two watchlist items.

## Main Value

This seed set supports the locked questions on:

- RQ1: what low-resource means beyond labeled hours.
- RQ2: how self-supervised, multilingual, weakly supervised, and foundation speech models changed the starting point.
- RQ5: how pseudo-labeling and supervision-transfer claims need later evidence, because Block A does not cover them deeply.
- RQ6: why evaluation must go beyond global WER/CER, including dialect, variety, data quality, and SpeechLM-era benchmarking.

## Core Anchors

| ID | Paper | Role | Main Use |
|---|---|---|---|
| BA01 | Besacier et al. (2014), under-resourced ASR survey | Historical survey anchor | Show what changed after the pre-SSL era. |
| BA02 | Prabhavalkar et al. (2024), end-to-end ASR survey | ASR architecture survey anchor | Stabilize terminology for hybrid, CTC, attention, and transducer systems. |
| BA03 | Cui et al. (2025), Speech Language Models survey | SpeechLM survey anchor | Bridge foundation speech models to LLM-assisted future directions. |
| BA04 | Ardila et al. (2020), Common Voice | Open corpus anchor | Discuss crowdsourced multilingual speech resources. |
| BA05 | Wang et al. (2021), VoxPopuli | Pretraining corpus anchor | Distinguish unlabeled multilingual pretraining corpora from benchmarks. |
| BA06 | Conneau et al. (2022), FLEURS | Cross-lingual benchmark anchor | Discuss standardized few-shot multilingual evaluation. |
| BA07 | Shi et al. (2023), ML-SUPERB | Multilingual benchmark anchor | Discuss reproducible multilingual speech model evaluation. |
| BA08 | Shi et al. (2024), ML-SUPERB 2.0 | Benchmark extension anchor | Connect benchmarking with adaptation and modeling constraints. |
| BA09 | Chen et al. (2025), ML-SUPERB 2.0 Challenge | Inclusive benchmark anchor | Support evaluation beyond pooled WER, especially dialect and variety coverage. |
| BA10 | Lau et al. (2025), dataset quality audit | Benchmark quality audit | Support the argument that low-resource ASR remains data- and benchmark-sensitive. |

## Watchlist

| ID | Paper | Reason |
|---|---|---|
| BA11 | FormosanBench | Reserve case box for endangered-language benchmarking and large-model-era evaluation. |
| BA12 | LoASR-Bench | Preprint watchlist for low-resource SpeechLM ASR evaluation across language families. |

## Limits

Block A does not yet provide deep evidence for pseudo-labeling, knowledge distillation, teacher disagreement, confidence filtering, or multi-teacher selection. Those should be covered in a later adaptation and supervision-transfer block.

## Repository Links

- Seed map: `05_synthesis_matrices/seed_paper_map.csv`
- Citation verification: `03_references/citation_verification_log.csv`
- Dataset and benchmark matrix: `05_synthesis_matrices/dataset_benchmark_matrix.csv`

