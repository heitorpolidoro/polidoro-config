"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

project = "Polidoro Config"
copyright = "2024, Heitor Polidoro"
author = "Heitor Polidoro"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "autodoc2",
    "sphinx_copybutton",
]
myst_enable_extensions = ["colon_fence", "fieldlist"]

# Autodoc2 Configuration
autodoc2_render_plugin = "myst"
autodoc2_packages = ["../pconfig"]

autodoc2_hidden_objects = ["inherited", "dunder", "private"]
autodoc2_sort_names = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
