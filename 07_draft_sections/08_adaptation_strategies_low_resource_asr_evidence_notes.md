# Evidence Notes For Section 8: Adaptation Strategies for Low-Resource ASR

## Scope

This companion note records the evidence used in `07_draft_sections/08_adaptation_strategies_low_resource_asr.md`. Section 8 answers RQ4 by organizing low-resource ASR adaptation strategies around conditions rather than rankings. The main evidence source is `adaptation_strategy_matrix.csv`, supported by `foundation_model_matrix.csv`, `data_centric_strategy_matrix.csv`, `evaluation_robustness_matrix.csv`, Core 60, and Block G controls.

## Block G Controls Used

| Control | Use In Section 8 |
|---|---|
| C-G4 | Main backbone: adaptation effectiveness depends on target-language data, domain mismatch, language relatedness, compute, and forgetting. |
| C-G2 | Links adaptation to the foundation-model-era shift from training from scratch to adapting pretrained systems. |
| C-G3 | Connects adaptation outcomes to data quality, filtering, normalization, and metadata from Section 7. |
| C-G5 | Used only as a bridge to Section 9 for pseudo-labeling and KD after adaptation. |
| C-G6 | Links adaptation claims to evaluation design, subgroup reporting, and WER/CER limits. |
| C-G8 | Supports reproducibility, compute, and future-agenda framing. |
| GAP-G5 | Adaptation comparability gap: data, compute, and forgetting are not standardized. |
| GAP-G6 | PEFT evidence gap: method anchors are strong, but direct ASR evidence is uneven. |
| GAP-G12 | Reproducibility and compute reporting gap. |

## Claim Map

| Section Claim | Section Location | Supporting IDs | Citation Keys Used | Verification Status | Risk Level | RQ Mapping | Linked Block G Claims | Linked Block G Gaps | Evidence Type | Watchlist Boundary |
|---|---|---|---|---|---|---|---|---|---|---|
| Adaptation is conditional: no method is universally best, and the correct choice depends on data, language, model, compute, and evaluation conditions. | 8.1 | C-G4; C-G2; CORE-16; CORE-22; CORE-26; CORE-27; BD04; BD05; BD06; BD07 | `conneau21_interspeech`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms` | Verified-primary-source anchors | Low | RQ2; RQ4; RQ6 | C-G2; C-G4; C-G6 | GAP-G5; GAP-G12 | Interpretive synthesis grounded in Core 60 | No watchlist support used |
| Full fine-tuning and multilingual transfer remain important baselines, but they can overfit, require compute, and hide language/domain failures. | 8.2 | CORE-04; CORE-16; CORE-22; CORE-26; CORE-27; CORE-29; BD04; BD05; BD06; BD07; BD08; BD10 | `conneau21_interspeech`; `babu22_interspeech`; `pmlr-v202-radford23a`; `pratap2024mms`; `shi2023mlsuperb`; `geng25c_interspeech` | Verified-primary-source anchors | Low to medium; single-language case evidence should not be generalized | RQ2; RQ4; RQ6 | C-G2; C-G4; C-G6 | GAP-G5 | Established evidence plus synthesis | No watchlist support used |
| Continued pretraining is useful when relevant unlabeled target-language or domain speech exists, but it depends on data quality, compute, and retention checks. | 8.3 | CORE-30; CORE-41; BD11; BD21 | `getman24_interspeech`; `tian25b_interspeech` | Verified-primary-source anchors | Medium; SpeechLM evidence is broader than ASR-only evidence | RQ2; RQ3; RQ4 | C-G2; C-G3; C-G4 | GAP-G5; GAP-G12 | Established evidence plus bounded interpretation | No watchlist support used |
| PEFT is attractive for low-resource ASR, but Houlsby adapters, LoRA, and QLoRA are method anchors rather than direct ASR proof. | 8.4 | CORE-37; CORE-38; CORE-39; CORE-42; CORE-43; BD01; BD02; BD03; BD22; BD23 | `pmlr-v97-houlsby19a`; `hu2022lora`; `dettmers2023qlora`; `udupa24_interspeech`; `qian24_interspeech` | Method anchors are verified-primary; ASR-specific anchors are verified-primary | Medium; avoid overtransferring NLP evidence to ASR | RQ4; RQ6 | C-G4; C-G8 | GAP-G5; GAP-G6; GAP-G12 | Method-anchor support plus direct ASR evidence | Watchlist PEFT papers excluded from central claims |
| Related-language, phonetic, and language-code adaptation can help when transfer assumptions match the target language, but relatedness can fail under dialect, script, phonological, or domain mismatch. | 8.5 | CORE-16; CORE-22; CORE-29; CORE-40; CORE-43; BD04; BD05; BD09; BD10; BD23 | `conneau21_interspeech`; `babu22_interspeech`; `feng23_interspeech`; `geng25c_interspeech`; `qian24_interspeech` | Verified-primary-source anchors | Medium; donor-language selection remains under-standardized | RQ2; RQ4; RQ6 | C-G2; C-G4; C-G6 | GAP-G5 | Established evidence plus interpretive synthesis | Watchlist donor-selection papers not used centrally |
| Prompting, contextual biasing, and decoder-side adaptation are bounded and emerging; they require leakage, over-correction, and hallucination-aware evaluation. | 8.6 | CORE-26; CORE-30; CORE-60; BD06; BD11; BF20 | `pmlr-v202-radford23a`; `tian25b_interspeech`; `koenecke2024carelesswhisper` | Mixed verified-primary and verified-secondary | Medium to high; direct contextual ASR evidence is mostly emerging | RQ4; RQ6 | C-G4; C-G6; C-G8 | GAP-G5; GAP-G12 | Bounded future-facing synthesis | Watchlist contextual/prompt-tuning papers are not used as central evidence |
| Forgetting, reproducibility, and compute reporting are major adaptation requirements because target-language gains may trade off with prior-language capability and practical deployability. | 8.7 | CORE-11; CORE-37; CORE-38; CORE-39; CORE-43; CORE-54; BD01; BD02; BD03; BD23; BF08 | `qian24_interspeech`; `pmlr-v97-houlsby19a`; `hu2022lora`; `dettmers2023qlora`; `yang2021superb`; `cornell2023chime7` | Mixed verified-primary and verified-secondary | Medium; compute evidence includes method-anchor support | RQ4; RQ6 | C-G4; C-G6; C-G8 | GAP-G5; GAP-G6; GAP-G12 | Established evidence plus reproducibility synthesis | No watchlist support used |
| Adaptation strategy should be chosen from the low-resource condition: label scarcity, unlabeled data, domain mismatch, donor languages, orthography, compute, forgetting, or contextual vocabulary each implies different evidence requirements. | 8.8 | C-G2; C-G3; C-G4; C-G5; C-G6; C-G8; GAP-G5; GAP-G6; GAP-G12; Core 60 adaptation anchors | Citation keys inherited from 8.1-8.7 | Matrix-supported synthesis | Low | RQ3; RQ4; RQ5; RQ6 | C-G2; C-G3; C-G4; C-G5; C-G6; C-G8 | GAP-G5; GAP-G6; GAP-G12 | Interpretive synthesis | No watchlist support used |

## Watchlist Use

The Section 8 draft does not use watchlist-only papers as central evidence. Watchlist PEFT, prompt-tuning, contextual ASR, and depth-aware adaptation entries remain bounded as emerging directions. They are mentioned only as categories of future or cautious interest, not as settled support for central claims.

## PEFT Boundary

Houlsby adapters, LoRA, and QLoRA are used as method anchors. Direct ASR claims rely on ASR-specific evidence such as adapter pre-training or new-language adaptation and forgetting-control work. The draft does not claim that LoRA or QLoRA is proven best for low-resource ASR.

## Duplication Check

The draft does not repeat Section 4's model history or Section 7's data-pipeline discussion. It uses those sections only as setup for adaptation conditions.

## Pashto Drift Check

Pashto is not mentioned in this Section 8 draft. Language-specific evidence is used only as field-level low-resource ASR support.

## Main Manuscript Status

`12_manuscript/main_manuscript.md` should point to this Section 8 draft and evidence-notes file. The full draft has not been pasted into the integrated manuscript.

## Follow-Up Items

- Section 9 should develop pseudo-labeling, KD, teacher quality, and disagreement after this adaptation section.
- Section 10 should expand the evaluation requirements for subgroup reporting, robustness, reproducibility, compute, and metric design.
- Section 13 should reuse the PEFT and compute caveats when building the future agenda.
