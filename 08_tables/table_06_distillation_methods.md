# Table 06: Distillation Methods

| Distillation type | Teacher type | Student type | Supervision signal | Limitation |
|---|---|---|---|---|
| Frame-level KD | Acoustic model | Compact ASR model | Soft frame outputs | Alignment complexity |
| Sequence-level KD | Encoder-decoder teacher | Student ASR model | Teacher-generated transcript | Pseudo-label errors |
| Multi-teacher KD | Diverse teacher ensemble | Target ASR model | Selected/agreed pseudo-labels | Teacher selection complexity |
| Confidence-filtered pseudo-labeling | Single or multiple teachers | Target model | High-confidence labels | Confidence may be miscalibrated |
