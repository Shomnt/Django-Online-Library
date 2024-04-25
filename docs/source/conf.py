# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OnlineLibrary'
copyright = '2024, Алексей Пашков, Егор Корчагин, Екатирина Захарова, Дмитрий Беляев'
author = 'Алексей Пашков, Егор Корчагин, Екатирина Захарова, Дмитрий Беляев'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

# Указываем путь до root-папки проекта Django
# Путь относительно файла conf.py
sys.path.insert(0, os.path.abspath('../../mainsite'))


django_settings = 'mainsite.settings'

extensions = ['sphinxcontrib_django',
              'sphinx.ext.autodoc',]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
