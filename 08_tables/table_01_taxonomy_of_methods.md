# Table 01: Taxonomy Of Methods

| Paradigm | Representative models | Core idea | Strength | Limitation | Low-resource relevance |
|---|---|---|---|---|---|
| End-to-end ASR | CTC, attention, RNN-T | Direct speech-to-token modeling | Simplifies pipeline | Often needs labeled data | Useful with careful adaptation |
| Self-supervised learning | CPC, wav2vec 2.0, HuBERT, WavLM, XLS-R | Learn from unlabeled speech | Reduces labeling burden | Transfer depends on pretraining data | Highly relevant |
| Multilingual transfer | Multilingual ASR, cross-lingual adaptation | Share knowledge across languages | Improves scarce-language training | Risk of negative transfer | Highly relevant |
| Knowledge distillation | Teacher-student, SeqKD, pseudo-labeling | Transfer teacher predictions | Improves efficiency and supervision | Pseudo-label noise | Relevant for limited labels |
| Foundation models | Whisper, MMS, SeamlessM4T | Large-scale pretrained speech models | Broad capability | Uneven low-resource coverage | Promising but needs scrutiny |
| Multimodal ASR | AV-HuBERT, AVSR systems | Use audio and visual cues | Robust under noise | Requires paired AV data | Important future direction |
