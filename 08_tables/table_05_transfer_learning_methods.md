# Table 05: Transfer Learning Methods

| Method | Source model | Target adaptation | Strength | Risk |
|---|---|---|---|---|
| Full fine-tuning | Pretrained ASR/SSL model | Update all parameters | Flexible adaptation | Compute cost and overfitting |
| Feature extraction | Frozen encoder | Train downstream head | Efficient | Limited adaptation |
| Adapter tuning | Frozen base model | Train adapters | Parameter efficient | Adapter placement matters |
| LoRA | Large pretrained model | Low-rank updates | Efficient for large models | May underfit some languages |
| Multilingual pretraining | Multilingual source data | Fine-tune target language | Cross-lingual transfer | Negative transfer |
