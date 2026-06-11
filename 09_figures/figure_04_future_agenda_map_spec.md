# Figure 4 Specification: Future Agenda Map for Reliable Low-Resource ASR

Purpose: Specification for a future figure supporting Section 13. Source basis: `05_synthesis_matrices/block_g_research_gap_agenda_matrix.csv`, `05_synthesis_matrices/block_g_additional_resource_candidates.csv`, and `07_draft_sections/13_future_research_agenda.md`.

Status: Draft specification only. Do not generate the final image yet.

## Core Message

The future agenda should be grounded in demonstrated gaps rather than speculative technology. Reliable low-resource ASR requires better definitions, better resource documentation, orthography- and dialect-aware benchmarks, compute-aware adaptation, reliable supervision expansion, robust evaluation, bounded multimodal and LLM-assisted methods, reproducibility, and deployability.

## Visual Layout

- Use a radial map or grouped agenda board with the center label: `Reliable low-resource ASR`.
- Arrange agenda clusters around the center:
  - `Definitions and resource conditions`: standardize what low-resource means; report labeled, unlabeled, weak-label, validation, metadata, and compute conditions.
  - `Documentation and metadata`: provenance, consent/licensing, dialect/accent metadata where ethical, validation protocol, access conditions.
  - `Orthography and dialect benchmarks`: transcript conventions, scoring scripts, raw/normalized scores, dialect/accent/domain breakdowns.
  - `Compute-aware adaptation`: matched adaptation comparisons, trainable parameters, memory, hardware, inference cost, forgetting checks.
  - `Reliable pseudo-labeling and KD`: teacher quality, confidence, uncertainty, agreement, filtering thresholds, multi-teacher selection.
  - `Evaluation and robustness`: language-wise, dialect-wise, domain-wise, noise/far-field, fairness, hallucination, reproducibility checks.
  - `AVSR and multimodal robustness`: multilingual and multidialect AVSR resources, modality coverage, missing-modality tests, privacy safeguards.
  - `Constrained LLM assistance`: N-best or lattice grounding, validated context, over-correction tests, semantic preservation, unsupported-insertion checks.
  - `Reproducibility and deployment`: model versions, data splits, scoring scripts, decoding settings, public artifacts, compute/deployment cost.
- Use small connector labels from clusters to the relevant gap families:
  - Definitions/resources: GAP-G1 and GAP-G2.
  - Orthography/dialect benchmarks: GAP-G3 and GAP-G4.
  - Adaptation and compute: GAP-G5, GAP-G6, and GAP-G12.
  - Supervision reliability: GAP-G7 and GAP-G8.
  - LLM/multimodal and robustness: GAP-G9, GAP-G10, and GAP-G11.

## Suggested Caption

Future research agenda for reliable low-resource ASR. The agenda clusters research priorities around documented gaps in definitions, resource documentation, benchmark design, adaptation comparability, pseudo-label reliability, evaluation, AVSR and multimodal robustness, constrained LLM assistance, reproducibility, and deployment.

## Design Notes

- Mark methodological documentation sources as background support, not ASR performance evidence.
- Keep watchlist-only directions visually bounded as future-facing items, especially AVSR, hallucination, contextual ASR, and LLM-assisted correction or rescoring.
- Avoid showing this as a technology roadmap where newer methods automatically supersede earlier controls; the message is evidence discipline.
