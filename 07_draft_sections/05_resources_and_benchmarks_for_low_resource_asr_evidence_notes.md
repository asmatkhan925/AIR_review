# Evidence Notes For Section 5: Resources and Benchmarks for Low-Resource ASR

## Scope

This companion note records the evidence used in `07_draft_sections/05_resources_and_benchmarks_for_low_resource_asr.md`. Section 5 primarily answers RQ3 and uses Block G claims C-G1, C-G2, C-G3, and C-G6 with the Section 5 control row from `block_g_section_to_evidence_map.csv`.

## Block G Controls Used

| Control | Use In Section 5 |
|---|---|
| C-G1 | Defines resources and benchmarks as part of the multidimensional low-resource condition. |
| C-G2 | Supports the claim that foundation models increase the need for careful data and benchmark interpretation. |
| C-G3 | Main Section 5 claim: data quality, filtering, normalization, metadata, and validation shape downstream behavior. |
| C-G6 | Supports the benchmark-comparability and evaluation-risk discussion. |
| GAP-G1 | Supports explicit reporting of what "low-resource" means in each study. |
| GAP-G2 | Supports dataset documentation, validation, metadata, licensing, and dialect-coverage requirements. |
| GAP-G3 | Supports orthographic normalization and transcript-comparability concerns. |
| GAP-G4 | Supports caution about aggregate foundation-model benchmark reporting. |
| GAP-G12 | Supports reproducibility and compute/deployment reporting as part of benchmark interpretation. |
| TABLE-G2 | Supports a future dataset and benchmark comparison table. |

## Claim Map

| Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Evidence Type |
|---|---|---|---|---|---|---|---|
| Strong pretrained models make resource and benchmark quality more important because benchmark design determines whether model gains are interpretable. | 5.1 | C-G1; C-G2; C-G3; CORE-01; CORE-09 | `besacier2014_underresourced_asr_survey`; `gales2014_babel_project_research_cued` | Verified-primary-source | Low | RQ1; RQ2; RQ3 | Cross-block interpretation grounded in established evidence |
| Labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal resources enable different parts of ASR development and carry different risks. | 5.2 | C-G1; C-G3; resource-layer taxonomy; CORE-03; CORE-34; CORE-36 | `ardila2020commonvoice`; `wang2021voxpopuli`; `tian24_interspeech` | Verified-primary-source | Low to medium; multimodal resources are discussed conceptually here and expanded later | RQ1; RQ3; RQ6 | Interpretation grounded in dataset and data-centric evidence |
| Major corpus and benchmark families support different evidentiary roles: openness, low-resource challenge design, multilingual transfer, benchmark organization, accent metadata, and data-pipeline quality. | 5.3 | CORE-03; CORE-04; CORE-05; CORE-06; CORE-09; CORE-10; CORE-12; CORE-13; CORE-14; CORE-33; CORE-34; CORE-52; CORE-36 | `ardila2020commonvoice`; `gales2014_babel_project_research_cued`; `peterson2022_openasr21`; `pratap20_interspeech`; `wang2021voxpopuli`; `conneau2022fleurs`; `conneau2022xtreme_s`; `shi2023mlsuperb`; `shi2024mlsuperb2`; `chen2025mlsuperb2challenge`; `javed2023indsuperb`; `olatunji2023_afrispeech200`; `tian24_interspeech` | Mostly verified-primary; FLEURS and XTREME-S are secondary in local logs and not sole support for strong claims | Medium due to mixed benchmark statuses and differing scopes | RQ2; RQ3; RQ6 | Established evidence plus comparative interpretation |
| Dataset size and language count are insufficient without validation, transcript quality, metadata, licensing, contribution-balance, and documentation. | 5.4 | C-G3; GAP-G2; CORE-03; CORE-07; CORE-14; CORE-34; BG-CAND-01; BG-CAND-02; BG-CAND-03 | `ardila2020commonvoice`; `wang2021voxpopuli`; `lau2025_data_quality_multilingual_speech`; `olatunji2023_afrispeech200` | Verified-primary-source for ASR evidence; documentation candidates are tracked methodological support only | Low; documentation frameworks are not used as ASR evidence | RQ1; RQ3; RQ6 | Established ASR evidence plus methodological support |
| Benchmark comparability is fragile because domains, scripts, transcription conventions, splits, metrics, normalization, robustness, and metadata differ across resources. | 5.5 | C-G6; GAP-G3; GAP-G4; GAP-G12; CORE-04; CORE-12; CORE-52; CORE-53; CORE-54 | `conneau2022fleurs`; `conneau2022xtreme_s`; `shi2023mlsuperb`; `karita2023lenient`; `cornell2023chime7` | Mixed verified-primary and verified-secondary; no watchlist-only central support | Medium; detailed fairness and hallucination evidence deferred to Section 10 | RQ3; RQ6 | Established evidence plus evaluation-risk interpretation |
| Resources and benchmarks motivate the next taxonomy section because no single dataset type, benchmark score, or model family can explain low-resource ASR reliability. | 5.6 | C-G1; C-G2; C-G3; C-G6; Section 5 control row | No new citation beyond prior section evidence | Matrix-supported synthesis | Low | RQ1; RQ2; RQ3; RQ6 | Cross-block interpretation |

## Watchlist Use

No watchlist-only paper is used as central support for Section 5. LoASR-Bench, GigaSpeech 2, AfriVox-v2, FormosanBench, and related current resources remain watchlist or future-agenda material unless later verified and explicitly needed.

## Documentation Candidate Use

Datasheets for Datasets, Data Statements, and Model Cards are tracked in `block_g_additional_resource_candidates.csv` as methodological support. They are not cited in Section 5 because they are not currently present as BibTeX keys in `03_references/references.bib`, and they are not treated as ASR evidence.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 5 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 6 should use Section 5 to motivate the foundation-model-era taxonomy.
- Section 7 should expand the data-centric methods behind filtering, normalization, validation, and augmentation.
- Section 10 should expand benchmark comparability into metric, robustness, fairness, reproducibility, and compute reporting.
