# Decision Log

| Date | Decision | Rationale | Implication |
|---|---|---|---|
| 2026-06-10 | Freeze Block F evaluation robustness evidence map | Block F now has conservative safeguards for LLM correction, compute-efficiency evidence, AVSR source status, demographic fairness evidence, and toolkit-only reproducibility support | Do not add new Block F literature unless a reviewer-level evidence gap appears; use BF24 only as watchlist-current emerging evidence and BF25 only for compute/generalization/efficiency support |
| 2026-06-10 | Refine Block F evaluation robustness evidence map | Block F needed stronger compute/efficiency support and a concrete LLM-based ASR correction paper | BF25 adds compute-efficiency evaluation support; BF24 now uses ASR Error Correction using Large Language Models; BF16 is high-value secondary AVSR evidence |
| 2026-06-10 | Start Block F evaluation and robustness evidence map | RQ6 requires a critical evaluation layer covering metrics, multilingual benchmarks, robustness, fairness, reproducibility, multimodal/AVSR extension, and LLM-assisted evaluation risks | Block F evidence must separate verified benchmark and robustness anchors from watchlist LLM, hallucination, and contextual-ASR items |
| 2026-06-10 | Freeze Block E pseudo-labeling and distillation evidence map | Block E now separates verified ASR pseudo-labeling/KD anchors, high-value secondary evidence, original IPL background, and LLM/SpeechLLM watchlist items with overclaiming controls | Do not add more Block E papers unless a reviewer-level RQ5 gap appears; next evidence block is Block F on evaluation, robustness, fairness, reproducibility, compute cost, multimodal robustness, AVSR, and LLM-assisted evaluation risks |
| 2026-06-10 | Refine Block E pseudo-labeling evidence classifications | Block E needed stricter separation between primary anchors, secondary high-value evidence, original IPL method background, and LLM/SpeechLLM watchlist items | BE03 and BE05 are high-value secondary-verified anchors; BE21 is added as original IPL background; BE17-BE20 remain watchlist-current only |
| 2026-06-10 | Start Block E evidence map | Pseudo-labeling, self-training, and knowledge distillation directly answer RQ5 and support the paper's third contribution | Core evidence must distinguish verified ASR pseudo-labeling/KD papers from watchlist LLM/SpeechLLM pseudo-label refinement papers |
| 2026-06-10 | Confirm Blocks A-D frozen and move to Block E | Final sanity checks confirmed BD16-BD20 remain watchlist-only, BD21-BD23 are verified primary ASR adaptation anchors, BC12 is upgraded to verified primary, and the required BibTeX and claim links are present | Stop expanding Blocks A-D unless a reviewer-level gap appears; next evidence block is pseudo-labeling, self-training, and knowledge distillation |
| 2026-06-10 | Post-freeze Block D refinement | Add three verified Interspeech 2024 adaptation anchors before final manuscript use | BD21 continued pretraining, BD22 adapter pre-training, and BD23 forgetting-aware new-language adaptation strengthen Block D with primary ASR-specific evidence |
| 2026-06-10 | Freeze Block D adaptation strategy seed map | Block D now separates PEFT method anchors, ASR-specific support, SpeechLM/future-facing adaptation, Block E bridge evidence, and watchlist-current preprints | Do not add more Block D papers unless a reviewer-level adaptation gap appears; next evidence block should be Block E pseudo-labeling, self-training, and knowledge distillation |
| 2026-06-09 | Freeze Block C data-centric low-resource ASR seed map | Block C now has verified core anchors, high-value support, watchlist separation, and C-C1 through C-C6 evidence-to-claim integration | Do not add more Block C papers unless a reviewer-level gap appears; next evidence block should be Block D adaptation strategies |
| 2026-06-09 | Supersede focused Pashto case-study framing with illustrative-only Pashto use | Aligns the repository with the locked field-level review scope | Pashto may appear only as an illustrative example for broader low-resource ASR issues, not as a contribution or organizing section. |
| 2026-05-06 | Superseded: Treat Pashto ASR as a focused case study rather than the whole review topic | This earlier framing kept the article broad but still gave Pashto too much structural weight | Superseded by the 2026-06-09 locked RQs: Pashto may be used only as an illustrative example, not as a focused case-study contribution |
| 2026-06-08 | Add a review control system for weekly planning, claim evidence, citation verification, and anti-thesis-drift checks | The review needs disciplined synthesis controls to remain suitable for Artificial Intelligence Review | Major claims must be tracked in the evidence-to-claim matrix; citation details must be verified before manuscript use; Pashto-heavy material must be reframed as case evidence |

## Future Decisions To Record

- Final title.
- Review date range.
- Whether to include preprints.
- Whether to use a systematic review diagram.
- Final table and figure set.

## Core 60 reference backbone added

Added a Core 60 reference-control layer under `05_synthesis_matrices/` to support high-quality, field-level synthesis for the AIR review. The Core 60 set was selected from Blocks A-F using conservative criteria: core/high-value use level, high relevance, verified-primary or verified-secondary status, and exclusion of watchlist-only papers from central claims.

Added files:
- `core_60_reference_set.csv`
- `supporting_demotions_from_candidate_pool.csv`
- `core_60_bibtex_gap_report.csv`
- `priority_watchlist_for_llm_and_emerging_directions.csv`
- `core_60_selection_report.md`

Use policy: Core 60 references should carry the main manuscript claims. Supporting demotions may be used for additional context. Watchlist items should be used only for emerging directions, especially LLM-assisted ASR, hallucination, contextual ASR, and 2025-2026 frontier work. Seven Core 60 entries still require BibTeX addition or confirmation before manuscript citation.

## Core 60 BibTeX gaps resolved

Resolved the seven remaining Core 60 BibTeX gaps using primary publisher, DOI, ACL Anthology, ISCA Archive, IEEE/ASRU, and Nature metadata where applicable. The Core 60 gap report is now header-only; BB05 and BB17 placeholder citation keys were replaced with `chung2021_w2vbert` and `seamless2025_joint_speech_text_mt`, and AfriSpeech-200 is consistently treated as a TACL 2023 source for the Core 60 layer.

## Section 3 evidence-grounded draft created

Created the first evidence-grounded draft of Section 3, `07_draft_sections/03_what_makes_asr_low_resource.md`, with companion evidence notes in `07_draft_sections/03_what_makes_asr_low_resource_evidence_notes.md`. The draft defines low-resource ASR as a multidimensional resource, language, domain/channel, and evaluation condition grounded in Core 60 and verified matrix evidence; Pashto remains illustrative only.

## Block G cross-block synthesis layer added

Added Block G as the cross-block synthesis layer, not as another raw literature-search block. New files under `05_synthesis_matrices/` map the six-layer taxonomy, core synthesis claims, research gaps, manuscript sections, table/figure plan, and additional resource candidates. The companion blueprint in `06_review_outline/block_g_synthesis_blueprint.md` states that future drafting should use Block G plus Core 60 as the manuscript synthesis backbone while preserving watchlist and verification safeguards.

## Section 3 revised using Block G controls

Revised `07_draft_sections/03_what_makes_asr_low_resource.md` using Block G as the synthesis-control layer, especially C-G1, C-G6, and the Section 3 control row. The section remains a draft pending final integration into `12_manuscript/main_manuscript.md`; the manuscript file continues to point to the draft and evidence-notes files rather than containing the full section.

## Section 4 drafted from Block B and Block G controls

Drafted `07_draft_sections/04_from_hybrid_asr_to_foundation_speech_models.md` with companion evidence notes using Block B, Core 60, the foundation-model matrix, and Block G claim C-G2 as the synthesis-control layer. The draft remains outside `12_manuscript/main_manuscript.md` pending review and final integration.

## Section 5 drafted from resource and benchmark controls

Drafted `07_draft_sections/05_resources_and_benchmarks_for_low_resource_asr.md` with companion evidence notes using the dataset/benchmark, data-centric, evaluation, Core 60, and Block G controls. The section remains a draft pending review and final integration into `12_manuscript/main_manuscript.md`.

## Section 6 drafted as foundation-model-era taxonomy

Drafted `07_draft_sections/06_foundation_model_era_taxonomy.md` with companion evidence notes using Block G as the taxonomy-control layer. Updated only the Section 6 heading and planning text in the manuscript and outline files so Section 6 now functions as the formal six-layer taxonomy section rather than a model-centric methods section.

## Section 7 drafted from data-centric evidence controls

Drafted `07_draft_sections/07_data_centric_strategies_foundation_model_era.md` with companion evidence notes using Block C, dataset/benchmark evidence, Core 60, and Block G controls. The section answers RQ3 by treating data-centric work as reliability control for foundation-model-era low-resource ASR rather than as a dataset catalog.

## Section 8 drafted from adaptation evidence controls

Drafted `07_draft_sections/08_adaptation_strategies_low_resource_asr.md` with companion evidence notes using the adaptation matrix, Core 60, foundation-model evidence, and Block G controls. The section answers RQ4 by framing adaptation effectiveness as conditional on target-language data, domain mismatch, language relatedness, compute, evaluation design, and forgetting risk.
