# Research Questions

## Main Research Question

How has low-resource automatic speech recognition evolved in the foundation-model era, and what bottlenecks remain in resources, adaptation, pseudo-label reliability, evaluation, and multimodal robustness?

## Specific Research Questions

### RQ1. What does “low-resource” mean in ASR beyond limited labeled speech?

This question examines low-resource status as a multidimensional condition involving labeled-data scarcity, weak validation, dialect imbalance, orthographic inconsistency, script complexity, code-switching, domain mismatch, noisy recordings, limited benchmarks, and compute constraints.

### RQ2. How have foundation speech models changed the starting point for low-resource ASR?

This question examines how self-supervised, multilingual, weakly supervised, and foundation-scale models such as wav2vec 2.0, HuBERT, WavLM, XLS-R, Whisper, MMS, SeamlessM4T, and OMNIASR affect low-resource ASR.

### RQ3. Which data-centric and model-centric strategies are used to adapt ASR systems to low-resource languages?

This question compares fine-tuning, continued pretraining, cross-lingual transfer, adapters, LoRA/QLoRA, prompt-based methods, data augmentation, normalization, filtering, and domain adaptation.

### RQ4. How are pseudo-labeling and knowledge distillation used in low-resource ASR, and what reliability problems remain?

This question focuses on single-teacher and multi-teacher pseudo-labeling, confidence filtering, agreement-based selection, iterative relabeling, teacher disagreement, pseudo-label noise, and student-model training.

### RQ5. How should low-resource ASR systems be evaluated beyond global WER/CER?

This question examines dialect-wise, domain-wise, speaker-wise, noise-wise, code-switching, fairness, reproducibility, compute-aware, and deployment-aware evaluation.

### RQ6. What future role will multimodal and LLM-assisted approaches play in robust low-resource ASR?

This question examines AVSR, visual speech recognition, lip-reading, audio-visual fusion, LLM-based correction, LLM rescoring, speech-language models, and multimodal robustness under noisy conditions.

## Expected Answer Form

The review should answer these questions through:
- a taxonomy of methods;
- comparative synthesis tables;
- critical discussion of limitations;
- gap analysis;
- future research agenda;
- recommendations for evaluation and reproducibility.
