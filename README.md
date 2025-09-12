![Top Language](https://img.shields.io/github/languages/top/iporepos/copyme)
![Status](https://img.shields.io/badge/status-development-yellow.svg)
[![Documentation](https://img.shields.io/badge/docs-online-brightgreen)](https://iporepos.github.io/copyme/)
[![Docs Status](https://github.com/iporepos/copyme/actions/workflows/docs.yml/badge.svg)](https://github.com/iporepos/copyme/actions/workflows/docs.yml)


<a logo>
<img src="https://raw.githubusercontent.com/iporepos/copyme/master/docs/figs/logo.png" height="130" width="130">
</a>

---

# copyme

A simple template for python development. 

Use this repository as a template for developing a python library or package. 

---

# Templates

When copying files from this repo, remember that they are templates. So:

1) look for '[CHANGE THIS]' for mandatory modifications;
2) look for '[CHECK THIS]' for possible modifications;
3) look for '[EXAMPLE]' for simple examples (comment or uncomment it if needed);
4) look for '[ADD MORE IF NEDDED]' for possible extra features;
5) placeholders are designated by curly braces: '{replace-this}'.


---

# Configuration Files

This repository relies on several **configuration files** that are essential for the proper functioning of the template. Each file has a specific role, and some of them work together, so they should be edited thoughtfully. Below is an overview of the main configuration files and what you should know about them.

> ![IMPORTANT]
> All config files are commented with recommended actions and extra steps.

## Project configuration 

> file `pyproject.toml`

This is the most important configuration file in the repository. It manages the project’s dependencies, build system, and other settings. Make sure to update this file if you add new dependencies or change the project structure. Proper configuration here is crucial for both development and continuous integration.

## Ignore files by Git

> file `.gitignore`

This file defines which files and folders should be ignored by Git. It is important because it prevents unnecessary or heavy files from being included in commits, keeping the repository clean. You can add patterns here for auxiliary files, large datasets, or temporary outputs that should not be tracked.

## Testing configuration 

> file `tests/conftest.py`

This module contains configurations for the `tests` suite. You are free to modify functions, classes, etc, to fit your development needs. It already includes some pre-defined tests that serve as examples or starting points.

## Sphinx configuration

> file `./docs/conf.py`

This file contains the configuration for [Sphinx](https://www.sphinx-doc.org/en/master/index.html), the documentation builder used in this project. It sets the theme, handles unused modules, and ensures that the documentation builds correctly. Any changes to the project’s structure or modules may require updates to this file to avoid broken documentation builds.

## Docs website configuration 

> file `.github/workflows/docs.yml`

This GitHub Actions workflow automates the build of the documentation website online. It relies on the other configuration files, particularly `pyproject.toml` and `docs/conf.py`. If you modify dependencies or the documentation setup, make sure the workflow still runs correctly. 

> ![IMPORTANT] 
> Some extra steps are required for building the docs online.


---

# Repo layout

A standard python repo may use the following layout. 
This layout is known as `src` layout, since it stores the source code under a `src/{repo}` folder.

> See more on [flat vs src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) 

```txt
copyme/
│
├── LICENSE
├── README.md                     # [CHECK THIS] this file (landing page)
├── .gitignore                    # [CHECK THIS] configuration of git vcs ignoring system
├── pyproject.toml                # [CHECK THIS] configuration of python project
├── MANIFEST.in                   # [CHECK THIS] configuration of source distribution
│
├── .venv/                        # [ignored by git] virtual environment (recommended for development)
│
├── .github/                      # github folder
│    └── workflows/               # folder for continuous integration services
│         └── docs.yml            # [CHECK THIS] configuration file for documentation build and deploy
│
├── src/                          # source code folder
│    └── copyme/                  # [CHANGE THIS] source code root
│         ├── __init__.py         # template init file
│         ├── module.py           # template module
│         ├── ...                 # develop your modules
│         ├── mypackage/          # template package
│         │    ├── __init__.py
│         │    └── submodule.py
│         └── data/               # run-time data
│              └── src_data.csv   # dummy data file
│
├── tests/                        # testing code folder
│    ├── conftest.py              # [CHECK THIS] configuration file of tests
│    ├──unit/                     # unit tests package     
│    │    ├── __init__.py
│    │    └── test_module.py      # template module for unit tests
│    ├── bcmk/                    # benchmarking tests package
│    │    ├── __init__.py               
│    │    └── test_bcmk.py        # template module for benchmarking tests
│    ├── data/                    # test-only data
│    │     ├── test_data.csv
│    │     ├── datasets.csv       # table of remote datasets
│    │     └── dataset1/          # [ignored by git] subfolders in data
│    └── outputs/                 # [ignored by git] tests outputs
│
├── docs/                         # documentation folder
│    ├── about.rst                # info about the repo
│    ├── api.rst                  # api reference using sphinx autodoc
│    ├── conf.py                  # [CHECK THIS] configuration file for sphinx
│    ├── dummy.md                 # markdown docs also works
│    ├── index.rst                # home page for documentation
│    ├── usage.rst                # instructions for using this repo
│    ├── make.bat                 # (optional) sphinx auxiliar file 
│    ├── Makefile                 # (optional) sphinx auxiliar file 
│    ├── figs/                    # figs-only files
│    │    ├── logo.png
│    │    ├── logo.svg
│    │    └── fig1.png               
│    ├── data/                    # docs-only data
│    │    ├── refs.bib
│    │    └── docs.csv
│    ├── generated/               # sphinx created files 
│    ├── _templates/              # [ignored] sphinx created stuff
│    ├── _static/                 # [ignored] sphinx created stuff
│    └── _build/                  # [ignored] sphinx build
│
└── examples/                     # (optional) learning resources 
     ├── examples_01.ipynb    
     └── examples_02.ipynb            

```
