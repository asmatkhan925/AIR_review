# Master Outline

## Working Title

**Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era: Resources, Adaptation, Evaluation, and Multimodal Robustness**

## 1. Introduction

### 1.1 Motivation
- ASR progress has been uneven across languages.
- Foundation models have improved starting points but have not solved low-resource ASR.
- Low-resource ASR remains constrained by data quality, language mismatch, dialect variation, normalization, pseudo-label reliability, evaluation, and robustness.

### 1.2 Scope and review identity
- Field-level review of low-resource ASR in the foundation-model era.
- Not limited to one language.
- Pashto and similar languages may appear as illustrative cases only.

### 1.3 Contributions
- Taxonomy.
- Data-centric/model-centric synthesis.
- Adaptation and distillation analysis.
- Evaluation critique.
- Future agenda.

## 2. Review Methodology and Search Protocol

### 2.1 Review type
- Systematic mapping review + critical taxonomy.

### 2.2 Search sources
- Google Scholar
- Semantic Scholar
- IEEE Xplore
- ACM Digital Library
- ISCA Archive
- ACL Anthology
- arXiv
- SpringerLink
- ScienceDirect
- Elsevier
- major ASR conference proceedings

### 2.3 Search queries
- Low-resource ASR
- Multilingual ASR
- Speech foundation models
- Pseudo-labeling ASR
- Knowledge distillation ASR
- Dialect ASR
- AVSR low-resource
- LLM ASR correction/rescoring

### 2.4 Inclusion/exclusion criteria
- Summarize criteria from the criteria file.

### 2.5 Data extraction
- Paper metadata.
- Language coverage.
- Datasets.
- Methods.
- Evaluation setup.
- Limitations.
- Relevance to low-resource ASR.

## 3. From Hybrid ASR to Foundation Speech Models

### 3.1 Hybrid ASR systems
- GMM-HMM
- DNN-HMM
- lexicons and pronunciation modeling

### 3.2 End-to-end ASR
- CTC
- attention encoder-decoder
- RNN-T
- hybrid CTC-attention

### 3.3 Self-supervised speech representation learning
- CPC
- wav2vec 2.0
- HuBERT
- WavLM

### 3.4 Multilingual and foundation-scale ASR
- XLS-R
- Whisper
- MMS
- SeamlessM4T
- OMNIASR
- speech-language models

### 3.5 Implications for low-resource languages
- Better initialization.
- Less dependence on labeled data.
- Persistent mismatch and evaluation problems.

## 4. What Makes ASR Low-Resource?

### 4.1 Labeled-data scarcity
- Limited hours.
- Weak validation.
- small speaker coverage.

### 4.2 Language and dialect mismatch
- Dialects.
- accents.
- unseen varieties.
- domain mismatch.

### 4.3 Script and orthographic inconsistency
- Arabic-derived scripts.
- Indic scripts.
- non-standard spelling.
- normalization and label fragmentation.

### 4.4 Noisy and spontaneous speech
- telephony.
- broadcast.
- web audio.
- conversational speech.

### 4.5 Code-switching and multilinguality
- mixed language utterances.
- borrowed words.
- evaluation complications.

### 4.6 Resource inequity and deployment constraints
- compute limitations.
- data access.
- licensing.
- community participation.

## 5. Resources and Benchmarks for Low-Resource ASR

### 5.1 Multilingual benchmark datasets
- Babel
- Common Voice
- FLEURS
- MLS
- VoxPopuli
- ML-SUPERB
- other multilingual benchmarks

### 5.2 Language-specific and regional datasets
- African languages.
- South Asian languages.
- Indigenous languages.
- Arabic dialects.
- Central Asian languages.
- other underrepresented languages.

### 5.3 Dataset quality issues
- validation.
- demographic skew.
- dialect imbalance.
- transcript inconsistency.
- licensing.
- metadata limitations.

### 5.4 Benchmark limitations
- comparability.
- domain mismatch.
- small test sets.
- normalization differences.
- lack of robustness testing.

## 6. Model-Centric Approaches

### 6.1 Supervised end-to-end ASR
- CTC and attention-based systems in low-resource contexts.

### 6.2 Self-supervised pretraining
- target-language pretraining.
- multilingual pretraining.
- representation transfer.

### 6.3 Multilingual transfer
- language relatedness.
- phonetic sharing.
- multilingual encoders.
- language-family effects.

### 6.4 Weakly supervised and foundation ASR
- large-scale weak supervision.
- model scaling.
- multilingual coverage.
- hallucination and mismatch.

### 6.5 Speech-language models
- speech encoders with LLM decoders.
- speech instruction tuning.
- ASR correction and generation.

## 7. Adaptation Strategies

### 7.1 Full fine-tuning
- benefits and risks.

### 7.2 Continued pretraining
- in-domain audio.
- target-language audio.
- catastrophic forgetting.

### 7.3 Parameter-efficient adaptation
- adapters.
- LoRA.
- QLoRA.
- prefix/prompt tuning.

### 7.4 Transfer learning design
- source language choice.
- relatedness.
- domain similarity.
- multilingual balancing.

### 7.5 Adaptation under compute constraints
- model size.
- training cost.
- deployment.

## 8. Data-Centric Approaches

### 8.1 Transcript normalization
- label inventory.
- punctuation.
- diacritics.
- script variants.
- evaluation comparability.

### 8.2 Corpus filtering and validation
- quality control.
- speaker/dialect balance.
- automatic filtering.
- human validation.

### 8.3 Data augmentation
- noise.
- speed perturbation.
- SpecAugment.
- codec and channel augmentation.

### 8.4 Pseudo-labeling and self-training
- teacher-generated transcripts.
- confidence filtering.
- iterative relabeling.
- pseudo-label noise.

### 8.5 Knowledge distillation
- frame-level KD.
- sequence-level KD.
- single-teacher KD.
- multi-teacher KD.
- teacher disagreement.
- agreement-based selection.

## 9. Evaluation and Reproducibility

### 9.1 Standard metrics
- WER.
- CER.
- limitations of pooled averages.

### 9.2 Dialect-aware evaluation
- dialect splits.
- imbalance.
- minoritized dialects.

### 9.3 Domain-wise and robustness evaluation
- noise.
- telephony.
- broadcast.
- spontaneous speech.
- out-of-domain testing.

### 9.4 Fairness and inclusiveness
- gender.
- age.
- region.
- accent.
- community representation.

### 9.5 Reproducibility
- preprocessing disclosure.
- normalization rules.
- decoding setup.
- language model use.
- compute cost.
- seed and checkpoint reporting.

## 10. Multimodal and LLM-Assisted Low-Resource ASR

### 10.1 Audio-visual speech recognition
- audio-visual fusion.
- visual speech recognition.
- lip-reading.
- robustness under noise.

### 10.2 Low-resource AVSR challenges
- scarce video data.
- face/mouth extraction.
- synchronization.
- language coverage.
- privacy and ethics.

### 10.3 LLM-assisted ASR
- correction.
- rescoring.
- contextual biasing.
- hallucination risks.
- evaluation.

### 10.4 Multimodal foundation models
- speech-language models.
- audio-visual-language models.
- Q-Former-style compression.
- modality reliability.

## 11. Taxonomy, Comparative Synthesis, and Gap Analysis

### 11.1 Proposed taxonomy
- resources.
- models.
- adaptation.
- data-centric methods.
- evaluation.
- multimodality.

### 11.2 Comparative matrices
- method families.
- strengths.
- weaknesses.
- resource needs.
- evaluation practices.

### 11.3 Main gaps
- data quality.
- normalization.
- adaptation strategy.
- pseudo-label reliability.
- dialect evaluation.
- reproducibility.
- multimodal resources.
- LLM reliability.

## 12. Future Research Agenda

### 12.1 Reliable pseudo-labeling
### 12.2 Dialect- and domain-aware adaptation
### 12.3 Better benchmark design
### 12.4 Low-resource AVSR
### 12.5 LLM-assisted ASR with safeguards
### 12.6 Compute-aware and deployable ASR
### 12.7 Community-centered data development

## 13. Conclusion

- Foundation models have improved low-resource ASR but not solved it.
- The next generation of work must combine model adaptation with data quality, evaluation rigor, and multimodal robustness.
