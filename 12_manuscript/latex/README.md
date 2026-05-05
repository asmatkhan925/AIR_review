# LaTeX Manuscript Workspace

## Purpose

This folder contains the working Springer Nature LaTeX setup for the Artificial Intelligence Review manuscript.

## Source

The setup uses Springer Nature's official journal article LaTeX package, December 2024 version. The required class file `sn-jnl.cls` and bibliography styles are copied here so the manuscript can compile as a self-contained LaTeX submission folder.

The working document class is:

```tex
\documentclass[pdflatex,sn-basic,iicol]{sn-jnl}
```

This uses the Springer Basic author-year reference style required by Artificial Intelligence Review's author guidelines and the `iicol` option for a double-column Springer layout.

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
- Keep `sn-basic` for AIR-style author-year citations unless the journal office requests a different reference style.
- Keep `iicol` when you want the manuscript to preview the double-column published layout. Remove `iicol` if the submission system or editor asks for a simpler single-column review copy.
- For the actual upload, AIR says not to use subfolders for LaTeX submission files. Keep all `.tex`, `.cls`, `.bst`, `.bib`, and figure files in one flat submission folder or zip.
- Keep the manuscript as one `.tex` file for submission. Avoid `\input{}` in the final submission source.
- Keep generated PDFs and build artifacts out of Git.
- Update `references.bib` from `03_references/references.bib` before serious citation work.
