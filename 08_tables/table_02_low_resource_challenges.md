# Table 02: Low-Resource Challenges

| Challenge | Description | Effect on ASR | Common mitigation | Remaining gap |
|---|---|---|---|---|
| Data scarcity | Limited labeled speech | Weak supervised training | SSL, transfer, pseudo-labeling | Quality and domain still matter |
| Dialect variation | Multiple dialects with uneven data | Biased recognition | Dialect-aware training | Fair benchmarks remain limited |
| Orthographic inconsistency | Variable spelling/script normalization | Inflated errors and noisy targets | Normalization | Standards vary by language |
| Domain mismatch | Training differs from deployment | Poor generalization | Fine-tuning, augmentation | Target data may be unavailable |
| Noisy speech | Telephony and environmental noise | Recognition errors | Robust training, AVSR | Noise types vary |
| Compute constraints | Limited training and deployment resources | Inaccessible large models | Distillation, adapters, LoRA | Trade-off with accuracy |
