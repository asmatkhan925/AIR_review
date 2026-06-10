#!/usr/bin/env python3
"""Prepare a self-contained ChatGPT handoff package for AIR_review.

The package gives ChatGPT the repository context it needs without relying on
GitHub pages, raw URLs, or APIs. Run from the repository root.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPO_NAME = "asmatkhan925/AIR_review"
OUTPUT_DIR = Path("_chatgpt_handoff")
STATE_FILE = Path(".air_handoff_state.json")

TEXT_EXTENSIONS = {
    ".bib",
    ".cff",
    ".csv",
    ".json",
    ".md",
    ".py",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}

EXCLUDED_PARTS = {
    ".git",
    ".hg",
    ".svn",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pycache__",
    "_chatgpt_handoff",
    "archive_large_files",
    "copyrighted_pdfs",
    "local_pdfs",
    "node_modules",
    "papers_pdf",
    "temp",
    ".tmp",
}

EXCLUDED_NAMES = {
    ".env",
    ".air_handoff_state.json",
}

ALWAYS_INCLUDE = [
    "README.md",
    "AGENTS.md",
    "CITATION.cff",
    "terminology_glossary.txt",
    "00_project_management/decision_log.md",
    "01_scope_and_planning/research_questions.md",
    "01_scope_and_planning/review_methodology.md",
    "02_literature_search/search_log.csv",
    "03_references/citation_verification_log.csv",
    "03_references/references.bib",
    "05_synthesis_matrices/seed_paper_map.csv",
    "05_synthesis_matrices/evidence_to_claim_matrix.csv",
    "05_synthesis_matrices/foundation_model_matrix.csv",
    "05_synthesis_matrices/dataset_benchmark_matrix.csv",
    "05_synthesis_matrices/data_centric_strategy_matrix.csv",
    "05_synthesis_matrices/adaptation_strategy_matrix.csv",
    "05_synthesis_matrices/pseudo_labeling_kd_matrix.csv",
    "05_synthesis_matrices/evaluation_robustness_matrix.csv",
    "06_review_outline/section_argument_map.md",
    "07_draft_sections/01_introduction.md",
    "12_manuscript/main_manuscript.md",
]

QUERY_RULES = [
    (
        ("introduction",),
        ["07_draft_sections/01_introduction.md", "12_manuscript/main_manuscript.md"],
    ),
    (
        ("foundation model", "whisper", "mms", "xls-r", "wav2vec", "hubert"),
        [
            "05_synthesis_matrices/foundation_model_matrix.csv",
            "05_synthesis_matrices/seed_paper_map.csv",
            "05_synthesis_matrices/evidence_to_claim_matrix.csv",
            "03_references/references.bib",
        ],
    ),
    (
        ("data", "dataset", "benchmark", "common voice", "fleurs"),
        [
            "05_synthesis_matrices/dataset_benchmark_matrix.csv",
            "05_synthesis_matrices/data_centric_strategy_matrix.csv",
            "02_literature_search/search_log.csv",
        ],
    ),
    (
        ("adaptation", "fine-tuning", "fine tuning", "lora", "adapter", "continued pretraining"),
        ["05_synthesis_matrices/adaptation_strategy_matrix.csv"],
    ),
    (
        ("pseudo-label", "pseudo label", "pseudo-labeling", "distillation", "kd", "teacher"),
        ["05_synthesis_matrices/pseudo_labeling_kd_matrix.csv"],
    ),
    (
        ("evaluation", "robustness", "avsr", "llm", "hallucination", "over-correction", "over correction"),
        ["05_synthesis_matrices/evaluation_robustness_matrix.csv"],
    ),
    (
        ("outline", "structure", "section"),
        [
            "06_review_outline/section_argument_map.md",
            "01_scope_and_planning/research_questions.md",
            "12_manuscript/main_manuscript.md",
        ],
    ),
    (
        ("references", "citation", "bibtex"),
        ["03_references/references.bib", "03_references/citation_verification_log.csv"],
    ),
]

ID_COLUMNS = ["PaperID", "ClaimID", "CitationKey", "SourceID", "DatasetID"]
AIR_CLAIM_IDS = [f"C-F{i}" for i in range(1, 9)]


@dataclass(frozen=True)
class GitInfo:
    commit: str
    short_commit: str
    branch: str
    dirty: bool
    dirty_files: list[str]


def run_git(args: list[str], check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def get_git_info() -> GitInfo:
    commit = run_git(["rev-parse", "HEAD"])
    branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    status = run_git(["status", "--porcelain"], check=False)
    dirty_files = []
    for line in status.splitlines():
        if not line:
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        dirty_files.append(normalize_rel_path(path))
    return GitInfo(
        commit=commit,
        short_commit=commit[:7],
        branch=branch,
        dirty=bool(status),
        dirty_files=sorted(set(dirty_files)),
    )


def normalize_rel_path(path: str | Path) -> str:
    return str(path).replace("\\", "/").strip("/")


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_state(git_info: GitInfo, query: str, timestamp: str, zip_path: str | None) -> None:
    state = {
        "last_handoff_commit": git_info.commit,
        "last_handoff_short_commit": git_info.short_commit,
        "last_handoff_timestamp_utc": timestamp,
        "last_query": query,
        "last_output_zip": zip_path,
    }
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def baseline_from_args(args: argparse.Namespace) -> tuple[str | None, str]:
    if args.since:
        return args.since, f"{args.since}..HEAD"
    state = load_state()
    state_commit = state.get("last_handoff_commit")
    if state_commit:
        return state_commit, f"{state_commit}..HEAD"
    if run_git(["rev-parse", "--verify", "HEAD~1"], check=False):
        return "HEAD~1", "HEAD~1..HEAD"
    return None, "none"


def changed_files_since(baseline: str | None, git_info: GitInfo, explicit_since: bool) -> list[str]:
    changed: set[str] = set()
    if baseline:
        diff_args = ["diff", "--name-only", f"{baseline}..HEAD"] if explicit_since else ["diff", "--name-only", f"{baseline}..HEAD"]
        output = run_git(diff_args, check=False)
        changed.update(normalize_rel_path(line) for line in output.splitlines() if line.strip())
    changed.update(git_info.dirty_files)
    return sorted(path for path in changed if is_safe_text_file(Path(path)))


def is_safe_text_file(path: Path) -> bool:
    rel = normalize_rel_path(path)
    parts = set(Path(rel).parts)
    if parts & EXCLUDED_PARTS:
        return False
    if Path(rel).name in EXCLUDED_NAMES:
        return False
    if Path(rel).suffix.lower() not in TEXT_EXTENSIONS:
        return False
    return Path(rel).is_file()


def list_all_repo_text_files() -> list[str]:
    output = run_git(["ls-files", "--cached", "--others", "--exclude-standard"], check=False)
    files = []
    for line in output.splitlines():
        rel = normalize_rel_path(line)
        if rel and is_safe_text_file(Path(rel)):
            files.append(rel)
    return sorted(set(files))


def query_files(query: str) -> list[str]:
    query_lower = query.lower()
    selected: set[str] = set()
    for keywords, paths in QUERY_RULES:
        if any(keyword in query_lower for keyword in keywords):
            selected.update(paths)
    return sorted(path for path in selected if Path(path).exists() and is_safe_text_file(Path(path)))


def select_files(args: argparse.Namespace, changed_files: list[str]) -> tuple[list[str], list[str]]:
    missing_core = [path for path in ALWAYS_INCLUDE if not Path(path).exists()]
    selected: set[str] = set(path for path in ALWAYS_INCLUDE if Path(path).exists() and is_safe_text_file(Path(path)))
    if args.full:
        selected.update(list_all_repo_text_files())
    elif args.changed_only:
        selected.update(changed_files)
    else:
        selected.update(query_files(args.query or ""))
        selected.update(changed_files)
    return sorted(selected), missing_core


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_type(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".bib": "bibtex",
        ".cff": "citation-file-format",
        ".csv": "csv",
        ".json": "json",
        ".md": "markdown",
        ".py": "python",
        ".tex": "latex",
        ".txt": "text",
        ".yaml": "yaml",
        ".yml": "yaml",
    }.get(suffix, "text")


def file_record(path: str) -> dict:
    real_path = Path(path)
    return {
        "path": path,
        "size": real_path.stat().st_size,
        "sha256": sha256_file(real_path),
        "type": detect_type(real_path),
    }


def result(status: str, check: str, details: str) -> dict:
    return {"status": status, "check": check, "details": details}


def validate_csv(path: Path) -> tuple[dict, list[dict]]:
    results: list[dict] = []
    metadata = {
        "path": normalize_rel_path(path),
        "row_count": 0,
        "column_count": 0,
        "headers": [],
        "sha256": sha256_file(path),
        "duplicate_ids": {},
        "empty_required_fields": {},
        "row_width_errors": [],
    }
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.reader(handle)
            rows = list(reader)
    except csv.Error as exc:
        results.append(result("FAIL", f"{path} parses as CSV", str(exc)))
        return metadata, results
    except UnicodeDecodeError as exc:
        results.append(result("FAIL", f"{path} decodes as UTF-8 CSV", str(exc)))
        return metadata, results

    if not rows:
        results.append(result("WARN", f"{path} has CSV rows", "CSV is empty."))
        return metadata, results

    headers = rows[0]
    metadata["headers"] = headers
    metadata["column_count"] = len(headers)
    data_rows = rows[1:]
    metadata["row_count"] = len(data_rows)

    width_errors = []
    for number, row in enumerate(data_rows, start=2):
        if len(row) != len(headers):
            width_errors.append({"line": number, "expected": len(headers), "actual": len(row)})
    metadata["row_width_errors"] = width_errors
    if width_errors:
        results.append(result("FAIL", f"{path} row widths match header", f"{len(width_errors)} row-width errors."))
    else:
        results.append(result("PASS", f"{path} row widths match header", f"{len(data_rows)} data rows parsed."))

    rows_as_dicts = [dict(zip(headers, row)) for row in data_rows if len(row) == len(headers)]
    id_columns = [column for column in ID_COLUMNS if column in headers]
    for id_column in id_columns:
        seen: set[str] = set()
        duplicates: list[str] = []
        empty_rows: list[int] = []
        for number, row in enumerate(rows_as_dicts, start=2):
            value = (row.get(id_column) or "").strip()
            if not value:
                empty_rows.append(number)
                continue
            if value in seen and value not in duplicates:
                duplicates.append(value)
            seen.add(value)
        if duplicates:
            metadata["duplicate_ids"][id_column] = duplicates
            results.append(result("FAIL", f"{path} duplicate {id_column}", ", ".join(duplicates)))
        else:
            results.append(result("PASS", f"{path} duplicate {id_column}", "No duplicates."))
        if empty_rows:
            metadata["empty_required_fields"][id_column] = empty_rows
            results.append(result("FAIL", f"{path} empty {id_column}", f"Rows: {empty_rows}"))
        else:
            results.append(result("PASS", f"{path} empty {id_column}", "No empty ID fields."))

    if not id_columns:
        results.append(result("PASS", f"{path} duplicate-ID check", "Not applicable; no known ID column found."))

    return metadata, results


def validate_air_targets(selected_files: list[str], csv_metadata: dict[str, dict]) -> list[dict]:
    results: list[dict] = []

    def csv_values(path: str, column: str) -> set[str]:
        real_path = Path(path)
        if not real_path.exists():
            return set()
        with real_path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            return {row.get(column, "").strip() for row in reader}

    seed_path = "05_synthesis_matrices/seed_paper_map.csv"
    eval_path = "05_synthesis_matrices/evaluation_robustness_matrix.csv"
    claims_path = "05_synthesis_matrices/evidence_to_claim_matrix.csv"
    references_path = Path("03_references/references.bib")
    citation_path = Path("03_references/citation_verification_log.csv")

    for path, expected in [(seed_path, {"BF24", "BF25"}), (eval_path, {"BF24", "BF25"})]:
        ids = csv_values(path, "PaperID")
        missing = sorted(expected - ids)
        status = "FAIL" if missing else "PASS"
        details = f"Missing: {', '.join(missing)}" if missing else f"Found {', '.join(sorted(expected))}."
        results.append(result(status, f"{path} contains BF24 and BF25", details))

    claim_ids = csv_values(claims_path, "ClaimID")
    missing_claims = sorted(set(AIR_CLAIM_IDS) - claim_ids)
    results.append(
        result(
            "FAIL" if missing_claims else "PASS",
            f"{claims_path} contains C-F1 through C-F8",
            f"Missing: {', '.join(missing_claims)}" if missing_claims else "Found C-F1 through C-F8.",
        )
    )

    references_ok = references_path.exists() and references_path.stat().st_size > 0
    results.append(
        result(
            "PASS" if references_ok else "FAIL",
            "03_references/references.bib is present and non-empty",
            f"{references_path.stat().st_size} bytes." if references_ok else "Missing or empty.",
        )
    )

    if citation_path.exists():
        results.append(result("PASS", "03_references/citation_verification_log.csv exists", "Citation verification log is present."))
    else:
        results.append(result("WARN", "03_references/citation_verification_log.csv exists", "Citation verification log is missing."))

    csv_failures = [
        path
        for path, metadata in csv_metadata.items()
        if metadata.get("row_width_errors")
    ]
    results.append(
        result(
            "FAIL" if csv_failures else "PASS",
            "All included CSV files parse without row-width errors",
            f"Failures: {', '.join(csv_failures)}" if csv_failures else "No row-width errors detected.",
        )
    )

    return results


def overall_status(results: Iterable[dict]) -> str:
    statuses = [item["status"] for item in results]
    if "FAIL" in statuses:
        return "FAIL"
    if "WARN" in statuses:
        return "WARN"
    return "PASS"


def recommended_reading_order(selected_files: list[str]) -> list[str]:
    preferred = [
        "CHATGPT_HANDOFF.md",
        "AIR_REVIEW_SNAPSHOT_MANIFEST.json",
        "VALIDATION_REPORT.md",
        "USER_QUERY.txt",
        "AGENTS.md",
        "README.md",
        "00_project_management/decision_log.md",
        "01_scope_and_planning/research_questions.md",
        "01_scope_and_planning/review_methodology.md",
        "05_synthesis_matrices/seed_paper_map.csv",
        "05_synthesis_matrices/evidence_to_claim_matrix.csv",
        "05_synthesis_matrices/foundation_model_matrix.csv",
        "05_synthesis_matrices/dataset_benchmark_matrix.csv",
        "05_synthesis_matrices/data_centric_strategy_matrix.csv",
        "05_synthesis_matrices/adaptation_strategy_matrix.csv",
        "05_synthesis_matrices/pseudo_labeling_kd_matrix.csv",
        "05_synthesis_matrices/evaluation_robustness_matrix.csv",
        "06_review_outline/section_argument_map.md",
        "07_draft_sections/01_introduction.md",
        "12_manuscript/main_manuscript.md",
        "03_references/citation_verification_log.csv",
        "03_references/references.bib",
    ]
    available = set(selected_files)
    order = [path for path in preferred if path in available or path in {"CHATGPT_HANDOFF.md", "AIR_REVIEW_SNAPSHOT_MANIFEST.json", "VALIDATION_REPORT.md", "USER_QUERY.txt"}]
    order.extend(path for path in selected_files if path not in order)
    return order


def markdown_validation_report(results: list[dict], csv_metadata: dict[str, dict]) -> str:
    lines = [
        "# Validation Report",
        "",
        "## Checklist",
        "",
        "| Status | Check | Details |",
        "|---|---|---|",
    ]
    for item in results:
        lines.append(f"| {item['status']} | {item['check']} | {item['details']} |")

    lines.extend(["", "## CSV Metadata", ""])
    for path, metadata in sorted(csv_metadata.items()):
        lines.extend(
            [
                f"### `{path}`",
                "",
                f"- Rows: {metadata['row_count']}",
                f"- Columns: {metadata['column_count']}",
                f"- SHA-256: `{metadata['sha256']}`",
                f"- Headers: {', '.join(f'`{header}`' for header in metadata['headers'])}",
                "",
            ]
        )
        if metadata["duplicate_ids"]:
            lines.append(f"- Duplicate IDs: `{json.dumps(metadata['duplicate_ids'], ensure_ascii=False)}`")
        if metadata["empty_required_fields"]:
            lines.append(f"- Empty required fields: `{json.dumps(metadata['empty_required_fields'], ensure_ascii=False)}`")
        if metadata["row_width_errors"]:
            lines.append(f"- Row-width errors: `{json.dumps(metadata['row_width_errors'], ensure_ascii=False)}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def markdown_handoff(
    manifest: dict,
    validation_results: list[dict],
    reading_order: list[str],
) -> str:
    clean_status = "dirty" if manifest["dirty"] else "clean"
    lines = [
        "# ChatGPT Handoff",
        "",
        f"- Repository: `{manifest['repository_name']}`",
        f"- Commit: `{manifest['current_commit']}`",
        f"- Branch: `{manifest['branch']}`",
        f"- Working tree: `{clean_status}`",
        f"- Generated UTC: `{manifest['generated_timestamp_utc']}`",
        "",
        "## User Query",
        "",
        manifest["query_text"] or "(No query supplied.)",
        "",
        "## Files Included",
        "",
    ]
    lines.extend(f"- `{path}`" for path in manifest["selected_files"])
    lines.extend(["", "## Changed Files Since Baseline", ""])
    if manifest["changed_files"]:
        lines.extend(f"- `{path}`" for path in manifest["changed_files"])
    else:
        lines.append("- None detected.")

    lines.extend(
        [
            "",
            "## Validation Checklist",
            "",
            "| Status | Check | Details |",
            "|---|---|---|",
        ]
    )
    for item in validation_results:
        lines.append(f"| {item['status']} | {item['check']} | {item['details']} |")

    lines.extend(["", "## Recommended Reading Order", ""])
    lines.extend(f"{index}. `{path}`" for index, path in enumerate(reading_order, start=1))

    lines.extend(
        [
            "",
            "## Notes For ChatGPT",
            "",
            "- Do not use GitHub or raw GitHub URLs.",
            "- Use this ZIP as the source of truth.",
            "- Start with the manifest, validation report, evidence matrices, and relevant draft/outline files.",
            "- Preserve the review's core argument: foundation models changed the starting point of low-resource ASR but did not solve data quality, mismatch, normalization, adaptation, pseudo-label reliability, evaluation, reproducibility, compute, and robustness challenges.",
            "- Avoid thesis/Pashto drift; Pashto is illustrative only.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_manifest(
    args: argparse.Namespace,
    git_info: GitInfo,
    timestamp: str,
    baseline_label: str,
    selected_files: list[str],
    changed_files: list[str],
    file_records: list[dict],
    csv_metadata: dict[str, dict],
    validation_results: list[dict],
    reading_order: list[str],
) -> dict:
    return {
        "repository_name": REPO_NAME,
        "current_commit": git_info.commit,
        "short_commit": git_info.short_commit,
        "branch": git_info.branch,
        "dirty": git_info.dirty,
        "dirty_files": git_info.dirty_files,
        "generated_timestamp_utc": timestamp,
        "query_text": args.query or "",
        "baseline": baseline_label,
        "selected_files": selected_files,
        "changed_files": changed_files,
        "file_count": len(selected_files),
        "files": file_records,
        "csv_metadata": csv_metadata,
        "validation_results": validation_results,
        "validation_status": overall_status(validation_results),
        "recommended_reading_order": reading_order,
    }


def prepare_output_dir(git_info: GitInfo, timestamp: str) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    handoff_dir = OUTPUT_DIR / f"AIR_review_handoff_{git_info.short_commit}_{timestamp}"
    if handoff_dir.exists():
        shutil.rmtree(handoff_dir)
    handoff_dir.mkdir(parents=True)
    return handoff_dir


def copy_selected_files(handoff_dir: Path, selected_files: list[str]) -> None:
    for rel_path in selected_files:
        src = Path(rel_path)
        dst = handoff_dir / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def write_generated_files(
    handoff_dir: Path,
    query: str,
    manifest: dict,
    validation_report: str,
    handoff_markdown: str,
) -> None:
    (handoff_dir / "USER_QUERY.txt").write_text(query or "", encoding="utf-8")
    (handoff_dir / "AIR_REVIEW_SNAPSHOT_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (handoff_dir / "VALIDATION_REPORT.md").write_text(validation_report, encoding="utf-8")
    (handoff_dir / "CHATGPT_HANDOFF.md").write_text(handoff_markdown, encoding="utf-8")


def create_zip(handoff_dir: Path, git_info: GitInfo, timestamp: str) -> Path:
    zip_path = OUTPUT_DIR / f"AIR_review_handoff_{git_info.short_commit}_{timestamp}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(handoff_dir.rglob("*")):
            if path.is_file():
                archive.write(path, arcname=path.relative_to(handoff_dir))
    return zip_path


def run_validation(selected_files: list[str], missing_core: list[str]) -> tuple[dict[str, dict], list[dict]]:
    csv_metadata: dict[str, dict] = {}
    validation_results: list[dict] = []

    for missing in missing_core:
        validation_results.append(result("WARN", f"Always-include file exists: {missing}", "File is missing and was not packaged."))

    for rel_path in selected_files:
        path = Path(rel_path)
        if path.suffix.lower() == ".csv":
            metadata, results = validate_csv(path)
            csv_metadata[rel_path] = metadata
            validation_results.extend(results)

    validation_results.extend(validate_air_targets(selected_files, csv_metadata))
    return csv_metadata, validation_results


def print_summary(
    zip_path: Path | None,
    handoff_dir: Path | None,
    git_info: GitInfo,
    file_count: int,
    validation_status: str,
) -> None:
    dirty = "yes" if git_info.dirty else "no"
    output_path = zip_path if zip_path else handoff_dir
    print("Created ChatGPT handoff:")
    print(f"ZIP: {zip_path.as_posix() if zip_path else '(not requested)'}")
    print(f"Commit: {git_info.commit}")
    print(f"Branch: {git_info.branch}")
    print(f"Dirty: {dirty}")
    print(f"Files included: {file_count}")
    print(f"Validation: {validation_status}")
    print(f"Recommended upload: {output_path.as_posix() if output_path else '(validate-only run)'}")


def validate_only(args: argparse.Namespace) -> int:
    git_info = get_git_info()
    baseline, _ = baseline_from_args(args)
    changed_files = changed_files_since(baseline, git_info, explicit_since=bool(args.since))
    selected_files, missing_core = select_files(args, changed_files)
    csv_metadata, validation_results = run_validation(selected_files, missing_core)
    report = markdown_validation_report(validation_results, csv_metadata)
    print(report)
    status = overall_status(validation_results)
    print(f"Validation: {status}")
    return 1 if status == "FAIL" else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default="", help="Task or question ChatGPT should continue from.")
    parser.add_argument("--zip", action="store_true", help="Create a ZIP package.")
    parser.add_argument("--full", action="store_true", help="Include all safe text-like repository files.")
    parser.add_argument("--since", help="Git baseline for changed-file detection, e.g. HEAD~1.")
    parser.add_argument("--changed-only", action="store_true", help="Include only always-required files and changed files.")
    parser.add_argument("--validate-only", action="store_true", help="Validate selected files without creating a handoff package.")
    args = parser.parse_args(argv)

    try:
        if args.validate_only:
            return validate_only(args)

        git_info = get_git_info()
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        baseline, baseline_label = baseline_from_args(args)
        changed_files = changed_files_since(baseline, git_info, explicit_since=bool(args.since))
        selected_files, missing_core = select_files(args, changed_files)
        csv_metadata, validation_results = run_validation(selected_files, missing_core)
        file_records = [file_record(path) for path in selected_files]
        reading_order = recommended_reading_order(selected_files)
        manifest = build_manifest(
            args=args,
            git_info=git_info,
            timestamp=timestamp,
            baseline_label=baseline_label,
            selected_files=selected_files,
            changed_files=changed_files,
            file_records=file_records,
            csv_metadata=csv_metadata,
            validation_results=validation_results,
            reading_order=reading_order,
        )
        validation_report = markdown_validation_report(validation_results, csv_metadata)
        handoff_markdown = markdown_handoff(manifest, validation_results, reading_order)

        handoff_dir = prepare_output_dir(git_info, timestamp)
        copy_selected_files(handoff_dir, selected_files)
        write_generated_files(handoff_dir, args.query, manifest, validation_report, handoff_markdown)
        zip_path = create_zip(handoff_dir, git_info, timestamp) if args.zip else None

        save_state(git_info, args.query, timestamp, zip_path.as_posix() if zip_path else None)
        print_summary(zip_path, handoff_dir, git_info, len(selected_files), manifest["validation_status"])
        return 1 if manifest["validation_status"] == "FAIL" else 0
    except Exception as exc:  # noqa: BLE001 - CLI should report a clear failure.
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
