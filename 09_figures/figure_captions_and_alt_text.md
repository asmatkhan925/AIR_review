# Figure Captions and Alt Text

Status: polished draft, preview exports created. Captions should be inserted during manuscript assembly, not inside the SVG files.

## Figure 1: Foundation-Model-Era Low-Resource ASR Bottleneck Stack

- Proposed manuscript caption: Foundation models shift the low-resource ASR bottleneck rather than eliminate it. Reliable recognition depends on interacting layers of resource quality, language fit, adaptation, supervision, evaluation, robustness, compute, reproducibility, and bounded use of multimodal or LLM-assisted methods.
- Short alt text: A stacked diagram shows foundation speech models above interacting low-resource ASR bottleneck layers, with feedback arrows linking resources, language, adaptation, supervision, evaluation, robustness, compute, and multimodal or LLM risks.
- Target manuscript section: Sections 1, 3, 12, and 13.
- Source specification file: `09_figures/figure_01_bottleneck_stack_spec.md`.
- Evidence source type: Block G synthesis; Sections 3, 4, 12, and 13.
- Status: polished draft; PNG and PDF previews exported in `09_figures/previews/`.

## Figure 2: Six-Layer Taxonomy of Low-Resource ASR

- Proposed manuscript caption: Six-layer taxonomy for low-resource ASR in the foundation-model era. The review treats resources, language conditions, model families, adaptation strategies, supervision sources, and evaluation protocols as interacting evidence layers rather than isolated method categories.
- Short alt text: A six-panel diagram shows Resource, Language, Model, Adaptation, Supervision, and Evaluation layers connected by cross-layer arrows.
- Target manuscript section: Section 6, with reuse in Section 12.
- Source specification file: `09_figures/figure_02_six_layer_taxonomy_spec.md`.
- Evidence source type: Block G taxonomy synthesis; Section 6 and Section 12.
- Status: polished draft; PNG and PDF previews exported in `09_figures/previews/`. The layer-based explanatory note is kept here rather than as a bottom sentence inside the SVG.

## Figure 3: Cross-Block Evidence Flow

- Proposed manuscript caption: Cross-block evidence flow for the review. Resource and language conditions shape model choice, adaptation, and supervision, while evaluation and robustness checks feed back into data design, adaptation comparison, and the future research agenda. Small feedback annotations are kept in the caption/alt-text layer rather than crowded into the SVG.
- Short alt text: A left-to-right flow diagram links resource and language conditions to model, adaptation, and supervision strategies, then to evaluation, robustness, and agenda priorities, with feedback arrows back to earlier blocks.
- Target manuscript section: Sections 4, 8, 10, and 12.
- Source specification file: `09_figures/figure_03_cross_block_evidence_flow_spec.md`.
- Evidence source type: Block G cross-block synthesis; Sections 8, 10, and 12.
- Status: polished draft; PNG and PDF previews exported in `09_figures/previews/`.

## Figure 4: Future Agenda Map for Reliable Low-Resource ASR

- Proposed manuscript caption: Future research agenda for reliable low-resource ASR. The agenda clusters research priorities around documented gaps in definitions, resource documentation, benchmark design, adaptation comparability, pseudo-label reliability, evaluation, AVSR and multimodal robustness, constrained LLM assistance, reproducibility, and deployment.
- Short alt text: A radial agenda map centers on reliable low-resource ASR and connects nine surrounding priorities, including documentation, orthography and dialect benchmarks, compute-aware adaptation, reliable pseudo-labeling, AVSR, constrained LLM assistance, reproducibility, and evaluation robustness.
- Target manuscript section: Section 13.
- Source specification file: `09_figures/figure_04_future_agenda_map_spec.md`.
- Evidence source type: Block G gap agenda; Section 13.
- Status: polished draft; PNG and PDF previews exported in `09_figures/previews/`.
