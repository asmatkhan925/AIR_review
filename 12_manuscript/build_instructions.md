# Manuscript Build Instructions

## Source Flow

- Main writing source: Markdown drafts in `07_draft_sections/`.
- Integrated manuscript source: `12_manuscript/main_manuscript.md`.
- LaTeX submission source: `12_manuscript/latex/main.tex`.
- Double-column preview source: `12_manuscript/latex/main_double_column_preview.tex`.
- Bibliography source of truth: `03_references/references.bib`.
- Local LaTeX bibliography copy: `12_manuscript/latex/references.bib`.

## Build Commands

From `12_manuscript/latex/`:

```bash
make
```

Double-column preview:

```bash
make preview
```

Synchronize bibliography:

```bash
make sync-bib
```

Clean build artifacts:

```bash
make clean
```

Scan manuscript source for unresolved placeholders:

```bash
make check
```

Check that basic submission source files are present:

```bash
make submission-check
```

Full clean:

```bash
make distclean
```

## Final Submission Packaging

For the actual Springer Nature upload, use a flat folder or ZIP. Do not use subfolders for figures, bibliography, or style files. Copy the final `.tex`, `sn-jnl.cls`, required `.bst`, bibliography or `.bbl`, figure files, and compiled PDF into `12_manuscript/submission_package/` only when preparing the final upload.
