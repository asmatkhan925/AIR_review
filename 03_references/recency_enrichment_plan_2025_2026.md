# 2025-2026 Recency Enrichment Plan

## Purpose

This audit defines a controlled path for strengthening the review's 2025-2026 evidence without changing the manuscript, BibTeX library, or citation-verification log in the current commit. It is a planning layer, not a claim that every candidate should be cited.

The review should retain its established evidence backbone while adding recent work only after bibliographic identity, venue status, relevance, and claim fit have been checked. Peer-reviewed and official proceedings sources should carry central claims. ArXiv-only work should remain watchlist evidence for emerging directions.

## Current Reference Distribution

`03_references/references.bib` currently contains 93 entries.

| Year | BibTeX entries |
|---|---:|
| 2011 | 1 |
| 2014 | 2 |
| 2015 | 2 |
| 2018 | 3 |
| 2019 | 5 |
| 2020 | 11 |
| 2021 | 12 |
| 2022 | 19 |
| 2023 | 14 |
| 2024 | 14 |
| 2025 | 8 |
| 2026 | 2 |

The library is strongest from 2020 through 2024. Only 10 of 93 entries are dated 2025-2026, which is too thin for a review explicitly framed around the foundation-model era.

## Current Manuscript Citation Distribution

The Markdown manuscript uses 76 unique citation keys.

| Year | Unique cited references |
|---|---:|
| 2011 | 1 |
| 2014 | 2 |
| 2015 | 2 |
| 2018 | 2 |
| 2019 | 5 |
| 2020 | 10 |
| 2021 | 10 |
| 2022 | 15 |
| 2023 | 12 |
| 2024 | 10 |
| 2025 | 7 |
| 2026 | 0 |

The seven cited 2025 keys are concentrated in inclusive benchmarking, dataset quality, SeamlessM4T, low-resource foundation-model evaluation, OpusLM, hallucination benchmarking, and contextual ASR. No 2026 reference is currently cited in the Markdown manuscript.

## Coverage Weaknesses

1. **Recent model coverage is narrow.** OWSM v4, AfriHuBERT, Omnilingual ASR, newer audio-language models, and recent open multilingual ASR systems are not yet represented consistently in the citation backbone.
2. **Adaptation evidence is dated relative to the manuscript framing.** The manuscript discusses adapters, LoRA, QLoRA, prompting, and compute-efficient adaptation, but recent ASR-specific evidence is underrepresented.
3. **Pseudo-labeling and KD need current reliability evidence.** Recent work on multi-ASR fusion, SpeechLLM correction, filtering, semi-supervised domain adaptation, and contemporary KD is not yet integrated.
4. **Evaluation needs stronger 2025-2026 support.** Dialect-aware scoring, accent robustness, contextual ASR, hallucination, script normalization, fairness, and non-monolithic ground truth are fast-moving areas.
5. **Multimodal coverage is historically anchored.** Recent AVSR challenges, datasets, and efficiency methods should be screened before Section 11 is considered current.
6. **Recent regional case studies are not balanced.** The review needs verified examples spanning Indigenous North America, Africa, the Middle East, South Asia, Europe, and code-switching settings without allowing any one language to become central.
7. **The current repository contains recency-label anomalies.** At least two existing adaptation records appear to assign 2025 to older arXiv work: the SeamlessM4T PEFT paper is arXiv:2410.04442 and S2-LoRA is arXiv:2312.06713. They are excluded from the 2025-2026 candidate matrix pending later source-data correction.
8. **Several repository 2026 watchlist identifiers are unresolved or mismatched.** They are not promoted into the candidate matrix unless an official page can be matched to the title.

## Improvement Targets

These are screening targets, not automatic citation quotas.

| Control | Current | Target after verification and integration |
|---|---:|---:|
| BibTeX entries dated 2025 | 8 | 20-25 |
| BibTeX entries dated 2026 | 2 | 6-10 |
| Unique manuscript citations dated 2025 | 7 | 15-20 |
| Unique manuscript citations dated 2026 | 0 | 3-6 |
| Recent verified-primary anchors | Limited and concentrated | At least 3 per major evidence area where suitable sources exist |
| ArXiv-only sources carrying central claims | Must remain zero | Zero |

Recent citations should be distributed by evidential need rather than inserted uniformly. Sections 8-11 require the largest increase. Sections 3, 6, 12, and 14 should change only if a recent source materially improves an existing claim.

## Priority Themes

1. Omnilingual and massively multilingual ASR.
2. OWSM v4 and other reproducible open Whisper-style models.
3. ML-SUPERB 2.0, code-switching datasets, dialect-aware benchmarks, and inclusive evaluation.
4. Low-resource SpeechLM and speech-LLM ASR.
5. LLM-assisted ASR correction, contextual biasing, and rescoring.
6. Hallucination, unsupported-content, and over-correction evaluation.
7. Pseudo-labeling, self-training, and KD reliability.
8. ASR-specific PEFT, adapters, prompt tuning, LoRA, AdaLoRA, and evidence gaps around QLoRA.
9. Dialect, accent, domain, script, and code-switching evaluation.
10. AVSR, multimodal data, missing-modality robustness, and efficient audiovisual modeling.
11. Low-resource case studies from multiple regions and language families.
12. Reproducibility, compute efficiency, and practical data-selection controls.

## Candidate Source Categories

| Source category | Intended use |
|---|---|
| Official conference or journal page | Eligible for primary-source verification and central or high-value support after full-text review |
| Official challenge or benchmark paper | Benchmark design, coverage, limitations, and evaluation protocol |
| Official dataset paper | Resource coverage, metadata, licensing, domain, dialect, and benchmark claims |
| Official model paper | Model capability and limitation claims bounded to reported tasks |
| ArXiv preprint | Watchlist and future-facing discussion only until venue status and evidence are verified |
| Repository record with unresolved source | Discovery queue only; no BibTeX or manuscript use |

## Verification Policy

1. Match the exact title, author list, year, venue, and DOI or official URL.
2. Prefer official publisher, ACL Anthology, ISCA Archive, IEEE, journal, challenge, or DOI pages.
3. Do not use GitHub raw URLs as bibliographic evidence.
4. Treat arXiv-only work as `Watchlist-ArXiv`, even when the abstract reports acceptance, until the official venue page is located.
5. Use `Verified-secondary-source` only when a reliable indexing or institutional page confirms identity but the primary publication page is unavailable.
6. Use `Needs-primary-source-verification` when title identity is plausible but venue, date, authors, or identifier is unresolved.
7. Verify task boundaries. ASR, speech translation, spoken dialogue, speech understanding, correction, and normalization are not interchangeable.
8. Verify claim scope. A single language, accent, disorder, or domain can illustrate a mechanism but cannot carry a field-wide claim alone.
9. Record limitations before adding a paper to the evidence-to-claim matrix.
10. Add BibTeX only after deduplication against existing keys and after deciding whether the source is central, supporting, or watchlist evidence.

## Recommended Next Commit Sequence

1. **Verify priority 1 candidate metadata.** Confirm official pages, full author lists, venue status, DOI, and publication year for the highest-value model, adaptation, supervision, evaluation, and AVSR candidates.
2. **Add verified BibTeX entries.** Add only verified candidates to `03_references/references.bib`; keep arXiv-only entries explicitly marked as watchlist if they are needed for future-facing discussion.
3. **Update citation verification.** Add or revise rows in `03_references/citation_verification_log.csv`, including source type, status, main use, and limitations.
4. **Extend synthesis matrices.** Add verified records to the appropriate model, adaptation, pseudo-labeling/KD, dataset, and evaluation matrices. Do not duplicate the same paper under inconsistent IDs.
5. **Update claims and tables.** Strengthen Tables 2-6 and the evidence-to-claim matrix before editing prose.
6. **Integrate manuscript citations selectively.** Add recent evidence to Sections 4, 5, 8, 9, 10, 11, and 13. Preserve the existing argument and avoid citation dumping.
7. **Resynchronize LaTeX.** Only after Markdown and BibTeX changes pass citation validation.
