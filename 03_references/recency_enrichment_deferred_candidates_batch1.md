# Recency Enrichment Deferred Candidates: Batch 1

## Scope

Batch 1 checked all P1 verified-primary candidates and all 2026 candidates in the recency matrix. Four P1 candidates were already present in BibTeX and required no new entry. Nine 2026 candidates were deferred because their currently verified source is arXiv-only.

## Already Present, Not Deferred

| Candidate | Existing key | Status |
|---|---|---|
| REC-001, ML-SUPERB 2.0 Challenge | `chen2025mlsuperb2challenge` | Verified-primary-source; already in BibTeX |
| REC-002, multilingual speech dataset quality audit | `lau2025_data_quality_multilingual_speech` | Verified-primary-source; already in BibTeX |
| REC-005, Kanyen'keha foundation-model evaluation | `geng25c_interspeech` | Verified-primary-source; already in BibTeX |
| REC-006, OpusLM | `tian25b_interspeech` | Verified-primary-source; already in BibTeX |

## Deferred Candidates

| Candidate | Current source status | Reason for deferral | Verification still needed | Emerging-direction use |
|---|---|---|---|---|
| REC-051, Qwen3-ASR Technical Report | Watchlist-ArXiv | Technical report without a verified accepted venue | Official publisher or proceedings version; independent benchmark audit | Sections 11 and 13 only |
| REC-053, LoASR-Bench | Watchlist-ArXiv; already in BibTeX | Preprint benchmark with unsettled protocol maturity | Accepted venue, stable benchmark release, and external uptake | Sections 11 and 13 only |
| REC-054, ReHear | Watchlist-ArXiv; already in BibTeX | Audio-LLM pseudo-label refinement remains preprint evidence | Accepted venue and stronger hallucination/leakage analysis | Sections 9, 11, and 13 only |
| REC-055, West Frisian LLM correction study | Watchlist-ArXiv | Single-language preprint and contamination-sensitive result | Accepted venue and full contamination/source-grounding review | Sections 11 and 13 only |
| REC-056, Responsible Benchmarking of Fairness for ASR | Watchlist-ArXiv | Very recent fairness proposal without verified venue | Accepted venue and stable evaluation framework | Sections 10 and 13 only |
| REC-057, Beyond Single Ground Truth | Watchlist-ArXiv | Conceptual and empirical scope not yet peer reviewed | Accepted venue and full review of multiple-reference evaluation | Sections 10 and 13 only |
| REC-058, SN-WER | Watchlist-ArXiv | New script-normalized metric without independent validation | Accepted venue, implementation, and cross-dataset validation | Sections 10 and 13 only |
| REC-059, GC-LoRA | Watchlist-ArXiv | Very recent PEFT preprint | Accepted venue, matched compute baselines, and robustness evidence | Sections 8 and 13 only |
| REC-060, SBPN Nigerian-language KD | Watchlist-ArXiv | Regional KD preprint with unresolved benchmark maturity | Accepted venue, dataset details, and reproducibility artifacts | Sections 9, 10, and 13 only |

## Deferral Rule

Deferred candidates remain useful for monitoring emerging directions, but they must not be the sole support for central manuscript claims. A future batch may add them as watchlist BibTeX entries only when a concrete manuscript need exists and their source identity is stable; peer-reviewed status must not be implied without an official venue page.
