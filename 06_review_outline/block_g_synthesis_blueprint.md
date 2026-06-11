# Block G Synthesis Blueprint

## 1. Purpose of Block G

Block G converts Blocks A-F into the review paper's synthesis layer. It is not a new literature-search block. Its role is to organize the completed evidence into the six-layer taxonomy, cross-block claims, research gaps, manuscript section mapping, and figure/table plan that will guide drafting.

## 2. Cross-Block Argument

Foundation models changed the starting point of low-resource ASR, but reliable recognition still depends on resource quality, language fit, adaptation, supervision reliability, evaluation design, reproducibility, compute, and robustness. The review should therefore argue from interacting conditions rather than from model families alone.

## 3. Claim Architecture

- C-G1: Low-resource ASR is multidimensional and cannot be reduced to labeled hours. Supported by Core 60 low-resource framing, corpus, benchmark, and evaluation anchors.
- C-G2: Foundation speech models improve the starting point but shift the bottleneck toward adaptation, data quality, and evaluation. Supported by SSL, multilingual, weakly supervised, and speech-text foundation model evidence.
- C-G3: Data-centric strategies remain necessary because corpus quality, filtering, normalization, metadata, and validation shape downstream behavior. Supported by Block C and dataset-quality evidence.
- C-G4: Adaptation effectiveness is conditional on target-language data, domain mismatch, language relatedness, compute budget, and forgetting risk. Supported by Block D.
- C-G5: Pseudo-labeling and KD expand supervision but depend on teacher quality, uncertainty filtering, teacher agreement, and mismatch. Supported by Block E.
- C-G6: Pooled WER/CER is insufficient because it can hide dialect, domain, orthographic, demographic, and hallucination-related failures. Supported by Block F and benchmark/fairness evidence.
- C-G7: Multimodal, AVSR, SpeechLM, and LLM-assisted ASR are promising but introduce new evaluation risks. Supported by Core AVSR and multimodal entries plus watchlist-only evidence used cautiously.
- C-G8: The field needs a reproducible future agenda around transparent datasets, dialect-aware benchmarks, compute-efficient adaptation, constrained LLM correction/rescoring, multimodal robustness, and community-aware resource development.

## 4. Section Writing Order

Recommended manuscript writing order:

1. Section 3: What Makes ASR Low-Resource?
2. Section 4: From Hybrid ASR to Foundation Speech Models
3. Section 5: Resources and Benchmarks
4. Section 7: Data-Centric Strategies
5. Section 8: Adaptation Strategies
6. Section 9: Pseudo-Labeling and Knowledge Distillation
7. Section 10: Evaluation Practice and Robustness
8. Section 11: Multimodal, AVSR, and LLM-Assisted ASR
9. Section 12: Cross-Block Synthesis and Gap Analysis
10. Section 13: Future Research Agenda
11. Then revise the Introduction, Abstract, and Conclusion.

## 5. Table and Figure Plan

Figures:

- FIG-G1: Foundation-model-era low-resource ASR bottleneck stack.
- FIG-G2: Six-layer taxonomy of low-resource ASR.
- FIG-G3: Evidence flow from resources to adaptation to evaluation.
- FIG-G4: Future agenda map for reliable low-resource ASR.

Tables:

- TABLE-G1: Low-resource ASR challenge taxonomy.
- TABLE-G2: Dataset and benchmark comparison table.
- TABLE-G3: Foundation model comparison table.
- TABLE-G4: Data-centric strategy comparison table.
- TABLE-G5: Adaptation strategy decision matrix.
- TABLE-G6: Pseudo-labeling and KD reliability matrix.
- TABLE-G7: Evaluation and robustness gap matrix.
- TABLE-G8: LLM-assisted ASR opportunities and risks.
- TABLE-G9: Future research agenda with near-term and long-term priorities.

## 6. Evidence Risk Controls

- Core 60 supports central claims.
- Verified-primary sources should carry strong claims.
- Verified-secondary sources can support claims but should be phrased carefully.
- Watchlist and arXiv-only sources can be used only for emerging directions or risk framing.
- Documentation-support sources in `block_g_additional_resource_candidates.csv` are methodological support, not ASR evidence.
- Pashto remains illustrative only and should not structure the review.

## 7. Next Drafting Step

Draft Section 3, "What Makes ASR Low-Resource?", only after Block G validation passes. Use `block_g_cross_block_taxonomy_synthesis_matrix.csv`, `block_g_core_claim_synthesis_map.csv`, and the Core 60 reference set as the synthesis backbone.
