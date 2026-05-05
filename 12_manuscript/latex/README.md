# LaTeX Manuscript Workspace

## Purpose

This folder contains the working Springer Nature LaTeX setup for the Artificial Intelligence Review manuscript.

## Source

The setup uses Springer Nature's official journal article LaTeX package, December 2024 version. The required class file `sn-jnl.cls` and bibliography styles are copied here so the manuscript can compile as a self-contained LaTeX submission folder.

## Main Files

- `main.tex`: canonical Springer Nature manuscript source.
- `references.bib`: local bibliography file, copied from `03_references/references.bib` when needed.
- `sn-jnl.cls`: Springer Nature journal article class.
- `sn-*.bst`: Springer Nature BibTeX style files.
- `Makefile`: convenience commands for building and cleaning.

## Build

From this folder:

```bash
make
```

Or directly:

```bash
latexmk -pdf -pdflatex="pdflatex %O %S" main.tex
```

## Notes

- Use `pdflatex`, matching Springer Nature submission guidance.
- Keep the manuscript as one `.tex` file for submission. Avoid `\input{}` in the final submission source.
- Keep generated PDFs and build artifacts out of Git.
- Update `references.bib` from `03_references/references.bib` before serious citation work.
