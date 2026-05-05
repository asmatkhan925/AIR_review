# Target Journal Requirements

## Target Journal

Artificial Intelligence Review or a similar high-quality review journal.

## Expected Article Character

- Broad but focused review scope.
- Clear taxonomy and synthesis.
- Critical comparison rather than descriptive listing.
- Strong tables and figures.
- Explicit research gaps and future directions.

## Items To Verify Before Submission

- Current author guidelines.
- Article type and word-count expectations.
- Formatting template.
- Reference style.
- Figure and table format.
- Graphical abstract or highlights requirements.
- Open-access and data availability policies.

## LaTeX Setup

- Working LaTeX source: `12_manuscript/latex/main.tex`.
- Template: Springer Nature journal article LaTeX package, December 2024 version.
- Current document class: `\documentclass[pdflatex,sn-basic,iicol]{sn-jnl}`.
- Rationale: AIR guidelines recommend Springer Nature's LaTeX template and require author-year citations; `iicol` uses the Springer template's double-column option.
- Build command: run `make` from `12_manuscript/latex/`.
- Submission note: Springer Nature guidance says Snapp submissions should compile with `pdflatex` and be compressed into a zip file.
- AIR upload note: do not use subfolders for the actual LaTeX submission files.

## AIR Guideline Findings Checked On 2026-05-06

- AIR says LaTeX submissions are encouraged to use the Springer Nature LaTeX template.
- AIR says the submission should include original source files, including style files and figures, plus a PDF of the compiled output.
- AIR says all source files uploaded online are automatically compiled into a single PDF for author approval.
- AIR says not to use subfolders for LaTeX submission files, including figures or bibliography files.
- AIR references should be cited in text by name and year.
- AIR asks for an abstract of 150 to 250 words and 4 to 6 keywords.

## Notes

Journal requirements can change. Verify the official instructions when preparing the submission package.
