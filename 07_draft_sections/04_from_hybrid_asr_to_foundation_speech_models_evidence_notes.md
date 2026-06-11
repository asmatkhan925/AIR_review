# Evidence Notes For Section 4: From Hybrid ASR to Foundation Speech Models

## Scope

This companion note records the evidence used in `07_draft_sections/04_from_hybrid_asr_to_foundation_speech_models.md`. Section 4 answers RQ2 and uses Block G claim C-G2 as the main control backbone, with C-G1, C-G3, C-G4, and C-G6 as secondary constraints where relevant.

## Block G Controls Used

| Control | Use In Section 4 |
|---|---|
| C-G2 | Main claim: foundation speech models improve the starting point but shift bottlenecks toward adaptation, data quality, and evaluation. |
| C-G1 | Keeps the discussion tied to the multidimensional low-resource definition from Section 3. |
| C-G3 | Supports the bridge to Section 5 on resource and benchmark quality. |
| C-G4 | Supports the claim that foundation-model gains lead into conditional adaptation choices. |
| C-G6 | Supports cautions about aggregate multilingual or foundation-model scores. |
| Section 4 control row | Keeps the section focused on RQ2 and prevents a paper-by-paper history. |

## Claim Map

| Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Evidence Type |
|---|---|---|---|---|---|---|---|
| Hybrid and early E2E ASR form the pre-foundation baseline in which low-resource ASR depended on labeled data, lexicons, alignments, language models, and expert resources. | 4.1 | CORE-01; CORE-02; CORE-09 | `besacier2014_underresourced_asr_survey`; `gales2014_babel_project_research_cued`; `prabhavalkar2023_e2e_asr_survey` | Verified-primary-source | Low | RQ1; RQ2 | Established evidence |
| SSL changed low-resource ASR by making unlabeled speech useful for representation learning, but downstream adaptation and evaluation remain necessary. | 4.2 | C-G2; CORE-08; CORE-15; CORE-17; CORE-18; CORE-19; CORE-20; CORE-21 | `mohamed2022_ssl_review`; `baevski2020wav2vec2`; `hsu2021hubert`; `chen2022wavlm`; `chung2021_w2vbert`; `pmlr-v162-chiu22a`; `pmlr-v162-baevski22a` | Mixed: mostly verified-primary; HuBERT and WavLM are marked secondary/source-pending in Core 60 | Medium; secondary SSL anchors are corroborated by verified-primary SSL evidence | RQ2; RQ4 | Established evidence plus interpretation |
| Multilingual SSL and weakly supervised ASR changed the starting point by enabling transfer, zero/few-shot baselines, and broader language coverage. | 4.3 | C-G2; CORE-16; CORE-22; CORE-26; CORE-27; CORE-04 | `conneau21_interspeech`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `shi2023mlsuperb` | Verified-primary-source | Low | RQ2; RQ6 | Established evidence |
| Multilingual scale does not guarantee reliable low-resource ASR because language-level, dialect-level, and domain-level weaknesses can be hidden by aggregate reporting. | 4.3, 4.5 | C-G2; C-G6; CORE-04; CORE-05; CORE-06 | `shi2023mlsuperb`; `shi2024mlsuperb2`; `chen2025mlsuperb2challenge` | Verified-primary-source | Low | RQ2; RQ6 | Interpretation grounded in benchmark evidence |
| Speech foundation models and SpeechLMs broaden ASR into speech-text and multimodal architectures, but ASR claims must stay bounded when systems are translation-centric or early-stage. | 4.4 | C-G2; CORE-23; CORE-24; CORE-25; CORE-28; CORE-30 | `ao2022speecht5`; `zhang2022speechut`; `zhang2024_speechlm`; `seamless2025_joint_speech_text_mt`; `tian25b_interspeech` | Verified-primary-source for cited Core 60 anchors | Medium; SeamlessM4T is translation-centric and should not be used as standalone low-resource ASR proof | RQ2; RQ6 | Established evidence plus bounded interpretation |
| Direct low-resource foundation-model evaluation shows that foundation models help but still depend on adaptation, augmentation, and evaluation choices. | 4.4, 4.5 | C-G2; C11; C-D1; CORE-29; BD10 | `geng25c_interspeech` | Verified-primary-source | Medium; single-language case cannot generalize alone | RQ2; RQ4; RQ6 | Established evidence with limited generalization |
| Foundation models shift the unit of work from training from scratch to selecting, adapting, validating, and evaluating pretrained systems under realistic constraints. | 4.5, 4.6 | C-G2; C-G3; C-G4; C-G6; CORE-15; CORE-22; CORE-26; CORE-27; CORE-29 | `baevski2020wav2vec2`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `geng25c_interspeech` | Verified-primary-source | Low to medium; should not be phrased as universal improvement for all languages | RQ2; RQ3; RQ4; RQ6 | Cross-block interpretation |

## Watchlist Use

The draft does not cite watchlist-only or arXiv-only papers as central evidence. LLM-assisted correction, rescoring, and contextual ASR are mentioned only as a bridge to Section 11 and are not used to support Section 4's main claims.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 4 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 5 should expand the resource and benchmark implications of foundation-model evaluation.
- Section 8 should develop adaptation choices, including full fine-tuning, continued pretraining, PEFT, and forgetting control.
- Section 10 should expand the evaluation limitations of multilingual and foundation-model benchmarks.
- Section 11 should handle SpeechLM, multimodal, AVSR, and LLM-assisted correction/rescoring in more detail.
