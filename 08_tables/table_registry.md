# Table Registry

This registry controls final manuscript-facing table numbering for the AIR review. Legacy table drafts remain source material and should not determine final numbering.

## Manuscript-Facing Tables

| Table number | Source file | Target section(s) | Primary RQ(s) | Main purpose | Status | Production notes |
|---|---|---|---|---|---|---|
| Table 1 | `08_tables/table_01_low_resource_asr_taxonomy.md` | Sections 3 and 6; supports Section 12 | RQ1-RQ6 | Compact taxonomy of low-resource ASR conditions and evidence layers. | Draft table ready for manuscript review. | Check final caption, callout, and row compression during assembly. |
| Table 2 | `08_tables/table_02_dataset_benchmark_comparison.md` | Section 5 | RQ1; RQ3; RQ6 | Compare dataset and benchmark properties that affect what low-resource ASR claims can prove. | Draft table ready for manuscript review. | Keep dataset limitations and normalization caveats visible. |
| Table 3 | `08_tables/table_03_adaptation_strategy_decision_matrix.md` | Section 8 | RQ4 | Compare adaptation strategies by data condition, compute, transfer assumptions, and evaluation risk. | Draft table ready for manuscript review. | Keep PEFT and prompting claims conditional and evidence bounded. |
| Table 4 | `08_tables/table_04_pseudo_labeling_kd_reliability_matrix.md` | Section 9 | RQ5 | Summarize reliability controls for pseudo-labeling and knowledge distillation. | Draft table ready for manuscript review. | Avoid treating pseudo-labels as clean labels; keep teacher quality and filtering explicit. |
| Table 5 | `08_tables/table_05_evaluation_robustness_checklist.md` | Section 10; supports Section 12 | RQ6 | Provide an evaluation, robustness, reproducibility, and compute checklist. | Draft table ready for manuscript review. | Keep LLM-assisted risks as evaluation checks, not mature solution claims. |
| Table 6 | `08_tables/table_06_future_agenda_reporting_checklist.md` | Section 13 | Main RQ; RQ3-RQ6 | Convert the future agenda into reporting and research-design requirements. | Draft table ready for manuscript review. | Align final row labels with GAP-G1 through GAP-G12 during assembly. |

## Legacy or Source-Material Tables

These files are retained as legacy/source material and should not be used as final manuscript numbering unless deliberately revived later:

| Legacy file | Status |
|---|---|
| `08_tables/table_01_taxonomy_of_methods.md` | Legacy/source material; superseded by manuscript-facing Table 1. |
| `08_tables/table_02_low_resource_challenges.md` | Legacy/source material; superseded by manuscript-facing Table 1 and Section 3 synthesis. |
| `08_tables/table_03_datasets_and_languages.md` | Legacy/source material; superseded by manuscript-facing Table 2. |
| `08_tables/table_04_foundation_models.md` | Legacy/source material; use only as background for Section 4 if needed. |
| `08_tables/table_05_transfer_learning_methods.md` | Legacy/source material; superseded by manuscript-facing Table 3. |
| `08_tables/table_06_distillation_methods.md` | Legacy/source material; superseded by manuscript-facing Table 4. |
| `08_tables/table_07_multimodal_asr_methods.md` | Legacy/source material; use cautiously for Section 11 if evidence remains verified and bounded. |
| `08_tables/table_08_research_gaps_future_work.md` | Legacy/source material; superseded by manuscript-facing Table 6 and Block G gap controls. |

## Assembly Rule

Do not delete or rename legacy tables during manuscript assembly. Use this registry plus `09_figures/figure_registry.md` to control final numbering, captions, and callouts.
