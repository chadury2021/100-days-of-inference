#!/usr/bin/env python3
"""Validate the numbered lecture series and its local Markdown navigation."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DAY_COUNT = 102
REQUIRED_SECTIONS = (
    "Learning objectives",
    "Lecture notes",
    "Board example",
    "Problem set and deliverable",
    "Check your understanding",
)


def heading_ids(text: str) -> set[str]:
    """Return GitHub-style IDs for the plain headings used in this course."""
    counts: dict[str, int] = {}
    ids: set[str] = set()
    for heading in re.findall(r"^#{1,6} (.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        ids.add(f"{slug}-{count}" if count else slug)
        counts[slug] = count + 1
    return ids


def validate() -> list[str]:
    errors: list[str] = []
    schedule_path = ROOT / "LECTURES.md"
    if not schedule_path.is_file():
        return ["Missing LECTURES.md"]
    schedule = schedule_path.read_text(encoding="utf-8")
    rows = re.findall(
        r"^\| Day (\d+) — Lecture (\d+) \| (.*?) \| (.*?) \|$",
        schedule,
        re.MULTILINE,
    )
    expected = [(f"{day:02d}", f"{day:02d}") for day in range(1, DAY_COUNT + 1)]
    if [(day, lecture) for day, lecture, _, _ in rows] != expected:
        errors.append("Schedule must contain Days/Lectures 01–102 exactly once in order")
    titles = {int(day): title for day, _, title, _ in rows}
    actual_notes = {p.relative_to(ROOT).as_posix() for p in ROOT.glob("day*/LECTURE.md")}
    expected_notes = {f"day{day:02d}/LECTURE.md" for day in range(1, DAY_COUNT + 1)}
    if actual_notes != expected_notes:
        errors.append(f"Lecture inventory mismatch: {sorted(actual_notes ^ expected_notes)}")
    files = [schedule_path, ROOT / "README.md"]
    for day in range(1, DAY_COUNT + 1):
        folder = ROOT / f"day{day:02d}"
        lecture = folder / "LECTURE.md"
        overview = folder / "README.md"
        files.extend([lecture, overview])
        if not lecture.is_file():
            continue
        text = lecture.read_text(encoding="utf-8")
        expected_heading = f"# Day {day:02d} — Lecture {day:02d}: {titles.get(day, '')}"
        if text.splitlines()[0] != expected_heading:
            errors.append(f"{lecture.relative_to(ROOT)}: title differs from schedule")
        for section in REQUIRED_SECTIONS:
            if f"\n## {section}\n\n" not in text:
                errors.append(f"{lecture.relative_to(ROOT)}: missing section {section}")
        if not any(f"\n## {name}\n\n" in text for name in ("Notebook lab", "Lab procedure")):
            errors.append(f"{lecture.relative_to(ROOT)}: missing lab")
        navigation = text.splitlines()[2]
        if "[Course schedule](../LECTURES.md)" not in navigation:
            errors.append(f"{lecture.relative_to(ROOT)}: missing course navigation")
        for label, neighbor in (("Previous", day - 1), ("Next", day + 1)):
            if 1 <= neighbor <= DAY_COUNT:
                target = f"[{label} lecture](../day{neighbor:02d}/LECTURE.md)"
                if target not in navigation:
                    errors.append(f"{lecture.relative_to(ROOT)}: missing {label.lower()} navigation")
        if day > 26:
            if "## Further reading" not in text:
                errors.append(f"{lecture.relative_to(ROOT)}: missing further reading")
            preparation = next((line for line in text.splitlines() if "**Preparation:**" in line), "")
            for prerequisite in re.findall(r"\[Day (\d+)\]", preparation):
                if not 1 <= int(prerequisite) < day:
                    errors.append(f"{lecture.relative_to(ROOT)}: invalid prerequisite {prerequisite}")
    for day, _, _, materials in rows:
        if f"./day{int(day):02d}/LECTURE.md" not in materials:
            errors.append(f"Day {day}: schedule does not link its lecture")
    for path in files:
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for raw in re.findall(r"\]\(([^)]+)\)", text):
            link = urlsplit(raw)
            if link.scheme or link.netloc:
                continue
            target = (path.parent / unquote(link.path)).resolve() if link.path else path
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {raw}")
            elif link.fragment and target.is_file() and target.suffix == ".md":
                if unquote(link.fragment) not in heading_ids(target.read_text(encoding="utf-8")):
                    errors.append(f"{path.relative_to(ROOT)}: broken anchor {raw}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("Validated 102 lectures: schedule titles, sections, prerequisites, navigation, and local links/anchors.")
