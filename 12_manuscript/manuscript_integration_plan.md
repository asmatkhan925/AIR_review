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

Figure 1, Figure 2, Table 1, Table 2, Table 3, and Table 4 are now callout-linked in the assembled Sections 3-9. Figure 3 remains deferred, likely for Section 12 after Sections 10-11 are assembled. Figure 4 and Tables 5-6 should remain unused until their corresponding later sections are integrated.

Insert tables and figures only when the corresponding manuscript section has been assembled and the local paragraph can introduce the asset as an argumentative aid. Use the registries to preserve final numbering, captions, and callouts.

## Stage 3: Second Body Assembly Batch

Status: completed. Sections 7-9 have been assembled into `12_manuscript/main_manuscript.md`.

Integrated Sections 7-9:

1. Integrate Section 7 on data-centric strategies.
2. Integrate Section 8 on adaptation strategies.
3. Integrate Section 9 on pseudo-labeling and KD.

Table 3 and Table 4 are callout-linked in Sections 8 and 9. Figure 3 was not inserted in this batch because the cross-block evidence-flow figure is better motivated after Sections 10-11 are assembled and can likely be placed in Section 12.

## Stage 4: Next Body Assembly Batch

Next integrate:

1. Integrate Section 10 on evaluation, reproducibility, and robustness.
2. Integrate Section 11 on multimodal, AVSR, SpeechLM, and LLM-assisted ASR.

Then continue with:

3. Integrate Section 12 as cross-block synthesis and gap analysis.
4. Integrate Section 13 as the future research agenda.
5. Integrate Section 14 as the conclusion.

Section 11 must keep LLM-assisted ASR bounded and risk-aware. It should distinguish post-ASR correction, rescoring, contextual biasing, post-ASR normalization, and speech-LLM systems from mature low-resource ASR solutions, and it should preserve safeguards around hallucination, over-correction, benchmark leakage, language bias, compute, and reproducibility.

Section 13 should include LLM-assisted ASR as part of the future agenda, not as a standalone new contribution. The locked contribution count remains four.

## Stage 5: Front Matter and Final Polish

After the body is assembled:

- Revise Section 1 so it previews the assembled argument, six-layer taxonomy, Core 60 evidence backbone, four contributions, and reliability-centered thesis.
- Draft the abstract after Sections 1-14, tables, and figures are stable.
- Harmonize section titles across `main_manuscript.md`, `06_review_outline/master_outline.md`, `06_review_outline/section_argument_map.md`, and Block G controls.
- Check all citation keys against `03_references/references.bib`.
- Run anti-Pashto-drift checks.
- Confirm that LLM-assisted ASR remains visible but bounded.
- Apply Artificial Intelligence Review style and submission checks before LaTeX conversion.
