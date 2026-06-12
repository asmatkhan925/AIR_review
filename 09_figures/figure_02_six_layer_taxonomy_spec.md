# Figure 2 Specification: Six-Layer Taxonomy of Low-Resource ASR

## Current Status

- Figure number: Figure 2
- Figure title: Six-layer taxonomy of low-resource ASR in the foundation-model era
- Status: Polished editable SVG draft available; PNG and PDF previews exported; ready for manuscript-level review.
- SVG source: `09_figures/figure_02_six_layer_taxonomy.svg`
- PNG preview: `09_figures/previews/figure_02_six_layer_taxonomy.png`
- PDF preview: `09_figures/previews/figure_02_six_layer_taxonomy.pdf`
- Target manuscript sections: Section 6, with reuse in Section 12
- Primary RQs: RQ1-RQ6, with strongest control function for RQ2, RQ4, RQ5, and RQ6
- Related tables: Table 1 (`08_tables/table_01_low_resource_asr_taxonomy.md`)

## Main Argument and Purpose

The review organizes low-resource ASR in the foundation-model era around six interacting layers: Resource, Language, Model, Adaptation, Supervision, and Evaluation. The figure is the central taxonomy visual and should be used to show cross-layer alignment rather than a method-by-method chronology.

## Visual Content

The polished draft uses six balanced panels around a central `Cross-layer alignment` node:

1. Resource.
2. Language.
3. Model.
4. Adaptation.
5. Supervision.
6. Evaluation.

Compact examples remain inside each panel. The model layer should acknowledge hybrid and end-to-end ASR, SSL and multilingual SSL, weakly supervised ASR, and speech-LLM systems without overcrowding the figure.

## Evidence Boundary Note

This taxonomy is controlled by `05_synthesis_matrices/block_g_cross_block_taxonomy_synthesis_matrix.csv`, Section 6, and Table 1. Emerging SpeechLM, AVSR, and LLM-assisted items may appear as concise examples, but the six-layer definitions must not depend on watchlist-only evidence.

## Caption Control

Use `09_figures/figure_captions_and_alt_text.md` as the caption and alt-text control file. The explanatory statement that the taxonomy is layer-based, not a method list, belongs in the caption or manuscript text rather than as a crowded note inside the SVG.

## Final Production Note

Final journal production may still adjust sizing, line weights, typography, and export format after the manuscript template and figure placement are fixed. The editable SVG remains the source asset.
