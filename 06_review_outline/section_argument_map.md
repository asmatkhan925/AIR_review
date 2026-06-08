# Section Argument Map

Use this file to keep every section argumentative rather than descriptive.

## Section 1: Introduction

### Purpose
Establish why low-resource ASR remains unresolved despite major progress in foundation speech models.

### Main Argument
Foundation models shift the starting point for low-resource ASR, but they do not remove data, dialect, domain, orthographic, evaluation, and compute constraints.

### Evidence Needed
- Recent low-resource ASR surveys.
- Foundation-model evaluation papers.
- Multilingual benchmark studies.
- Examples of persistent data and evaluation limitations.

### Tables/Figures Used
- Review taxonomy figure.
- Evidence-to-claim matrix.

### Risk
The introduction may overclaim that foundation models have failed or may over-focus on Pashto.

### Quality Check
Does the section frame a broad low-resource ASR problem and use Pashto only as an optional example?

## Section 2: Scope, Method, and Review Protocol

### Purpose
Explain the review type, search process, inclusion criteria, and synthesis method.

### Main Argument
A systematic mapping review with critical taxonomy is appropriate because the field spans data, models, adaptation, evaluation, and deployment constraints.

### Evidence Needed
- Search logs.
- Inclusion and exclusion criteria.
- Citation verification log.

### Tables/Figures Used
- Search protocol table.
- Screening flow diagram if used.

### Risk
The method may look informal if search and screening decisions are not logged.

### Quality Check
Are search decisions reproducible enough for a review journal?

## Section 3: Low-Resource ASR Problem Space

### Purpose
Define low-resource ASR challenges beyond label scarcity.

### Main Argument
Low-resource ASR is shaped by interacting constraints: data quantity, data quality, dialect variation, orthography, domain mismatch, noise, and evaluation design.

### Evidence Needed
- Low-resource ASR challenge papers.
- Dataset and benchmark papers.
- Orthography and transcript normalization studies.

### Tables/Figures Used
- Challenge-solution matrix.
- Dataset benchmark matrix.

### Risk
The section may become a generic background section.

### Quality Check
Does the section explain why each challenge changes method choice or evaluation reliability?

## Section 4: Resources and Benchmarks

### Purpose
Compare datasets, benchmarks, and evaluation resources used for low-resource ASR.

### Main Argument
Dataset availability alone is insufficient; transcription quality, metadata, dialect coverage, domain, and access conditions shape whether benchmarks support fair evaluation.

### Evidence Needed
- Dataset papers.
- Benchmark comparison studies.
- Documentation for public and restricted corpora.

### Tables/Figures Used
- Dataset benchmark matrix.

### Risk
The section may list datasets without analyzing their limitations.

### Quality Check
Does the section compare resources by evaluation use, access, dialect metadata, and limitations?

## Section 5: Model-Centric Approaches

### Purpose
Explain how hybrid ASR, E2E ASR, SSL, multilingual transfer, and foundation models changed low-resource ASR.

### Main Argument
Foundation models reduce the need to train from scratch, but adaptation remains necessary because of language, domain, dialect, and orthographic mismatch.

### Evidence Needed
- SSL foundation papers.
- Multilingual ASR benchmark papers.
- Whisper, MMS, OMNIASR, and related evaluations.
- Low-resource adaptation studies.

### Tables/Figures Used
- Foundation model matrix.
- Adaptation strategy matrix.

### Risk
This section may become a model list instead of a critical synthesis.

### Quality Check
Does the section compare methods by assumptions, data needs, limitations, and evaluation practice?

## Section 6: Data-Centric Methods

### Purpose
Analyze transcript normalization, filtering, augmentation, corpus construction, and data quality control.

### Main Argument
Data-centric decisions often determine whether model-centric gains transfer to real low-resource languages.

### Evidence Needed
- Corpus construction papers.
- Transcript normalization studies.
- Augmentation and filtering studies.

### Tables/Figures Used
- Challenge-solution matrix.
- Dataset benchmark matrix.

### Risk
The section may understate data quality and overstate architecture effects.

### Quality Check
Does the section connect data decisions to measurable ASR reliability?

## Section 7: Adaptation Strategies

### Purpose
Compare fine-tuning, continued pretraining, adapters, LoRA, QLoRA, and prompt-based approaches.

### Main Argument
Adaptation choices are tradeoffs among evidence strength, compute cost, data availability, and robustness.

### Evidence Needed
- Fine-tuning and parameter-efficient adaptation papers.
- Low-resource adaptation evaluations.
- Compute and reproducibility reports.

### Tables/Figures Used
- Adaptation strategy matrix.

### Risk
The section may recommend methods without enough evidence.

### Quality Check
Are recommendations conditioned on data, compute, and evaluation setting?

## Section 8: Pseudo-Labeling and Knowledge Distillation

### Purpose
Explain self-training, pseudo-label selection, teacher reliability, and KD for low-resource ASR.

### Main Argument
Pseudo-labeling and KD can expand supervision, but their value depends on teacher quality, confidence filtering, disagreement handling, and validation under dialect and domain shift.

### Evidence Needed
- Self-training papers.
- Sequence-level KD papers.
- Multi-teacher KD papers.
- Pseudo-label confidence and filtering studies.

### Tables/Figures Used
- Evidence-to-claim matrix.
- Adaptation strategy matrix.

### Risk
The section may treat pseudo-labels as clean labels.

### Quality Check
Does the section state how pseudo-label noise is detected, filtered, or propagated?

## Section 9: Evaluation and Reproducibility

### Purpose
Evaluate WER, CER, dialect-wise evaluation, domain robustness, fairness, compute cost, and reproducibility.

### Main Argument
Low-resource ASR progress cannot be judged reliably without evaluation protocols that expose dialect, domain, orthographic, and robustness variation.

### Evidence Needed
- Evaluation methodology papers.
- Dialect and domain benchmark papers.
- Reproducibility and compute reporting studies.

### Tables/Figures Used
- Research gap matrix.
- Evidence-to-claim matrix.

### Risk
The section may describe metrics without critiquing what they hide.

### Quality Check
Does the section explain what common metrics miss in low-resource settings?

## Section 10: Case Examples from Underrepresented Languages

### Purpose
Use selected languages, including Pashto where useful, to illustrate cross-cutting problems.

### Main Argument
Case examples are valuable only when they reveal generalizable low-resource ASR constraints.

### Evidence Needed
- Case studies from multiple underrepresented languages.
- Pashto ASR evidence where verified.
- Dialect, script, and domain examples.

### Tables/Figures Used
- Case examples file.
- Dataset benchmark matrix.

### Risk
The section may drift into thesis summary.

### Quality Check
Does each example support a general argument rather than merely describing one language?

## Section 11: Future Directions

### Purpose
Propose a research agenda for reliable low-resource ASR.

### Main Argument
The next stage of low-resource ASR should combine better data governance, adaptation, evaluation, multimodal robustness, and cautious LLM-assisted methods.

### Evidence Needed
- Gap matrix.
- Recent speech-language model studies.
- AVSR and multimodal robustness papers.
- Evidence-to-claim matrix.

### Tables/Figures Used
- Research gap matrix.
- Future direction matrix.

### Risk
The section may become speculative.

### Quality Check
Are future directions linked to demonstrated gaps and not only personal research interests?

