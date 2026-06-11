# Evidence Notes for Section 13: Future Research Agenda

This companion note records the evidence controls used for `07_draft_sections/13_future_research_agenda.md`. Section 13 converts the cross-block synthesis from Section 12 into a future research agenda. Block G claim `C-G8` is the main backbone, with C-G1-C-G7 used as supporting claims.

## Source Controls Used

- `07_draft_sections/12_cross_block_synthesis_gap_analysis.md`
- `05_synthesis_matrices/block_g_core_claim_synthesis_map.csv`
- `05_synthesis_matrices/block_g_cross_block_taxonomy_synthesis_matrix.csv`
- `05_synthesis_matrices/block_g_research_gap_agenda_matrix.csv`
- `05_synthesis_matrices/block_g_section_to_evidence_map.csv`
- `05_synthesis_matrices/block_g_table_figure_plan.csv`
- `05_synthesis_matrices/block_g_additional_resource_candidates.csv`
- `05_synthesis_matrices/core_60_reference_set.csv`
- `05_synthesis_matrices/dataset_benchmark_matrix.csv`
- `05_synthesis_matrices/data_centric_strategy_matrix.csv`
- `05_synthesis_matrices/adaptation_strategy_matrix.csv`
- `05_synthesis_matrices/pseudo_labeling_kd_matrix.csv`
- `05_synthesis_matrices/evaluation_robustness_matrix.csv`
- `05_synthesis_matrices/priority_watchlist_for_llm_and_emerging_directions.csv`
- `03_references/references.bib`
- `03_references/citation_verification_log.csv`

## Agenda Claim Map

| Agenda Claim | Section Location | Supporting C-G Claims | Supporting GAP IDs | Supporting CoreIDs/PaperIDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Taxonomy Layers | Evidence Type |
|---|---|---|---|---|---|---|---|---|---|---|
| The future agenda should convert cross-block bottlenecks into practical priorities tied to RQ1-RQ6. | 13.1 | C-G8; C-G1-C-G7 | GAP-G1-GAP-G12 | Section 12; Block G controls | No new citation needed | Matrix-supported synthesis | Low | Main; RQ1-RQ6 | All layers | Interpretive agenda |
| Low-resource definitions should report labeled, unlabeled, weakly labeled, validation, dialect, domain, orthographic, compute, and deployment conditions. | 13.2 | C-G1; C-G8 | GAP-G1; GAP-G2; GAP-G3 | CORE-01; CORE-10 | `besacier2014_underresourced_asr_survey`; `peterson2022_openasr21` | Verified-primary-source | Low | RQ1; RQ3; RQ6 | Resource; language; evaluation | Established evidence |
| Dataset documentation should cover provenance, consent, licensing, metadata, validation, transcript conventions, community expertise, and normalization/scoring scripts. | 13.3 | C-G3; C-G8 | GAP-G2; GAP-G3; GAP-G12 | CORE-03; CORE-07; CORE-14; BG-CAND-01; BG-CAND-02; BG-CAND-03; BG-CAND-04 | `ardila2020commonvoice`; `lau2025_data_quality_multilingual_speech`; `olatunji2023_afrispeech200`; `gebru2021_datasheets_for_datasets`; `bender2018_data_statements`; `mitchell2019_model_cards`; `strubell2019_energy_policy` | ASR anchors verified-primary; documentation papers verified-primary background support | Low | RQ1; RQ3; RQ6 | Resource; language; evaluation | Established ASR evidence plus background methodological support |
| Future benchmarks should be orthography-aware, dialect-aware, and transparent about raw/normalized scoring and subgroup reporting. | 13.4 | C-G1; C-G3; C-G6; C-G8 | GAP-G3; GAP-G4 | CORE-04; CORE-05; CORE-14; CORE-53 | `karita2023lenient`; `conneau2022fleurs`; `shi2023mlsuperb`; `olatunji2023_afrispeech200` | Mixed verified-primary and verified-secondary | Medium because normalization is language-specific | RQ1; RQ3; RQ6 | Language; resource; evaluation | Established evidence plus interpretive agenda |
| Adaptation research should use compute-normalized, forgetting-aware, and ASR-specific comparisons rather than promoting one universal method. | 13.5 | C-G4; C-G8 | GAP-G5; GAP-G6; GAP-G12 | CORE-37; CORE-38; CORE-39; CORE-42; CORE-43; BG-CAND-04 | `pmlr-v97-houlsby19a`; `hu2022lora`; `dettmers2023qlora`; `udupa24_interspeech`; `qian24_interspeech`; `strubell2019_energy_policy` | PEFT method anchors verified-primary but not all direct ASR evidence; ASR anchors verified-primary | Medium | RQ4; RQ6 | Adaptation; model; evaluation | Method-anchor support plus ASR evidence |
| Pseudo-labeling and KD need teacher-quality reporting, filtering transparency, disagreement analysis, and evaluation of damage as well as gains. | 13.6 | C-G5; C-G8 | GAP-G7; GAP-G8 | CORE-44; CORE-46; CORE-48; CORE-51 | `park20d_interspeech`; `khurana2020dust`; `leal21_interspeech`; `bhogale24_interspeech` | Mixed verified-primary and verified-secondary | Medium | RQ5; RQ3; RQ6 | Supervision; resource; evaluation | Established evidence and interpretive agenda |
| Evaluation should move beyond aggregate WER/CER through subgroup, robustness, hallucination, contextual, reproducibility, and compute protocols. | 13.7 | C-G6; C-G8 | GAP-G4; GAP-G9; GAP-G12 | CORE-04; CORE-11; CORE-54; CORE-55; CORE-60; BF13; BF14; BF15 | `koenecke2024carelesswhisper`; `yang2021superb`; `watanabe2018espnet`; `ravanelli2021speechbrain`; `povey2011kaldi` | Mixed verified-primary and verified-secondary | Medium | RQ6 | Evaluation; model; adaptation | Established evidence and infrastructure support |
| Multimodal, AVSR, SpeechLM, and LLM-assisted ASR should be pursued only under reliability controls. | 13.8 | C-G7; C-G8 | GAP-G10; GAP-G11; GAP-G9; GAP-G12 | CORE-28; CORE-30; CORE-57; CORE-59; CORE-60; BF22; BF23; BF24 | `shi2022avhubert`; `anwar23_interspeech`; `seamless2025_joint_speech_text_mt`; `tian25b_interspeech`; `ma2024asrerrorcorrection`; `koudounas2025shallow`; `wang2025contextasrbench` | Mixed verified-primary, verified-secondary, and watchlist-ArXiv | High if overclaimed | RQ2; RQ5; RQ6 | Model; resource; evaluation; supervision | Watchlist-bounded evidence plus agenda synthesis |
| Future reports should include a practical checklist spanning resources, metadata, transcripts, models, adaptation, pseudo-labeling, decoding, evaluation, robustness, compute, and artifacts. | 13.9 | C-G8; C-G1-C-G7 | GAP-G1-GAP-G12 | Block G matrices; background documentation candidates | Background keys inherited from 13.3 and 13.5 | Matrix-supported; background support | Low | Main; RQ1-RQ6 | All layers | Interpretive reporting agenda |
| The conclusion should frame future progress around reliability, reproducibility, deployability, multimodal robustness, and constrained LLM assistance. | 13.10 | C-G8; C-G2; C-G7 | GAP-G1-GAP-G12 | Section 12; Section 13 controls | No new citation needed | Matrix-supported synthesis | Low | Main; RQ6 | All layers | Transition synthesis |

## Background-Support Reference Boundary

- `gebru2021_datasheets_for_datasets`, `bender2018_data_statements`, `mitchell2019_model_cards`, and `strubell2019_energy_policy` were added to `references.bib` and `citation_verification_log.csv` as `Background-support`.
- These entries are not added to Core 60.
- They are not used as ASR performance evidence.
- They support reporting standards for datasets, language-resource documentation, model reporting, and compute transparency.

## Watchlist-Boundary Notes

- `ma2024asrerrorcorrection`, `koudounas2025shallow`, and `wang2025contextasrbench` are cited only in Section 13.8 as future-facing evaluation-risk sources.
- Watchlist sources do not support strong central claims about reliable low-resource ASR performance.
- The section does not claim that AVSR or LLM-assisted correction is mature for all low-resource ASR.

## Quality Safeguards Checked

- Section 13 converts GAP-G1-GAP-G12 into priorities rather than repeating Section 12.
- C-G8 is the main agenda backbone.
- The agenda is not Pashto-centered.
- Foundation models are not described as solving low-resource ASR.
- No method family is presented as universally best.
- Methodological documentation papers are background support only and are not Core 60 entries.
- The required table placeholder is included.
