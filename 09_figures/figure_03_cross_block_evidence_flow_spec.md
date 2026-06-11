# Figure 3 Specification: Cross-Block Evidence Flow

Purpose: Specification for a future figure supporting Sections 4, 8, 10, and 12. Source basis: Section 12 cross-block synthesis, `05_synthesis_matrices/block_g_cross_block_taxonomy_synthesis_matrix.csv`, and `05_synthesis_matrices/block_g_section_to_evidence_map.csv`.

Status: Draft specification only. Do not generate the final image yet.

## Core Message

Low-resource ASR evidence flows from resource and language conditions into model choice, adaptation, supervision, and evaluation. Evaluation is not the endpoint only; it feeds back into data design, adaptation choice, and future research priorities.

## Visual Layout

- Use a left-to-right flow diagram with three regions:
  - Left region: `Resource and language conditions`
  - Middle region: `Model, adaptation, and supervision strategies`
  - Right region: `Evaluation, robustness, and future agenda`
- Left region nodes:
  - Labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal resources.
  - Dialect, orthography, script, morphology, code-switching, domain, and channel conditions.
- Middle region nodes:
  - Foundation model family: SSL, multilingual SSL, weakly supervised ASR, SpeechLM, multimodal systems.
  - Adaptation path: full fine-tuning, continued pretraining, PEFT, transfer, prompting/contextual biasing, forgetting control.
  - Supervision path: human labels, self-supervised learning, pseudo-labeling, self-training, KD, multi-teacher agreement.
- Right region nodes:
  - Evaluation protocol: WER/CER plus language, dialect, domain, normalization, robustness, hallucination, compute, and reproducibility checks.
  - Research agenda: definitions/resources, documentation, orthography/dialect benchmarks, compute-aware adaptation, reliable pseudo-labeling/KD, AVSR/multimodal, constrained LLM assistance, reproducibility/deployment.
- Add feedback arrows:
  - From evaluation back to resource design: failures expose missing data, metadata, or normalization controls.
  - From evaluation back to adaptation: failures require different adaptation baselines, compute budgets, or forgetting checks.
  - From future agenda back to all earlier blocks: gaps become priorities for the next research cycle.

## Suggested Caption

Cross-block evidence flow for the review. Resource and language conditions shape model choice, adaptation, and supervision, while evaluation and robustness checks feed back into data design, adaptation comparison, and the future research agenda.

## Design Notes

- Use the same color family for all nodes within each region so the diagram remains readable.
- Avoid implying that every study must cover every path. The point is that claims should identify which path they use and which risks remain.
- Watchlist-only evidence should be shown only as bounded emerging-risk annotations in the evaluation or future-agenda region.
