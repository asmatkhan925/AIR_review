# Recent 2025-2026 Evidence Gap Summary

## Audit Result

The review has a strong historical and 2020-2024 foundation, but its 2025-2026 evidence is too concentrated for the breadth of its foundation-model-era claims. The main weakness is not the absence of all recent work; it is uneven distribution. Benchmarking and general framing have several recent anchors, while adaptation, pseudo-label reliability, dialect/domain evaluation, recent AVSR, and LLM-assisted ASR rely on fewer current verified sources.

The companion candidate matrix contains 60 records. It separates official venue sources from arXiv watchlist items and does not authorize manuscript citation by itself.

## Sections Requiring the Most Enrichment

| Priority | Section | Main weakness | Needed evidence |
|---:|---|---|---|
| 1 | Section 8: Adaptation Strategies | Recent ASR-specific PEFT evidence is underrepresented. | Verified prompt tuning, LoRA experts, multi-accent LoRA, AdaLoRA, efficient invocation, and compute reporting |
| 1 | Section 9: Pseudo-Labeling and KD | Current reliability claims lean on older anchors. | Multi-ASR fusion, SpeechLLM correction, filtering, unsupervised domain adaptation, self-training, and contemporary KD |
| 1 | Section 10: Evaluation, Reproducibility, and Robustness | Recent dialect, fairness, script, hallucination, and context evaluation is thin. | ML-SUPERB 2.0, accent diversity, geographic metadata, non-monolithic references, script-normalized scoring, and hallucination benchmarks |
| 1 | Section 11: Multimodal, AVSR, and LLM-Assisted ASR | Emerging directions move faster than the current evidence base. | Recent AVSR challenges and efficient AVSR, SpeechLM low-resource tests, LLM correction safeguards, contextual ASR, and source-grounding checks |
| 2 | Section 4: Foundation Speech Models | Recent open and massively multilingual systems are only partially represented. | OWSM v4, AfriHuBERT, Omnilingual ASR, OpusLM, and bounded audio-language-model evidence |
| 2 | Section 5: Resources and Benchmarks | Recent dialect, code-switching, impaired-speech, and regional datasets are absent. | CS-FLEURS, SardinianVoxes, German dialect data, MISP 2025, and community data-collection evidence |
| 2 | Section 13: Future Research Agenda | The agenda is appropriate but needs more current evidence behind its priorities. | 2026 fairness, script normalization, LLM correction, LoRA, KD, and low-resource SpeechLM watchlist evidence |
| 3 | Sections 3, 6, and 12 | Conceptual framing is stable. | Add recent evidence only where it changes taxonomy interpretation or cross-block synthesis |
| 3 | Sections 1 and 14 | These sections should remain concise. | Update only after body enrichment; avoid adding citation lists |

## Existing Tables to Expand After Verification

1. **Table 2, Dataset and Benchmark Comparison**
   - Add ML-SUPERB 2.0 if not already represented at sufficient detail.
   - Screen CS-FLEURS, SardinianVoxes, the German dialect dataset, MISP 2025, and recent regional benchmark candidates.
   - Preserve provenance, language/dialect coverage, transcript policy, domain, and evaluation limitations.

2. **Table 3, Adaptation Strategy Decision Matrix**
   - Add verified 2025 prompt tuning, LoRA language experts, mixture-of-LoRA experts, AdaLoRA, contextual biasing, and selective invocation.
   - Separate parameter count from end-to-end compute, memory, decoding cost, and robustness.
   - Mark direct QLoRA evidence as a remaining gap unless an ASR-specific verified source is found.

3. **Table 4, Pseudo-Labeling and KD Reliability Matrix**
   - Add multi-ASR fusion with SpeechLLM correction, multi-stage filtering, CER estimation for Arabic dialects, MSDA, self-training, delayed KD, and blank-aware CTC KD.
   - Record teacher identity, filtering, retained-data reporting, calibration, disagreement, and subgroup risk.

4. **Table 5, Evaluation and Robustness Checklist**
   - Add accent diversity, dialect metadata, code-switching, hallucination-on-non-speech, contextual ASR, fairness, script normalization, and multiple-valid-reference evaluation.
   - Keep WER/CER as necessary but insufficient metrics.

5. **Table 6, Future Agenda and Reporting Checklist**
   - Add explicit requirements for source-grounded LLM correction, contamination checks, recent-evidence maturity labels, and recency maintenance.

Table 1 does not need immediate expansion. The six-layer taxonomy is already broad enough; new papers should populate its evidence rather than add more layers.

## New Tables to Create

1. **Recent Evidence Verification and Use Matrix**
   - A supplementary or repository-control table derived from the candidate CSV after verification.
   - Columns should distinguish verified-primary, verified-secondary, watchlist, rejected, target section, claim type, and integration status.
   - This should remain separate from the Core 60 unless a formal Core-set revision is approved.

2. **Foundation-Model-Era Adaptation Evidence Table**
   - Create only if Table 3 becomes too compressed.
   - Compare base model, adaptation method, trainable parameters, data condition, language/domain, compute, robustness, and verification status.

3. **LLM/SpeechLM ASR Reliability Table**
   - Create only after enough verified evidence exists.
   - Separate direct ASR, post-ASR correction, rescoring, contextual biasing, pseudo-label refinement, speech translation, and dialogue tasks.
   - Include hallucination, over-correction, leakage, contamination, language bias, and compute safeguards.

## New Figures to Create

1. **Evidence Maturity Map for 2025-2026**
   - Candidate figure after verification, not before.
   - Plot evidence themes against maturity: verified primary, verified secondary, arXiv watchlist, and unresolved.
   - Use it to show where the recent literature is active but not yet stable.

2. **Optional Recency-to-Section Flow**
   - Create only if the maturity map does not sufficiently show manuscript impact.
   - Link recent themes to Sections 4, 5, 8, 9, 10, 11, and 13.

No existing manuscript figure should be replaced during the audit. Figure creation should wait until source verification and manuscript integration decisions are complete.

## Claims Currently Under-Supported by Recent Literature

1. Recent PEFT methods are practical and reliable for low-resource ASR under realistic compute constraints.
2. QLoRA has mature ASR-specific evidence comparable to LoRA or adapters.
3. LLM-assisted correction improves low-resource ASR without dialect erasure, semantic rewriting, contamination, or over-correction.
4. SpeechLLMs generalize reliably to unsupported low-resource languages.
5. Pseudo-label refinement with SpeechLLMs is more reliable than conventional filtering across languages and domains.
6. Recent massively multilingual systems provide uniform quality across long-tail languages, scripts, and dialects.
7. Contemporary AVSR methods are robust in genuinely low-resource, multilingual, and missing-modality conditions.
8. Aggregate WER/CER improvements transfer to dialect, accent, code-switching, impaired-speech, and deployment settings.
9. Recent adaptation papers report enough compute, data provenance, decoding, and subgroup detail for fair comparison.
10. Foundation-model-era benchmarks adequately represent orthographic variation and multiple acceptable transcriptions.

## Integration Rule

Candidates should enter the manuscript only after this order is followed:

`official source verification -> BibTeX -> citation log -> synthesis matrix -> evidence-to-claim mapping -> table update -> manuscript prose -> LaTeX synchronization`

ArXiv watchlist items may inform Section 13 or explicitly labeled emerging-direction discussion, but they must not be the sole support for strong claims.
