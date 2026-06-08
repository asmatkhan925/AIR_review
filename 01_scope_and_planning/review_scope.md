# Review Scope

## Working Title

**Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era: Resources, Adaptation, Evaluation, and Multimodal Robustness**

## Review Type

Systematic mapping review + critical taxonomy.

## Scope Statement

This review examines automatic speech recognition for low-resource languages in the foundation-model era. The paper focuses on how modern speech foundation models, multilingual representation learning, weak supervision, adaptation strategies, pseudo-labeling, knowledge distillation, and multimodal methods have reshaped low-resource ASR. It also critically examines why low-resource ASR remains unsolved despite large pretrained models.

The review is not limited to Pashto and should not be written as a thesis summary. Pashto may be used selectively as an illustrative example of broader low-resource ASR problems.

## Included Topics

### 1. Low-resource ASR problem definition
- Limited labeled data
- Limited validated data
- Noisy or spontaneous recordings
- Dialect and accent variation
- Code-switching and multilingual speech
- Orthographic inconsistency
- Script complexity
- Domain mismatch
- Weak benchmarks and poor metadata
- Deployment and compute constraints

### 2. Datasets and benchmarks
- Babel
- Common Voice
- FLEURS
- MLS
- Multilingual LibriSpeech and related corpora
- ML-SUPERB and other multilingual benchmarks
- Regional and language-specific datasets
- Low-resource AVSR datasets where relevant

### 3. Model-centric methods
- Hybrid ASR
- End-to-end CTC, attention, and RNN-T systems
- Self-supervised speech models
- Multilingual speech representation learning
- Weakly supervised ASR
- Foundation ASR models
- Speech-language models

### 4. Adaptation strategies
- Full fine-tuning
- Continued pretraining
- Domain adaptation
- Cross-lingual transfer
- Parameter-efficient adaptation
- Adapters
- LoRA and QLoRA
- Prompt-based and instruction-based methods

### 5. Data-centric methods
- Transcript normalization
- Corpus filtering and validation
- Data augmentation
- Semi-supervised learning
- Self-training
- Pseudo-labeling
- Knowledge distillation
- Teacher selection and teacher disagreement
- Confidence filtering and iterative relabeling

### 6. Evaluation and reproducibility
- WER and CER
- Dialect-wise evaluation
- Domain-wise evaluation
- Noise robustness
- Code-switching evaluation
- Fairness and inclusion
- Compute cost and deployment constraints
- Reproducibility and benchmark comparability

### 7. Multimodal and future directions
- Audio-visual speech recognition
- Visual speech recognition and lip-reading
- Audio-visual fusion
- LLM-assisted ASR correction
- LLM rescoring
- Speech-language models
- Multimodal robustness

## Excluded Topics

The review excludes:
- General NLP papers without direct relevance to ASR.
- High-resource-only ASR papers unless they introduce methods later used in low-resource ASR.
- Speaker recognition, speaker verification, diarization, or speech emotion recognition unless directly connected to ASR evaluation or multimodal speech recognition.
- Purely engineering or application papers without methodological or evaluative contribution.
- General multimodal learning papers without speech recognition relevance.
- Papers without enough technical detail to extract method, dataset, evaluation, and limitations.

## Time Range

Priority range: **2019–2026**

Older work may be included only when foundational, such as:
- GMM-HMM and DNN-HMM ASR foundations
- CTC
- sequence-to-sequence ASR
- early self-supervised speech learning
- early AVSR foundations
- major multilingual benchmark papers

## Review Boundary

The paper should be broad enough to serve researchers working on underrepresented languages generally, while still offering detailed technical synthesis of adaptation, pseudo-labeling, knowledge distillation, evaluation, and multimodal robustness.
