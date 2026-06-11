# Evidence Notes For Section 3: What Makes ASR Low-Resource?

## Scope

This companion note records the evidence used in `07_draft_sections/03_what_makes_asr_low_resource.md`. It is intended to keep the Section 3 draft traceable to the Core 60 reference layer, seed-paper map, evidence-to-claim matrix, and evaluation matrices.

## Claim Map

| Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping |
|---|---|---|---|---|---|---|
| Low-resource ASR cannot be reduced to labeled-hour counts; it is shaped by resource quality, validation, language variation, and evaluation design. | 3.1 | CORE-01 / BA01; CORE-09 / BA13; CORE-10 / BA15; C5 | `besacier2014_underresourced_asr_survey`; `gales2014_babel_project_research_cued`; `peterson2022_openasr21` | Verified-primary-source | Low for CORE-01, CORE-09, CORE-10 | RQ1; RQ3; RQ6 |
| Modern shared tasks and multilingual benchmarks treat low-resource ASR as a benchmark-design and coverage problem, not only a training-data problem. | 3.1, 3.4, 3.5 | CORE-04 / BA07 / BF01; CORE-05 / BA08; CORE-06 / BA09; CORE-12 / BA17 / BF03 | `shi2023mlsuperb`; `shi2024mlsuperb2`; `chen2025mlsuperb2challenge`; `conneau2022xtreme_s` | Verified-primary-source | Low | RQ1; RQ2; RQ6 |
| Labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal resources serve different roles and carry different reliability risks. | 3.2 | Locked taxonomy; CORE-08 / BA11; CORE-15 to CORE-22 / Block B; C-C4; C-E1 | `mohamed2022_ssl_review`; `baevski2020wav2vec2`; `hsu2021hubert`; `chen2022wavlm`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms` | Mixed: mostly verified-primary; HuBERT and WavLM are marked verified-secondary/source-pending in Core 60 | Low to medium; secondary entries are used with primary anchors, not as sole support | RQ1; RQ2; RQ3; RQ5 |
| Public multilingual corpora increase language coverage but require validation, metadata, and quality auditing before supporting strong low-resource claims. | 3.2, 3.4 | CORE-03 / BA04 / BC03; CORE-07 / BA10; BC04; BC05; C7; C-C3 | `ardila2020commonvoice`; `wang2021voxpopuli`; `lau2025_data_quality_multilingual_speech` | Verified-primary-source | Low for Core 60 records used here | RQ1; RQ3; RQ6 |
| FLEURS, ML-SUPERB, XTREME-S, IndicSUPERB, AfriSpeech-200, and ML-SUPERB 2.0 show why multilingual evaluation must track language coverage, variety, and benchmark constraints. | 3.3, 3.4, 3.5 | CORE-04 / BA07; CORE-05 / BA08; CORE-06 / BA09; CORE-12 / BA17 / BF03; CORE-13 / BA18; CORE-14 / BA21; CORE-52 / BF02 | `conneau2022fleurs`; `shi2023mlsuperb`; `shi2024mlsuperb2`; `chen2025mlsuperb2challenge`; `conneau2022xtreme_s`; `javed2023indsuperb`; `olatunji2023_afrispeech200` | Mixed: most verified-primary; FLEURS Core 60 row is verified-secondary and medium risk | FLEURS is not used as sole support for strong claims; it is corroborated by primary benchmark anchors | RQ1; RQ3; RQ6 |
| Language conditions such as dialect variation, orthography, code-switching, morphology, and script complexity affect both model behavior and metric interpretation. | 3.3, 3.5 | RQ1 locked scope; C5; C-F1; C-F2; C-F4; CORE-06 / BA09; CORE-13 / BA18; CORE-14 / BA21 | `chen2025mlsuperb2challenge`; `javed2023indsuperb`; `olatunji2023_afrispeech200` | Verified-primary-source for cited Core 60 anchors | Low; orthography/normalization claim also depends on matrix-level synthesis and should be expanded later in Sections 7 and 10 | RQ1; RQ3; RQ6 |
| Domain and channel mismatch make read speech, broadcast speech, telephony, conversational speech, web audio, and weak supervision non-interchangeable. | 3.4 | CORE-09 / BA13; CORE-10 / BA15; CORE-03 / BA04; CORE-07 / BA10; C5; C7; C-C1; C-C3 | `gales2014_babel_project_research_cued`; `peterson2022_openasr21`; `ardila2020commonvoice`; `wang2021voxpopuli`; `lau2025_data_quality_multilingual_speech` | Verified-primary-source | Low | RQ1; RQ3; RQ6 |
| Foundation models improve the starting point for low-resource ASR but still require target-language adaptation, validation, transcript normalization, and fair evaluation. | 3.1, 3.2, 3.4, 3.6 | CORE-15 / BB02; CORE-16 / BB03; CORE-22 / BB09; CORE-26 / BB14; CORE-27 / BB16; CORE-28 / BB17; C1; C8; C9; C-D1 | `baevski2020wav2vec2`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `seamless2025_joint_speech_text_mt` | Verified-primary-source | Low to medium; SeamlessM4T is translation-centric and used only as speech-text foundation-model context | RQ1; RQ2; RQ3; RQ6 |
| Pooled WER/CER can hide dialect, domain, demographic, orthographic, and benchmark weaknesses, so low-resource evaluation must report more than aggregate scores. | 3.5 | C-F1; C-F2; C-F4; CORE-04 / BF01; CORE-12 / BF03; CORE-14 / BA21; BF09/BF10 matrix evidence | `shi2023mlsuperb`; `conneau2022xtreme_s`; `olatunji2023_afrispeech200`; `chen2025mlsuperb2challenge` | Core citations are verified-primary; BF09/BF10 are matrix support and not cited directly in this draft | Low for cited anchors; fairness-specific evidence should be expanded in Section 10 | RQ1; RQ6 |
| Reproducibility, compute, and deployment constraints are part of low-resource evaluation because strong models may be hard to adapt or deploy. | 3.5 | CORE-11 / BA16; BF25; C-F5; C-F8 | `yang2021superb`; `feng2022superbslt` | SUPERB verified-primary; BF25 verified-secondary-source with accepted-workshop indication | Low to medium; compute-efficiency point is supporting evidence, not a standalone performance claim | RQ1; RQ4; RQ6 |

## Watchlist Use

The Section 3 draft does not use watchlist-only papers as sole support for strong claims. Watchlist themes such as LLM-assisted correction, hallucination, contextual ASR, and current 2025-2026 frontier benchmarks are mentioned only as evaluation implications or future-facing risks when needed. The section does not cite BF21-BF24 or other watchlist-only items directly.

## Pashto Drift Check

Pashto appears only once as an illustrative example of dialect variation, transcript normalization, and script consistency. It is not used as a central case-study contribution and does not determine the section structure.

## Open Follow-Up Items

- Section 7 should later expand the transcript-normalization and formatting evidence beyond the short Section 3 framing.
- Section 10 should later expand the WER/CER, demographic fairness, and dialect-wise evaluation evidence with full Block F support.
- If the manuscript requires a table, Section 3 can be paired with a compact taxonomy table mapping resource, language, domain/channel, and evaluation conditions to evidence rows.
