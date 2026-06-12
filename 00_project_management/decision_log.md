# Decision Log

| Date | Decision | Rationale | Implication |
|---|---|---|---|
| 2026-06-12 | Polish table assets with representative evidence anchors | Tables 1-5 needed compact local citation anchors and Section 13 still needed the future-agenda/reporting checklist table | Tables 1-6 now have representative evidence support or table notes; final manuscript assembly should still check captions, cross-references, and bounded watchlist use |
| 2026-06-12 | Create first table and figure draft assets | Core 60, Block G synthesis controls, and current section drafts now support high-priority manuscript tables and figure specifications | Use the new `08_tables/` drafts and `09_figures/` specifications as review assets before inserting tables or figures into the main manuscript |
| 2026-06-12 | Perform Section 2 methodology micro-audit | The readiness report had stale Section 2 wording, and the screening-log count needed a local traceability check and packaged dependency | Updated the readiness report, kept the screening-log count locally verified, and ensured the handoff packager includes `02_literature_search/screening_log.csv` |
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

## Section 9 drafted from pseudo-labeling and KD evidence controls

Drafted `07_draft_sections/09_pseudo_labeling_kd_low_resource_asr.md` with companion evidence notes using the pseudo-labeling/KD matrix, Core 60, foundation-model evidence, evaluation-risk evidence, and Block G controls. The section answers RQ5 by treating supervision expansion as useful only when teacher quality, filtering, uncertainty, agreement, normalization, and evaluation controls are explicit.

## Section 10 drafted from evaluation and robustness controls

Drafted `07_draft_sections/10_evaluation_reproducibility_robustness.md` with companion evidence notes using the evaluation/robustness matrix, Core 60, Block G controls, and previous Section 7-9 reliability arguments. The section answers RQ6 by treating WER/CER as necessary but insufficient without orthography-aware, subgroup-aware, robustness, reproducibility, compute, hallucination, and contextual evaluation controls.

## Section 11 drafted from multimodal and LLM-assisted controls

Drafted `07_draft_sections/11_multimodal_avsr_llm_assisted_asr.md` with companion evidence notes using multimodal/AVSR, SpeechLM, LLM-assisted, evaluation-risk, Core 60, watchlist, and Block G controls. The section answers the future-facing part of RQ6 by treating multimodal and LLM-assisted ASR as promising but reliability-sensitive directions that require source grounding, task-boundary clarity, hallucination and over-correction checks, modality-mismatch controls, reproducibility, and compute reporting.

## Section 12 drafted as cross-block synthesis and gap analysis

Drafted `07_draft_sections/12_cross_block_synthesis_gap_analysis.md` with companion evidence notes using Block G, Core 60, Sections 3-11, and Blocks A-F. The section answers the main review question by synthesizing C-G1-C-G8 and GAP-G1-GAP-G12 around cross-layer reliability: foundation models change the starting point of low-resource ASR, but reliable progress still depends on resource documentation, language fit, adaptation comparability, supervision reliability, evaluation, robustness, reproducibility, compute, and bounded multimodal or LLM-assisted use.

## Section 13 drafted as future research agenda

Drafted `07_draft_sections/13_future_research_agenda.md` with companion evidence notes using Section 12, Block G, Core 60, gap clusters, and bounded methodological/watchlist support. The section uses C-G8 as the main agenda backbone and converts GAP-G1-GAP-G12 into priorities for low-resource definitions, dataset documentation, orthography-aware and dialect-aware benchmarks, compute-efficient adaptation, reliable pseudo-labeling and KD, evaluation beyond aggregate WER/CER, multimodal robustness, constrained LLM assistance, reproducibility, and deployment transparency.

## Section 14 drafted as conclusion

Drafted `07_draft_sections/14_conclusion.md` with companion evidence notes using Sections 12-13, Block G, Core 60, and the locked four-contribution structure. The conclusion answers the main review question by closing on the claim that foundation speech models changed the starting point of low-resource ASR, but reliable recognition still depends on cross-layer alignment across resources, language conditions, adaptation, supervision, evaluation, reproducibility, compute transparency, multimodal robustness, and bounded LLM-assisted use.

## Integration readiness and line-ending hygiene pass completed

Performed a pre-assembly integration-readiness pass after Sections 3-14 were drafted. Added `.gitattributes` and renormalized repository text files to resolve the line-ending-only dirty working tree, then created `12_manuscript/integration_readiness_report.md` and `12_manuscript/manuscript_integration_plan.md` to document section readiness, evidence controls, title alignment, table/figure placeholders, remaining assembly work, and risks before full manuscript integration.

## Section 2 drafted as structured critical review methodology

Drafted `07_draft_sections/02_review_methodology_search_protocol.md` with companion traceability notes using local review-methodology files, inclusion/exclusion criteria, search and screening logs, citation verification records, Core 60, evidence matrices, and Block G controls. The section frames the paper as a structured critical review with systematic mapping elements rather than a fully exhaustive PRISMA-style systematic review.

## First editable SVG figure drafts created

Created first editable SVG draft sources for Figures 1-4 from the approved figure specifications and Block G controls. The figure set now covers the bottleneck stack, six-layer taxonomy, cross-block evidence flow, and future agenda map. Captions and alt text are tracked in `09_figures/figure_captions_and_alt_text.md`; the SVGs are draft visual assets that still require final journal-style polish before manuscript assembly.

## SVG figure drafts polished and preview exports created

Polished the first editable SVG drafts for Figures 1-4 to improve readability, typography, connector clarity, and cross-figure visual consistency without changing claims, evidence, citations, Core 60, Block G, or manuscript content. Created PNG and PDF previews under `09_figures/previews/` for review; the editable SVG files remain the source assets.

## Post-figure status cleanup and manuscript assembly readiness

Date: 2026-06-12
Commit context: after `994029a` (`Polish SVG figures and add previews`)

Decision:
Figures 1-4 are now the active manuscript-facing visual assets, with editable SVG sources and PNG/PDF previews available under `09_figures/`. Table and figure registries now control final manuscript numbering: `08_tables/table_registry.md` for Tables 1-6 and `09_figures/figure_registry.md` for Figures 1-4. The next phase is manuscript assembly, beginning with Sections 3-6.

Rationale:
The evidence controls, section drafts, manuscript-facing tables, and polished figure drafts are sufficiently mature to begin integration. The main risk has shifted from asset creation to manuscript-level integration, redundancy control, citation consistency, table/figure callout placement, and cross-section flow.

Constraints:
No new RQs, no fifth contribution, no Pashto-centered drift, no unverified citations, and no claims that LLMs solve low-resource ASR.

## Assemble manuscript Sections 3-6

Date: 2026-06-12
Starting commit: `57887cb` (`Update post-figure integration status`)

Decision:
Assembled Sections 3-6 into `12_manuscript/main_manuscript.md` using the existing section drafts as the source base. Figure 1, Figure 2, Table 1, and Table 2 were connected through manuscript callout placeholders and captions rather than embedding binary figure content or large table bodies.

Files changed:
`12_manuscript/main_manuscript.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Sections 3-6 establish the conceptual and taxonomic base for the review before the manuscript turns to data-centric strategies, adaptation, pseudo-labeling/KD, evaluation, multimodal/LLM-assisted ASR, synthesis, and future agenda sections.

Constraints preserved:
No new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no unverified citation keys, and no claims that LLM-assisted ASR solves low-resource ASR.

Next step:
Assemble Sections 7-9, then recheck compression, citation consistency, and cross-section transitions.

## Assemble manuscript Sections 7-9

Date: 2026-06-12
Starting commit: `0e3dba2` (`Assemble manuscript sections 3-6`)

Decision:
Assembled Sections 7-9 into `12_manuscript/main_manuscript.md` using the existing section drafts and companion evidence notes as the source base. Table 3 and Table 4 were connected through manuscript callout placeholders and captions. Figure 3 was deferred because the cross-block evidence-flow figure is better placed after Sections 10-11 are assembled, likely in Section 12.

Files changed:
`12_manuscript/main_manuscript.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Sections 7-9 develop the data-centric, adaptation, and supervision layers that follow the Section 6 taxonomy. They establish why corpus validation, normalization, filtering, adaptation strategy choice, pseudo-label reliability, and KD controls remain necessary in the foundation-model era.

Constraints preserved:
No new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no unverified citation keys, no new synthesis-matrix or reference edits, and no claims that LLM-assisted ASR solves low-resource ASR.

Next step:
Assemble Sections 10-11, then recheck transition consistency, citation density, Figure 3 placement, and bounded treatment of multimodal, SpeechLM, and LLM-assisted ASR.

## Assemble manuscript Sections 10-11

Date: 2026-06-12
Starting commit: `2f7aa84` (`Assemble manuscript sections 7-9`)

Decision:
Assembled Sections 10-11 into `12_manuscript/main_manuscript.md` using the existing section drafts and companion evidence notes as the source base. Table 5 was connected through a manuscript callout placeholder and caption. Figure 3 was deferred to Section 12, and Figure 4 was deferred to Section 13.

Files changed:
`12_manuscript/main_manuscript.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Sections 10-11 complete the evaluation, reproducibility, robustness, multimodal/AVSR, SpeechLM, and bounded LLM-assisted ASR layers needed before cross-block synthesis. The integrated prose strengthens RQ6 while preserving the field-level review framing and separating established evidence from emerging/watchlist directions.

Constraints preserved:
No new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no unverified citation keys, no reference or synthesis-matrix edits, no figure asset edits, and no claims that AVSR, SpeechLMs, or LLM-assisted ASR solve low-resource ASR.

Next step:
Assemble Section 12 as cross-block synthesis and gap analysis, then assemble Sections 13-14 and recheck citation density, compression, figure placement, and bounded LLM-assisted ASR framing.

## Assemble manuscript Section 12

Date: 2026-06-12
Starting commit: `3fa5db0` (`Assemble manuscript sections 10-11`)

Decision:
Assembled Section 12 into `12_manuscript/main_manuscript.md` using the existing Section 12 draft, companion evidence notes, and Block G synthesis controls as the source base. Figure 3 was connected through the requested manuscript callout placeholder and caption. Figure 4 and Table 6 remain deferred to Section 13.

Files changed:
`12_manuscript/main_manuscript.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Section 12 synthesizes the resource, language, model, adaptation, supervision, evaluation, robustness, multimodal/AVSR, SpeechLM, and bounded LLM-assisted ASR layers developed across Sections 3-11. The assembled prose frames low-resource ASR as a reliability problem shaped by cross-layer interactions rather than as either a labeled-hours shortage or a solved foundation-model transfer problem.

Constraints preserved:
No new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no unverified citation keys, no reference or synthesis-matrix edits, no figure asset edits, no Figure 4 or Table 6 insertion, and no claims that foundation models, AVSR, SpeechLMs, or LLM-assisted ASR solve low-resource ASR.

Next step:
Assemble Sections 13-14, then recheck transition consistency, citation density, compression, Figure 4 and Table 6 placement, and bounded LLM-assisted ASR framing in the future agenda.

## Assemble manuscript Sections 13-14

Date: 2026-06-12
Starting commit: `76a120f` (`Assemble manuscript section 12`)

Decision:
Assembled Sections 13-14 into `12_manuscript/main_manuscript.md` using the existing future-agenda and conclusion drafts, companion evidence notes, Block G gap controls, and manuscript-facing figure/table registries as the source base. Figure 4 and Table 6 were connected through manuscript callout placeholders and concise captions.

Files changed:
`12_manuscript/main_manuscript.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Sections 13-14 complete the main body assembly from Sections 3-14. Section 13 converts the cross-block gap synthesis into a reliability-centered future agenda covering definitions, documentation, benchmarks, adaptation, pseudo-labeling and KD, robustness, reproducibility, compute transparency, multimodal/AVSR directions, and bounded LLM-assisted ASR safeguards. Section 14 answers the locked main review question and closes around the four contributions and six-layer taxonomy.

Constraints preserved:
No new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no unverified citation keys, no reference or synthesis-matrix edits, no figure asset edits, no table source edits, and no claims that foundation models, AVSR, SpeechLMs, or LLM-assisted ASR solve low-resource ASR.

Next step:
Assemble Section 2 methodology/search protocol, then revise the introduction and abstract after the full body, figures, and tables are stable. Final polish should check global flow, citation density, cross-reference consistency, table/figure placement, and compression.

## Assemble manuscript Section 2

Date: 2026-06-12
Starting commit: `a3a6abc` (`Assemble manuscript sections 13-14`)

Decision:
Assembled Section 2 into `12_manuscript/main_manuscript.md` using the existing methodology draft, traceability notes, search/screening logs, verification controls, Core 60 controls, seed map, evidence-to-claim matrix, and section-to-evidence map as the source base. The section frames the review as a structured critical review with systematic mapping elements and explicitly avoids claiming a complete PRISMA-style systematic review or exhaustive retrieval count. `01_scope_and_planning/review_methodology.md` was lightly aligned to remove stale TBD language.

Files changed:
`12_manuscript/main_manuscript.md`, `01_scope_and_planning/review_methodology.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Section 2 now explains the review design, locked RQs, search sources, eligibility boundaries, screening and verification workflow, evidence classification, data extraction, synthesis controls, and methodological limitations. The prose strengthens review-journal credibility while remaining transparent about non-exhaustiveness, partial screening counts, broad discovery rows, variable verification status, and watchlist/preprint limits.

Constraints preserved:
No new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no new citation keys, no reference or synthesis-matrix edits, no figure or table source edits, no PRISMA-style retrieval claim, and no equal evidential weighting of verified-primary, verified-secondary, watchlist, and background-support sources.

Next step:
Revise the Introduction after Sections 2-14 are stable. Write the Abstract last, after the introduction and final body flow are checked for accuracy, citation density, cross-reference consistency, and compression.

## Assemble manuscript Section 1

Date: 2026-06-12
Starting commit: `e70740b` (`Assemble manuscript section 2`)

Decision:
Assembled Section 1 into `12_manuscript/main_manuscript.md` using the existing introduction draft, abstract draft for awareness only, locked RQs, contribution statement, review scope, methodology controls, and the assembled Sections 2-14 argument as the source base. The abstract remains a placeholder and was not drafted or finalized.

Files changed:
`12_manuscript/main_manuscript.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
Section 1 now opens the manuscript around uneven ASR progress, the foundation-model-era shift, persistent low-resource bottlenecks, the need for a new review, the locked main review question and six supporting RQs, the four contribution claims, the structured critical-review method, and the manuscript organization. The prose previews the full Sections 2-14 body while preserving the field-level Artificial Intelligence Review framing.

Constraints preserved:
No abstract drafting, no new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no reference or synthesis-matrix edits, no figure or table source edits, no claims that foundation models solve low-resource ASR, and no overstatement of AVSR, SpeechLMs, or LLM-assisted ASR.

Next step:
Write the Abstract based on the now-assembled Sections 1-14. Final polish should then check global flow, citation density, cross-reference consistency, table/figure placement, compression, and abstract accuracy.

## Write manuscript Abstract

Date: 2026-06-12
Starting commit: `7965ae7` (`Assemble manuscript section 1`)

Decision:
Wrote the manuscript abstract in `12_manuscript/main_manuscript.md` after Sections 1-14 were assembled. Replaced the older planning notes in `07_draft_sections/00_abstract.md` with the same final abstract and a short status note.

Files changed:
`12_manuscript/main_manuscript.md`, `07_draft_sections/00_abstract.md`, `12_manuscript/integration_readiness_report.md`, `12_manuscript/manuscript_integration_plan.md`, and `00_project_management/decision_log.md`.

Rationale:
The abstract now reflects the assembled manuscript: low-resource ASR remains unreliable despite foundation-model progress; the review is a structured critical review with systematic mapping elements; the paper contributes a six-layer taxonomy, synthesis of resources/models/adaptation/supervision/evaluation, and a reliability-centered future agenda. The abstract avoids citations and does not introduce claims beyond the assembled Sections 1-14.

Constraints preserved:
No section rewrites, no title change, no new RQs, no fifth contribution, no new literature, no Pashto-centered drift, no reference or synthesis-matrix edits, no figure or table edits, no PRISMA-style systematic-review claim, and no claims that foundation models, AVSR, SpeechLMs, or LLM-assisted ASR solve low-resource ASR.

Next step:
Run a global flow, compression, citation-density, and cross-reference consistency pass. Remaining risks include overall length, transition smoothness, figure/table placement consistency, title/abstract alignment, anti-Pashto drift, and bounded LLM-assisted ASR claims.
