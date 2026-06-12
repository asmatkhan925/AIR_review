# Manuscript Integration Readiness Report

## 1. Current Repository State

- Current branch: `main`
- Post-figure source state: after commit `994029a` (`Polish SVG figures and add previews`)
- Scope and RQs: ready; canonical source remains `01_scope_and_planning/research_questions.md`
- Main manuscript state: not yet fully assembled; `12_manuscript/main_manuscript.md` remains a section-pointer shell
- Next phase: manuscript assembly, beginning with Sections 3-6

This report is a metadata and readiness snapshot. It does not assemble manuscript sections, add literature, alter RQs, change contributions, or modify Core 60, references, Block G, or synthesis matrices.

## 2. Evidence-Control Readiness

| Evidence control | Status | Assembly implication |
|---|---|---|
| Locked RQs and scope | Ready | Preserve the field-level, taxonomy-based review framing. |
| Core 60 reference set | Ready; verify 60 rows during validation | Use Core 60 as the main evidence backbone for manuscript claims. |
| Citation verification | Ready; verify duplicate BibTeX keys during validation | Do not cite unverified keys during assembly. |
| Block G synthesis layer | Ready | Use Block G claims, taxonomy rows, section-to-evidence mapping, and gap controls as synthesis scaffolding. |
| Evidence-to-claim matrix | Ready | Check each assembled claim against existing evidence controls. |
| Section drafts | Ready for integration; still need compression and cross-section harmonization | Integrate one section at a time and preserve companion evidence notes outside the manuscript body. |

## 3. Draft Section Inventory

| Section | Draft file | Evidence notes | Readiness |
|---|---|---|---|
| 1. Introduction | `07_draft_sections/01_introduction.md` | Not separate | Revise after body sections are assembled. |
| 2. Review Methodology and Search Protocol | `07_draft_sections/02_review_methodology_search_protocol.md` | Yes | Ready for review and integration. |
| 3. What Makes ASR Low-Resource? | `07_draft_sections/03_what_makes_asr_low_resource.md` | Yes | Ready for first assembly batch. |
| 4. From Hybrid ASR to Foundation Speech Models | `07_draft_sections/04_from_hybrid_asr_to_foundation_speech_models.md` | Yes | Ready for first assembly batch. |
| 5. Resources and Benchmarks | `07_draft_sections/05_resources_and_benchmarks_for_low_resource_asr.md` | Yes | Ready for first assembly batch. |
| 6. Foundation-Model-Era Taxonomy of Low-Resource ASR | `07_draft_sections/06_foundation_model_era_taxonomy.md` | Yes | Ready for first assembly batch. |
| 7. Data-Centric Strategies in the Foundation-Model Era | `07_draft_sections/07_data_centric_strategies_foundation_model_era.md` | Yes | Ready after Sections 3-6 are integrated. |
| 8. Adaptation Strategies for Low-Resource ASR | `07_draft_sections/08_adaptation_strategies_low_resource_asr.md` | Yes | Ready after conceptual/taxonomy base is assembled. |
| 9. Pseudo-Labeling and Knowledge Distillation | `07_draft_sections/09_pseudo_labeling_kd_low_resource_asr.md` | Yes | Ready after adaptation framing is assembled. |
| 10. Evaluation, Reproducibility, and Robustness | `07_draft_sections/10_evaluation_reproducibility_robustness.md` | Yes | Ready after Sections 7-9 are integrated. |
| 11. Multimodal, AVSR, and LLM-Assisted ASR | `07_draft_sections/11_multimodal_avsr_llm_assisted_asr.md` | Yes | Ready, but must keep LLM-assisted ASR bounded and risk-aware. |
| 12. Cross-Block Synthesis and Gap Analysis | `07_draft_sections/12_cross_block_synthesis_gap_analysis.md` | Yes | Ready after Sections 3-11 are assembled. |
| 13. Future Research Agenda | `07_draft_sections/13_future_research_agenda.md` | Yes | Ready after synthesis is assembled; LLM-assisted ASR remains part of the future agenda, not a new contribution. |
| 14. Conclusion | `07_draft_sections/14_conclusion.md` | Yes | Ready after Sections 12-13 are stable. |

Older method-by-method draft files remain source material only and should not steer final manuscript structure.

## 4. Table Readiness

Tables are ready for manuscript-level review. Final numbering is controlled by `08_tables/table_registry.md`.

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

Figures are ready for manuscript-level review. Final numbering is controlled by `09_figures/figure_registry.md`.

| Figure | Source files | Status |
|---|---|---|
| Figure 1 | `09_figures/figure_01_bottleneck_stack.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 2 | `09_figures/figure_02_six_layer_taxonomy.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 3 | `09_figures/figure_03_cross_block_evidence_flow.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 4 | `09_figures/figure_04_future_agenda_map.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |

Older `09_figures/fig_01_*` through `fig_06_*` folders remain legacy placeholders or source ideas only.

## 6. Recommended Next Assembly Batch

Begin manuscript assembly with Sections 3-6:

1. Section 3: What Makes ASR Low-Resource?
2. Section 4: From Hybrid ASR to Foundation Speech Models.
3. Section 5: Resources and Benchmarks.
4. Section 6: Foundation-Model-Era Taxonomy of Low-Resource ASR.

Rationale: these sections establish the conceptual and taxonomic base before adaptation, pseudo-labeling/KD, evaluation, multimodal/LLM-assisted ASR, cross-block synthesis, and the final agenda. Integrating them first also lets Figure 1, Figure 2, Table 1, and Table 2 be placed and tested before the later method and reliability sections depend on them.

## 7. Remaining Risks Before Assembly

- Section drafts need compression and cross-section harmonization; avoid duplicating the same foundation-model caveat in every section.
- Citation density must be checked after prose is assembled into `main_manuscript.md`.
- Figures and tables should be introduced as argumentative aids, not decorative inserts.
- LLM-assisted ASR must remain bounded to correction, rescoring, contextual biasing, post-ASR normalization, and speech-LLM systems with hallucination, over-correction, leakage, bias, compute, and reproducibility safeguards.
- Pashto must remain illustrative only, not a focused case-study contribution.
- Do not add new RQs, a fifth contribution, unverified citations, or unsupported performance claims during assembly.
