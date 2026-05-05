# AI Review: Low-Resource ASR

This repository supports the development of a comprehensive academic review paper on Artificial Intelligence methods for low-resource automatic speech recognition. The review focuses on the evolution of ASR from classical systems to self-supervised, multilingual, foundation-model, distillation-based, and multimodal approaches. It uses Pashto ASR as a focused case study to examine how data scarcity, dialect variation, noisy speech, orthographic normalization, and evaluation constraints interact in a realistic low-resource language setting.

## Review Topic

**Artificial Intelligence for Low-Resource Speech Recognition: Methods, Challenges, Trends, and Future Directions, with Pashto ASR as a focused case study.**

## Research Motivation

Automatic speech recognition has advanced rapidly through end-to-end modeling, self-supervised speech representation learning, multilingual transfer, large foundation models, and audio-visual learning. However, low-resource languages continue to face persistent barriers: limited labeled data, weak benchmarks, dialect diversity, noisy recordings, inconsistent orthography, and compute constraints. This project is designed to turn those issues into a structured, critical, journal-quality review rather than a paper list.

## Repository Structure

- `00_project_management/`: timelines, task board, decisions, revisions, and reviewer-response notes.
- `01_scope_and_planning/`: scope, research questions, inclusion criteria, journal requirements, contributions, and reader profile.
- `02_literature_search/`: keywords, academic queries, source databases, and screening logs.
- `03_references/`: BibTeX references and curated reference lists.
- `04_paper_notes/`: structured notes grouped by technical theme.
- `05_synthesis_matrices/`: comparison matrices for methods, datasets, challenges, gaps, and future directions.
- `06_review_outline/`: master outline, argument flow, dependency map, and storyline.
- `07_draft_sections/`: section-level draft files with purpose, arguments, literature, and open questions.
- `08_tables/`: planned review tables.
- `09_figures/`: figure plans and per-figure workspaces.
- `10_case_study_pashto/`: focused Pashto ASR case-study materials.
- `11_quality_control/`: checklists for synthesis, citations, redundancy, journal style, and final submission.
- `12_manuscript/`: integrated manuscript, Springer Nature LaTeX setup, abstract, highlights, cover letter, and graphical abstract notes.
- `13_appendices/`: supplementary search protocol, paper list, tables, and abbreviation list.
- `14_archive/`: old drafts, rejected structures, and outdated notes.

## Workflow

1. Define the review scope and research questions.
2. Build keyword groups and reusable search queries.
3. Collect seminal, dataset, survey, and recent papers.
4. Screen papers using explicit inclusion and exclusion criteria.
5. Write structured notes for each paper.
6. Fill synthesis matrices before drafting final prose.
7. Build the taxonomy of methods and challenge-solution map.
8. Draft sections in `07_draft_sections/`.
9. Convert section drafts into integrated manuscript prose.
10. Create tables and figures from the matrices.
11. Revise for argument flow, synthesis, and citation quality.
12. Prepare final submission materials in `12_manuscript/`.

## Literature Search Strategy

Searches should combine core ASR terms, low-resource language terms, method terms, and Pashto-specific terms. Logs in `02_literature_search/` should preserve the search date, database, query, result count, selected papers, and screening decision.

## Drafting Workflow

Each draft section should begin with its purpose, key arguments, literature to include, expected tables or figures, drafting notes, and open questions. Final manuscript prose should be thematic and analytical, not organized as a sequence of individual paper summaries.

## Citation Management

The main BibTeX file is `03_references/references.bib`. Every citation used in draft or manuscript prose should exist there, and every reference should have a clear purpose in the review. Use `03_references/missing_references.md` to track papers mentioned in notes but not yet added to BibTeX.

## LaTeX Workflow

The working Springer Nature LaTeX manuscript is in `12_manuscript/latex/main.tex`. It uses the official Springer Nature journal article template package, December 2024 version, with `sn-jnl.cls` and Springer BibTeX styles stored beside the manuscript for reliable compilation. The current AIR-facing configuration is `\documentclass[pdflatex,sn-basic,iicol]{sn-jnl}`, which gives Springer Basic author-year references and the Springer double-column option.

AIR does not provide a separate AIR-only LaTeX class on its guideline page. Its instructions point authors to Springer Nature's LaTeX template, require original source plus compiled PDF, require author-year citations, and warn not to use subfolders for the actual LaTeX submission upload.

Build from `12_manuscript/latex/`:

```bash
make
```

Generated PDFs and LaTeX build artifacts are ignored by Git. Keep the final submission source self-contained and avoid `\input{}` in the submitted `.tex` file.

## Quality Control

Before moving a section into the manuscript, check that it synthesizes evidence, supports claims, discusses limitations, avoids repetition, and connects to the main review argument. Use `11_quality_control/` before major revisions and before submission.

## Planned Output

The target output is a high-quality review article suitable for a journal such as *Artificial Intelligence Review*, with:

- A taxonomy of AI methods for low-resource ASR.
- A critical synthesis of persistent challenges.
- Comparative analysis across end-to-end, SSL, multilingual, distillation, foundation-model, and multimodal approaches.
- A Pashto ASR case study.
- Research gaps and future directions grounded in evidence.

## Author Notes

Keep the repository traceable. Record important conceptual choices in `00_project_management/decision_log.md`, use structured paper notes, and update synthesis matrices as literature coverage expands.
