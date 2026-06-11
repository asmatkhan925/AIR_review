# Evidence Notes for Section 11: Multimodal, AVSR, and LLM-Assisted ASR

This companion note records the evidence used in `07_draft_sections/11_multimodal_avsr_llm_assisted_asr.md`. Section 11 answers the future-facing part of RQ6. It uses Block G claim `C-G7` as the main backbone, with secondary links to `C-G2`, `C-G3`, `C-G5`, `C-G6`, and `C-G8`.

## Source Controls Used

- `05_synthesis_matrices/block_g_core_claim_synthesis_map.csv`
- `05_synthesis_matrices/block_g_research_gap_agenda_matrix.csv`
- `05_synthesis_matrices/block_g_section_to_evidence_map.csv`
- `05_synthesis_matrices/block_g_table_figure_plan.csv`
- `05_synthesis_matrices/core_60_reference_set.csv`
- `05_synthesis_matrices/foundation_model_matrix.csv`
- `05_synthesis_matrices/evaluation_robustness_matrix.csv`
- `05_synthesis_matrices/priority_watchlist_for_llm_and_emerging_directions.csv`
- `03_references/references.bib`

## Block G Claim and Gap Mapping

| Control ID | Local meaning for Section 11 |
|---|---|
| C-G7 | Main backbone: multimodal AVSR, SpeechLM, and LLM-assisted ASR are promising but introduce hallucination, over-correction, contextual bias, modality mismatch, and compute opacity. |
| C-G2 | Foundation models reshape the bottleneck rather than remove low-resource ASR constraints. |
| C-G3 | Data quality, normalization, metadata, and validation remain central even with strong pretrained models. |
| C-G5 | Generated or corrected supervision remains reliability-sensitive and must not be treated as clean labels. |
| C-G6 | Pooled WER/CER cannot expose all dialect, domain, orthographic, demographic, robustness, or hallucination-related failures. |
| C-G8 | Future work must connect multimodal robustness and constrained LLM assistance to reproducibility, compute, and community-aware resource development. |
| GAP-G9 | LLM evaluation metrics: hallucination, over-correction, semantic drift, and contextual ASR need metrics beyond WER/CER. |
| GAP-G10 | Low-resource AVSR: multilingual and multidialect AVSR resources and comparable protocols remain limited. |
| GAP-G11 | Constrained LLM-assisted ASR: correction or rescoring should be bounded by ASR hypotheses, lattices, or validated context. |
| GAP-G12 | Reproducibility and compute: foundation-scale and multimodal systems need transparent cost and deployment reporting. |

## Claim-Level Evidence Map

| Section Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Linked Block G Claims | Linked Block G Gaps | Evidence Type | Watchlist Boundary |
|---|---|---|---|---|---|---|---|---|---|---|
| Multimodal, AVSR, SpeechLM, and LLM-assisted systems expand the design space but do not remove low-resource ASR reliability constraints. | 11.1 | C-G7; C-G8; CORE-28; CORE-30; CORE-57; CORE-58; CORE-59; CORE-60 | `shi2022avhubert`; `shi2022robustavsr`; `anwar23_interspeech`; `seamless2025_joint_speech_text_mt`; `tian25b_interspeech`; `koenecke2024carelesswhisper` | Mixed verified-primary and verified-secondary | Medium | RQ6; RQ2 | C-G7; C-G8 | GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Interpretive synthesis with Core 60 backbone | Watchlist only motivates future risks, not central claim. |
| AVSR can improve robustness under degraded audio when visual streams are available, but it is not a general solution to low-resource ASR. | 11.2 | CORE-57; CORE-58; CORE-59; BF16; BF17; BF18 | `shi2022avhubert`; `shi2022robustavsr`; `anwar23_interspeech` | AV-HuBERT and robust AVSR verified-secondary; MuAViC verified-primary | Medium | RQ6 | C-G7; C-G8 | GAP-G10 | Multimodal/AVSR evidence | No watchlist-only support for the core AVSR claim. |
| Multilingual speech-text foundation models broaden ASR-adjacent transfer, but ASR, speech translation, and correction must remain separate evaluation tasks. | 11.3 | CORE-26; CORE-27; CORE-28; BB14; BB16; BB17 | `pmlr-v202-radford23a`; `pratap2024mms`; `seamless2025_joint_speech_text_mt` | Verified-primary-source anchors | Medium because SeamlessM4T is translation-centric | RQ2; RQ6 | C-G2; C-G7 | GAP-G9; GAP-G12 | Foundation-model evidence plus interpretive task-boundary synthesis | No watchlist-only support. |
| SpeechLM and Speech-LLM systems may connect speech evidence with text-side knowledge, but low-resource ASR reliability is constrained by language coverage, task definition, decoding, data quality, and compute. | 11.4 | CORE-25; CORE-30; BB12; BB22 | `zhang2024_speechlm`; `tian25b_interspeech` | SpeechLM verified-secondary with primary pending; OpusLM verified-primary | Medium | RQ2; RQ6 | C-G2; C-G7; C-G8 | GAP-G9; GAP-G12 | Foundation-model evidence | SpeechLM evidence is used cautiously and not as a universal performance claim. |
| LLM-assisted ASR is most defensible as bounded correction, rescoring, contextualization, or normalization support rather than unconstrained rewriting. | 11.5 | CORE-60; BF20; BF24 | `koenecke2024carelesswhisper`; `ma2024asrerrorcorrection` | Core hallucination evidence verified-secondary; LLM correction watchlist-ArXiv | High | RQ6; RQ5 | C-G5; C-G6; C-G7 | GAP-G9; GAP-G11 | Watchlist-bounded evidence plus interpretive synthesis | `ma2024asrerrorcorrection` is used only as emerging evidence for constrained correction and over-correction risk. |
| Hallucination, over-correction, modality mismatch, context leakage, task-boundary confusion, and compute opacity are the central Section 11 reliability risks. | 11.6 | CORE-57; CORE-58; CORE-59; CORE-60; BF22; BF23; BF24 | `shi2022avhubert`; `shi2022robustavsr`; `anwar23_interspeech`; `koenecke2024carelesswhisper`; `koudounas2025shallow`; `wang2025contextasrbench`; `ma2024asrerrorcorrection` | Mixed verified-secondary, verified-primary, and watchlist-ArXiv | High | RQ6 | C-G6; C-G7; C-G8 | GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Evaluation-risk synthesis | Watchlist sources are used only to mark emerging evaluation risks, not settled general behavior. |
| System choice should follow the enabling condition: visual stream availability, multilingual transfer need, orthographic uncertainty, terminology support, acoustic constraints, privacy, compute, and hallucination sensitivity. | 11.7 | C-G2; C-G3; C-G5; C-G6; C-G7; C-G8; GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Citation keys inherited from 11.1-11.6 | Matrix-supported synthesis | Low to medium | RQ6; RQ2; RQ5 | C-G2; C-G3; C-G5; C-G6; C-G7; C-G8 | GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Interpretive decision framework | No watchlist-only central support. |
| Section 12 should integrate multimodal and LLM-assisted directions with the review's resource, language, adaptation, supervision, evaluation, reproducibility, and compute constraints. | 11.8 | C-G7; C-G8 | Citation keys inherited from 11.1-11.7 | Block G synthesis | Low | RQ6; Main review question | C-G7; C-G8 | GAP-G9; GAP-G10; GAP-G11; GAP-G12 | Integrative synthesis | Watchlist remains future-facing only. |

## Watchlist-Boundary Notes

- `ma2024asrerrorcorrection`, `koudounas2025shallow`, and `wang2025contextasrbench` are used only for future-facing or evaluation-risk comments.
- They do not support strong claims that LLM-assisted correction reliably improves all low-resource ASR.
- Other frontier candidates in `priority_watchlist_for_llm_and_emerging_directions.csv` are not cited in the draft because the instruction was not to introduce new references or rely on watchlist-only evidence for central claims.

## Quality Safeguards Checked

- The draft does not claim that AVSR solves low-resource ASR.
- The draft does not claim that LLM-assisted correction reliably improves all low-resource ASR.
- The draft separates ASR, speech translation, SpeechLM systems, and post-ASR correction/rescoring.
- Watchlist-only sources are bounded as emerging evidence or risk motivation.
- Section 10's evaluation framework is built upon rather than duplicated.
- Section 9's pseudo-labeling details are not repeated.
- Pashto is not used as a central example.

## Follow-Up Items

- When Section 12 is drafted, reuse the Section 11 decision matrix as a cross-block synthesis input.
- If primary-source status changes for `shi2022avhubert`, `shi2022robustavsr`, `zhang2024_speechlm`, or `koenecke2024carelesswhisper`, update the evidence notes and citation verification log.
- Before final manuscript integration, decide whether Table G8 should be a standalone Section 11 table or folded into the Section 13 future agenda table.
