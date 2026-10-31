#!/usr/bin/env python3
"""Build the complete lecture PDF using Pandoc, XeLaTeX, and STIX Two Text.

Run from any directory: python3 scripts/build_lecture_pdf.py
Dependencies: pandoc, xelatex (TeX Live), and the STIX Two Text system font.
"""

from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/inference-engineering-complete-lectures.pdf"
WORK = ROOT / "tmp/pdfs"
REPOSITORY = "https://github.com/chadury2021/100-days-of-inference/blob/main/"


def prepare_text(text: str, source: Path) -> str:
    """Resolve source links for the book and typeset mathematical Unicode."""
    def link(match: re.Match[str]) -> str:
        label, target = match.groups()
        if target.startswith(("http://", "https://", "#")):
            return match[0]
        path, _, fragment = target.partition("#")
        resolved = (source.parent / path).resolve()
        day = re.search(r"day(\d+)/LECTURE\.md$", resolved.as_posix())
        if day:
            destination = f"#day-{int(day[1]):02d}"
        elif resolved.name == "LECTURES.md":
            destination = "#" + (fragment or "course-guide")
        else:
            destination = REPOSITORY + resolved.relative_to(ROOT).as_posix()
        return f"[{label}]({destination})"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    replacements = {
        "—": "-", "–": "-", "‑": "-", "−": "-",
        "√dₖ": r"\(\sqrt{d_k}\)", "√d": r"\(\sqrt{d}\)",
        "x̂": r"\(\hat{x}\)", "Ŵ": r"\(\hat{W}\)",
        "⁻¹": r"\(^{-1}\)", "ᵀ": r"\(^{\mathsf{T}}\)",
        "₁": r"\(_1\)", "ₖ": r"\(_k\)", "ₙ": r"\(_n\)",
        "²": r"\(^2\)", "⁶": r"\(^6\)", "λ": r"\(\lambda\)",
        "∞": r"\(\infty\)", "≈": r"\(\approx\)",
        "×": r"\(\times\)", "→": r"\(\rightarrow\)", "′": r"\(^{\prime}\)",
    }
    for old, new in replacements.items():
        if new.startswith(r"\("):
            new = r"\ensuremath{" + new[2:-2] + "}"
        text = text.replace(old, new)
    return text


def build() -> None:
    for executable in ("pandoc", "xelatex"):
        if not shutil.which(executable):
            raise SystemExit(f"Missing required executable: {executable}")
    WORK.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    header = WORK / "header.tex"
    header.write_text(r"""
\usepackage{fancyhdr}
\usepackage{needspace}
\usepackage{titlesec}
\usepackage{fvextra}
\definecolor{courseink}{HTML}{17354A}
\definecolor{coursegray}{HTML}{536371}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily\color{coursegray}INFERENCE ENGINEERING}
\fancyhead[R]{\small\sffamily\color{coursegray}COMPLETE LECTURE SERIES}
\fancyfoot[L]{\small\color{coursegray}Independent course | 102 lectures}
\fancyfoot[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\headheight}{15pt}
\titleformat{\section}{\Large\bfseries\color{courseink}}{}{0pt}{}
\titleformat{\subsection}{\normalsize\bfseries\color{courseink}}{}{0pt}{}
\titlespacing*{\section}{0pt}{0pt}{14pt}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}
\let\oldsubsection\subsection
\renewcommand{\subsection}{\Needspace{5\baselineskip}\oldsubsection}
\setlength{\emergencystretch}{3em}
\widowpenalty=10000
\clubpenalty=10000
\setcounter{tocdepth}{1}
\AtBeginDocument{\hypersetup{bookmarksdepth=1}}
""", encoding="utf-8")
    parts = [r"""---
title: "Inference Engineering"
subtitle: "The complete 102-day lecture series"
author: "Independent study edition"
date: ""
lang: en-US
documentclass: article
fontsize: 10pt
mainfont: STIX Two Text
mathfont: STIX Two Math
sansfont: Helvetica
monofont: Menlo
geometry:
  - letterpaper
  - top=0.75in
  - bottom=0.7in
  - left=0.8in
  - right=0.8in
colorlinks: true
linkcolor: courseink
urlcolor: courseink
linestretch: 1.04
---

\thispagestyle{empty}

\vspace{1.2cm}

**From token generation to a production inference stack**

Runtime foundations, implementation, serving infrastructure, observability,
multimodal inference, advanced techniques, and a five-day capstone.

Every day includes learning objectives, lecture notes, a worked example,
a lab or implementation assignment, and a comprehension check.

\vfill

This independent course follows a university lecture-and-problem-set format.
It is not affiliated with Stanford University. Days 01-26 refer to the existing
course notebooks; later days supply written student assignments. Numerical
examples are illustrative and are not reported hardware benchmarks.

\clearpage
\tableofcontents
\clearpage

# Course guide {#course-guide}
"""]
    syllabus = ROOT / "LECTURES.md"
    text = syllabus.read_text(encoding="utf-8")
    guide = text.split("## Course guide\n", 1)[1].split("## Daily schedule", 1)[0]
    parts.append(prepare_text(guide, syllabus))
    for day in range(1, 103):
        source = ROOT / f"day{day:02d}/LECTURE.md"
        lines = source.read_text(encoding="utf-8").splitlines()
        lines[0] += f" {{#day-{day:02d}}}"
        # Contents and bookmarks provide navigation in the compiled edition.
        lines = [line for line in lines if not line.startswith(("[Previous lecture]", "[Course schedule]"))]
        parts.append("\n\\clearpage\n\n" + prepare_text("\n".join(lines), source))
    manuscript = WORK / "complete-lectures.md"
    manuscript.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    subprocess.run([
        "pandoc", str(manuscript), "--from=markdown+tex_math_single_backslash-tex_math_dollars",
        "--standalone", "--pdf-engine=xelatex",
        "--include-in-header", str(header), "--output", str(OUTPUT),
        "--resource-path", str(ROOT),
    ], check=True)
    subprocess.run(["python3", str(ROOT / "scripts/validate_lectures.py")], check=True)
    print(OUTPUT)


if __name__ == "__main__":
    build()
