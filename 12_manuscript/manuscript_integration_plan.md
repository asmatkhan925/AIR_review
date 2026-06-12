# Manuscript Integration Plan

## Control Files

- Canonical RQs and scope: `01_scope_and_planning/research_questions.md`
- Table numbering and status: `08_tables/table_registry.md`
- Figure numbering and status: `09_figures/figure_registry.md`
- Table/figure notes: `08_tables/table_figure_creation_notes.md`
- Integration readiness report: `12_manuscript/integration_readiness_report.md`
- Manuscript shell: `12_manuscript/main_manuscript.md`

## Stage 1: First Assembly Batch, Sections 3-6

Status: completed. Sections 3-6 have been assembled into `12_manuscript/main_manuscript.md`.

1. Section 3: `07_draft_sections/03_what_makes_asr_low_resource.md`
2. Section 4: `07_draft_sections/04_from_hybrid_asr_to_foundation_speech_models.md`
3. Section 5: `07_draft_sections/05_resources_and_benchmarks_for_low_resource_asr.md`
4. Section 6: `07_draft_sections/06_foundation_model_era_taxonomy.md`

Reason: these sections establish the conceptual and taxonomic base for the rest of the manuscript. They define low-resource ASR beyond labeled hours, explain the foundation-model transition, compare resource and benchmark conditions, and introduce the six-layer taxonomy before later sections discuss data-centric strategies, adaptation, pseudo-labeling/KD, evaluation, multimodal/LLM-assisted ASR, synthesis, and future work. The introduction and abstract should still remain unfixed until the main body is assembled.

## Stage 2: Tables and Figures During Assembly

Polished figures and previews are now available:

- `09_figures/figure_01_bottleneck_stack.svg`
- `09_figures/figure_02_six_layer_taxonomy.svg`
- `09_figures/figure_03_cross_block_evidence_flow.svg`
- `09_figures/figure_04_future_agenda_map.svg`
- PNG previews in `09_figures/previews/`
- PDF previews in `09_figures/previews/`
- Captions and alt text in `09_figures/figure_captions_and_alt_text.md`

Tables 1-6 are also drafted and controlled by `08_tables/table_registry.md`.

Figure 1, Figure 2, Figure 3, Figure 4, Table 1, Table 2, Table 3, Table 4, Table 5, and Table 6 are now callout-linked in the assembled body Sections 3-14.

Insert tables and figures only when the corresponding manuscript section has been assembled and the local paragraph can introduce the asset as an argumentative aid. Use the registries to preserve final numbering, captions, and callouts.

## Stage 3: Second Body Assembly Batch

Status: completed. Sections 7-9 have been assembled into `12_manuscript/main_manuscript.md`.

Integrated Sections 7-9:

1. Integrate Section 7 on data-centric strategies.
2. Integrate Section 8 on adaptation strategies.
3. Integrate Section 9 on pseudo-labeling and KD.

Table 3 and Table 4 are callout-linked in Sections 8 and 9. Figure 3 was not inserted in this batch because the cross-block evidence-flow figure is better motivated after Sections 10-11 are assembled and can likely be placed in Section 12.

## Stage 4: Third Body Assembly Batch

Status: completed. Sections 10-11 have been assembled into `12_manuscript/main_manuscript.md`.

Integrated Sections 10-11:

1. Integrate Section 10 on evaluation, reproducibility, and robustness.
2. Integrate Section 11 on multimodal, AVSR, SpeechLM, and LLM-assisted ASR.

Table 5 is callout-linked in Section 10. Figure 3 was not inserted in this batch and remains deferred to Section 12, where the cross-block evidence-flow argument can be introduced after the full Sections 3-11 body exists. Figure 4 remains deferred to Section 13.

Section 11 keeps LLM-assisted ASR bounded and risk-aware. It distinguishes post-ASR correction, rescoring, contextual biasing, post-ASR normalization, and speech-LLM systems from mature low-resource ASR solutions, and it preserves safeguards around hallucination, over-correction, benchmark leakage, language bias, compute, and reproducibility.

## Stage 5: Cross-Block Synthesis Assembly

Status: completed. Section 12 has been assembled into `12_manuscript/main_manuscript.md`.

Integrated Section 12:

1. Integrate Section 12 as cross-block synthesis and gap analysis.

Figure 3 is callout-linked in Section 12 with the cross-block evidence-flow caption. Figure 4 and Table 6 remain deferred to Section 13.

## Stage 6: Future Agenda and Conclusion Assembly

Status: completed. Sections 13-14 have been assembled into `12_manuscript/main_manuscript.md`.

Integrated Sections 13-14:

1. Integrate Section 13 as the future research agenda.
2. Integrate Section 14 as the conclusion.

Figure 4 and Table 6 are callout-linked in Section 13. Section 13 keeps LLM-assisted ASR as part of the future reliability agenda, not as a standalone new contribution. Section 14 introduces no new citation keys and closes around the locked four contributions and six-layer taxonomy.

## Stage 7: Methodology Assembly

Status: completed. Section 2 has been assembled into `12_manuscript/main_manuscript.md`.

Integrated Section 2:

1. Integrate Section 2 so the review methodology, search protocol, evidence extraction, synthesis controls, and citation verification workflow are clear.

Section 2 frames the article as a structured critical review with systematic mapping elements. It explicitly avoids claiming a complete PRISMA-style systematic review, exhaustive retrieval counts, or equal verification strength for emerging/watchlist evidence.

## Stage 8: Introduction Assembly

Status: completed. Section 1 has been assembled into `12_manuscript/main_manuscript.md`.

Integrated Section 1:

1. Revise Section 1 so it previews the assembled argument, six-layer taxonomy, Core 60 evidence backbone, four contributions, and reliability-centered thesis.

Section 1 frames the paper as a field-level review on low-resource and underrepresented-language ASR in the foundation-model era. It keeps the locked four contributions, avoids Pashto-centered framing, and treats foundation models, AVSR, SpeechLMs, and LLM-assisted ASR as important but reliability-sensitive rather than solved solutions.

## Stage 9: Abstract Assembly

Status: completed. The abstract has been written in `12_manuscript/main_manuscript.md` and copied to `07_draft_sections/00_abstract.md`.

Integrated Abstract:

1. Draft the abstract after Sections 1-14, tables, and figures are stable.

The abstract summarizes the problem, foundation-model-era shift, structured critical review method, six-layer taxonomy, synthesis contributions, and reliability-centered conclusion without adding citations, new RQs, a fifth contribution, or solved-problem claims.

## Stage 10: Global Flow and Compression Pass

Status: completed. A light global flow, compression, citation-density, and cross-reference consistency pass has been applied to `12_manuscript/main_manuscript.md`.

Completed checks and edits:

- Reduced repeated transition language around the foundation-model starting point and the reliability bottleneck.
- Tightened section bridges across Sections 3-5, 10-12, 13, and 14.
- Preserved the cautious methodology framing, locked four contributions, and field-level scope.
- Kept LLM-assisted ASR, SpeechLM, AVSR, and multimodal claims bounded as reliability-sensitive directions.
- Verified that Figure 1-Figure 4 and Table 1-Table 6 callouts remain present exactly once.

## Stage 11: Formal QA Audit

Status: completed. The formal QA audit has been run and documented in `12_manuscript/final_quality_audit_report.md`.

Completed checks and edits:

- Verified Abstract and Sections 1-14 are present and contain no TODO/TBD markers.
- Verified Figure 1-Figure 4 and Table 1-Table 6 callouts appear exactly once.
- Checked citation keys against `03_references/references.bib`; no missing keys or duplicate BibTeX keys were found.
- Re-ran anti-Pashto-drift checks; Pashto appears once as an illustrative example.
- Confirmed LLM-assisted ASR, SpeechLM, AVSR, and multimodal claims remain bounded and risk-aware.
- Removed pre-abstract assembly metadata and project-facing wording from the manuscript.
- Trimmed the abstract to 245 words to fit the recorded target-journal abstract guidance.

## Stage 12: Journal Formatting and Submission-Package QA

Status: in progress. The LaTeX workspace has been synchronized from the audited
manuscript (see Stage 13). Remaining: author metadata, submission-package flattening,
final word-count and proofread checks.

- Plan journal-template formatting/export using the Springer Nature/AIR LaTeX setup.
- Check table and figure placement in the formatted manuscript.
- Verify final word count, title/abstract/body alignment, citation balance, and author-guideline compliance.
- Run a final proofread before submission-package preparation.

## Stage 13: LaTeX Workspace Synchronization

Status: completed. `12_manuscript/latex/main.tex` and
`12_manuscript/latex/main_double_column_preview.tex` have been synchronized from
`12_manuscript/main_manuscript.md`, and `references.bib` was synced from
`03_references/references.bib`.

Completed work:

1. Converted the audited Abstract and Sections 1-14 into Springer Nature LaTeX,
   replacing the old placeholder section prose. The argument is unchanged.
2. Converted Markdown `[@...]` citations to author-year `\citep{...}` (all citations
   are parenthetical; no narrative bare cites exist).
3. Built real `figure` environments for Figures 1-4 using the `09_figures/previews/`
   PDFs and real `tabularx` tables for Tables 1-6 from the `08_tables/` sources, with
   table numbering counter-pinned to `08_tables/table_registry.md`.
4. Kept the preview file content-identical with the `iicol` option and full-width
   spanning floats for layout inspection only.
5. Compiled both sources: `main.pdf` (56 pages) and
   `main_double_column_preview.pdf` (45 pages), with no undefined citations.
6. Made the conversion reproducible via `scripts/sync_manuscript_latex.py`.

Outstanding (do not invent): author department/`\orgdiv` and the Declarations block
(funding, conflict of interest, data availability, author contributions, ethics).
Wide tables (especially Table 2) need final layout adjustment. Final-submission
readiness is not claimed. The flat submission package remains a separate next task;
its plan is recorded in `12_manuscript/latex/latex_formatting_readiness_report.md`.

## Stage 14: 2025-2026 Recency Enrichment Audit

Status: completed as an audit and planning layer. No manuscript, LaTeX, BibTeX,
citation-verification, table, or figure content was changed.

Created:

1. `03_references/recency_enrichment_plan_2025_2026.md`
2. `05_synthesis_matrices/recent_2025_2026_evidence_candidates.csv`
3. `05_synthesis_matrices/recent_2025_2026_gap_summary.md`

Audit findings:

- The BibTeX library has 93 entries: 8 from 2025 and 2 from 2026.
- The Markdown manuscript has 76 unique citations: 7 from 2025 and none from 2026.
- The candidate matrix contains 60 records spanning multilingual models, OWSM v4,
  inclusive benchmarking, SpeechLMs, LLM correction, hallucination, pseudo-label/KD,
  PEFT, dialect/code-switching, AVSR, and regional low-resource cases.
- Official venue sources are separated from arXiv watchlist evidence.
- Older papers mislabeled as 2025 in existing adaptation controls were excluded from
  the recency matrix pending later source-data correction.

## Stage 15: Verify and Integrate Recent Evidence

Status: bibliography and citation-verification batch 1 completed; synthesis and
manuscript integration remain planned.

Completed:

1. Checked all 30 P1 candidates and all ten 2026 candidates.
2. Added 26 verified-primary BibTeX entries: 25 from Interspeech 2025 and one from EACL 2026.
3. Updated and consolidated citation-verification records; final count is 186 rows.
4. Created the batch report, deferred-candidate report, and 26-row verified-additions matrix.
5. Deferred nine 2026 arXiv candidates without promoting their publication status.

## Stage 16: Extract and Integrate Recent Evidence

Status: planned.

1. Read and extract the 26 verified additions into the relevant synthesis matrices.
2. Update the evidence-to-claim matrix before editing prose.
3. Expand Tables 2-5 only where verified evidence materially improves them.
4. Add recent citations selectively to Sections 4, 5, 7, 8, 9, 10, 11, and 13.
5. Keep deferred arXiv papers in future-facing or explicitly watchlisted roles.
6. Resynchronize Markdown and LaTeX only after citation validation passes.
