# AIR LaTeX Guidelines Check

Checked: 2026-05-06

## Official AIR Page

Artificial Intelligence Review submission guidelines:

`https://link.springer.com/journal/10462/submission-guidelines`

## What AIR Says

- Use LaTeX for manuscript submission; Word is also accepted.
- AIR recommends Springer Nature's LaTeX template.
- Include the original source files, including style files and figures.
- Include a PDF version of the compiled output.
- Online submission compiles uploaded source files into a single PDF for author approval.
- Do not use subfolders for LaTeX submission files, including figures or bibliography files.
- Cite references by author name and year.
- Abstract length: 150 to 250 words.
- Keywords: 4 to 6.

## Template Source

Springer Nature LaTeX Author Support:

`https://www.springernature.com/gp/authors/campaigns/latex-author-support`

Downloaded package:

Springer Nature journal article template package, December 2024 version.

## Repository Decision

There is no separate AIR-only LaTeX class linked from the AIR guideline page. The correct base template is Springer Nature's `sn-jnl` journal article template.

The conservative working manuscript uses:

```tex
\documentclass[pdflatex,sn-basic]{sn-jnl}
```

Reasons:

- `pdflatex`: Springer Nature submission support requires pdflatex-compatible files for Snapp and recommends the pdflatex option for template compilation.
- `sn-basic`: AIR requires author-year citations.

The repository also keeps an optional preview file:

```tex
\documentclass[pdflatex,sn-basic,iicol]{sn-jnl}
```

This is `main_double_column_preview.tex`. It is useful because published AIR articles are double-column, but AIR's guideline page does not explicitly require double-column formatting for submission.

## Submission Packaging Note

When preparing final upload files, copy the manuscript source, `sn-jnl.cls`, needed `.bst` file, `references.bib` or pasted `.bbl`, and all figures into one flat folder or zip. Do not submit nested folders.
