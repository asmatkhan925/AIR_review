# Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era

This repository contains the working materials for a review paper targeted at **Artificial Intelligence Review**.

## Working Title

**Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era: Resources, Adaptation, Evaluation, and Multimodal Robustness**

## Review Identity

This project develops a field-level, critical, taxonomy-based review of low-resource automatic speech recognition (ASR) in the foundation-model era. The review is not a thesis summary and is not limited to Pashto. Pashto ASR may be used selectively as an illustrative low-resource case, especially for issues such as dialect variation, Arabic-derived script normalization, noisy speech, pseudo-label reliability, and multimodal extension.

## Core Argument

Foundation models have changed the starting point of low-resource ASR, but they have not solved low-resource ASR. Remaining bottlenecks include data quality, language and dialect mismatch, orthographic normalization, adaptation strategy, pseudo-label reliability, fair evaluation, reproducibility, compute cost, and robustness under noisy or multimodal conditions.

## Review Type

**Systematic mapping review + critical taxonomy**

The review aims to synthesize recent work, classify methods, compare data-centric and model-centric solutions, identify research gaps, and propose a future research agenda for reliable low-resource ASR.

## Main Contribution Claims

1. A modern taxonomy of low-resource ASR in the foundation-model era.
2. A synthesis of data-centric and model-centric solutions.
3. A critical analysis of adaptation, pseudo-labeling, and knowledge distillation.
4. A discussion of evaluation gaps, including dialect, domain, robustness, fairness, and reproducibility.
5. A future research agenda for multimodal, LLM-assisted, and reliable low-resource ASR.

## Repository Workflow

1. Define scope, research questions, inclusion/exclusion criteria, and search strategy.
2. Search and screen papers from major databases and venues.
3. Extract paper-level metadata into structured matrices.
4. Build taxonomy and comparative synthesis tables.
5. Draft section-by-section in `07_draft_sections/`.
6. Integrate mature sections into `12_manuscript/`.
7. Run quality-control checks before submission.

## Main Folders

- `01_scope_and_planning/`: scope, research questions, contribution statement, inclusion/exclusion criteria.
- `02_literature_search/`: search queries, search logs, screening documentation.
- `03_references/`: BibTeX and citation files.
- `04_paper_notes/`: individual paper notes.
- `05_synthesis_matrices/`: comparative matrices and gap tables.
- `06_review_outline/`: master outline and section plans.
- `07_draft_sections/`: working draft sections.
- `08_tables/`: final manuscript tables.
- `09_figures/`: taxonomy figures, timelines, and conceptual diagrams.
- `10_case_study_pashto/`: optional background material; Pashto should remain illustrative, not central.
- `11_quality_control/`: checklist, reviewer-positioning notes, reproducibility checks.
- `12_manuscript/`: integrated manuscript files and submission package.

## Writing Principles

- Keep the review broad and field-level.
- Prioritize work from 2019 onward, especially 2022–2026.
- Include older foundational studies only when necessary.
- Prefer taxonomy, comparative synthesis, critical analysis, and future directions over paper-by-paper summaries.
- Separate established evidence from interpretation.
- Use Pashto only as an illustrative example, not as the main scope.
- Avoid inflated claims and unsupported statements.
