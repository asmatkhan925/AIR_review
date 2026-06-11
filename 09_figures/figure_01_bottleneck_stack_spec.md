# Figure 1 Specification: Foundation-Model-Era Low-Resource ASR Bottleneck Stack

Purpose: Specification for a future figure supporting Sections 1, 3, 12, and 13. Source basis: Section 3 low-resource framing, Section 4 foundation-model transition, Section 12 cross-block synthesis, Section 13 future agenda, and Block G claims C-G1, C-G2, and C-G8.

Status: Draft specification only. Do not generate the final image yet.

## Core Message

Foundation speech models improve the starting point of low-resource ASR, but they do not remove the reliability bottleneck. The remaining bottlenecks interact across resources, language conditions, adaptation, supervision, evaluation, robustness, reproducibility, compute, and emerging multimodal or LLM-assisted risks.

## Visual Layout

- Use a vertical stack or layered pipeline with the top label: `Foundation speech models: stronger starting point`.
- Beneath that starting point, show remaining bottleneck layers as stacked bands:
  - `Resource quality and documentation`: labeled data, unlabeled speech, weak labels, metadata, licensing, validation.
  - `Language fit`: dialect, accent, orthography, script, morphology, code-switching, language-family mismatch.
  - `Adaptation choice`: full fine-tuning, continued pretraining, PEFT, transfer, prompting, forgetting control.
  - `Supervision reliability`: pseudo-label quality, teacher confidence, uncertainty, agreement, KD objective.
  - `Evaluation and comparability`: WER/CER plus language-wise, dialect-wise, domain-wise, and normalization-aware scoring.
  - `Robustness and deployment`: noise, far-field, channel shift, speaker variation, fairness, reproducibility.
  - `Compute and reporting`: hardware, trainable parameters, inference cost, model version, decoding and scoring scripts.
  - `Multimodal and LLM risks`: AVSR modality mismatch, hallucination, over-correction, context leakage, source grounding.
- Show the foundation-model starting point as reducing the initial model-training burden, not erasing the lower layers.
- Use two-way arrows among adjacent bottleneck layers and a few diagonal arrows to show interactions, for example:
  - Resource quality affects adaptation and supervision reliability.
  - Language fit affects evaluation and pseudo-label filtering.
  - Evaluation feedback affects data collection and adaptation choices.
  - Multimodal/LLM risks feed back into evaluation and reproducibility requirements.

## Suggested Caption

Foundation models shift the low-resource ASR bottleneck rather than eliminate it. Reliable recognition depends on interacting layers of resource quality, language fit, adaptation, supervision, evaluation, robustness, compute, reproducibility, and bounded use of multimodal or LLM-assisted methods.

## Design Notes

- Avoid presenting the layers as a simple linear pipeline. Use arrows and feedback loops to show cross-layer dependence.
- Keep the figure field-level and not language-specific.
- If watchlist-only evidence is referenced in the caption or notes, restrict it to emerging multimodal, hallucination, contextual-ASR, or LLM-assisted risks.
