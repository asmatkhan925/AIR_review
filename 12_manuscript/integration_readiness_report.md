# Manuscript Integration Readiness Report

## 1. Current Repository State

- Current branch: `main`
- Post-figure source state: after commit `994029a` (`Polish SVG figures and add previews`)
- Scope and RQs: ready; canonical source remains `01_scope_and_planning/research_questions.md`
- Main manuscript state: Sections 3-9 have been assembled into `12_manuscript/main_manuscript.md`; Sections 1-2 and 10-14 remain pointer-based or pending integration
- Next phase: manuscript assembly of Sections 10-11

This report is a metadata and readiness snapshot after the second manuscript assembly batch. It does not add literature, alter RQs, change contributions, or modify Core 60, references, Block G, or synthesis matrices.

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
| 3. What Makes ASR Low-Resource? | `07_draft_sections/03_what_makes_asr_low_resource.md` | Yes | Assembled into `main_manuscript.md`; needs later cross-section polish. |
| 4. From Hybrid ASR to Foundation Speech Models | `07_draft_sections/04_from_hybrid_asr_to_foundation_speech_models.md` | Yes | Assembled into `main_manuscript.md`; needs later cross-section polish. |
| 5. Resources and Benchmarks | `07_draft_sections/05_resources_and_benchmarks_for_low_resource_asr.md` | Yes | Assembled into `main_manuscript.md`; Table 2 callout connected. |
| 6. Foundation-Model-Era Taxonomy of Low-Resource ASR | `07_draft_sections/06_foundation_model_era_taxonomy.md` | Yes | Assembled into `main_manuscript.md`; Figure 2 and Table 1 callouts connected. |
| 7. Data-Centric Strategies in the Foundation-Model Era | `07_draft_sections/07_data_centric_strategies_foundation_model_era.md` | Yes | Assembled into `main_manuscript.md`; needs later cross-section polish. |
| 8. Adaptation Strategies for Low-Resource ASR | `07_draft_sections/08_adaptation_strategies_low_resource_asr.md` | Yes | Assembled into `main_manuscript.md`; Table 3 callout connected. |
| 9. Pseudo-Labeling and Knowledge Distillation | `07_draft_sections/09_pseudo_labeling_kd_low_resource_asr.md` | Yes | Assembled into `main_manuscript.md`; Table 4 callout connected. |
| 10. Evaluation, Reproducibility, and Robustness | `07_draft_sections/10_evaluation_reproducibility_robustness.md` | Yes | Ready for next assembly batch. |
| 11. Multimodal, AVSR, and LLM-Assisted ASR | `07_draft_sections/11_multimodal_avsr_llm_assisted_asr.md` | Yes | Ready for next assembly batch, but must keep LLM-assisted ASR bounded and risk-aware. |
| 12. Cross-Block Synthesis and Gap Analysis | `07_draft_sections/12_cross_block_synthesis_gap_analysis.md` | Yes | Ready after Sections 3-11 are assembled. |
| 13. Future Research Agenda | `07_draft_sections/13_future_research_agenda.md` | Yes | Ready after synthesis is assembled; LLM-assisted ASR remains part of the future agenda, not a new contribution. |
| 14. Conclusion | `07_draft_sections/14_conclusion.md` | Yes | Ready after Sections 12-13 are stable. |

Older method-by-method draft files remain source material only and should not steer final manuscript structure.

## 4. Table Readiness

Tables are ready for manuscript-level review. Final numbering is controlled by `08_tables/table_registry.md`. Table 1, Table 2, Table 3, and Table 4 are now callout-linked in the assembled Sections 5-9.

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

Figures are ready for manuscript-level review. Final numbering is controlled by `09_figures/figure_registry.md`. Figure 1 and Figure 2 are now callout-linked in the assembled Sections 3 and 6. Figure 3 remains deferred, likely for Section 12 after Sections 10-11 are assembled.

| Figure | Source files | Status |
|---|---|---|
| Figure 1 | `09_figures/figure_01_bottleneck_stack.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 2 | `09_figures/figure_02_six_layer_taxonomy.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 3 | `09_figures/figure_03_cross_block_evidence_flow.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |
| Figure 4 | `09_figures/figure_04_future_agenda_map.svg`; PNG/PDF previews in `09_figures/previews/` | Polished editable SVG draft; previews available. |

Older `09_figures/fig_01_*` through `fig_06_*` folders remain legacy placeholders or source ideas only.

## 6. Completed and Next Assembly Batches

Completed manuscript assembly batches:

1. Section 3: What Makes ASR Low-Resource?
2. Section 4: From Hybrid ASR to Foundation Speech Models.
3. Section 5: Resources and Benchmarks.
4. Section 6: Foundation-Model-Era Taxonomy of Low-Resource ASR.
5. Section 7: Data-Centric Strategies in the Foundation-Model Era.
6. Section 8: Adaptation Strategies for Low-Resource ASR.
7. Section 9: Pseudo-Labeling and Knowledge Distillation.

Recommended next manuscript assembly batch:

1. Section 10: Evaluation, Reproducibility, and Robustness.
2. Section 11: Multimodal, AVSR, and LLM-Assisted ASR.

Rationale: Sections 3-9 now establish the conceptual, taxonomic, data-centric, adaptation, and supervision layers. Sections 10-11 should next develop evaluation, robustness, reproducibility, multimodal/AVSR, SpeechLM, and bounded LLM-assisted ASR before the manuscript moves to cross-block synthesis and the final agenda.

## 7. Remaining Risks Before Assembly

- Sections 3-9 are assembled but will still need final compression, citation-density harmonization, and transition checks after Sections 10-14 are integrated.
- Citation consistency must continue to be checked after each new assembly batch.
- Figure 3 remains deferred until the cross-block evidence flow is better motivated by Sections 10-11 and/or Section 12.
- Figures and tables should continue to be introduced as argumentative aids, not decorative inserts.
- LLM-assisted ASR must remain bounded to correction, rescoring, contextual biasing, post-ASR normalization, and speech-LLM systems with hallucination, over-correction, leakage, bias, compute, and reproducibility safeguards.
- Pashto must remain illustrative only, not a focused case-study contribution.
- Do not add new RQs, a fifth contribution, unverified citations, or unsupported performance claims during assembly.
