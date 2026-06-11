# Evidence Notes For Section 10: Evaluation, Reproducibility, and Robustness

## Scope

This companion note records the evidence used in `07_draft_sections/10_evaluation_reproducibility_robustness.md`. Section 10 answers RQ6 by arguing that WER/CER remain necessary but insufficient for foundation-model-era low-resource ASR. The main evidence source is `evaluation_robustness_matrix.csv`, with support from dataset/benchmark, data-centric, adaptation, pseudo-labeling/KD, Core 60, and Block G controls.

## Block G Controls Used

| Control | Use In Section 10 |
|---|---|
| C-G6 | Main backbone: pooled WER/CER can hide dialect, domain, orthographic, demographic, and hallucination-related failures. |
| C-G1 | Connects evaluation to the multidimensional definition of low-resource ASR. |
| C-G2 | Links foundation models to stronger baselines and hidden aggregate failures. |
| C-G3 | Connects transcript normalization, filtering, and metadata to evaluation validity. |
| C-G4 | Connects adaptation claims to compute, forgetting, and reproducibility reporting. |
| C-G5 | Connects pseudo-labeling and KD to teacher-error evaluation. |
| C-G7 | Used only for bounded multimodal, hallucination, and LLM-assisted risk framing. |
| C-G8 | Supports reproducibility, compute, and future-agenda reporting controls. |
| GAP-G3 | Orthographic normalization and transcript comparability gap. |
| GAP-G4 | Aggregate reporting gap for language, dialect, and domain failures. |
| GAP-G5 | Adaptation comparability gap. |
| GAP-G7 | Pseudo-label reliability evaluation gap. |
| GAP-G9 | Hallucination and over-correction metric gap. |
| GAP-G10 | Low-resource AVSR evaluation gap. |
| GAP-G11 | Constrained LLM-assisted ASR evaluation gap. |
| GAP-G12 | Reproducibility and compute reporting gap. |

## Claim Map

| Section Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Linked Block G Claims | Linked Block G Gaps | Evidence Type | Watchlist Boundary |
|---|---|---|---|---|---|---|---|---|---|---|
| Foundation models make evaluation more important because aggregate improvements can hide uneven language, dialect, domain, normalization, and generation failures. | 10.1 | C-G2; C-G6; CORE-04; CORE-05; CORE-06; CORE-12; CORE-52; BF01; BF02; BF03 | `shi2023mlsuperb`; `conneau2022fleurs`; `conneau2022xtreme_s`; `shi2024mlsuperb2`; `chen2025mlsuperb2challenge` | Mixed verified-primary and verified-secondary | Low to medium | RQ2; RQ6 | C-G2; C-G6 | GAP-G4; GAP-G12 | Benchmark evidence plus interpretive synthesis | No watchlist-only central support |
| WER and CER remain necessary but are insufficient without reporting pooling, averaging, tokenization, normalization, script, and subgroup conditions. | 10.2 | CORE-04; CORE-06; CORE-11; CORE-13; CORE-53; BF01; BF05 | `shi2023mlsuperb`; `javed2023indsuperb`; `chen2025mlsuperb2challenge`; `karita2023lenient` | Mixed verified-primary and verified-secondary | Low | RQ6 | C-G6 | GAP-G3; GAP-G4 | Benchmark and evaluation evidence | No watchlist-only central support |
| Orthography-aware and normalization-aware evaluation is needed because spelling variation, punctuation, casing, script, morphology, and transcript conventions can change measured errors. | 10.3 | CORE-07; CORE-35; CORE-36; CORE-53; BC08; BC12; BF05 | `karita2023lenient`; `lau2025_data_quality_multilingual_speech`; `tian24_interspeech` | Mixed verified-primary and verified-secondary | Medium; normalization is language-specific | RQ3; RQ6 | C-G3; C-G6 | GAP-G3 | Evaluation evidence plus interpretive synthesis | No watchlist-only central support |
| Language-, dialect-, domain-, and demographic-aware reporting is required because aggregate scores can hide uneven performance and harms. | 10.4 | CORE-04; CORE-05; CORE-06; CORE-12; CORE-13; CORE-14; CORE-55; CORE-56; BF01; BF09; BF10 | `conneau2022fleurs`; `conneau2022xtreme_s`; `shi2023mlsuperb`; `javed2023indsuperb`; `shi2024mlsuperb2`; `chen2025mlsuperb2challenge`; `koenecke2020racialdisparities`; `liu2021casualconversations` | Mixed verified-primary and verified-secondary | Medium; demographic evidence is important but not low-resource-language-only | RQ1; RQ6 | C-G1; C-G6 | GAP-G4 | Benchmark evidence and fairness/subgroup evidence | Fairness watchlist items excluded from central claims |
| Robustness evaluation must cover noise, far-field, overlap, conversation, multi-device conditions, and channel shift because clean read speech does not cover many deployments. | 10.5 | CORE-54; BF07; BF08 | `watanabe2020chime6`; `cornell2023chime7` | Verified-secondary-source anchors | Medium; robustness benchmarks are not low-resource-language-specific | RQ3; RQ6 | C-G6; C-G8 | GAP-G4; GAP-G12 | Robustness evidence plus synthesis | No watchlist-only central support |
| Reproducibility, compute, and deployment reporting should include model version, data, adaptation method, decoding, normalization, hardware, compute, trainable parameters, inference cost, splits, and artifacts. | 10.6 | CORE-11; CORE-37; CORE-38; CORE-39; CORE-54; BF13; BF14; BF15; BF25 | `feng2022superbslt`; `watanabe2018espnet`; `ravanelli2021speechbrain`; `povey2011kaldi` | Mixed verified-secondary and toolkit background | Medium; toolkits are infrastructure support, not performance evidence | RQ4; RQ6 | C-G4; C-G6; C-G8 | GAP-G5; GAP-G12 | Reproducibility and compute-reporting synthesis | No watchlist-only central support |
| Hallucination, over-correction, contextual bias, and named-entity errors require evaluation beyond pooled WER when ASR becomes generative or LLM-assisted. | 10.7 | CORE-60; BF20; BF21; BF22; BF23; BF24 | `koenecke2024carelesswhisper`; `frieske2024hallucinations`; `koudounas2025shallow`; `wang2025contextasrbench`; `ma2024asrerrorcorrection` | Core hallucination evidence is secondary verified; contextual/hallucination benchmarks are watchlist | High; kept as bounded risk framing and bridge to Section 11 | RQ6 | C-G6; C-G7; C-G8 | GAP-G9; GAP-G11 | Watchlist-bounded evidence plus evaluation-risk synthesis | Watchlist sources are not used as central settled evidence |
| Evaluation design should be selected from the risk condition: orthography, multilinguality, dialect, domain, pseudo-labeling, adaptation, PEFT, generative ASR, multimodality, or public benchmark comparison. | 10.8 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7; C-G8; GAP-G3; GAP-G4; GAP-G5; GAP-G7; GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Citation keys inherited from 10.1-10.7 | Matrix-supported synthesis | Low | RQ1; RQ3; RQ4; RQ5; RQ6 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7; C-G8 | GAP-G3; GAP-G4; GAP-G5; GAP-G7; GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Interpretive synthesis | No watchlist-only central support |

## Watchlist Use

The Section 10 draft uses watchlist hallucination, contextual ASR, and LLM-assisted correction sources only as emerging evaluation-risk examples in Section 10.7. The central claims are carried by Core 60, benchmark, robustness, fairness, reproducibility, and evaluation matrices. Section 11 remains the main place for multimodal, SpeechLM, and LLM-assisted ASR methods.

## Title Alignment Note

The canonical Section 10 title is `Evaluation, Reproducibility, and Robustness`. The draft uses that title and the main manuscript should point to this file without pasting the full section.

## Pashto Drift Check

Pashto is not mentioned in this Section 10 draft. Examples remain field-level.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 10 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 11 should expand multimodal, SpeechLM, and LLM-assisted ASR methods while preserving the evaluation safeguards introduced here.
- Section 12 should integrate the evaluation checklist with the six-layer taxonomy and gap analysis.
- Section 13 should reuse reproducibility, compute, hallucination, and subgroup-reporting requirements as future-agenda items.
