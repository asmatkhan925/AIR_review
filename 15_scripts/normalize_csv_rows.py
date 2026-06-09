from pathlib import Path
import re


FILES_AND_PATTERNS = {
    "05_synthesis_matrices/seed_paper_map.csv": r"\s+(?=(BA|BB)\d{2},)",
    "03_references/citation_verification_log.csv": r"\s+(?=(BA|BB)\d{2},)",
    "05_synthesis_matrices/dataset_benchmark_matrix.csv": r"\s+(?=BA\d{2},)",
    "05_synthesis_matrices/foundation_model_matrix.csv": r"\s+(?=BB\d{2},)",
    "05_synthesis_matrices/method_comparison_matrix.csv": r"\s+(?=[A-Za-z][^,\n]*,)",
    "05_synthesis_matrices/adaptation_strategy_matrix.csv": r'\s+(?="[^"]+",)',
    "05_synthesis_matrices/evidence_to_claim_matrix.csv": r"\s+(?=C\d+,)",
    "02_literature_search/search_log.csv": r"\s+(?=20\d{2}-\d{2}-\d{2},)",
}


def main() -> None:
    repo = Path(".")

    for rel_path, pattern in FILES_AND_PATTERNS.items():
        path = repo / rel_path
        if not path.exists():
            print(f"Missing: {rel_path}")
            continue

        text = path.read_text(encoding="utf-8").strip()
        if "\n" in text:
            print(f"Skipped (already multiline): {rel_path}")
            continue

        fixed = re.sub(pattern, "\n", text)
        path.write_text(fixed + "\n", encoding="utf-8")
        print(f"Normalized: {rel_path}")


if __name__ == "__main__":
    main()
