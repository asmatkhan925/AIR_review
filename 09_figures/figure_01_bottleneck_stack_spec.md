# Figure 1 Specification: Foundation-Model-Era Low-Resource ASR Bottleneck Stack

## Current Status

- Figure number: Figure 1
- Figure title: Foundation-model-era low-resource ASR bottleneck stack
- Status: Polished editable SVG draft available; PNG and PDF previews exported; ready for manuscript-level review.
- SVG source: `09_figures/figure_01_bottleneck_stack.svg`
- PNG preview: `09_figures/previews/figure_01_bottleneck_stack.png`
- PDF preview: `09_figures/previews/figure_01_bottleneck_stack.pdf`
- Target manuscript sections: Sections 1, 3, 12, and 13
- Primary RQs: Main RQ, RQ1, RQ2, RQ6
- Related tables: Table 1 (`08_tables/table_01_low_resource_asr_taxonomy.md`), Table 5 (`08_tables/table_05_evaluation_robustness_checklist.md`), Table 6 (`08_tables/table_06_future_agenda_reporting_checklist.md`)

## Main Argument and Purpose

Foundation speech models improve the starting point for low-resource ASR, but they do not remove the reliability bottleneck. The figure shows that remaining constraints interact across resource quality, language fit, adaptation, supervision, evaluation, robustness, reproducibility, compute, and bounded multimodal or LLM-assisted risks/safeguards.

## Visual Content

The polished draft uses a vertical bottleneck stack. A neutral `Foundation speech models` starting node sits above eight bottleneck layers:

1. Resource quality and documentation.
2. Language fit.
3. Adaptation choice.
4. Supervision reliability.
5. Evaluation and comparability.
6. Robustness and deployment.
7. Compute and reporting.
8. Multimodal and LLM risks/safeguards.

Side feedback loops indicate that evaluation and deployment failures should feed back into resource documentation, adaptation choices, and reliability controls.

## Evidence Boundary Note

This is a field-level synthesis figure based on Block G claims and the drafted Sections 3, 4, 12, and 13. It must not be read as a claim that every cited study covers every layer. LLM-assisted and multimodal items are bounded as reliability-sensitive directions, not as solved low-resource ASR methods.

## Caption Control

Use `09_figures/figure_captions_and_alt_text.md` as the caption and alt-text control file. Do not add citations, long captions, or detailed evidence notes inside the SVG.

## Final Production Note

Final journal production may still adjust sizing, line weights, typography, and export format after the manuscript template and figure placement are fixed. The editable SVG remains the source asset.
