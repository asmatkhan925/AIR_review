# One-Page Concept Note

## Working Title

**Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era: Resources, Adaptation, Evaluation, and Multimodal Robustness**

## Review Rationale

Automatic speech recognition has changed substantially with the rise of self-supervised learning, multilingual speech representation models, weakly supervised ASR systems, and speech foundation models. These models have improved the starting point for low-resource languages by reducing the need to train recognition systems entirely from scratch. However, low-resource ASR remains far from solved. Many languages still face limited labeled data, weak benchmark infrastructure, dialect variation, code-switching, noisy recordings, inconsistent orthography, limited validation, and poor reproducibility.

This review argues that the foundation-model era has shifted the central problem of low-resource ASR from basic model construction to reliable adaptation, data quality control, fair evaluation, and robust deployment.

## Core Argument

Foundation models have changed the starting point of low-resource ASR, but they have not solved low-resource ASR. Remaining bottlenecks include data quality, language and dialect mismatch, orthographic normalization, adaptation strategy, pseudo-label reliability, fair evaluation, reproducibility, compute cost, and robustness under noisy or multimodal conditions.

## Locked Main Review Question

**How have foundation speech models changed low-resource ASR, and what resource, adaptation, evaluation, and robustness challenges still prevent reliable recognition for underrepresented languages?**

## Supporting Review Questions

**RQ1.** What does "low-resource" mean in ASR beyond limited labeled hours?

**RQ2.** How have self-supervised, weakly supervised, multilingual, and foundation speech models changed low-resource ASR?

**RQ3.** Which data-centric strategies remain necessary in the foundation-model era?

**RQ4.** Which adaptation strategies are most effective for low-resource ASR, and under what conditions?

**RQ5.** How reliable are pseudo-labeling and knowledge distillation for low-resource ASR?

**RQ6.** How should low-resource ASR be evaluated and extended toward robust, multimodal, and LLM-assisted systems?

## Scope

The review focuses on automatic speech recognition for low-resource and underrepresented languages. It covers the evolution from hybrid and end-to-end ASR to self-supervised, multilingual, weakly supervised, and foundation-model-based systems. It also examines data resources, model adaptation, pseudo-labeling, knowledge distillation, evaluation practice, dialect and domain robustness, and emerging multimodal or LLM-assisted approaches.

The review is not limited to one language. Individual languages, including Pashto, may be used as illustrative examples, but the main contribution is a general taxonomy and synthesis for low-resource ASR.

## Proposed Contributions

1. **A foundation-model-era taxonomy of low-resource ASR**, organizing the field by resource condition, language condition, model family, adaptation method, supervision strategy, and evaluation setting.

2. **A synthesis of data-centric and model-centric solutions**, showing how corpus quality, normalization, filtering, augmentation, self-supervised learning, multilingual transfer, and foundation models interact.

3. **A critical review of adaptation, pseudo-labeling, and knowledge distillation**, focusing on parameter-efficient tuning, continued pretraining, teacher reliability, confidence filtering, and multi-teacher disagreement.

4. **A future research agenda for reliable low-resource ASR**, covering dialect-aware evaluation, reproducibility, compute efficiency, multimodal robustness, AVSR, and LLM-assisted correction or rescoring.

## Organizing Taxonomy

The review will organize low-resource ASR along six layers:

1. **Resource layer:** labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal data.
2. **Language layer:** dialect variation, orthographic inconsistency, code-switching, morphology, and script complexity.
3. **Model layer:** hybrid ASR, end-to-end ASR, self-supervised models, multilingual ASR, weakly supervised ASR, and speech foundation models.
4. **Adaptation layer:** fine-tuning, continued pretraining, adapters, LoRA/QLoRA, prompting, and transfer learning.
5. **Supervision layer:** supervised learning, self-supervised learning, self-training, pseudo-labeling, single-teacher knowledge distillation, and multi-teacher knowledge distillation.
6. **Evaluation layer:** WER/CER, dialect-wise evaluation, domain-wise evaluation, noise robustness, reproducibility, and compute/deployment cost.

## Target Contribution to the Field

The review aims to clarify why low-resource ASR remains a difficult and important research problem despite recent progress in foundation speech models. Its main value is not to summarize papers one by one, but to provide a critical taxonomy, compare methodological assumptions, identify evaluation weaknesses, and define a future research agenda for reliable, inclusive, and robust ASR for underrepresented languages.

