# Manuscript Integration Readiness Report

## 1. Current Repository State

- Current branch: `main`
- Source state: after commit `4269b06` (`Audit 2025-2026 recency coverage`)
- Scope and RQs: ready; canonical source remains `01_scope_and_planning/research_questions.md`
- Main manuscript state: Abstract and Sections 1-14 have been assembled into `12_manuscript/main_manuscript.md`; global flow/compression and formal QA audit passes have been completed
- LaTeX workspace state: `12_manuscript/latex/main.tex` and `main_double_column_preview.tex` are now synchronized from the audited Markdown manuscript; both compile to PDF; `references.bib` synced from `03_references/references.bib`
- Final QA report: `12_manuscript/final_quality_audit_report.md`
- LaTeX formatting report: `12_manuscript/latex/latex_formatting_readiness_report.md`
- Recency audit: `03_references/recency_enrichment_plan_2025_2026.md`, `05_synthesis_matrices/recent_2025_2026_evidence_candidates.csv`, and `05_synthesis_matrices/recent_2025_2026_gap_summary.md`
- Next evidence phase: extract and synthesize the 26 batch-1 additions before adding manuscript citations; author department, Declarations metadata, and flat-package work remain separate submission tasks

This report is a metadata and readiness snapshot after the formal QA audit and the
LaTeX-workspace synchronization. It does not add literature, alter RQs, change
contributions, or modify Core 60, references, Block G, or synthesis matrices.

## 1a. LaTeX Workspace Synchronization

- `12_manuscript/latex/main.tex`: synchronized from `12_manuscript/main_manuscript.md`
  (single-column `sn-basic`); old placeholder section prose replaced with the audited
  Abstract and Sections 1-14; Markdown `[@...]` citations converted to `\citep{...}`.
- `12_manuscript/latex/main_double_column_preview.tex`: same content with the `iicol`
  preview option and full-width spanning floats; for layout inspection only.
- `12_manuscript/latex/references.bib`: synced from `03_references/references.bib`
  at commit `d60bf38` (93 entries; 0 duplicate keys; 78 cited keys; 0 undefined).
  The canonical bibliography now has 119 entries after batch 1 and LaTeX resynchronization
  is intentionally deferred until manuscript citation integration.
- Figures 1-4 are real `figure` environments using the PDF previews in
  `09_figures/previews/`. Tables 1-6 are real `tabularx` tables generated from the
  `08_tables/` source files; table numbering is counter-pinned to the registry.
- Compile status: `main.tex` PASS (56 pages); preview PASS (45 pages).
- Conversion is reproducible via `scripts/sync_manuscript_latex.py`.
- Details and blockers: `12_manuscript/latex/latex_formatting_readiness_report.md`.
- Outstanding metadata blockers (do not invent): author department/`\orgdiv` and the
  Declarations block (funding, conflict of interest, data availability, author
  contributions, ethics). Final submission readiness is NOT claimed.
- Final submission-package flattening (flat folder, no subfolders, flat figure copies,
  compiled PDF) remains a separate next task.

## 1b. 2025-2026 Recency Audit

- Current BibTeX library: 119 entries, including 33 from 2025 and 3 from 2026.
- Current Markdown manuscript: 76 unique citation keys, including 7 from 2025 and none from 2026.
- Candidate layer: 60 records; batch 1 added 26 verified-primary BibTeX entries and deferred nine 2026 arXiv watchlist candidates.
- Citation-verification log: 186 rows with no duplicate or empty citation keys.
- The batch does not change the manuscript, synchronized LaTeX, Core 60, tables, figures, or existing non-recency synthesis matrices.
- Highest-priority enrichment areas are Sections 8-11: recent PEFT, pseudo-label/KD reliability, dialect/fairness/hallucination evaluation, AVSR, and bounded LLM-assisted ASR.
- Existing repository year anomalies for older SeamlessM4T PEFT and S2-LoRA preprints are documented in the recency plan and are not propagated into the new candidate matrix.

## 2. Evidence-Control Readiness

| Evidence control | Status | Assembly implication |
|---|---|---|
| Locked RQs and scope | Ready | Preserve the field-level, taxonomy-based review framing. |
| Core 60 reference set | Ready; verify 60 rows during validation | Use Core 60 as the main evidence backbone for manuscript claims. |
| Citation verification | Batch 1 ready; 186 rows and no duplicate keys | Do not cite newly added keys until claim-level extraction is complete. |
| 2025-2026 recency candidate layer | 26 verified-primary additions; 9 deferred 2026 watchlist candidates | Extract official-source evidence into the appropriate matrices before manuscript integration. |
| Block G synthesis layer | Ready | Use Block G claims, taxonomy rows, section-to-evidence mapping, and gap controls as synthesis scaffolding. |
| Evidence-to-claim matrix | Ready | Check each assembled claim against existing evidence controls. |
| Section drafts | Integrated; global compression and cross-section harmonization completed | Preserve companion evidence notes outside the manuscript body and use formal QA before journal formatting. |

## 3. Draft Section Inventory

| Section | Draft file | Evidence notes | Readiness |
|---|---|---|---|
| Abstract | `07_draft_sections/00_abstract.md` | Not separate | Written in `main_manuscript.md`; trimmed to 245 words for target-journal abstract guidance and copied back to the draft file for consistency. |
| 1. Introduction | `07_draft_sections/01_introduction.md` | Not separate | Assembled into `main_manuscript.md`; previews the full Sections 2-14 argument and locked four contributions. |
| 2. Review Methodology and Search Protocol | `07_draft_sections/02_review_methodology_search_protocol.md` | Yes | Assembled into `main_manuscript.md`; framed as a structured critical review with systematic mapping elements. |
| 3. What Makes ASR Low-Resource? | `07_draft_sections/03_what_makes_asr_low_resource.md` | Yes | Assembled into `main_manuscript.md`; globally polished for flow and compression. |
| 4. From Hybrid ASR to Foundation Speech Models | `07_draft_sections/04_from_hybrid_asr_to_foundation_speech_models.md` | Yes | Assembled into `main_manuscript.md`; globally polished for transition and repetition control. |
| 5. Resources and Benchmarks | `07_draft_sections/05_resources_and_benchmarks_for_low_resource_asr.md` | Yes | Assembled into `main_manuscript.md`; Table 2 callout connected. |
| 6. Foundation-Model-Era Taxonomy of Low-Resource ASR | `07_draft_sections/06_foundation_model_era_taxonomy.md` | Yes | Assembled into `main_manuscript.md`; Figure 2 and Table 1 callouts connected. |
| 7. Data-Centric Strategies in the Foundation-Model Era | `07_draft_sections/07_data_centric_strategies_foundation_model_era.md` | Yes | Assembled into `main_manuscript.md`; globally polished for transition consistency. |
| 8. Adaptation Strategies for Low-Resource ASR | `07_draft_sections/08_adaptation_strategies_low_resource_asr.md` | Yes | Assembled into `main_manuscript.md`; Table 3 callout connected. |
| 9. Pseudo-Labeling and Knowledge Distillation | `07_draft_sections/09_pseudo_labeling_kd_low_resource_asr.md` | Yes | Assembled into `main_manuscript.md`; Table 4 callout connected. |
| 10. Evaluation, Reproducibility, and Robustness | `07_draft_sections/10_evaluation_reproducibility_robustness.md` | Yes | Assembled into `main_manuscript.md`; Table 5 callout connected. |
| 11. Multimodal, AVSR, and LLM-Assisted ASR | `07_draft_sections/11_multimodal_avsr_llm_assisted_asr.md` | Yes | Assembled into `main_manuscript.md`; LLM-assisted ASR kept bounded and risk-aware. |
| 12. Cross-Block Synthesis and Gap Analysis | `07_draft_sections/12_cross_block_synthesis_gap_analysis.md` | Yes | Assembled into `main_manuscript.md`; Figure 3 callout connected. |
| 13. Future Research Agenda | `07_draft_sections/13_future_research_agenda.md` | Yes | Assembled into `main_manuscript.md`; Figure 4 and Table 6 callouts connected. |
| 14. Conclusion | `07_draft_sections/14_conclusion.md` | Yes | Assembled into `main_manuscript.md`; no new citation keys introduced. |

Older method-by-method draft files remain source material only and should not steer final manuscript structure.

## 4. Table Readiness

Tables are ready for manuscript-level review. Final numbering is controlled by `08_tables/table_registry.md`. Table 1, Table 2, Table 3, Table 4, Table 5, and Table 6 are now callout-linked in the assembled Sections 5-13.

| Table | Source file | Status |
|---|---|---|
| Table 1 | `08_tables/table_01_low_resource_asr_taxonomy.md` | Drafted, manuscript-facing. |
| Table 2 | `08_tables/table_02_dataset_benchmark_comparison.md` | Drafted, manuscript-facing. |
| Table 3 | `08_tables/table_03_adaptation_strategy_decision_matrix.md` | Drafted, manuscript-facing. |
| Table 4 | `08_tables/table_04_pseudo_labeling_kd_reliability_matrix.md` | Drafted, manuscript-facing. |
| Table 5 | `08_tables/table_05_evaluation_robustness_checklist.md` | Drafted, manuscript-facing. |
| Table 6 | `08_tables/table_06_future_agenda_reporting_checklist.md` | Drafted, manuscript-facing. |

Legacy table drafts remain in `08_tables/` and are documented in `08_tables/table_registry.md`. They should not determine final numbering.

## 5. Figure Readiness

Figures are ready for manuscript-level review. Final numbering is controlled by `09_figures/figure_registry.md`. Figure 1, Figure 2, Figure 3, and Figure 4 are now callout-linked in the assembled Sections 3, 6, 12, and 13.

| Figure | Source files | Status |
|---|---|---|
| Figure 1 | `09_figures/figure_01_bottleneck_stack.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 2 | `09_figures/figure_02_six_layer_taxonomy.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 3 | `09_figures/figure_03_cross_block_evidence_flow.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 4 | `09_figures/figure_04_future_agenda_map.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |

Older `09_figures/fig_01_*` through `fig_06_*` folders remain legacy placeholders or source ideas only.

## 6. Completed and Next Assembly Batches

Completed manuscript assembly batches:

1. Abstract.
2. Section 1: Introduction.
3. Section 2: Review Methodology and Search Protocol.
4. Section 3: What Makes ASR Low-Resource?
5. Section 4: From Hybrid ASR to Foundation Speech Models.
6. Section 5: Resources and Benchmarks.
7. Section 6: Foundation-Model-Era Taxonomy of Low-Resource ASR.
8. Section 7: Data-Centric Strategies in the Foundation-Model Era.
9. Section 8: Adaptation Strategies for Low-Resource ASR.
10. Section 9: Pseudo-Labeling and Knowledge Distillation.
11. Section 10: Evaluation, Reproducibility, and Robustness.
12. Section 11: Multimodal, AVSR, and LLM-Assisted ASR.
13. Section 12: Cross-Block Synthesis and Gap Analysis.
14. Section 13: Future Research Agenda.
15. Section 14: Conclusion.

16. LaTeX-workspace synchronization from the audited manuscript (`main.tex`,
    `main_double_column_preview.tex`, `references.bib`); both sources compile.

Recommended next evidence and manuscript batch:

1. Extract the 26 batch-1 additions into the relevant model, adaptation, pseudo-label/KD, dataset, evaluation, and evidence-to-claim matrices.
2. Select only claim-relevant additions for Sections 4, 5, 7, 8, 9, 10, 11, and 13.
3. Expand Tables 2-5 where the new evidence materially changes comparison or reporting guidance.
4. Add manuscript citations selectively, then resynchronize LaTeX and its bibliography.
5. Recheck the nine deferred 2026 watchlist candidates for accepted venue versions.
6. Complete author department/`\orgdiv` and the Declarations block (do not invent).
7. Build the flat AIR submission package and run final proofread/submission-package QA.

Rationale: The abstract and Sections 1-14 establish the full first manuscript assembly,
the formal QA audit passed, and the LaTeX workspace is synchronized and compiling.
Batch 1 strengthens the canonical bibliography, but citation dumping would weaken the
review. The next step is controlled extraction and synthesis before manuscript changes.

## 7. Remaining Risks Before Journal Formatting

- Final word count should be checked against the selected journal template.
- Citation balance should be reviewed for over-dense paragraphs and under-supported claims.
- Only 7 unique 2025 references and no 2026 references are currently cited in the Markdown manuscript.
- Recent evidence must be added by claim need; arXiv watchlist papers must not carry central claims.
- The canonical and LaTeX-local bibliographies now differ intentionally until the next manuscript/LaTeX synchronization.
- Deferred 2026 papers must remain watchlist-only unless official venue versions are verified.
- Table and figure placement should be checked after journal formatting.
- Cross-reference consistency for Figure 1-Figure 4 and Table 1-Table 6 must be checked after formatting/export.
- Title/abstract/introduction/body alignment should be checked during proofread.
- Anti-Pashto drift and bounded LLM-assisted ASR claims should be rechecked during final proofread.
- Figures and tables should continue to be introduced as argumentative aids, not decorative inserts.
- LLM-assisted ASR must remain bounded to correction, rescoring, contextual biasing, post-ASR normalization, and speech-LLM systems with hallucination, over-correction, leakage, bias, compute, and reproducibility safeguards.
- Pashto must remain illustrative only, not a focused case-study contribution.
- Do not add new RQs, a fifth contribution, unverified citations, or unsupported performance claims during formatting or proofread.
