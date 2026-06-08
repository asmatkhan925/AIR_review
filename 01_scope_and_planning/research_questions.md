# Research Questions

This file is the canonical source of truth for the review questions. Other files should follow these questions, not redefine them.

## Locked Version

- Version: 1.0
- Status: Locked
- Date locked: 2026-06-09
- Related decision file: `00_project_management/locked_decisions.md`

## Main Review Question

How have foundation speech models changed low-resource ASR, and what resource, adaptation, evaluation, and robustness challenges still prevent reliable recognition for underrepresented languages?

## Supporting Review Questions

### RQ1. What does "low-resource" mean in ASR beyond limited labeled hours?

This question covers dialect variation, orthographic inconsistency, script complexity, code-switching, noisy speech, weak validation, benchmark limitations, compute constraints, and resource inequity.

### RQ2. How have self-supervised, weakly supervised, multilingual, and foundation speech models changed low-resource ASR?

This question covers model families such as wav2vec 2.0, HuBERT, WavLM, XLS-R, Whisper, MMS, SeamlessM4T, OMNIASR, and newer speech-language models.

### RQ3. Which data-centric strategies remain necessary in the foundation-model era?

This question covers corpus creation, transcription quality, text normalization, filtering, augmentation, validation, metadata, and benchmark design.

### RQ4. Which adaptation strategies are most effective for low-resource ASR, and under what conditions?

This question covers full fine-tuning, continued pretraining, adapters, LoRA, QLoRA, prompt-based methods, parameter-efficient tuning, language-family transfer, and adaptation under compute constraints.

### RQ5. How reliable are pseudo-labeling and knowledge distillation for low-resource ASR?

This question covers teacher errors, confidence filtering, multi-teacher disagreement, agreement-based selection, iterative relabeling, pseudo-label noise, and student-model training.

### RQ6. How should low-resource ASR be evaluated and extended toward robust, multimodal, and LLM-assisted systems?

This question covers WER/CER limitations, dialect-wise evaluation, domain-wise evaluation, noise robustness, reproducibility, compute/deployment constraints, AVSR, LLM correction, LLM rescoring, and multimodal robustness.

## Contribution Logic

The locked questions support four contribution claims:

1. A foundation-model-era taxonomy of low-resource ASR, organized by resource condition, language condition, model family, adaptation method, supervision strategy, and evaluation setting.
2. A synthesis of data-centric and model-centric solutions, showing how corpus quality, normalization, filtering, augmentation, SSL, multilingual transfer, and foundation models interact.
3. A critical review of adaptation, pseudo-labeling, and knowledge distillation, focusing on parameter-efficient tuning, continued pretraining, teacher reliability, confidence filtering, and multi-teacher disagreement.
4. A future research agenda for reliable low-resource ASR, covering dialect-aware evaluation, reproducibility, compute efficiency, multimodal robustness, AVSR, and LLM-assisted correction or rescoring.

## Six-Layer Taxonomy

| Layer | Categories |
|---|---|
| Resource layer | Labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, multimodal |
| Language layer | Dialect variation, orthographic inconsistency, code-switching, morphology, script complexity |
| Model layer | Hybrid ASR, E2E ASR, SSL models, multilingual ASR, weakly supervised ASR, speech foundation models |
| Adaptation layer | Fine-tuning, continued pretraining, adapters, LoRA/QLoRA, prompting, transfer learning |
| Supervision layer | Supervised learning, SSL, self-training, pseudo-labeling, single-teacher KD, multi-teacher KD |
| Evaluation layer | WER/CER, dialect-wise, domain-wise, noise robustness, reproducibility, compute/deployment cost |

## Backbone Statement

This review examines how foundation speech models have reshaped low-resource ASR, while arguing that reliable recognition for underrepresented languages still depends on resource quality, language-aware adaptation, pseudo-label reliability, fair evaluation, reproducibility, and robustness under noisy or multimodal conditions.

