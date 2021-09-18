# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from setuptools_scm import get_version

# -- Project information -----------------------------------------------------

project = 'ansi2html'
copyright = '2021, Ralph Bean, Robin Schneider and various contributors'
author = 'Ralph Bean, Robin Schneider and various contributors'

# The full version, including alpha/beta/rc tags
release = get_version(root='../..', relative_to=__file__)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.doctest',
              'sphinx_rtd_theme']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
