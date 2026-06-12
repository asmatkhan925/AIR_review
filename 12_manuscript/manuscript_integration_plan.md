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

## Stage 7: Methodology, Front Matter, and Final Polish

After the body is assembled:

- Integrate Section 2 so the review methodology, search protocol, evidence extraction, synthesis controls, and citation verification workflow are clear.
- Revise Section 1 so it previews the assembled argument, six-layer taxonomy, Core 60 evidence backbone, four contributions, and reliability-centered thesis.
- Draft the abstract after Sections 1-14, tables, and figures are stable.
- Harmonize section titles across `main_manuscript.md`, `06_review_outline/master_outline.md`, `06_review_outline/section_argument_map.md`, and Block G controls.
- Check all citation keys against `03_references/references.bib`.
- Run anti-Pashto-drift checks.
- Confirm that LLM-assisted ASR remains visible but bounded.
- Apply Artificial Intelligence Review style and submission checks before LaTeX conversion.
