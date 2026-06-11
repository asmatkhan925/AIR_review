# Evidence Notes For Section 9: Pseudo-Labeling and Knowledge Distillation for Low-Resource ASR

## Scope

This companion note records the evidence used in `07_draft_sections/09_pseudo_labeling_kd_low_resource_asr.md`. Section 9 answers RQ5 by treating pseudo-labeling, self-training, and KD as supervision-expansion strategies whose reliability depends on teacher quality, filtering, agreement, normalization, language/domain match, and evaluation design. The main evidence source is `pseudo_labeling_kd_matrix.csv`, with support from the data-centric, adaptation, foundation-model, and evaluation matrices.

## Block G Controls Used

| Control | Use In Section 9 |
|---|---|
| C-G5 | Main backbone: pseudo-labeling and KD expand supervision but require teacher-quality and filtering controls. |
| C-G2 | Connects foundation speech models to stronger teacher models and foundation-era pseudo-labeling. |
| C-G3 | Connects pseudo-labels to data quality, filtering, transcript normalization, and validation. |
| C-G4 | Links pseudo-labeling and KD to adaptation conditions from Section 8. |
| C-G6 | Connects pseudo-label reliability to evaluation design and pooled WER/CER limitations. |
| C-G7 | Used only for bounded hallucination and LLM/SpeechLLM risk framing. |
| C-G8 | Supports reproducibility, reporting, and future-agenda controls. |
| GAP-G7 | Pseudo-label reliability gap. |
| GAP-G8 | Multi-teacher disagreement and selection-rule gap. |
| GAP-G9 | LLM/hallucination metric gap, used only for bounded generative-teacher risk. |
| GAP-G11 | Constrained LLM-assisted ASR gap, used only as future-facing caution. |
| GAP-G12 | Reproducibility and compute/reporting gap. |

## Claim Map

| Section Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Linked Block G Claims | Linked Block G Gaps | Evidence Type | Watchlist Boundary |
|---|---|---|---|---|---|---|---|---|---|---|
| Supervision expansion matters because low-resource ASR often has unlabeled or teacher-labeled speech but too few verified labels; expansion is not automatically improvement. | 9.1 | C-G5; CORE-44; CORE-45; CORE-46; CORE-51; BE03; BE04; BE05; BE15 | Citation keys introduced in following subsections | Matrix-supported synthesis | Low | RQ5 | C-G3; C-G5; C-G8 | GAP-G7; GAP-G12 | Interpretive synthesis | No watchlist support used |
| Self-training and pseudo-label generation can use unlabeled speech for larger training sets and domain adaptation, but teacher errors become training data. | 9.2 | CORE-44; CORE-45; CORE-47; CORE-51; BE03; BE04; BE06; BE07; BE11; BE15 | `kahn2019selftraining`; `park20d_interspeech`; `xu2020iterativepseudolabeling`; `likhomanenko2020slimipl`; `bhogale24_interspeech` | Mixed verified-primary and verified-secondary | Medium; iterative evidence is partly secondary | RQ3; RQ5 | C-G3; C-G5 | GAP-G7; GAP-G12 | Direct ASR evidence plus synthesis | No watchlist-only central support |
| Filtering, confidence, uncertainty, curriculum, and calibration determine whether pseudo-labeling reduces or amplifies noise. | 9.3 | CORE-46; CORE-47; BE05; BE06; BE10; BE12 | `khurana2020dust`; `xu2020selftraining` | Verified-secondary-source anchors; no watchlist-only support | Medium; calibration/curriculum details need stronger primary verification later | RQ5; RQ6 | C-G5; C-G6; C-G8 | GAP-G7; GAP-G12 | Direct ASR evidence plus interpretive synthesis | No watchlist-only central support |
| KD transfers information from stronger teachers to students, but KD should be framed as reliability-sensitive supervision transfer, not only compression. | 9.4 | BE01; BE09; BE14; CORE-50 | `hinton2015distilling`; `yoon2022interkd`; `ferraz2023multilingualdistilwhisper` | Method anchor verified-primary; ASR KD evidence mostly secondary verified | Medium; foundation-model distillation source is secondary locally | RQ5 | C-G5; C-G8 | GAP-G7; GAP-G12 | Method-anchor support plus direct ASR evidence | Distil-Whisper watchlist not used centrally |
| Multi-teacher KD can reduce single-teacher dependence but introduces teacher-disagreement, posterior-mapping, label-space, and orthography-alignment risks. | 9.5 | CORE-48; CORE-49; CORE-51; BE08; BE13; BE15 | `leal21_interspeech`; `farooq2023must`; `bhogale24_interspeech` | Mixed verified-primary and verified-secondary | Medium; disagreement reporting remains uneven | RQ5; RQ6 | C-G5; C-G8 | GAP-G8; GAP-G12 | Direct ASR evidence plus synthesis | No watchlist-only central support |
| Foundation models can provide stronger teachers and broader language coverage, but they can also introduce hallucination, formatting bias, over-normalization, and hidden language/domain errors. | 9.6 | CORE-26; CORE-27; CORE-60; BE14; BF20 | `pmlr-v202-radford23a`; `pratap2024mms`; `koenecke2024carelesswhisper` | Mixed verified-primary and verified-secondary | Medium to high; hallucination evidence is used as risk framing | RQ2; RQ5; RQ6 | C-G2; C-G5; C-G6; C-G7 | GAP-G7; GAP-G9; GAP-G11 | Established evidence plus bounded future-facing synthesis | Watchlist LLM pseudo-label refinement is not used as central evidence |
| Reliability risks include teacher-error amplification, dialect/domain mismatch, orthographic normalization effects, generative hallucination, hidden subgroup damage, and weak reproducibility reporting. | 9.7 | C-G5; C-G6; C-G8; CORE-46; CORE-51; CORE-53; CORE-60; BE05; BE15; BF05; BF20 | `khurana2020dust`; `bhogale24_interspeech`; `karita2023lenient`; `koenecke2024carelesswhisper` | Mixed verified-primary and verified-secondary | Medium; orthography and hallucination risks need language-specific expansion in Section 10/11 | RQ5; RQ6 | C-G5; C-G6; C-G7; C-G8 | GAP-G7; GAP-G9; GAP-G11; GAP-G12 | Direct ASR evidence plus evaluation-risk synthesis | No watchlist-only central support |
| The decision matrix should select pseudo-labeling, KD, multi-teacher KD, or no pseudo-labeling yet from the supervision condition and available validation controls. | 9.8 | C-G2; C-G3; C-G4; C-G5; C-G6; C-G8; GAP-G7; GAP-G8; GAP-G9; GAP-G11; GAP-G12; Core 60 pseudo-labeling/KD anchors | Citation keys inherited from 9.1-9.7 | Matrix-supported synthesis | Low | RQ3; RQ4; RQ5; RQ6 | C-G2; C-G3; C-G4; C-G5; C-G6; C-G8 | GAP-G7; GAP-G8; GAP-G9; GAP-G11; GAP-G12 | Interpretive synthesis | No watchlist-only central support |

## Watchlist Use

The Section 9 draft does not use watchlist-only papers as central evidence. Distil-Whisper, LLM-enhanced semi-supervised learning, ReHear, efficient data selection, contextual ASR, and audio-LLM refinement are treated as watchlist or future-facing material unless later verified and explicitly integrated. The draft mentions LLM/SpeechLLM refinement only as a bounded emerging direction requiring constrained evaluation.

## Pseudo-Labeling Boundary

Section 9 focuses on generated supervision, filtering, teacher reliability, KD, and agreement. It does not repeat Section 7's broader data-pipeline discussion or Section 8's adaptation-method comparison except where needed to explain supervision expansion.

## Pashto Drift Check

Pashto is not mentioned in this Section 9 draft. Examples remain field-level.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 9 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 10 should specify evaluation protocols that can reveal pseudo-label damage, subgroup failures, hallucination, and reproducibility gaps.
- Section 11 should develop the LLM/SpeechLLM correction and pseudo-label refinement risks only as bounded emerging directions.
- Section 13 should reuse the teacher-quality, filtering, disagreement, and reporting requirements in the future agenda.
