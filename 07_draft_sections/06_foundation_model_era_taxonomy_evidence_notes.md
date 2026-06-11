# Evidence Notes For Section 6: Foundation-Model-Era Taxonomy of Low-Resource ASR

## Scope

This companion note records the evidence used in `07_draft_sections/06_foundation_model_era_taxonomy.md`. Section 6 presents the review's six-layer taxonomy and primarily uses `block_g_cross_block_taxonomy_synthesis_matrix.csv`, the Section 6 control row, and Block G claims C-G1 through C-G7.

## Block G Controls Used

| Control | Use In Section 6 |
|---|---|
| C-G1 | Defines low-resource ASR as a multidimensional condition requiring a layered taxonomy. |
| C-G2 | Positions foundation models as changing the starting point while shifting bottlenecks. |
| C-G3 | Supports the resource layer and bridge to Section 7. |
| C-G4 | Supports the adaptation layer and bridge to Section 8. |
| C-G5 | Supports the supervision layer and bridge to Section 9. |
| C-G6 | Supports the evaluation layer and bridge to Section 10. |
| C-G7 | Supports multimodal, AVSR, SpeechLM, and LLM-assisted risk framing for Sections 10-11. |
| Section 6 control row | Keeps the section taxonomy-centered and prevents repetition of Section 4's model history. |

## Claim Map

| Taxonomy Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Linked Block G Claims | Evidence Type |
|---|---|---|---|---|---|---|---|---|
| A foundation-model-era taxonomy is needed because low-resource ASR depends on interactions among resources, languages, models, adaptation, supervision, and evaluation. | 6.1, 6.8, 6.9 | Section 6 control row; C-G1; C-G2; C-G6; CORE-15; CORE-22; CORE-26; CORE-27; CORE-04; CORE-12; CORE-06 | `baevski2020wav2vec2`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `shi2023mlsuperb`; `conneau2022xtreme_s`; `chen2025mlsuperb2challenge` | Mostly verified-primary; XTREME-S is secondary in local logs | Low to medium; taxonomy is interpretive synthesis grounded in Core 60 | RQ1; RQ2; RQ6 | C-G1; C-G2; C-G6 | Interpretive synthesis |
| The resource layer distinguishes labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal resources by function and reliability risk. | 6.2 | Resource-layer rows; CORE-03; CORE-07; CORE-33; CORE-34 | `ardila2020commonvoice`; `wang2021voxpopuli`; `pratap20_interspeech`; `lau2025_data_quality_multilingual_speech` | Verified-primary-source | Low | RQ1; RQ3; RQ6 | C-G1; C-G3 | Established evidence plus synthesis |
| The language layer explains why dialect, orthography, code-switching, morphology, script complexity, and language-family mismatch affect both modeling and scoring. | 6.3 | Language-layer rows; CORE-05; CORE-06; CORE-13; CORE-14; CORE-53 | `shi2024mlsuperb2`; `chen2025mlsuperb2challenge`; `javed2023indsuperb`; `olatunji2023_afrispeech200`; `karita2023lenient` | Verified-primary-source for cited anchors except local medium-risk scoring caveats | Low to medium; code-switching and morphology need fuller treatment later | RQ1; RQ2; RQ6 | C-G1; C-G6 | Established evidence plus synthesis |
| The model layer summarizes model families conceptually rather than repeating model history: hybrid, E2E, SSL, multilingual, weakly supervised, speech foundation, SpeechLM, and multimodal systems. | 6.4 | Model-layer rows; CORE-02; CORE-08; CORE-15; CORE-17; CORE-21; CORE-22; CORE-26; CORE-27; CORE-28; CORE-30 | `prabhavalkar2023_e2e_asr_survey`; `mohamed2022_ssl_review`; `baevski2020wav2vec2`; `hsu2021hubert`; `chen2022wavlm`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `seamless2025_joint_speech_text_mt`; `tian25b_interspeech` | Mostly verified-primary; HuBERT/WavLM are locally cautious; SeamlessM4T is translation-centric | Medium; avoid treating SpeechLM or translation-centric sources as direct low-resource ASR proof | RQ2; RQ6 | C-G2; C-G7 | Established evidence plus bounded interpretation |
| The adaptation layer organizes how pretrained systems are specialized: full fine-tuning, continued pretraining, adapters, LoRA/QLoRA, prompting/contextual biasing, transfer, and forgetting control. | 6.5 | Adaptation-layer rows; CORE-37; CORE-38; CORE-39; CORE-41; CORE-42; CORE-43 | `pmlr-v97-houlsby19a`; `hu2022lora`; `dettmers2023qlora`; `getman24_interspeech`; `udupa24_interspeech`; `qian24_interspeech` | Mixed: method anchors plus verified-primary ASR adaptation anchors | Medium; PEFT method anchors are not all ASR-specific | RQ2; RQ4; RQ6 | C-G2; C-G4 | Interpretive synthesis grounded in adaptation evidence |
| The supervision layer separates verified supervision from SSL, self-training, pseudo-label filtering, KD, multi-teacher KD, and agreement-based teacher selection. | 6.6 | Supervision-layer rows; CORE-44; CORE-45; CORE-46; CORE-48; CORE-49; CORE-50; CORE-51 | `kahn2019selftraining`; `park20d_interspeech`; `khurana2020dust`; `leal21_interspeech`; `farooq2023must`; `ferraz2023multilingualdistilwhisper`; `bhogale24_interspeech` | Mixed verified-primary and secondary; central claim is supported by multiple non-watchlist anchors | Medium; pseudo-label and KD claims should not imply clean supervision | RQ3; RQ5; RQ6 | C-G5 | Established evidence plus synthesis |
| The evaluation layer expands beyond WER/CER to orthography-aware, dialect-wise, domain/channel-wise, robustness, fairness, reproducibility, compute, AVSR, hallucination, and LLM-assisted evaluation. | 6.7 | Evaluation-layer rows; CORE-11; CORE-53; CORE-54; CORE-55; CORE-56; CORE-57; CORE-58; CORE-59; CORE-60 | `yang2021superb`; `karita2023lenient`; `cornell2023chime7`; `koenecke2020racialdisparities`; `liu2021casualconversations`; `shi2022avhubert`; `shi2022robustavsr`; `anwar23_interspeech`; `koenecke2024carelesswhisper` | Mixed verified-primary and secondary; no watchlist-only source carries a central claim | Medium; LLM-assisted evaluation remains future-facing and should be expanded cautiously in Section 11 | RQ6 | C-G6; C-G7 | Established evidence plus future-facing synthesis |
| Layer interactions explain many failures: strong models can fail because of weak resource evidence, language mismatch, adaptation trade-offs, unreliable pseudo-labels, or pooled evaluation. | 6.8 | All taxonomy rows; C-G1-C-G7 | Citations are inherited from prior layer rows | Matrix-supported synthesis | Low | RQ1-RQ6 | C-G1; C-G2; C-G3; C-G4; C-G5; C-G6; C-G7 | Interpretive synthesis |

## Watchlist Use

The draft does not use watchlist-only papers as central evidence. It mentions LLM-assisted and contextual risks only at the taxonomy level and relies on Core 60 hallucination and multimodal anchors rather than watchlist-only sources.

## Pashto Drift Check

Pashto is not mentioned in this Section 6 draft. Language-layer examples remain field-level.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 6 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 7 should develop the resource and transcript-quality implications of the taxonomy.
- Section 8 should expand adaptation methods and trade-offs.
- Section 9 should expand supervision reliability, pseudo-label filtering, and teacher disagreement.
- Sections 10 and 11 should expand evaluation, robustness, AVSR, hallucination, and LLM-assisted ASR risks.
