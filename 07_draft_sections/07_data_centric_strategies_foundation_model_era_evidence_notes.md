# Evidence Notes For Section 7: Data-Centric Strategies in the Foundation-Model Era

## Scope

This companion note records the evidence used in `07_draft_sections/07_data_centric_strategies_foundation_model_era.md`. Section 7 answers RQ3 by explaining why data-centric strategies remain necessary after foundation models. The section uses `data_centric_strategy_matrix.csv` as the main evidence source, with support from `dataset_benchmark_matrix.csv`, `evaluation_robustness_matrix.csv`, Core 60, and Block G controls.

## Block G Controls Used

| Control | Use In Section 7 |
|---|---|
| C-G3 | Main backbone: data quality, filtering, normalization, metadata, and validation shape downstream behavior. |
| C-G1 | Connects data strategy to the multidimensional definition of low-resource ASR. |
| C-G2 | Connects foundation models to shifted data and evaluation bottlenecks. |
| C-G5 | Used only as a bridge for pseudo-labeling reliability; detailed treatment deferred to Section 9. |
| C-G6 | Connects normalization, metadata, and benchmark design to evaluation comparability. |
| GAP-G2 | Dataset documentation, validation, licensing, and metadata gap. |
| GAP-G3 | Orthographic normalization and transcript comparability gap. |
| GAP-G4 | Aggregate reporting gap, especially for dialect/domain hidden failures. |
| GAP-G7 | Pseudo-label reliability gap, introduced only as a Section 9 bridge. |
| GAP-G12 | Reproducibility and compute reporting gap. |

## Claim Map

| Section Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Linked Block G Claims/Gaps | Evidence Type |
|---|---|---|---|---|---|---|---|---|
| Data-centric work remains necessary after foundation models because scale does not guarantee reliable target-language data, validation, normalization, or evaluation. | 7.1 | C-G2; C-G3; CORE-26; CORE-27; CORE-36; CORE-07; BC12; BA10 | `pmlr-v202-radford23a`; `pratap2024mms`; `tian24_interspeech`; `lau2025_data_quality_multilingual_speech` | Mostly verified-primary; no watchlist-only support | Low | RQ2; RQ3; RQ6 | C-G2; C-G3; GAP-G2; GAP-G12 | Interpretive synthesis grounded in Core 60 |
| Corpus creation, validation, documentation, and metadata determine whether a dataset can support reliable low-resource ASR claims. | 7.2 | CORE-03; CORE-04; CORE-09; CORE-10; CORE-14; CORE-33; CORE-34; CORE-52; CORE-07; BC03; BC04; BC05; BA13; BA15; BA21; BF02 | `ardila2020commonvoice`; `gales2014_babel_project_research_cued`; `peterson2022_openasr21`; `pratap20_interspeech`; `wang2021voxpopuli`; `olatunji2023_afrispeech200`; `conneau2022fleurs`; `shi2023mlsuperb`; `lau2025_data_quality_multilingual_speech` | Mostly verified-primary; FLEURS is locally secondary verified | Low to medium | RQ1; RQ3; RQ6 | C-G1; C-G3; GAP-G2; GAP-G4 | Established evidence plus synthesis |
| Transcript normalization, punctuation, casing, spelling variants, scripts, and tokenization affect training targets and WER/CER comparability. | 7.3 | CORE-07; CORE-35; CORE-36; CORE-53; BC08; BC12; BF05 | `lau2025_data_quality_multilingual_speech`; `tian24_interspeech`; `chen21d_interspeech`; `karita2023lenient` | Mixed verified-primary and verified-secondary; orthography-aware evaluation is secondary verified | Medium; normalization rules are language-specific | RQ3; RQ6 | C-G3; C-G6; GAP-G3 | Established evidence plus evaluation-risk interpretation |
| Filtering, segmentation, alignment, language identification, and source analysis are active data interventions in heterogeneous foundation-model-era pipelines. | 7.4 | CORE-34; CORE-36; BC05; BC07; BC12 | `wang2021voxpopuli`; `tian24_interspeech` | Verified-primary-source for central anchors; GigaSpeech-style support is not cited as central because local status is pending | Low to medium | RQ3; RQ6 | C-G3; GAP-G2; GAP-G4 | Established evidence plus bounded interpretation |
| Augmentation remains useful for robustness and limited supervised data, but it is not a substitute for representative language, dialect, domain, or channel coverage. | 7.5 | CORE-31; CORE-32; CORE-54; CORE-59; BC01; BC02; BF08; BF18 | `ko15_interspeech`; `park19e_interspeech`; `cornell2023chime7`; `anwar23_interspeech` | Verified-primary for augmentation anchors; robustness support mixed primary/secondary | Medium; augmentation anchors are general ASR rather than low-resource-specific | RQ3; RQ6 | C-G3; C-G6; GAP-G4 | Established evidence plus synthesis |
| Unlabeled, weakly labeled, and pseudo-labeled data expand training possibilities but require source documentation, filtering, and validation. | 7.6 | CORE-15; CORE-22; CORE-26; CORE-34; CORE-45; CORE-46; CORE-51; BC05; BC10; BC11; BE15 | `baevski2020wav2vec2`; `babu22_interspeech`; `pmlr-v202-radford23a`; `wang2021voxpopuli`; `park20d_interspeech`; `khurana2020dust`; `bhogale24_interspeech` | Mixed verified-primary and verified-secondary; no watchlist-only central support | Medium; pseudo-labeling is only introduced here and deferred to Section 9 | RQ3; RQ5; RQ6 | C-G3; C-G5; GAP-G7 | Established evidence plus bridge synthesis |
| Data-centric strategy should be selected from the failure mode: scarcity, weak labels, orthography, dialect, domain, or compute limits require different interventions and evaluations. | 7.7 | C-G1; C-G3; C-G5; C-G6; GAP-G2; GAP-G3; GAP-G4; GAP-G7; GAP-G12; Core 60 data/evaluation anchors | Citation keys inherited from 7.1-7.6 | Matrix-supported synthesis | Low | RQ1; RQ3; RQ5; RQ6 | C-G1; C-G3; C-G5; C-G6; GAP-G2; GAP-G3; GAP-G4; GAP-G7; GAP-G12 | Interpretive synthesis |

## Watchlist Use

The Section 7 draft does not use watchlist-only papers as central evidence. GigaSpeech 2, recent efficient data-selection preprints, and transcript-normalization watchlist items remain excluded from central claims unless later verified and added to the citation backbone.

## Pseudo-Labeling Boundary

Pseudo-labeling appears only as a data-pipeline bridge in Section 7. Teacher quality, teacher disagreement, calibration, KD, and multi-teacher supervision should be developed in Section 9.

## Dataset-Catalog Check

The draft mentions Common Voice, Babel/OpenASR, MLS, VoxPopuli, AfriSpeech-200, and robustness benchmarks only to illustrate intervention types and risks. It does not organize the section as a dataset-by-dataset catalog.

## Pashto Drift Check

Pashto is not mentioned in this Section 7 draft. Examples remain field-level.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 7 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 8 should use the Section 7 decision framework when discussing adaptation under data, domain, and compute constraints.
- Section 9 should expand pseudo-label reliability, teacher disagreement, and KD beyond the brief data-pipeline bridge here.
- Section 10 should formalize the normalization, subgroup, robustness, reproducibility, and compute evaluation requirements introduced here.
