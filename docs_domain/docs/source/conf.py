import sys
from pathlib import Path

# чтобы autodoc мог импортировать пакет sales без установки
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

project = "Sales report"
author = "vfibyfhbev"
release = "0.1.0"
language = "ru"

extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns: list[str] = []

html_theme = "alabaster"
