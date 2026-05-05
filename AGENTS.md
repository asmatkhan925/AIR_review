# AGENTS.md

## Project Role

This repository is a research-workflow environment for a review article on AI methods for low-resource ASR, with Pashto ASR as a focused case study. Agents working here should support systematic literature collection, structured synthesis, rigorous drafting, revision, and manuscript preparation.

## Working Principles

- Keep the project organized as a review-paper workspace, not a general file dump.
- Prefer synthesis over paper-by-paper listing.
- Preserve traceability from search query, to screened paper, to note, to matrix, to draft claim, to final citation.
- Use formal academic prose suitable for a high-quality review journal.
- Treat Pashto ASR as a focused case study that illustrates the broader low-resource ASR problem.
- Keep claims evidence-grounded; mark uncertain statements as TODOs rather than presenting them as facts.
- Do not add fabricated citations, invented results, or unsupported performance claims.

## File Conventions

- Put structured paper notes in `04_paper_notes/<theme>/`.
- Put comparison evidence in `05_synthesis_matrices/` before turning it into manuscript prose.
- Put section-level drafts in `07_draft_sections/`.
- Put integrated manuscript text in `12_manuscript/main_manuscript.md`.
- Put obsolete but potentially useful material in `14_archive/`.
- Keep `03_references/references.bib` clean, deduplicated, and consistent.

## Draft Section Expectations

Each draft section should include:

1. Purpose of the section.
2. Key arguments to develop.
3. Literature to include.
4. Expected tables or figures.
5. Drafting notes.
6. Open questions.

Final prose should use clear topic sentences, comparative framing, limitations, and transitions.

## Review Quality Checklist

Before considering a section complete, verify:

- The section has a clear function in the paper.
- It synthesizes themes rather than listing papers.
- Claims are supported by citations.
- Limitations and trade-offs are explicit.
- The section connects to the overall argument.
- Redundancy with neighboring sections has been reduced.

## Security And Git Hygiene

- Never commit `.ssh/`, credentials, tokens, passwords, or private keys.
- Keep generated PDFs and LaTeX build artifacts out of Git unless explicitly needed.
- Commit logically grouped changes with descriptive messages.
- Use `main` for stable working content; use topic branches for large drafting or literature-search changes.
