# Core 60 Reference Selection Report

Source snapshot: AIR_review handoff ZIP, commit `27adadb60f2b804299ce2357baf55e671d8a505a`, validation `PASS`.

## Selection rule

The Core 60 were selected from the 66 unique strong candidates in Blocks A-F. A reference was eligible when it was marked `Core-citable` or `High-value-citable`, had relevance >= 4, and was not watchlist-only or needs-primary-source-verification. Six eligible candidates were demoted because they were redundant, narrower than the field-level backbone, or better treated as supporting evidence.

## Distribution by primary block

- A framing/datasets/benchmarks: 14
- B foundation models: 16
- C data-centric: 6
- D adaptation: 7
- E pseudo-labeling/KD: 8
- F evaluation/robustness: 9

## Verification mix

- Verified-primary-source: 42
- Verified-secondary-source: 18

## BibTeX readiness

- Present in `references.bib`: 53
- Need BibTeX addition/confirmation before manuscript citation: 7

Missing BibTeX entries among Core 60:
- CORE-01 `BA01`: Automatic speech recognition for under-resourced languages: A survey — suggested key `besacier2014_underresourced_asr_survey`
- CORE-07 `BA10`: Data Quality Issues in Multilingual Speech Datasets: The Need for Sociolinguistic Awareness and Proactive Language Planning — suggested key `lau2025_data_quality_multilingual_speech`
- CORE-09 `BA13`: Speech recognition and keyword spotting for low-resource languages: Babel project research at CUED — suggested key `gales2014_babel_project_research_cued`
- CORE-10 `BA15`: OpenASR21: The Second Open Challenge for Automatic Speech Recognition of Low-Resource Languages — suggested key `peterson2022_openasr21`
- CORE-14 `BA21`: AfriSpeech-200: Pan-African Accented Speech Dataset for Clinical and General Domain ASR — suggested key `olatunji2023_afrispeech200`
- CORE-18 `BB05`: W2v-BERT: Combining Contrastive Learning and Masked Language Modeling for Self-Supervised Speech Pre-Training — suggested key `citation_block_b_04`
- CORE-28 `BB17`: Joint speech and text machine translation for up to 100 languages — suggested key `citation_block_b_19`

## Use policy

- Use Core 60 papers as the main backbone for claims, section framing, and synthesis tables.
- Use demoted candidates as supporting/background references when a section needs additional breadth.
- Use watchlist papers only for emerging directions, especially LLM-assisted correction/rescoring, contextual ASR, hallucination, speech-LLM systems, and 2026 benchmark signals.
- Do not use watchlist/arXiv-only papers as sole evidence for strong claims.

## Recommended repository update

Add these files to `05_synthesis_matrices/`:

- `core_60_reference_set.csv`
- `supporting_demotions_from_candidate_pool.csv`
- `core_60_bibtex_gap_report.csv`
- `priority_watchlist_for_llm_and_emerging_directions.csv`

Add this report as:

- `05_synthesis_matrices/core_60_selection_report.md`
