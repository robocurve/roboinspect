"""Generate ``llms.txt`` and ``llms-full.txt`` for LLM consumers.

``llms.txt`` follows the emerging convention (https://llmstxt.org): an H1 title, a
blockquote summary, and curated link sections. ``llms-full.txt`` concatenates the
hand-written guide prose for direct ingestion. Both are written into
``docs/_llms/`` which Sphinx copies to the site root via ``html_extra_path``.

Run before ``sphinx-build`` (the docs workflow does this automatically):

    python docs/gen_llms.py
"""

from __future__ import annotations

from pathlib import Path

BASE = "https://robocurve.github.io/robolens"
DOCS = Path(__file__).resolve().parent
OUT = DOCS / "_llms"

SUMMARY = (
    "RoboLens is the open-source evaluation framework for physical AI and VLA "
    '(vision-language-action) models — the "Inspect AI for robotics". A benchmark '
    "is a Task (dataset of Scenes + scorers) run against two swappable inputs: a "
    "Policy (the VLA) and an Embodiment (a real robot or simulator)."
)

# (relative source page, hosted .html suffix, one-line description)
PAGES: list[tuple[str, str, str]] = [
    ("guide/quickstart.md", "guide/quickstart.html", "Install and run your first evaluation."),
    (
        "guide/concepts.md",
        "guide/concepts.html",
        "Core abstractions: the two inputs, tasks, rollout, scoring, errors.",
    ),
    (
        "guide/writing-a-benchmark.md",
        "guide/writing-a-benchmark.html",
        "Define a Task with scenes, targets, epochs, and scorers.",
    ),
    (
        "guide/policies-and-embodiments.md",
        "guide/policies-and-embodiments.html",
        "Implement a Policy (VLA) and an Embodiment (robot/sim).",
    ),
    (
        "guide/scoring.md",
        "guide/scoring.html",
        "Scorers, epoch reducers, operator/VLM scoring.",
    ),
    (
        "guide/logging-and-rerun.md",
        "guide/logging-and-rerun.html",
        "Eval logs, sinks, Rerun visualization, frame side-cars.",
    ),
    ("guide/plugins.md", "guide/plugins.html", "Registry and entry-point plugins."),
    ("guide/cli.md", "guide/cli.html", "The robolens list/run/inspect commands."),
    ("index.md", "api/index.html", "Auto-generated API reference."),
]


def build_llms_txt() -> str:
    lines = ["# RoboLens", "", f"> {SUMMARY}", "", "## Documentation", ""]
    for _src, html, desc in PAGES:
        title = html.rsplit("/", 1)[-1].removesuffix(".html").replace("-", " ").title()
        lines.append(f"- [{title}]({BASE}/{html}): {desc}")
    lines += [
        "",
        "## Resources",
        "",
        f"- [Full text for LLMs]({BASE}/llms-full.txt): all guide prose in one file.",
        "- [Source](https://github.com/robocurve/robolens): the framework repository.",
        "",
    ]
    return "\n".join(lines)


def build_llms_full() -> str:
    parts = [
        "# RoboLens — full documentation for LLMs",
        "",
        SUMMARY,
        "",
        "---",
        "",
    ]
    sources = ["index.md", *[p for p, _, _ in PAGES if p.startswith("guide/")]]
    seen: set[str] = set()
    for rel in sources:
        if rel in seen:
            continue
        seen.add(rel)
        text = (DOCS / rel).read_text(encoding="utf-8")
        parts.append(text.strip())
        parts.append("\n\n---\n\n")
    return "\n".join(parts)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "llms.txt").write_text(build_llms_txt(), encoding="utf-8")
    (OUT / "llms-full.txt").write_text(build_llms_full(), encoding="utf-8")
    print(f"wrote {OUT / 'llms.txt'} and {OUT / 'llms-full.txt'}")


if __name__ == "__main__":
    main()
