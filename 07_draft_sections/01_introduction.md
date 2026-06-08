# 1. Introduction

## Purpose of This Section

The introduction should establish the importance of low-resource ASR in the foundation-model era, motivate why the problem remains unsolved, define the review scope, and state the paper’s contributions.

## Key Argument

Foundation models shift low-resource ASR from building recognition systems from scratch to adapting large pretrained systems under data, language, domain, and evaluation mismatch. However, this shift introduces or exposes new problems: pseudo-label reliability, benchmark comparability, dialect fairness, orthographic normalization, compute cost, hallucination risk, and multimodal robustness.

## Points to Cover

### 1. Uneven progress in ASR

ASR performance has improved substantially in high-resource languages, but progress remains uneven across underrepresented languages, dialects, domains, and scripts.

### 2. Foundation models changed the starting point

Self-supervised, multilingual, weakly supervised, and foundation-scale models now provide stronger initial systems for low-resource languages than earlier supervised-only approaches.

Examples to discuss:
- wav2vec 2.0
- HuBERT
- WavLM
- XLS-R
- Whisper
- MMS
- SeamlessM4T
- OMNIASR
- speech-language models

### 3. Foundation models did not solve low-resource ASR

Persistent bottlenecks include:
- limited validated speech;
- noisy and spontaneous recordings;
- dialect imbalance;
- language and domain mismatch;
- orthographic inconsistency;
- script complexity;
- code-switching;
- pseudo-label noise;
- weak evaluation design;
- limited reproducibility;
- compute and deployment constraints.

### 4. Need for a new review

Existing reviews often focus on:
- classical ASR;
- language-specific ASR;
- Indian or Chinese dialect ASR;
- general speech recognition;
- general foundation models;
- knowledge distillation or multimodal learning outside ASR.

A gap remains for a modern review that unifies low-resource ASR under the foundation-model era and critically analyzes resources, adaptation, evaluation, and multimodal robustness.

### 5. Review contribution

This review provides:
1. a modern taxonomy of low-resource ASR in the foundation-model era;
2. a synthesis of data-centric and model-centric solutions;
3. a critical analysis of adaptation, pseudo-labeling, and knowledge distillation;
4. a future research agenda for reliable, multimodal, and LLM-assisted low-resource ASR, covering dialect-aware evaluation, reproducible benchmarking, compute-efficient adaptation, multimodal and audio-visual robustness, and cautious LLM-assisted correction, rescoring, contextual biasing, and post-ASR normalization.

## Draft Opening Paragraph

Automatic speech recognition (ASR) has advanced rapidly during the past decade, driven by end-to-end modeling, self-supervised speech representation learning, multilingual pretraining, and more recently, foundation-scale speech and speech-language models. These advances have changed the technical starting point for low-resource ASR: many languages that previously required systems to be trained almost from scratch can now benefit from pretrained multilingual representations or weakly supervised recognition models. However, the availability of larger pretrained models does not eliminate the low-resource problem. In many underrepresented languages, recognition quality remains constrained by scarce validated speech, noisy or spontaneous recordings, dialect and domain mismatch, inconsistent orthography, limited metadata, weak evaluation practice, and deployment constraints.

## Draft Scope Paragraph

This review examines low-resource ASR in the foundation-model era. Rather than treating low-resource ASR as a single problem of limited labeled hours, it frames low-resource recognition as a multidimensional challenge involving data quality, language coverage, dialect variation, script and normalization, adaptation strategy, pseudo-label reliability, evaluation design, and multimodal robustness. The review synthesizes recent work on self-supervised and multilingual speech models, weakly supervised foundation ASR, parameter-efficient adaptation, pseudo-labeling, knowledge distillation, evaluation practice, and emerging multimodal and LLM-assisted directions. Individual languages, including Pashto and other underrepresented languages, are used as illustrative examples when they clarify broader methodological issues.

## Draft Contribution Paragraph

The review makes four contributions. First, it develops a foundation-model-era taxonomy of low-resource ASR, organized by resource condition, language condition, model family, adaptation method, supervision strategy, and evaluation setting. Second, it synthesizes data-centric and model-centric solutions, showing how corpus quality, normalization, filtering, augmentation, self-supervised learning, multilingual transfer, and foundation models interact. Third, it critically analyzes adaptation, pseudo-labeling, and knowledge distillation, with particular attention to parameter-efficient tuning, continued pretraining, teacher reliability, confidence filtering, and multi-teacher disagreement. Fourth, it proposes a future research agenda for reliable, multimodal, and LLM-assisted low-resource ASR, covering dialect-aware evaluation, reproducible benchmarking, compute-efficient adaptation, multimodal and audio-visual robustness, and cautious LLM-assisted correction, rescoring, contextual biasing, and post-ASR normalization.

## Notes for Later Revision

- Add verified citations after the literature matrix is populated.
- Avoid overclaiming that foundation models fail; use balanced language.
- Do not make Pashto central in the introduction.
- Use Pashto only as an illustrative example later in the paper.
