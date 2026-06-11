# Section Argument Map

Use this file with `06_review_outline/master_outline.md`. The section numbering and names intentionally match the 14-section master outline and follow the locked RQs in `01_scope_and_planning/research_questions.md`.

## Section 1: Introduction

### Purpose
Establish the central tension: foundation speech models have changed low-resource ASR, but reliable recognition for underrepresented languages remains unresolved.

### Main Argument
Foundation models shift the starting point from training from scratch to adaptation and validation, but resource quality, language mismatch, pseudo-label reliability, evaluation, reproducibility, and robustness remain bottlenecks.

### Evidence Needed
- Recent low-resource ASR reviews.
- Foundation-model evaluation papers.
- Multilingual benchmark studies.
- Evidence on persistent resource, dialect, and evaluation gaps.

### Tables/Figures Used
- Review taxonomy figure.
- Evidence-to-claim matrix.

### Risk
The introduction may overclaim that foundation models fail or drift toward Pashto-specific motivation.

### Quality Check
Does the section answer the main RQ at a high level and keep Pashto only as an optional illustrative example?

## Section 2: Review Methodology and Search Protocol

### Purpose
Explain the review type, search process, inclusion criteria, extraction fields, synthesis method, and citation verification workflow.

### Main Argument
A systematic mapping review plus critical taxonomy is appropriate because the field spans resources, model families, adaptation, supervision, evaluation, and deployment.

### Evidence Needed
- Search logs.
- Inclusion and exclusion criteria.
- Citation verification log.
- Evidence-to-claim matrix.

### Tables/Figures Used
- Search protocol table.
- Screening flow diagram if used.

### Risk
The method may appear informal if search and screening decisions are not logged.

### Quality Check
Are the search and screening decisions traceable enough for a review journal?

## Section 3: What Makes ASR Low-Resource?

### Purpose
Define low-resource ASR beyond limited labeled hours.

### Main Argument
Low-resource ASR is a multidimensional condition shaped by labeled-data scarcity, weak validation, dialect and domain mismatch, orthography, noise, code-switching, licensing, and compute constraints.

### Evidence Needed
- Low-resource ASR challenge papers.
- Dataset and benchmark studies.
- Orthography and transcript-normalization studies.

### Tables/Figures Used
- Challenge-solution matrix.
- Dataset benchmark matrix.

### Risk
The section may become generic background instead of explaining why low-resource conditions change method choice and evaluation reliability.

### Quality Check
Does the section directly answer RQ1?

## Section 4: From Hybrid ASR to Foundation Speech Models

### Purpose
Explain how ASR model families evolved and why foundation models changed the low-resource starting point.

### Main Argument
Hybrid, end-to-end, SSL, multilingual, weakly supervised, and foundation models represent changing assumptions about labeled data, transfer, language coverage, and adaptation.

### Evidence Needed
- Hybrid and E2E ASR background sources.
- SSL foundation papers.
- Multilingual and weakly supervised ASR papers.
- Foundation-model benchmark papers.

### Tables/Figures Used
- Foundation model matrix.
- Taxonomy figure.

### Risk
The section may become a historical model list.

### Quality Check
Does the section compare model families by assumptions, evidence, and low-resource limitations?

## Section 5: Resources and Benchmarks

### Purpose
Compare datasets, benchmarks, and resource infrastructures used for low-resource ASR.

### Main Argument
Dataset availability alone is insufficient; transcription quality, metadata, dialect coverage, domain coverage, access conditions, and normalization rules shape what benchmarks can prove.

### Evidence Needed
- Dataset papers.
- Benchmark comparison studies.
- Documentation for public and restricted corpora.

### Tables/Figures Used
- Dataset benchmark matrix.
- Search protocol table if relevant.

### Risk
The section may list datasets without critiquing their evaluation implications.

### Quality Check
Does the section connect resources and benchmarks to RQ1, RQ3, and RQ6?

## Section 6: Foundation-Model-Era Taxonomy of Low-Resource ASR

### Purpose
Present the review's six-layer taxonomy for low-resource ASR in the foundation-model era.

### Main Argument
Low-resource ASR should be organized through interacting resource, language, model, adaptation, supervision, and evaluation layers rather than through model families alone.

### Evidence Needed
- Block G cross-block taxonomy matrix.
- Core 60 synthesis anchors.
- Foundation model, adaptation, supervision, and evaluation matrices.

### Tables/Figures Used
- Six-layer taxonomy figure.
- Low-resource ASR challenge taxonomy table.

### Risk
The section may repeat Sections 3-5 instead of abstracting their shared taxonomy.

### Quality Check
Does each taxonomy layer map to the locked RQs, evidence matrices, and later manuscript sections?

## Section 7: Data-Centric Strategies

### Purpose
Analyze corpus creation, normalization, filtering, augmentation, validation, metadata, and benchmark design.

### Main Argument
Data-centric strategies remain necessary because foundation models inherit and expose problems in transcript quality, language coverage, domain mismatch, and evaluation design.

### Evidence Needed
- Corpus construction papers.
- Transcript normalization studies.
- Filtering, augmentation, and validation papers.
- Benchmark-design papers.

### Tables/Figures Used
- Dataset benchmark matrix.
- Challenge-solution matrix.

### Risk
The section may treat data preparation as secondary engineering rather than a central low-resource ASR problem.

### Quality Check
Does the section directly answer RQ3?

## Section 8: Adaptation Strategies

### Purpose
Compare full fine-tuning, continued pretraining, adapters, LoRA, QLoRA, prompting, transfer learning, and adaptation under compute constraints.

### Main Argument
No adaptation strategy is universally best; effectiveness depends on labeled data, unlabeled audio, language relatedness, domain match, model architecture, compute budget, and evaluation target.

### Evidence Needed
- Fine-tuning and continued-pretraining studies.
- Parameter-efficient tuning papers.
- Low-resource adaptation evaluations.
- Compute and reproducibility reports.

### Tables/Figures Used
- Adaptation strategy matrix.
- Foundation model matrix.

### Risk
The section may recommend methods without specifying conditions.

### Quality Check
Does the section directly answer RQ4 and state when each adaptation method is appropriate?

## Section 9: Pseudo-Labeling and Knowledge Distillation

### Purpose
Assess the reliability of pseudo-labeling and KD for low-resource ASR.

### Main Argument
Pseudo-labeling and KD can expand supervision, but their value depends on teacher quality, confidence filtering, disagreement handling, label normalization, and validation under dialect and domain shift.

### Evidence Needed
- Self-training papers.
- Sequence-level KD papers.
- Multi-teacher KD papers.
- Pseudo-label confidence, filtering, and disagreement studies.

### Tables/Figures Used
- Evidence-to-claim matrix.
- Adaptation strategy matrix.

### Risk
The section may treat pseudo-labels as clean labels or present KD as automatically beneficial.

### Quality Check
Does the section directly answer RQ5 and distinguish supervision gains from error propagation?

## Section 10: Evaluation, Reproducibility, and Robustness

### Purpose
Critique how low-resource ASR is evaluated and reported.

### Main Argument
Low-resource ASR progress cannot be judged reliably without protocols that expose dialect, domain, orthographic, speaker, noise, compute, and reproducibility variation.

### Evidence Needed
- Evaluation methodology papers.
- Dialect and domain benchmark papers.
- Reproducibility and compute-reporting studies.
- Robustness testing studies.

### Tables/Figures Used
- Research gap matrix.
- Evidence-to-claim matrix.

### Risk
The section may describe WER/CER without showing what those metrics hide.

### Quality Check
Does the section directly support RQ6?

## Section 11: Multimodal, AVSR, and LLM-Assisted ASR

### Purpose
Examine how robust low-resource ASR may extend toward multimodal AVSR, SpeechLM systems, and LLM-assisted correction, rescoring, contextual biasing, or post-ASR normalization.

### Main Argument
Multimodal, speech-LLM, and LLM-assisted methods are promising for noisy and underrepresented settings, but they introduce new data, privacy, hallucination, over-correction, benchmark leakage, language bias, cost, and evaluation risks.

### Evidence Needed
- AVSR and visual speech recognition papers.
- Speech-language model studies.
- LLM correction and rescoring studies.
- Multimodal robustness evaluations.
- Studies on hallucination, over-correction, data contamination, and language bias in LLM-assisted ASR.

### Tables/Figures Used
- Future direction matrix.
- Research gap matrix.

### Risk
The section may become speculative or borrow claims from non-low-resource settings.

### Quality Check
Does the section separate speech-LLM architectures from post-ASR LLM correction/rescoring, and distinguish demonstrated ASR evidence from future-facing interpretation?

## Section 12: Cross-Block Synthesis and Gap Analysis

### Purpose
Integrate Sections 3-11, the six taxonomy layers, synthesis matrices, and evidence-based gap analysis into a cross-block synthesis.

### Main Argument
Low-resource ASR should be understood through interacting resource, language, model, adaptation, supervision, and evaluation layers rather than through model families alone.

### Evidence Needed
- Completed synthesis matrices.
- Evidence-to-claim matrix.
- Verified references for major claims.

### Tables/Figures Used
- Six-layer taxonomy figure.
- Method comparison matrix.
- Dataset benchmark matrix.
- Foundation model matrix.
- Adaptation strategy matrix.
- Research gap matrix.

### Risk
The section may repeat earlier sections instead of synthesizing them.

### Quality Check
Does the section show interactions across all locked RQs?

## Section 13: Future Research Agenda

### Purpose
Propose a research agenda for reliable low-resource ASR.

### Main Argument
Future work should combine data governance, language-aware adaptation, reliable pseudo-labeling, dialect-aware evaluation, reproducibility, compute efficiency, multimodal robustness, and cautious LLM-assisted methods.

### Evidence Needed
- Research gap matrix.
- Future direction matrix.
- Recent speech-language model and AVSR studies.
- Evidence-to-claim matrix.

### Tables/Figures Used
- Research gap matrix.
- Future direction matrix.

### Risk
The section may become speculative or too closely aligned with thesis interests.

### Quality Check
Is every future direction linked to a demonstrated gap?

## Section 14: Conclusion

### Purpose
Answer the main review question and restate the field-level contribution.

### Main Argument
Foundation speech models have reshaped low-resource ASR, but reliable recognition for underrepresented languages still depends on resource quality, language-aware adaptation, pseudo-label reliability, fair evaluation, reproducibility, and robustness under noisy or multimodal conditions.

### Evidence Needed
- Final evidence-to-claim matrix.
- Completed synthesis and gap matrices.

### Tables/Figures Used
- None required unless final summary figure is added.

### Risk
The conclusion may overstate certainty.

### Quality Check
Does the conclusion synthesize rather than introduce new claims?
