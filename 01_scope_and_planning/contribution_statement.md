# Contribution Statement

## Draft Contribution Statement

This review contributes a field-level synthesis of low-resource automatic speech recognition in the foundation-model era. Rather than treating low-resource ASR as a problem solved by scaling pretrained models, the review argues that resource quality, language mismatch, dialect variation, orthographic normalization, adaptation strategy, pseudo-label reliability, evaluation design, and multimodal robustness remain central bottlenecks.

## Main Contributions

### Contribution 1: Modern taxonomy of low-resource ASR in the foundation-model era

The review organizes low-resource ASR methods across classical hybrid systems, end-to-end ASR, self-supervised learning, multilingual transfer, weakly supervised foundation models, parameter-efficient adaptation, pseudo-labeling, knowledge distillation, speech-language models, and multimodal ASR.

### Contribution 2: Synthesis of data-centric and model-centric solutions

The review compares model-centric approaches such as foundation models, cross-lingual adaptation, and parameter-efficient tuning with data-centric approaches such as normalization, corpus filtering, augmentation, validation, pseudo-labeling, and benchmark construction.

### Contribution 3: Critical analysis of adaptation, pseudo-labeling, and knowledge distillation

The review provides a detailed analysis of how low-resource ASR systems are adapted using fine-tuning, continued pretraining, adapters, LoRA/QLoRA, pseudo-labeling, self-training, and knowledge distillation. Particular attention is given to teacher reliability, teacher disagreement, confidence filtering, and multi-teacher selection.

### Contribution 4: Future research agenda for reliable, multimodal, and LLM-assisted low-resource ASR

The review identifies future directions for reliable low-resource ASR, including dialect-aware evaluation, reproducible benchmarking, compute-efficient adaptation, multimodal and audio-visual robustness, and cautious LLM-assisted correction, rescoring, contextual biasing, and post-ASR normalization.

## What This Review Is Not

This review is not:
- a thesis summary;
- a Pashto-only review;
- a simple list of papers;
- a general ASR tutorial detached from low-resource issues;
- a review focused only on model architectures.

## What This Review Should Be

This review should be:
- broad enough for low-resource languages generally;
- current enough to reflect the foundation-model era;
- critical enough for Artificial Intelligence Review;
- structured around taxonomy, comparison, evidence, gaps, and future directions;
- connected to the author’s expertise without being limited by the author’s thesis.
