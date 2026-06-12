#!/usr/bin/env python3
"""Synchronize the audited Markdown manuscript into the Springer/AIR LaTeX workspace.

This is a formatting conversion, not a rewriting task. It reads:
  - 12_manuscript/main_manuscript.md   (source of truth for prose, headings, callouts)
  - 08_tables/table_0X_*.md            (manuscript-facing table bodies)
and writes:
  - 12_manuscript/latex/main.tex                       (sn-basic single-column submission source)
  - 12_manuscript/latex/main_double_column_preview.tex (sn-basic + iicol preview source)

All Markdown citations [@a; @b] are converted to author-year \\citep{a,b}. Every
citation in the manuscript is already parenthetical (bracketed), so \\citep is used
consistently; no narrative/parenthetical disambiguation is required.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MS = ROOT / "12_manuscript" / "main_manuscript.md"
TABLES = ROOT / "08_tables"
LATEX = ROOT / "12_manuscript" / "latex"

FIGURE_PATHS = {
    1: "../../09_figures/previews/figure_01_bottleneck_stack.pdf",
    2: "../../09_figures/previews/figure_02_six_layer_taxonomy.pdf",
    3: "../../09_figures/previews/figure_03_cross_block_evidence_flow.pdf",
    4: "../../09_figures/previews/figure_04_future_agenda_map.pdf",
}
TABLE_FILES = {
    1: "table_01_low_resource_asr_taxonomy.md",
    2: "table_02_dataset_benchmark_comparison.md",
    3: "table_03_adaptation_strategy_decision_matrix.md",
    4: "table_04_pseudo_labeling_kd_reliability_matrix.md",
    5: "table_05_evaluation_robustness_checklist.md",
    6: "table_06_future_agenda_reporting_checklist.md",
}

CITE_RE = re.compile(r"\[([^\]]*@[^\]]*)\]")


def convert_citations(text: str) -> str:
    def repl(m):
        keys = [k.strip().lstrip("@").strip() for k in m.group(1).split(";")]
        keys = [k for k in keys if k]
        return r"\citep{" + ",".join(keys) + "}"
    return CITE_RE.sub(repl, text)


def escape_after_cites(text: str) -> str:
    # Minimal escaping. The manuscript prose/cells contain no &, %, or # in
    # practice, and underscores appear only inside citation keys (already inside
    # \citep{} after convert_citations), so underscores are intentionally left raw.
    text = text.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")
    return text


def convert_quotes(text: str) -> str:
    return re.sub(r'"([^"]*)"', r"``\1''", text)


def inline(text: str) -> str:
    """Convert one chunk of inline Markdown to LaTeX (citations, quotes, emphasis)."""
    text = convert_citations(text)
    text = convert_quotes(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = escape_after_cites(text)
    return text


def parse_markdown_table(path: Path):
    """Return (header_cells, rows) from the first pipe-table block in the file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    table_lines = []
    in_table = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("|"):
            in_table = True
            table_lines.append(s)
        elif in_table:
            break
    # Drop the markdown separator row (|---|---|...)
    rows = []
    for tl in table_lines:
        cells = [c.strip() for c in tl.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") and c for c in cells):
            continue
        rows.append(cells)
    header = rows[0]
    body = rows[1:]
    return header, body


def latex_table(num: int, caption_tex: str, starred: bool) -> str:
    header, body = parse_markdown_table(TABLES / TABLE_FILES[num])
    ncols = len(header)
    size = r"\small" if ncols <= 5 else r"\footnotesize"
    colspec = "Y" * ncols
    env = "table*" if starred else "table"

    def fmt_cells(cells):
        return " & ".join(escape_after_cites(convert_citations(c)) for c in cells) + r" \\"

    out = []
    out.append(f"% Table {num} (auto-numbered by LaTeX; counter set for registry consistency)")
    out.append(f"\\begin{{{env}}}[htbp]")
    # Force AIR table numbering: callouts appear in document order 2,1,3,4,5,6,
    # so set the counter explicitly to keep Table N consistent with the registry.
    out.append(f"\\setcounter{{table}}{{{num - 1}}}")
    out.append(size)
    out.append(r"\centering")
    out.append(f"\\caption{{{caption_tex}}}")
    out.append(f"\\label{{tab:{num}}}")
    out.append(f"\\begin{{tabularx}}{{\\textwidth}}{{{colspec}}}")
    out.append(r"\toprule")
    out.append(" & ".join(rf"\textbf{{{escape_after_cites(h)}}}" for h in header) + r" \\")
    out.append(r"\midrule")
    for r in body:
        out.append(fmt_cells(r))
    out.append(r"\bottomrule")
    out.append(r"\end{tabularx}")
    out.append(f"\\end{{{env}}}")
    return "\n".join(out)


def latex_figure(num: int, caption_tex: str, starred: bool) -> str:
    env = "figure*" if starred else "figure"
    return "\n".join([
        f"% Figure {num}",
        f"\\begin{{{env}}}[htbp]",
        f"\\setcounter{{figure}}{{{num - 1}}}",
        r"\centering",
        f"\\includegraphics[width=\\linewidth]{{{FIGURE_PATHS[num]}}}",
        f"\\caption{{{caption_tex}}}",
        f"\\label{{fig:{num}}}",
        f"\\end{{{env}}}",
    ])


def caption_from_paragraph(para: str) -> str:
    """Turn '**Figure 1. Title.** body' into '\\textbf{Title.} body' (LaTeX auto-numbers)."""
    m = re.match(r"\*\*(?:Figure|Table)\s+\d+\.\s*(.+?)\*\*\s*(.*)", para, re.S)
    if not m:
        return inline(para)
    title, rest = m.group(1).strip(), m.group(2).strip()
    title_tex = escape_after_cites(convert_quotes(title))
    rest_tex = inline(rest)
    if rest_tex:
        return rf"\textbf{{{title_tex}}} {rest_tex}"
    return rf"\textbf{{{title_tex}}}"


def build_body(starred_floats: bool):
    raw = MS.read_text(encoding="utf-8")
    # Split into paragraphs on blank lines, preserving structure.
    lines = raw.splitlines()
    # Drop the H1 title line and the Abstract block (handled in the preamble).
    out = []
    i = 0
    # collect abstract separately
    abstract = None
    pending_float = None  # ("figure"|"table", num)
    paragraphs = []
    block = []
    for ln in lines:
        if ln.strip() == "":
            if block:
                paragraphs.append("\n".join(block))
                block = []
        else:
            block.append(ln)
    if block:
        paragraphs.append("\n".join(block))

    body_parts = []
    in_abstract = False
    for para in paragraphs:
        stripped = para.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            continue  # H1 title
        if stripped.startswith("## Abstract"):
            in_abstract = True
            continue
        if in_abstract and not stripped.startswith("#"):
            abstract = inline(stripped)
            in_abstract = False
            continue
        in_abstract = False
        # Headings
        m2 = re.match(r"^##\s+(?:\d+\.\s+)?(.*)$", stripped)
        m3 = re.match(r"^###\s+(?:\d+(?:\.\d+)?\s+)?(.*)$", stripped)
        if m3:
            body_parts.append(rf"\subsection{{{escape_after_cites(convert_quotes(m3.group(1).strip()))}}}")
            continue
        if m2:
            body_parts.append(rf"\section{{{escape_after_cites(convert_quotes(m2.group(1).strip()))}}}")
            continue
        # Float callouts
        mf = re.match(r"^\[Figure (\d+) about here\]$", stripped)
        mt = re.match(r"^\[Table (\d+) about here\]$", stripped)
        if mf:
            pending_float = ("figure", int(mf.group(1)))
            continue
        if mt:
            pending_float = ("table", int(mt.group(1)))
            continue
        # Caption paragraph following a callout
        if pending_float and re.match(r"^\*\*(?:Figure|Table)\s+\d+\.", stripped):
            kind, num = pending_float
            cap = caption_from_paragraph(stripped)
            if kind == "figure":
                body_parts.append(latex_figure(num, cap, starred_floats))
            else:
                body_parts.append(latex_table(num, cap, starred_floats))
            pending_float = None
            continue
        # Normal paragraph
        body_parts.append(inline(stripped))

    return abstract, "\n\n".join(body_parts)


PREAMBLE_PACKAGES = r"""\usepackage{graphicx}
\usepackage{multirow}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{amsthm}
\usepackage{mathrsfs}
\usepackage[title]{appendix}
\usepackage{xcolor}
\usepackage{textcomp}
\usepackage{manyfoot}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{algorithm}
\usepackage{algorithmicx}
\usepackage{algpseudocode}
\usepackage{listings}

\newcolumntype{Y}{>{\raggedright\arraybackslash}X}

\theoremstyle{thmstyleone}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}

\theoremstyle{thmstyletwo}
\newtheorem{example}{Example}
\newtheorem{remark}{Remark}

\theoremstyle{thmstylethree}
\newtheorem{definition}{Definition}

\raggedbottom"""

TITLE = "Automatic Speech Recognition for Low-Resource Languages in the Foundation-Model Era: Resources, Adaptation, Evaluation, and Multimodal Robustness"
SHORT_TITLE = "Low-Resource ASR in the Foundation-Model Era"
KEYWORDS = "low-resource speech recognition, foundation speech models, multilingual ASR, self-supervised learning, model adaptation, ASR evaluation"

# Author metadata. Name and institution are taken from CITATION.cff and the
# buaa.edu.cn (Beihang University) email; the department is unknown and is left
# as a LaTeX comment so no placeholder text renders in the compiled PDF.
AUTHOR_BLOCK = r"""\author*[1]{\fnm{Asmat} \sur{Khan}}\email{asmatkhan924@buaa.edu.cn}

% Department/school is not yet confirmed; complete \orgdiv before submission.
\affil*[1]{\orgname{Beihang University}, \orgaddress{\city{Beijing}, \country{China}}}"""

# Declarations are required by Springer Nature but must not be invented. The block
# is kept commented out so no TODO/placeholder text appears in the compiled PDF;
# the formatting-readiness report tracks these as outstanding metadata items.
DECLARATIONS = r"""% ----------------------------------------------------------------------
% Author metadata to complete before submission (do not invent values):
% \section*{Declarations}
% \subsection*{Funding}            % state funding or that none was received
% \subsection*{Conflict of interest}
% \subsection*{Data availability}
% \subsection*{Author contributions}
% \subsection*{Ethics approval}
% ----------------------------------------------------------------------"""


def build_file(docclass: str, starred_floats: bool, header_comment: str) -> str:
    abstract, body = build_body(starred_floats)
    parts = [
        header_comment,
        "",
        docclass,
        "",
        PREAMBLE_PACKAGES,
        "",
        r"\begin{document}",
        "",
        rf"\title[{SHORT_TITLE}]{{{TITLE}}}",
        "",
        AUTHOR_BLOCK,
        "",
        rf"\abstract{{{abstract}}}",
        "",
        rf"\keywords{{{KEYWORDS}}}",
        "",
        r"\maketitle",
        "",
        body,
        "",
        DECLARATIONS,
        "",
        r"\bibliography{references}",
        "",
        r"\end{document}",
        "",
    ]
    return "\n".join(parts)


MAIN_HEADER = r"""% Version: Springer Nature LaTeX template package, December 2024.
% Target journal: Artificial Intelligence Review.
% Conservative single-column author-year submission source.
% Synchronized from 12_manuscript/main_manuscript.md by scripts/sync_manuscript_latex.py.
% This is a formatting conversion of the audited manuscript; the argument is unchanged.
% Compile from this folder:
%   latexmk -pdf -pdflatex="pdflatex %O %S" main.tex"""

PREVIEW_HEADER = r"""% Version: Springer Nature LaTeX template package, December 2024.
% Double-column preview for Artificial Intelligence Review (layout inspection only).
% Same content as main.tex; adds the iicol class option and uses spanning floats.
% Synchronized from 12_manuscript/main_manuscript.md by scripts/sync_manuscript_latex.py.
% Use main.tex as the conservative submission source.
% Compile from this folder:
%   latexmk -pdf -pdflatex="pdflatex %O %S" main_double_column_preview.tex"""


def main():
    main_tex = build_file(
        r"\documentclass[pdflatex,sn-basic]{sn-jnl}", starred_floats=False,
        header_comment=MAIN_HEADER)
    preview_tex = build_file(
        r"\documentclass[pdflatex,sn-basic,iicol]{sn-jnl}", starred_floats=True,
        header_comment=PREVIEW_HEADER)
    (LATEX / "main.tex").write_text(main_tex, encoding="utf-8")
    (LATEX / "main_double_column_preview.tex").write_text(preview_tex, encoding="utf-8")
    print("Wrote main.tex and main_double_column_preview.tex")


if __name__ == "__main__":
    main()
