# Configuration file for the Sphinx documentation builder.
# For the full list of options see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design',
]

autosummary_generate = True

source_suffix = ['.rst']

master_doc = 'index'

# General information about the project.
from dwave.theme import __version__

project = 'dwave-theme'
copyright = '2026, D-Wave'
author = 'D-Wave'
version = __version__
release = __version__

exclude_patterns = ['_build']

language = 'en'

pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "collapse_navigation": True,
    "show_prev_next": False,
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'dwave': ('https://docs.dwavequantum.com/en/latest/', None),
}

doctest_global_setup = """
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
"""

doctest_global_cleanup = """
import matplotlib.pyplot as plt
plt.close("all")
"""
