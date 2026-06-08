# Inclusion and Exclusion Criteria

## Purpose

These criteria define which papers should be included in the review and which papers should be excluded during screening.

## Inclusion Criteria

A paper should be included if it satisfies at least one of the following criteria:

### IC1. Low-resource or underrepresented-language ASR
The paper studies ASR for a low-resource, under-resourced, endangered, minority, regional, dialectal, or underrepresented language or language variety.

### IC2. Multilingual or cross-lingual ASR transfer
The paper proposes or evaluates multilingual ASR, cross-lingual transfer, language adaptation, multilingual pretraining, or language expansion relevant to low-resource ASR.

### IC3. Self-supervised or foundation speech models for ASR
The paper studies or applies models such as wav2vec 2.0, HuBERT, WavLM, XLS-R, Whisper, MMS, SeamlessM4T, OMNIASR, or related speech foundation models in a way relevant to low-resource ASR.

### IC4. Adaptation strategies for ASR
The paper proposes or evaluates fine-tuning, continued pretraining, domain adaptation, adapters, LoRA/QLoRA, prompt-based methods, parameter-efficient tuning, or transfer learning for ASR.

### IC5. Pseudo-labeling, self-training, or knowledge distillation
The paper studies pseudo-labeling, self-training, semi-supervised ASR, teacher-student learning, sequence-level KD, multi-teacher KD, confidence filtering, teacher selection, or iterative relabeling.

### IC6. Evaluation and benchmarking
The paper contributes datasets, benchmarks, evaluation methods, robustness tests, dialect-aware evaluation, domain-wise evaluation, code-switching evaluation, fairness analysis, or reproducibility analysis for ASR.

### IC7. Multimodal or LLM-assisted ASR
The paper studies audio-visual speech recognition, visual speech recognition, lip-reading, speech-language models, LLM-based ASR correction, LLM rescoring, or multimodal ASR relevant to low-resource or noisy conditions.

## Preferred Time Range

Priority should be given to papers from **2019–2026**, especially **2022–2026**.

## Foundational Exceptions

Older papers may be included if they are foundational, including:
- hybrid ASR foundations;
- CTC;
- attention-based encoder-decoder ASR;
- RNN-T;
- early self-supervised speech learning;
- early AVSR foundations;
- major datasets or benchmarks.

## Exclusion Criteria

A paper should be excluded if it satisfies any of the following criteria:

### EC1. No direct ASR relevance
The paper focuses on general NLP, machine translation, text generation, speech emotion recognition, speaker verification, or speech synthesis without meaningful ASR relevance.

### EC2. High-resource-only focus without transferable insight
The paper focuses only on high-resource ASR and does not introduce a method, dataset, or evaluation insight relevant to low-resource ASR.

### EC3. Insufficient technical detail
The paper does not provide enough information about method, dataset, language coverage, evaluation setup, or results to support extraction.

### EC4. No empirical or conceptual contribution
The paper is a short demonstration, product note, blog-style summary, or purely engineering report without research contribution.

### EC5. Duplicate or superseded version
The paper is an earlier preprint when a peer-reviewed or updated version exists, unless the preprint contains important details missing from the final version.

### EC6. General multimodal learning without ASR connection
The paper studies multimodal AI but does not involve speech recognition, visual speech recognition, audio-visual speech recognition, or ASR post-processing.

## Screening Decision Labels

Use the following labels during screening:
- Include
- Exclude
- Maybe
- Needs verification
- Foundational background
- Not ASR-relevant
- Duplicate
- Out of scope

## Minimum Extraction Fields

For each included paper, extract:
- full citation;
- year;
- venue;
- language(s);
- dataset(s);
- model or method;
- category;
- evaluation metrics;
- main contribution;
- limitations;
- relevance to low-resource ASR;
- verification status.
