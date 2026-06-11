# Manuscript Integration Plan

## Stage 1: Methodology and Front Matter

- Review and polish Section 2 from `07_draft_sections/02_review_methodology_search_protocol.md` and its traceability notes, checking it against `01_scope_and_planning/review_methodology.md`, `01_scope_and_planning/inclusion_exclusion_criteria.md`, search logs, screening logs, citation verification records, Core 60 controls, and the handoff validation workflow.
- Revise Section 1 after the body is stable so the introduction previews the final six-layer taxonomy, Core 60 evidence backbone, four contributions, and reliability-centered thesis.
- Draft the abstract only after Sections 1-14 are assembled and the table/figure set is known.

## Stage 2: Tables and Figures

Prioritize these assets before full assembly:

1. Six-layer taxonomy figure.
2. Low-resource ASR bottleneck stack.
3. Dataset/benchmark comparison table.
4. Adaptation strategy decision matrix.
5. Pseudo-labeling/KD reliability matrix.
6. Evaluation and robustness checklist.
7. Future agenda/reporting checklist.

Use `05_synthesis_matrices/block_g_table_figure_plan.csv` as the control file, then update `08_tables/` and `09_figures/` so the final assets match the manuscript sections rather than the older method-by-method structure.

First draft assets created for review:

- `08_tables/table_01_low_resource_asr_taxonomy.md`
- `08_tables/table_02_dataset_benchmark_comparison.md`
- `08_tables/table_03_adaptation_strategy_decision_matrix.md`
- `08_tables/table_04_pseudo_labeling_kd_reliability_matrix.md`
- `08_tables/table_05_evaluation_robustness_checklist.md`
- `08_tables/table_06_future_agenda_reporting_checklist.md`
- `08_tables/table_figure_creation_notes.md`
- `09_figures/figure_01_bottleneck_stack_spec.md`
- `09_figures/figure_02_six_layer_taxonomy_spec.md`
- `09_figures/figure_03_cross_block_evidence_flow_spec.md`
- `09_figures/figure_04_future_agenda_map_spec.md`
- `09_figures/figure_01_bottleneck_stack.svg`
- `09_figures/figure_02_six_layer_taxonomy.svg`
- `09_figures/figure_03_cross_block_evidence_flow.svg`
- `09_figures/figure_04_future_agenda_map.svg`
- `09_figures/previews/figure_01_bottleneck_stack.png`
- `09_figures/previews/figure_02_six_layer_taxonomy.png`
- `09_figures/previews/figure_03_cross_block_evidence_flow.png`
- `09_figures/previews/figure_04_future_agenda_map.png`
- `09_figures/previews/figure_01_bottleneck_stack.pdf`
- `09_figures/previews/figure_02_six_layer_taxonomy.pdf`
- `09_figures/previews/figure_03_cross_block_evidence_flow.pdf`
- `09_figures/previews/figure_04_future_agenda_map.pdf`
- `09_figures/figure_captions_and_alt_text.md`

Tables 1-6 now require final captions, numbering checks, and cross-reference insertion when the relevant manuscript sections are assembled.
Figure captions and cross-references should be inserted during manuscript assembly, not now. The preview exports are for review and layout checking; the editable SVG files remain the source assets.

## Stage 3: Main Manuscript Assembly

- Assemble Sections 3-14 into `12_manuscript/main_manuscript.md` in order, replacing pointer TODOs one section at a time.
- Keep companion evidence notes in `07_draft_sections/` and do not paste them into the manuscript body.
- After each section is inserted, check cited keys against `03_references/references.bib`, verify that claims remain supported by the relevant matrix rows, and update `00_project_management/decision_log.md` only for material integration decisions.
- Preserve traceability by leaving draft-section filenames and evidence-note filenames in integration comments or assembly notes until final cleanup.

## Stage 4: Consistency and Journal Polish

- Harmonize section titles across `main_manuscript.md`, `master_outline.md`, `section_argument_map.md`, and Block G controls.
- Standardize terminology for foundation speech models, speech-language models, LLM-assisted ASR, AVSR, pseudo-labeling, KD, and low-resource conditions.
- Check all contribution statements against the locked four-contribution structure.
- Run anti-Pashto-drift checks so illustrative examples do not become a case-study contribution.
- Balance citation density, especially in synthesis and conclusion sections.
- Check figure and table callouts, captions, and matrix traceability.
- Apply the Artificial Intelligence Review style checklist before LaTeX conversion and journal-format checks.
