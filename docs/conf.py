"""Sphinx configuration for the RoboLens documentation site."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from importlib.metadata import version as _pkg_version
from pathlib import Path

# Make the package importable for autodoc (editable installs already work, but be
# explicit so a clean checkout builds too).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

# -- Project ---------------------------------------------------------------
project = "RoboLens"
author = "RoboLens contributors"
copyright = f"{datetime.now(timezone.utc):%Y}, {author}"
try:
    release = _pkg_version("robolens")
except Exception:  # pragma: no cover
    release = "0.0.0"
version = release

# -- General ---------------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

_HERE = Path(__file__).resolve().parent
# Only register these if present — empty dirs don't survive a git checkout.
templates_path = ["_templates"] if (_HERE / "_templates").is_dir() else []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Markdown (MyST) for the homepage and guides; reStructuredText for API pages.
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "attrs_inline"]
myst_heading_anchors = 3

# -- autodoc / autosummary -------------------------------------------------
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
    "member-order": "bysource",
}
autodoc_typehints = "description"
autodoc_class_signature = "separated"
autodoc_member_order = "bysource"
# We use native Sphinx cross-reference roles in docstrings, not Google/NumPy
# sections, so leave Napoleon's parsers enabled but harmless.
napoleon_google_docstring = True
napoleon_numpy_docstring = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- HTML ------------------------------------------------------------------
html_theme = "furo"
html_title = f"RoboLens {version}"
html_static_path = ["_static"] if (_HERE / "_static").is_dir() else []
# Ship llms.txt / llms-full.txt at the site root for LLM consumers.
html_extra_path = ["_llms"]
html_baseurl = "https://robocurve.github.io/robolens/"

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "source_repository": "https://github.com/robocurve/robolens",
    "source_branch": "main",
    "source_directory": "docs/",
}

# -- OpenGraph (social cards) ----------------------------------------------
ogp_site_url = html_baseurl
ogp_description_length = 200
ogp_enable_meta_description = True
