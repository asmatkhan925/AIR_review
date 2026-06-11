# Evidence Notes For Section 3: What Makes ASR Low-Resource?

## Scope

This companion note records the evidence used in `07_draft_sections/03_what_makes_asr_low_resource.md` after revision with the Block G synthesis layer. Section 3 answers RQ1 and uses Block G claims C-G1 and C-G6 as the control backbone.

## Block G Controls Used

| Control | Use In Section 3 |
|---|---|
| C-G1 | Defines low-resource ASR as multidimensional and not reducible to labeled hours. |
| C-G6 | Frames WER/CER as necessary but insufficient when pooled scores hide dialect, domain, orthographic, demographic, robustness, or cost failures. |
| GAP-G1 | Supports the need for an explicit definition of low-resource ASR. |
| GAP-G2 | Supports the argument that dataset size needs quality, validation, metadata, licensing, and dialect information. |
| GAP-G3 | Supports the orthography and transcript-normalization discussion. |
| GAP-G4 | Supports the warning that aggregate foundation-model scores can hide per-language, dialect, and domain failures. |
| GAP-G12 | Supports reproducibility, compute, and deployment-cost reporting as evaluation conditions. |
| Section 3 control row | Keeps the section focused on RQ1 with RQ3 and RQ6 as secondary links; no watchlist papers support central claims. |

## Claim Map

| Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping |
|---|---|---|---|---|---|---|
| Low-resource ASR is a multidimensional reliability condition, not simply a shortage of labeled hours. | 3.1, 3.6 | C-G1; GAP-G1; CORE-01; CORE-09; CORE-10; CORE-06 | `besacier2014_underresourced_asr_survey`; `gales2014_babel_project_research_cued`; `peterson2022_openasr21`; `chen2025mlsuperb2challenge` | Verified-primary-source | Low | RQ1; RQ3; RQ6 |
| Different resource types serve different functions and carry different risks: labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal resources are not interchangeable. | 3.2 | C-G1; GAP-G2; CORE-03; CORE-07; CORE-15; CORE-17; CORE-21; CORE-22; CORE-26; CORE-27 | `ardila2020commonvoice`; `wang2021voxpopuli`; `lau2025_data_quality_multilingual_speech`; `baevski2020wav2vec2`; `hsu2021hubert`; `chen2022wavlm`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms` | Mixed: mostly verified-primary; HuBERT and WavLM remain secondary/source-pending in Core 60 | Medium; secondary model papers are not sole support for central definition | RQ1; RQ2; RQ3 |
| Language variation affects both modeling and scoring because dialect, orthography, code-switching, morphology, and script complexity shape acoustic coverage, text representation, and metric interpretation. | 3.3 | C-G1; C-G6; GAP-G3; CORE-04; CORE-06; CORE-13; CORE-14; CORE-53 | `javed2023indsuperb`; `shi2023mlsuperb`; `olatunji2023_afrispeech200`; `chen2025mlsuperb2challenge` | Verified-primary-source for cited anchors | Low to medium; orthography evidence should be expanded in Sections 7 and 10 | RQ1; RQ3; RQ6 |
| Dataset presence is not deployment readiness; domain, channel, and benchmark mismatch can invalidate broad claims from nominal language coverage. | 3.4 | C-G1; C-G6; GAP-G2; GAP-G4; CORE-03; CORE-07; CORE-09; CORE-10; CORE-12; CORE-26; CORE-27; CORE-34; CORE-52 | `gales2014_babel_project_research_cued`; `peterson2022_openasr21`; `conneau2022fleurs`; `conneau2022xtreme_s`; `shi2024mlsuperb2`; `ardila2020commonvoice`; `wang2021voxpopuli`; `lau2025_data_quality_multilingual_speech`; `pmlr-v202-radford23a`; `pratap2024mms` | Mostly verified-primary; FLEURS remains verified-secondary in Core 60 and is not sole support | Medium; aggregate foundation-model claims must stay bounded | RQ1; RQ2; RQ3; RQ6 |
| WER/CER are necessary but insufficient; low-resource evaluation should include subgroup, domain, normalization, reproducibility, and cost reporting. | 3.5 | C-G6; GAP-G3; GAP-G4; GAP-G12; CORE-04; CORE-11; CORE-12; CORE-13; CORE-14; CORE-52; BF25 | `shi2023mlsuperb`; `conneau2022xtreme_s`; `conneau2022fleurs`; `javed2023indsuperb`; `olatunji2023_afrispeech200`; `chen2025mlsuperb2challenge`; `lau2025_data_quality_multilingual_speech`; `yang2021superb`; `feng2022superbslt` | Mixed verified-primary and verified-secondary; no watchlist-only central support | Medium; fairness and hallucination details are deferred to Section 10 and Section 11 | RQ1; RQ6 |
| Foundation speech models change the starting point but do not remove resource, language, adaptation, supervision, and evaluation constraints. | 3.1, 3.2, 3.4, 3.6 | C-G2 as bridge; CORE-15; CORE-22; CORE-26; CORE-27 | `baevski2020wav2vec2`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms` | Verified-primary-source | Low | RQ1; RQ2; RQ3; RQ6 |

## Watchlist Use

No watchlist-only paper is used as central support for Section 3. The section does not cite BF21-BF24 or other watchlist-only LLM/contextual ASR sources. Emerging hallucination and LLM-assisted risks are left for Sections 10 and 11.

## Pashto Drift Check

Pashto appears once as an illustrative example of dialect variation, transcript normalization, and script consistency. It is not used as a focused case study and does not determine the section structure.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should continue to point to the Section 3 draft and this evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 5 should expand dataset and benchmark documentation using GAP-G2.
- Section 7 should expand orthography, transcript normalization, and data-quality controls using GAP-G3.
- Section 10 should expand C-G6 with dialect-wise, domain-wise, fairness, robustness, reproducibility, and compute evidence.
- Section 4 should pick up the RQ2 bridge: foundation models change the starting point but do not erase low-resource constraints.
