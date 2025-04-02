import os
import sys
import gdsfactory as gf
sys.path.insert(0, os.path.abspath(".."))

project = 'PSI TFLN PDK'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'gdsfactory.sphinx.ext']  # includes gdsfactory doc plugin
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
