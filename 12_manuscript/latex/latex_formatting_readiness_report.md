# LaTeX Formatting Readiness Report

Date: 2026-06-12

Starting commit: `a2233d1` (`Run formal manuscript QA audit`)

Scope: synchronize the audited Markdown manuscript (`12_manuscript/main_manuscript.md`)
into the Springer Nature / Artificial Intelligence Review LaTeX workspace
(`12_manuscript/latex/`). This is a formatting conversion, not a rewrite. No new
literature, RQs, contributions, or scholarly claims were added.

## 1. Synchronization Summary

- `main.tex`: synchronized from the audited manuscript (single-column,
  `\documentclass[pdflatex,sn-basic]{sn-jnl}`). Old placeholder section prose was
  fully replaced with the audited Abstract and Sections 1-14.
- `main_double_column_preview.tex`: synchronized to the same content with the
  `iicol` preview option (`\documentclass[pdflatex,sn-basic,iicol]{sn-jnl}`) and
  full-width spanning floats (`table*`/`figure*`). Preview/layout inspection only.
- `references.bib`: synchronized from `03_references/references.bib` (93 entries,
  no duplicate keys). No BibTeX entries were edited.
- Conversion is reproducible via `scripts/sync_manuscript_latex.py`.

## 2. Conversion Method

| Item | Conversion |
|---|---|
| Title | Full working title preserved in `\title[short]{full}`. |
| Abstract | Audited 245-word abstract copied verbatim into `\abstract{...}`. |
| Headings | `## N. X` -> `\section{X}`; `### N.M X` -> `\subsection{X}` (LaTeX numbers naturally). |
| Citations | All `[@a; @b]` -> `\citep{a,b}`. See note below. |
| Figures | `[Figure N about here]` + caption -> `figure` environment with PDF preview. |
| Tables | `[Table N about here]` + caption -> real `tabularx` table built from `08_tables/` sources. |
| Emphasis/quotes | `**bold**` -> `\textbf{}`; straight quotes -> LaTeX `` `` ''. |

Citation-style note: every citation in the audited manuscript is parenthetical
(bracketed `[@...]`); there are no narrative bare `@key` uses. `\citep` is therefore
used consistently for all citations, so no narrative/parenthetical disambiguation
was required. `\citet` is available (natbib author-year via `sn-basic`) if narrative
citations are wanted later.

Table numbering note: the manuscript callouts appear in document order 2, 1, 3, 4,
5, 6 (the dataset table is introduced in Section 5 before the taxonomy table in
Section 6). To keep `Table N` consistent with `08_tables/table_registry.md`, each
table float sets `\setcounter{table}{N-1}` before `\caption`. Figures already appear
in order 1-4 and are counter-pinned for robustness.

## 3. Readiness Checklist

| Item | Status | Notes |
|---|---|---|
| Author name | OK | Asmat Khan (from `CITATION.cff`). |
| Author email | OK | `asmatkhan924@buaa.edu.cn` (matches `CITATION.cff`). |
| Affiliation (institution) | OK | Beihang University, Beijing, China (from buaa.edu.cn). Not invented. |
| Affiliation (department/`\orgdiv`) | BLOCKER | Unknown; left as a LaTeX comment, not rendered. Must be confirmed before submission. |
| Keywords | OK | 6 keywords (within AIR 4-6). Pashto keyword removed to respect the limit and field-level scope. |
| Abstract length | OK | 245 words; within the recorded AIR 150-250 range. |
| Template/class files | OK | `sn-jnl.cls` and `sn-*.bst` present locally in `12_manuscript/latex/`. |
| LaTeX toolchain | OK | `pdflatex`, `latexmk`, `bibtex`, `make` all available. |
| Bibliography | OK | `references.bib` synced (93 entries); 78 keys cited; 0 undefined; 0 duplicate keys. |
| Figure paths | OK (working source) | Relative `../../09_figures/previews/figure_0X_*.pdf` compile locally. Need flat copies for the upload package (AIR forbids subfolders). |
| Table conversion | OK with caveat | All 6 tables converted to real `tabularx` tables. Wide tables (esp. Table 2, 7 columns) produce overfull-hbox warnings and need final layout adjustment. |
| Compile (main.tex) | PASS | 56 pages, exit 0, no undefined references/citations. |
| Compile (preview) | PASS | 45 pages, exit 0, no undefined references/citations. |
| Declarations | BLOCKER | Funding, conflict of interest, data availability, author contributions, ethics — not invented; kept as commented template, not rendered. |

## 4. Compile Status

- `make` (main.tex): PASS — `main.pdf`, 56 pages.
- `make preview` (double-column): PASS — `main_double_column_preview.pdf`, 45 pages.
- Warnings only (no errors): ~31 overfull `\hbox` in single-column main (wide tables),
  ~8 in the double-column preview (mitigated by full-width `table*`), plus benign font
  size-substitution and underfull `\vbox` warnings from float placement.
- Build artifacts (`*.pdf`, `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.fls`,
  `*.fdb_latexmk`) are gitignored and not committed.

## 5. Remaining Formatting Blockers

1. Department/`\orgdiv` for the affiliation is unknown (do not invent).
2. Declarations (funding, conflict of interest, data availability, author
   contributions, ethics) are not yet written (do not invent).
3. Wide tables — particularly Table 2 (7 columns) and the 6-column matrices
   (Tables 3-5) — produce overfull warnings in single-column layout and need final
   layout work (e.g., `sidewaystable`/landscape, column-width tuning, or font sizing).
4. Final word count must be checked inside the journal template.
5. AIR author guidelines should be re-verified at submission time.

Because of items 1-2, this LaTeX source is a credible working source but is NOT
claimed to be final-submission-ready: required author metadata and declarations are
still missing.

## 6. Submission-Package Flattening Plan (separate later task)

AIR/Springer requires a flat upload (no subfolders) and the compiled PDF. A later
submission-package task should:

1. Create one flat folder (e.g., `12_manuscript/submission_package/`).
2. Copy into it, with no subfolders: `main.tex`, `references.bib`, `sn-jnl.cls`, the
   required `sn-*.bst`, and flat copies of the four figure files renamed without
   directory paths (e.g., `figure_01_bottleneck_stack.pdf`).
3. Update `\includegraphics` paths in the flattened `main.tex` to bare filenames.
4. Compile the flattened source end-to-end and verify all four figures resolve.
5. Verify the bibliography compiles (bibtex) with no undefined citations.
6. Include the compiled `main.pdf` for author approval.
7. Complete the affiliation department and the Declarations block first.
8. Zip the flat folder for upload.

Do not create the upload ZIP until the metadata/declarations blockers are resolved.
