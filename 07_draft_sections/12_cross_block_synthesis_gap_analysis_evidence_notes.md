# Evidence Notes for Section 12: Cross-Block Synthesis and Gap Analysis

This companion note records the evidence controls used for `07_draft_sections/12_cross_block_synthesis_gap_analysis.md`. Section 12 answers the main review question by integrating Sections 3-11, Blocks A-F, Core 60, Block G claims C-G1-C-G8, and Block G gaps GAP-G1-GAP-G12.

## Source Controls Used

- `05_synthesis_matrices/block_g_core_claim_synthesis_map.csv`
- `05_synthesis_matrices/block_g_cross_block_taxonomy_synthesis_matrix.csv`
- `05_synthesis_matrices/block_g_research_gap_agenda_matrix.csv`
- `05_synthesis_matrices/block_g_section_to_evidence_map.csv`
- `05_synthesis_matrices/core_60_reference_set.csv`
- `05_synthesis_matrices/evidence_to_claim_matrix.csv`
- `05_synthesis_matrices/foundation_model_matrix.csv`
- `05_synthesis_matrices/dataset_benchmark_matrix.csv`
- `05_synthesis_matrices/data_centric_strategy_matrix.csv`
- `05_synthesis_matrices/adaptation_strategy_matrix.csv`
- `05_synthesis_matrices/pseudo_labeling_kd_matrix.csv`
- `05_synthesis_matrices/evaluation_robustness_matrix.csv`
- Section drafts 3-11 in `07_draft_sections/`

## Claim-Level Evidence Map

| Section Claim | Section Location | Supporting C-G Claims | Supporting GAP IDs | Supporting CoreIDs/PaperIDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Taxonomy Layers | Evidence Type |
|---|---|---|---|---|---|---|---|---|---|---|
| Section 12 integrates the separate component sections into a cross-layer answer to the main review question. | 12.1 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7; C-G8 | GAP-G1-GAP-G12 | Section drafts 3-11; Block G controls | No new citation needed | Matrix-supported synthesis | Low | Main; RQ1-RQ6 | All layers | Interpretive synthesis |
| Foundation models improve the low-resource ASR starting point but shift the bottleneck toward reliability, adaptation, data quality, and evaluation rather than eliminating it. | 12.2 | C-G2; C-G1; C-G3; C-G4; C-G5; C-G6; C-G7; C-G8 | GAP-G4; GAP-G5; GAP-G12 | CORE-01; CORE-09; CORE-15; CORE-22; CORE-26; CORE-27; CORE-28; CORE-30 | `besacier2014_underresourced_asr_survey`; `gales2014_babel_project_research_cued`; `baevski2020wav2vec2`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `seamless2025_joint_speech_text_mt`; `tian25b_interspeech` | Mostly verified-primary; SeamlessM4T bounded as translation-centric | Low to medium | Main; RQ2; RQ6 | Model; adaptation; evaluation; resource | Established evidence plus interpretive synthesis |
| Persistent bottlenecks come from interactions among layers, not from isolated method weaknesses. | 12.3 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7 | GAP-G1; GAP-G2; GAP-G3; GAP-G4; GAP-G7; GAP-G9; GAP-G10; GAP-G11 | CORE-03; CORE-04; CORE-14; CORE-26; CORE-27; CORE-43; CORE-51; CORE-57; CORE-59; CORE-60 | `ardila2020commonvoice`; `conneau2022fleurs`; `pmlr-v202-radford23a`; `pratap2024mms`; `udupa24_interspeech`; `qian24_interspeech`; `park20d_interspeech`; `khurana2020dust`; `leal21_interspeech`; `bhogale24_interspeech`; `shi2023mlsuperb`; `olatunji2023_afrispeech200`; `koenecke2020racialdisparities`; `koenecke2024carelesswhisper`; `shi2022avhubert`; `anwar23_interspeech`; `ma2024asrerrorcorrection` | Mixed verified-primary, verified-secondary, and one watchlist-bounded correction source | Medium | RQ1-RQ6 | All layers | Cross-layer interpretive synthesis |
| Solution families should be compared by enabling conditions, residual risks, and evaluation requirements rather than ranked universally. | 12.4 | C-G3; C-G4; C-G5; C-G6; C-G7; C-G8 | GAP-G5; GAP-G6; GAP-G7; GAP-G8; GAP-G9; GAP-G10; GAP-G11; GAP-G12 | CORE-37; CORE-38; CORE-39; CORE-43; CORE-44; CORE-45; CORE-46; CORE-48; CORE-51; CORE-57; CORE-59; CORE-60 | `pmlr-v97-houlsby19a`; `hu2022lora`; `dettmers2023qlora` plus citations inherited from 12.3 | Method anchors include non-ASR PEFT evidence; used only as method anchors | Medium | RQ3; RQ4; RQ5; RQ6 | Data; adaptation; supervision; evaluation | Method-anchor support plus synthesis |
| Central claims are carried by Core 60 and verified matrix evidence; watchlist sources are limited to future-facing risks and should not support strong central claims. | 12.5 | C-G7; C-G8 | GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Core 60; priority watchlist; Section 11 evidence notes | No new citation needed | Matrix and verification-policy support | Low | Main; RQ6 | Evaluation; model; all layers | Evidence-boundary synthesis |
| GAP-G1-GAP-G12 can be reduced to four high-level gap clusters: definition/resource documentation, model/adaptation comparability, supervision reliability, and evaluation/robustness. | 12.6 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7; C-G8 | GAP-G1; GAP-G2; GAP-G3; GAP-G4; GAP-G5; GAP-G6; GAP-G7; GAP-G8; GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Block G gap matrix; related CoreIDs listed in each gap | No new citation needed | Matrix-supported synthesis | Low | Main; RQ1-RQ6 | All layers | Gap-cluster synthesis |
| The review adds a foundation-model-era taxonomy, cross-block synthesis, integration of adaptation/supervision/evaluation, and a reliability-controlled future agenda. | 12.7 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7; C-G8 | GAP-G1-GAP-G12 | Section drafts 3-11; Block G controls | No new citation needed | Interpretive synthesis based on prior sections | Low | Main | All layers | Contribution synthesis |
| Section 13 should convert cross-block bottlenecks into a concrete future research agenda. | 12.8 | C-G8; C-G7 | GAP-G1-GAP-G12 | Block G research gap agenda matrix | No new citation needed | Matrix-supported synthesis | Low | RQ6; Main | All layers | Transition synthesis |

## Gap Cluster Mapping

| Gap Cluster | Included GAP IDs | Affected Taxonomy Layers | Evidence Base | Future Research Need |
|---|---|---|---|---|
| Cluster 1: Definition and resource documentation gaps | GAP-G1; GAP-G2; GAP-G3 | Resource; language; evaluation | Low-resource framing, Common Voice, dataset-quality, normalization, and benchmark evidence | Shared reporting schema for low-resource condition, data quality, metadata, licensing, dialect, validation, and normalization |
| Cluster 2: Model and adaptation comparability gaps | GAP-G4; GAP-G5; GAP-G6 | Model; adaptation; evaluation | Foundation-model, multilingual benchmark, PEFT, and ASR adaptation evidence | Matched comparisons across data volume, compute, trainable parameters, forgetting, and subgroup performance |
| Cluster 3: Supervision reliability gaps | GAP-G7; GAP-G8 | Supervision; resource; evaluation | Self-training, pseudo-labeling, KD, multi-teacher, and large-scale low-resource pseudo-labeling evidence | Teacher-error analysis, uncertainty/confidence reporting, disagreement handling, and reproducible selection protocols |
| Cluster 4: Evaluation and robustness gaps | GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Evaluation; model; resource; adaptation | Evaluation/robustness matrix, AVSR evidence, hallucination evidence, PEFT/reproducibility evidence, and watchlist-bounded LLM sources | Robustness, hallucination, source grounding, AVSR coverage, constrained correction, reproducibility, and compute reporting |

## Evidence-Boundary Notes

- Watchlist sources are used only in future-facing or risk-bound contexts, especially for LLM-assisted correction, contextual ASR, and emerging hallucination benchmarks.
- `ma2024asrerrorcorrection` is used only as watchlist-bounded evidence for constrained correction/rescoring risk, not as proof that LLM correction is mature.
- `shi2022avhubert` is verified-secondary and is used with `anwar23_interspeech` as a stronger verified-primary AVSR benchmark anchor.
- `pmlr-v97-houlsby19a`, `hu2022lora`, and `dettmers2023qlora` are method anchors for PEFT and are not treated as direct ASR performance evidence.
- Pashto/thesis material is not used as central evidence in Section 12.

## Quality Safeguards Checked

- Section 12 synthesizes Sections 3-11 rather than restating them mechanically.
- The six taxonomy layers are treated as interacting constraints.
- No solution family is ranked as universally best.
- Foundation models are described as changing the starting point, not solving low-resource ASR.
- Watchlist LLM/SpeechLM/AVSR sources are bounded.
- The required figure/table placeholders are included.
- The main manuscript should point to the draft and evidence notes only, not contain the full draft.
