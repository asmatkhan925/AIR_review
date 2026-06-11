# Master Outline

This outline follows the locked review questions in `01_scope_and_planning/research_questions.md`.

## Working Title

**Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era: Resources, Adaptation, Evaluation, and Multimodal Robustness**

## RQ Map

| Section | Title | Primary RQs |
|---|---|---|
| 1 | Introduction | Main RQ; RQ1-RQ6 |
| 2 | Review methodology and search protocol | Main RQ; RQ1-RQ6 |
| 3 | What makes ASR low-resource? | RQ1 |
| 4 | From hybrid ASR to foundation speech models | RQ2 |
| 5 | Resources and benchmarks | RQ1; RQ3; RQ6 |
| 6 | Model-centric approaches | RQ2; RQ4 |
| 7 | Data-centric strategies | RQ3 |
| 8 | Adaptation strategies | RQ4 |
| 9 | Pseudo-labeling and knowledge distillation | RQ5 |
| 10 | Evaluation, reproducibility, and robustness | RQ6 |
| 11 | Multimodal, AVSR, and LLM-Assisted ASR | RQ6 |
| 12 | Cross-Block Synthesis and Gap Analysis | Main RQ; RQ1-RQ6 |
| 13 | Future research agenda | Main RQ; RQ3-RQ6 |
| 14 | Conclusion | Main RQ; RQ1-RQ6 |

## 1. Introduction

**Maps to:** Main RQ; RQ1-RQ6

### Purpose
Frame the review around the central tension: foundation speech models have changed low-resource ASR, but reliable recognition for underrepresented languages remains unsolved.

### Key Points
- ASR progress remains uneven across languages.
- Foundation models improve starting points but do not remove resource, language, adaptation, evaluation, and robustness bottlenecks.
- The review is field-level, not Pashto-centered.
- Pashto and similar languages may appear only as illustrative cases.

### Contribution Link
- Introduce the four contribution claims.
- Introduce the six-layer taxonomy.

## 2. Review Methodology and Search Protocol

**Maps to:** Main RQ; RQ1-RQ6

### Purpose
Define the review as a systematic mapping review plus critical taxonomy.

### Key Points
- Search sources: Google Scholar, Semantic Scholar, IEEE Xplore, ACM Digital Library, ISCA Archive, ACL Anthology, arXiv, SpringerLink, ScienceDirect, and major ASR proceedings.
- Search topics: low-resource ASR, multilingual ASR, speech foundation models, pseudo-labeling, knowledge distillation, dialect ASR, AVSR, and LLM-assisted ASR.
- Data extraction: paper metadata, language coverage, datasets, methods, evaluation setup, limitations, and relevance to the locked RQs.
- Citation reliability: every citation used in the manuscript must be verified.

### Outputs
- Search log.
- Citation verification log.
- Inclusion/exclusion record.
- Evidence-to-claim matrix.

## 3. What Makes ASR Low-Resource?

**Maps to:** RQ1

### Purpose
Define low-resource ASR beyond limited labeled hours.

### Key Points
- Labeled-data scarcity.
- Weak validation and small test sets.
- Dialect, accent, and speaker imbalance.
- Orthographic inconsistency, script complexity, and normalization.
- Code-switching and morphology.
- Noisy, spontaneous, telephony, broadcast, and web speech.
- Compute, licensing, and deployment constraints.

### Synthesis Target
Show that "low-resource" is a multidimensional condition, not only a dataset-size label.

## 4. From Hybrid ASR to Foundation Speech Models

**Maps to:** RQ2

### Purpose
Explain how model families changed the low-resource ASR starting point.

### Key Points
- Hybrid ASR: GMM-HMM, DNN-HMM, lexicons, pronunciation modeling.
- End-to-end ASR: CTC, attention encoder-decoder, RNN-T, hybrid CTC-attention.
- SSL models: CPC, wav2vec 2.0, HuBERT, WavLM.
- Multilingual and foundation models: XLS-R, Whisper, MMS, SeamlessM4T, OMNIASR, and speech-language models.
- Changed assumptions: less training from scratch, more transfer, more reliance on model coverage and adaptation.

### Synthesis Target
Compare model families by data assumptions, transfer mechanisms, language coverage, and remaining mismatch.

## 5. Resources and Benchmarks

**Maps to:** RQ1; RQ3; RQ6

### Purpose
Evaluate the datasets and benchmarks that structure low-resource ASR research.

### Key Points
- Multilingual benchmarks: Babel, Common Voice, FLEURS, MLS, VoxPopuli, ML-SUPERB, and others.
- Language-specific and regional datasets.
- Metadata, dialect labels, speaker diversity, domain coverage, transcription quality, and licensing.
- Benchmark limitations: comparability, normalization, small test sets, domain mismatch, and lack of robustness testing.

### Synthesis Target
Show that benchmark design affects what progress can be claimed.

## 6. Foundation-Model-Era Taxonomy of Low-Resource ASR

**Maps to:** RQ2; RQ4

### Purpose
Present the review's six-layer taxonomy for low-resource ASR in the foundation-model era.

### Key Points
- Resource layer: labeled, unlabeled, weakly labeled, pseudo-labeled, multilingual, and multimodal resources.
- Language layer: dialect, orthography, code-switching, morphology, script complexity, and language-family mismatch.
- Model layer: hybrid, E2E, SSL, multilingual, weakly supervised, SpeechLM, and multimodal foundation systems.
- Adaptation layer: fine-tuning, continued pretraining, PEFT, transfer, prompting, and forgetting control.
- Supervision and evaluation layers: pseudo-labeling, KD, WER/CER limits, robustness, fairness, reproducibility, and LLM-assisted risks.

### Synthesis Target
Show how the six layers interact and prepare the transition to data-centric strategies, adaptation, supervision, and evaluation sections.

## 7. Data-Centric Strategies

**Maps to:** RQ3

### Purpose
Analyze which data-centric strategies remain necessary even with foundation models.

### Key Points
- Corpus creation and validation.
- Transcript normalization.
- Corpus filtering and quality control.
- Speaker, dialect, and domain balance.
- Data augmentation and robustness-oriented data design.
- Benchmark construction.

### Synthesis Target
Show how data quality and data design interact with model performance.

## 8. Adaptation Strategies

**Maps to:** RQ4

### Purpose
Compare adaptation strategies and specify when each is appropriate.

### Key Points
- Full fine-tuning.
- Continued pretraining.
- Adapters.
- LoRA and QLoRA.
- Prompt-based methods.
- Transfer learning and language-family selection.
- Adaptation under compute constraints.

### Synthesis Target
Condition recommendations on labeled data, unlabeled data, compute cost, model type, language relatedness, domain match, and evaluation setting.

## 9. Pseudo-Labeling and Knowledge Distillation

**Maps to:** RQ5

### Purpose
Assess the reliability of pseudo-labeling and KD for low-resource ASR.

### Key Points
- Self-training and teacher-generated transcripts.
- Confidence filtering.
- Agreement-based selection.
- Iterative relabeling.
- Single-teacher and multi-teacher KD.
- Teacher disagreement and pseudo-label noise.
- Student-model training and evaluation.

### Synthesis Target
Explain when pseudo-labeling expands supervision and when it transfers teacher bias or errors.

## 10. Evaluation, Reproducibility, and Robustness

**Maps to:** RQ6

### Purpose
Critique how low-resource ASR is evaluated and reported.

### Key Points
- WER and CER limitations.
- Dialect-wise, domain-wise, speaker-wise, and noise-wise evaluation.
- Code-switching and orthographic normalization effects.
- Fairness and inclusiveness.
- Reproducibility: preprocessing, decoding, language model use, compute cost, seeds, checkpoints, and test-set disclosure.

### Synthesis Target
Show that global WER/CER can hide the exact failures that matter for underrepresented languages.

## 11. Multimodal, AVSR, and LLM-Assisted ASR

**Maps to:** RQ6

### Purpose
Examine how robust low-resource ASR may extend toward multimodal AVSR, SpeechLM systems, and LLM-assisted correction, rescoring, contextual biasing, or post-ASR normalization.

### Key Points
### 11.1 Why audio-only ASR remains fragile in low-resource settings
- Noise, channel mismatch, dialect variation, weak language modeling, and limited metadata.

### 11.2 Audio-visual ASR and multimodal robustness
- Audio-visual speech recognition.
- Visual speech recognition and lip-reading.
- Audio-visual fusion under noise.
- Low-resource AVSR data challenges.

### 11.3 Speech-language models and speech-to-LLM architectures
- Speech encoders connected to LLMs.
- Speech instruction tuning.
- Multitask speech recognition and understanding.
- Low-resource language coverage and adaptation constraints.

### 11.4 LLM-assisted ASR correction, rescoring, and contextual biasing
- Post-ASR correction.
- N-best or lattice rescoring.
- Contextual biasing.
- Post-ASR normalization.

### 11.5 Risks: hallucination, over-correction, benchmark leakage, cost, and language bias
- Hallucinated or over-normalized outputs.
- Benchmark leakage and data contamination.
- Compute and deployment cost.
- Bias toward high-resource language norms.

### 11.6 What is established and what remains speculative
- Separate demonstrated ASR improvements from future-facing claims.
- Require evaluation beyond global WER/CER.

### Synthesis Target
Separate demonstrated ASR improvements from speculative multimodal or LLM-assisted claims.

## 12. Cross-Block Synthesis and Gap Analysis

**Maps to:** Main RQ; RQ1-RQ6

### Purpose
Integrate Sections 3-11, the six taxonomy layers, synthesis matrices, and evidence-based gap analysis into a cross-block synthesis.

### Six-Layer Taxonomy
- Resource layer.
- Language layer.
- Model layer.
- Adaptation layer.
- Supervision layer.
- Evaluation layer.

### Comparative Matrices
- Method comparison matrix.
- Dataset benchmark matrix.
- Foundation model matrix.
- Adaptation strategy matrix.
- Evidence-to-claim matrix.
- Research gap matrix.

### Synthesis Target
Show how resource conditions, language conditions, model choice, adaptation strategy, supervision method, and evaluation practice interact.

## 13. Future Research Agenda

**Maps to:** Main RQ; RQ3-RQ6

### Purpose
Propose a research agenda for reliable low-resource ASR.

### Directions
- Reliable pseudo-labeling and teacher validation.
- Dialect- and domain-aware adaptation.
- Better benchmark design and metadata.
- Reproducible and compute-aware evaluation.
- Low-resource AVSR and multimodal robustness.
- LLM-assisted ASR with safeguards.
- Community-centered data development.

### Synthesis Target
Tie every future direction to an observed evidence gap.

## 14. Conclusion

**Maps to:** Main RQ; RQ1-RQ6

### Purpose
Answer the main review question concisely.

### Closing Argument
Foundation speech models have reshaped low-resource ASR, but reliable recognition for underrepresented languages still depends on resource quality, language-aware adaptation, pseudo-label reliability, fair evaluation, reproducibility, and robustness under noisy or multimodal conditions.
