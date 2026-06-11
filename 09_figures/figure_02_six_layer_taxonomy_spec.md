# Figure 2 Specification: Six-Layer Taxonomy of Low-Resource ASR

Purpose: Specification for a future figure supporting Section 6 and the cross-block synthesis in Section 12. Source basis: `05_synthesis_matrices/block_g_cross_block_taxonomy_synthesis_matrix.csv` and `07_draft_sections/06_foundation_model_era_taxonomy.md`.

Status: Draft specification only. Do not generate the final image yet.

## Core Message

The review organizes low-resource ASR in the foundation-model era around six interacting layers: Resource, Language, Model, Adaptation, Supervision, and Evaluation. The taxonomy is not a method list; it shows why resource conditions, language conditions, model families, adaptation choices, supervision sources, and evaluation protocols must be aligned.

## Visual Layout

- Use six horizontal layers or six linked panels labeled:
  1. `Resource`
  2. `Language`
  3. `Model`
  4. `Adaptation`
  5. `Supervision`
  6. `Evaluation`
- Place compact examples inside each layer:
  - Resource: labeled speech, unlabeled speech, weak labels, pseudo-labels, multilingual corpora, multimodal resources.
  - Language: dialect, accent, orthography, script, morphology, code-switching, language-family mismatch.
  - Model: hybrid ASR, end-to-end ASR, SSL encoders, multilingual SSL, weakly supervised ASR, SpeechLMs, multimodal systems.
  - Adaptation: full fine-tuning, continued pretraining, adapters, LoRA/QLoRA, related-language transfer, contextual biasing, forgetting control.
  - Supervision: supervised labels, self-supervision, self-training, confidence/uncertainty filtering, single-teacher KD, multi-teacher KD.
  - Evaluation: WER/CER, orthography-aware scoring, language/dialect/domain breakdowns, robustness, fairness, compute, reproducibility, hallucination checks.
- Use cross-layer arrows rather than only top-to-bottom arrows:
  - Resource to Supervision: supervision source quality controls training labels.
  - Language to Evaluation: orthography and dialect affect scoring.
  - Model to Adaptation: model family constrains adaptation choices.
  - Adaptation to Evaluation: adaptation claims require matched evaluation.
  - Evaluation to Resource/Adaptation: evaluation failures should guide data and adaptation revisions.

## Foundation-Model-Era Annotation

Add a small side label: `Foundation-model-era emphasis: stronger pretrained starting points, but reliability depends on cross-layer alignment.` This note should make clear that the taxonomy is specific to the current foundation-model context rather than a generic ASR methods taxonomy.

## Suggested Caption

Six-layer taxonomy for low-resource ASR in the foundation-model era. The review treats resources, language conditions, model families, adaptation strategies, supervision sources, and evaluation protocols as interacting evidence layers rather than isolated method categories.

## Design Notes

- Keep examples short; the detailed taxonomy belongs in Table 1 and Block G, not inside the figure.
- Emerging SpeechLM, AVSR, and LLM-assisted items can appear as examples, but central layer definitions should not depend on watchlist-only evidence.
