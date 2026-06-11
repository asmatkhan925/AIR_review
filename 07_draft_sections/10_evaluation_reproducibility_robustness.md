# 10. Evaluation, Reproducibility, and Robustness

## 10.1 Why Evaluation Becomes Harder After Foundation Models

Foundation models make evaluation more important, not less important. Sections 3-9 show why: low-resource ASR is a multidimensional reliability problem; foundation models improve the starting point; resource quality and transcript conventions shape evidence; adaptation is conditional; and pseudo-labeling can expand supervision while amplifying teacher errors. When baseline accuracy improves, the remaining failures may become less visible in aggregate scores. They may concentrate in particular languages, dialects, domains, scripts, speaker groups, channels, or generation behaviors.

This is the evaluation problem of the foundation-model era. A model that performs well on a pooled benchmark can still fail for a low-resource language variety, noisy channel, orthographic convention, or demographic group. A model that reports better WER can still over-normalize transcripts, hallucinate content, or depend on undocumented decoding and normalization settings. The review therefore treats evaluation as part of the evidence chain, not as a final numeric summary. Reliable low-resource ASR claims require metrics, breakdowns, normalization policies, robustness tests, reproducibility information, compute reporting, and bounded evaluation of generative or contextual behavior.

The central claim of this section is deliberately balanced: WER and CER remain necessary but insufficient when used alone. Multilingual benchmark evidence such as ML-SUPERB, FLEURS, XTREME-S, ML-SUPERB 2.0, and related inclusive benchmark work supports broader comparison, but also shows why language coverage, modeling constraints, and reporting protocols matter [@shi2023mlsuperb; @conneau2022fleurs; @conneau2022xtreme_s; @shi2024mlsuperb2; @chen2025mlsuperb2challenge]. The goal is not to replace standard ASR metrics. It is to surround them with reporting that exposes reliability failures aggregate scores can hide.

## 10.2 WER and CER: Necessary but Insufficient

WER and CER remain useful because ASR needs standardized error measures. They allow comparisons across models, data conditions, and benchmark splits; they make system development measurable; and they provide a common language for reporting recognition quality. Low-resource ASR should not abandon WER or CER. The problem is narrower and more important: WER and CER become misleading when their preprocessing, tokenization, normalization, averaging, and subgroup conditions are hidden.

Pooled WER can hide which language, dialect, speaker group, or domain carries most of the error. Language-level averages can hide whether a model performs well on high-resource or well-represented languages while failing on tail languages. CER can be useful for some scripts and languages, but it does not automatically solve word-boundary, morphology, punctuation, or normalization problems. WER can be sensitive to tokenization, spelling variants, casing, punctuation, and segmentation. Two systems may therefore look comparable while using different scoring conventions or reference transcript policies.

The safest position is to treat WER and CER as baseline metrics that require context. Reports should state whether scores are pooled, macro-averaged, language-wise, dialect-wise, speaker-wise, domain-wise, or normalized. They should document tokenization, punctuation, casing, script handling, and text normalization. Multilingual benchmarks provide necessary shared evaluation infrastructure, but no single benchmark solves low-resource ASR evaluation for every language, domain, and deployment condition [@shi2023mlsuperb; @javed2023indsuperb; @chen2025mlsuperb2challenge]. Standard metrics remain necessary; they just should not be the only evidence.

## 10.3 Orthography-Aware and Normalization-Aware Evaluation

Orthography-aware evaluation is central because low-resource ASR often lacks stable or universally documented transcript conventions. Spelling variation, diacritics, word spacing, punctuation, casing, script choice, morphology, numerals, and abbreviation handling can all affect measured error. These are not minor formatting decisions. They determine what the model is trained to output and what the scorer treats as correct.

Section 7 argued that transcript normalization is part of the data pipeline, and Section 9 showed that pseudo-labels can inherit or impose teacher normalization. Section 10 makes the evaluation consequence explicit: normalization rules must be reported, and raw and normalized scoring may both be informative. Raw scoring can reveal whether a system matches the reference convention. Normalized scoring can reveal whether recognition quality improves after removing conventions that are not central to the task. Neither is universally superior. The appropriate protocol depends on the language, script, task, and deployment setting.

Lenient and orthography-sensitive ASR evaluation evidence shows how naturally occurring spelling variation can distort error rates when scoring does not account for acceptable variants [@karita2023lenient]. Dataset-quality and transcript-formatting evidence also supports the broader claim that punctuation, casing, and transcript consistency affect comparability [@lau2025_data_quality_multilingual_speech; @tian24_interspeech]. The practical requirement is simple: evaluation reports should publish normalization rules, scoring scripts where possible, and enough examples or documentation to make transcript conventions auditable.

## 10.4 Language-, Dialect-, Domain-, and Demographic-Aware Reporting

Low-resource ASR evaluation should report performance at the level where failures matter. For multilingual models, language-wise and macro-averaged results can prevent large languages or high-resource subsets from dominating the interpretation. For inclusive benchmarks, dialect, accent, and language-variety reporting can reveal whether the system serves the communities that motivated the work. For deployment, domain and channel reporting can show whether a model trained or evaluated on clean read speech transfers to conversational, telephony, clinical, classroom, field, broadcast, or far-field speech.

Multilingual and regional benchmark evidence supports this reporting principle. FLEURS, XTREME-S, ML-SUPERB, IndicSUPERB, ML-SUPERB 2.0, and the ML-SUPERB 2.0 Challenge all contribute to broader language or variety-aware evaluation, but each still has scope limits [@conneau2022fleurs; @conneau2022xtreme_s; @shi2023mlsuperb; @javed2023indsuperb; @shi2024mlsuperb2; @chen2025mlsuperb2challenge]. Their value is not that they close the evaluation problem. Their value is that they make language and benchmark structure visible enough for comparison.

Demographic fairness evidence should be handled carefully. Studies on racial disparities in commercial ASR and demographic metadata in conversational speech show that aggregate ASR scores can hide systematic performance differences across speaker groups [@koenecke2020racialdisparities; @liu2021casualconversations]. This is important support for subgroup reporting, but Section 10 is not a fairness-only section. Fairness is one dimension of a larger evaluation problem that also includes language, dialect, accent, domain, channel, orthography, robustness, reproducibility, and compute.

## 10.5 Robustness Under Noise, Far-Field Speech, Conversation, and Channel Shift

Many low-resource ASR use cases are not clean read speech. They involve mobile recordings, telephone speech, far-field microphones, overlapping speakers, noisy environments, conversational turns, code-switching, broadcast audio, clinical interaction, classroom speech, or fieldwork recordings. A model evaluated only on clean benchmark audio may look strong while failing in the actual setting where the language technology is needed.

Robustness benchmarks make this point concrete. CHiME-6 and CHiME-7 style evidence addresses distant, multi-speaker, multi-device, meeting, and diarization-aware ASR conditions that standard clean-speech evaluations do not cover [@watanabe2020chime6; @cornell2023chime7]. These benchmarks are not low-resource-language benchmarks by themselves, so they should be used as robustness evidence rather than as proof of low-resource coverage. Their value is methodological: they show the kinds of scenario differences that ASR evaluation must expose.

For low-resource ASR, robustness reporting should therefore be domain- and channel-aware. If the target use is telephony, conversational, noisy, far-field, or multi-speaker speech, evaluation should include those conditions or explicitly state that it does not. If a system uses data augmentation, continued pretraining, pseudo-labeling, or foundation-model adaptation to handle domain mismatch, the evaluation should test whether the mismatch was actually reduced. Clean-speech WER alone cannot answer that question.

## 10.6 Reproducibility, Compute, and Deployment Reporting

Reproducibility is a major evaluation dimension in foundation-model-era low-resource ASR. A result is difficult to interpret if the model version, training data, adaptation data, decoding settings, tokenization, normalization, hardware, compute budget, trainable parameters, inference cost, random seeds where relevant, split construction, or scoring script are missing. These details are not administrative. They determine whether a reported gain can be reproduced, compared, or deployed.

This requirement is especially important for low-resource languages. Independent evaluation capacity may be limited, datasets may be small or restricted, and large foundation models may be expensive to adapt. Without compute and reproducibility reporting, the field may favor methods that only large labs can run. Parameter-efficient adaptation and compute-aware benchmarks make this issue visible, but they also show why accuracy alone is not enough [@feng2022superbslt]. Speech toolkits such as ESPnet, SpeechBrain, and Kaldi provide reproducibility infrastructure and recipes, but they should be treated as infrastructure support rather than direct evidence that every ASR result is reproducible [@watanabe2018espnet; @ravanelli2021speechbrain; @povey2011kaldi].

A minimal report for low-resource foundation-model ASR should include the base model, checkpoint or version, training and adaptation data, filtering rules, supervised and unsupervised data amounts where available, normalization and tokenization policy, decoding parameters, hardware, training and inference cost where feasible, random seeds or variance reporting when relevant, evaluation splits, and public artifacts where possible. These requirements apply to full fine-tuning, PEFT, continued pretraining, pseudo-labeling, KD, and LLM-assisted correction. Without them, a benchmark score is not enough evidence for reliable progress.

## 10.7 Hallucination, Over-Correction, and Contextual Evaluation

Generative ASR and speech-language-model systems introduce evaluation risks that are not fully captured by WER or CER. A system can produce fluent text that is not supported by the audio, over-correct a speaker's words, insert contextually plausible but false content, or rewrite domain terms. LLM-assisted correction and contextual ASR add related risks: external context can help named entities or terminology, but it can also leak answers, bias decoding, or mask recognition errors.

The central Section 10 point is evaluation, not a full discussion of LLM-assisted ASR. Speech-to-text hallucination evidence shows why unsupported generated content is a serious evaluation concern and why harmful errors may require analysis beyond aggregate WER [@koenecke2024carelesswhisper]. Watchlist evidence on hallucination benchmarks, contextual ASR, and LLM-based ASR correction should be treated only as emerging evaluation motivation, not as settled support for central claims [@frieske2024hallucinations; @koudounas2025shallow; @wang2025contextasrbench; @ma2024asrerrorcorrection]. These watchlist sources are not evidence that these behaviors are universal, but they justify evaluation protocols that can detect unsupported or context-driven errors.

Evaluation protocols for these systems should include checks for unsupported insertions, deletions that alter meaning, over-correction, semantic drift, named-entity accuracy, source grounding, and leakage from prompts or context. If a correction model uses N-best lists, lattices, retrieved context, or external vocabulary, the report should state those constraints. Section 11 will discuss multimodal, SpeechLM, and LLM-assisted systems more fully. Section 10 only establishes the evaluation requirement: generative and contextual ASR must be tested for reliability failures that surface metrics may hide.

## 10.8 Evaluation Protocol Checklist and Decision Matrix

The following decision framework summarizes how evaluation design should follow the risk condition:

- Low-resource language with unstable orthography: report transcript conventions, tokenization, normalization rules, raw and normalized scores where feasible, and examples of difficult variants.
- Multilingual benchmark with many languages: report language-wise and macro-averaged results, not only pooled averages; document language coverage and benchmark constraints.
- Dialect- or accent-sensitive deployment: report performance by dialect, accent, or speaker-community metadata where ethically and practically available.
- Noisy, far-field, or conversational deployment: include robustness tests for noise, overlap, multi-speaker speech, far-field microphones, channel shift, or conversation style.
- Pseudo-labeling or KD pipeline: evaluate teacher errors, filtering thresholds, retained data, normalization policy, and student performance by language or domain.
- Adapted foundation model: report base model version, adaptation data, trainable parameters, decoding settings, forgetting checks where relevant, and target-domain breakdowns.
- Parameter-efficient adaptation under compute constraints: report trainable parameters, memory, training cost, inference cost, and matched full-fine-tuning or fixed-budget comparisons where possible.
- Generative ASR or LLM-assisted correction: evaluate hallucination, over-correction, semantic drift, context leakage, source grounding, and named-entity errors.
- Multimodal or AVSR system: report audio-only, visual-only where appropriate, and audio-visual results under clean and degraded audio conditions.
- Public benchmark comparison: state scoring scripts, preprocessing, model version, decoding settings, data access constraints, and whether results are directly comparable.

[Table placeholder: Evaluation and robustness checklist linking evaluation risk, required breakdown, metric/protocol, evidence source, and reporting requirement.]

## 10.9 Section Takeaway

Evaluation, reproducibility, and robustness determine whether low-resource ASR progress can be trusted. WER and CER remain necessary, but they are not sufficient on their own. Reliable evaluation must expose orthographic, dialectal, domain, demographic, robustness, hallucination, reproducibility, and compute-related failures that aggregate scores can hide.

This section answers RQ6 by converting the review's earlier reliability arguments into evaluation requirements. Section 11 extends the problem further. Once systems move toward multimodal, speech-language-model, and LLM-assisted ASR, evaluation must also handle modality mismatch, hallucination, correction drift, contextual bias, and compute opacity.
