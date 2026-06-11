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
