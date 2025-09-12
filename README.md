![](https://img.shields.io/badge/status-development-red.svg)
![Top Language](https://img.shields.io/github/languages/top/iporepos/copyme)

<a logo>
<img src="https://raw.githubusercontent.com/iporepos/copyme/master/docs/figs/logo.png" height="130" width="130">
</a>

---

# copyme

A simple template for python development. 

Use this repository as a template for developing a python library or package. 

---

# Layout

A standard python repo may use the following layout. 
This layout is known as `src` layout, since it stores the source code under a `src/repo` folder.

```txt
copyme/
│
├── LICENSE
├── README.md                     # [CHECK THIS] this file (landing page)
├── .gitignore                    # [CHECK THIS] configuration of git vcs ignoring system
├── pyproject.toml                # [CHECK THIS] configuration of python project
├── MANIFEST.in                   # [CHECK THIS] configuration of source distribution
├── .venv/                        # [ignored by git] virtual environment (recommended)
│
├── src/                          # source code folder
│    └── copyme/                  # library root
│         ├── __init__.py         # template init file
│         ├── module.py           # template module
│         ├── mypackage/          # template package
│         │    ├── __init__.py
│         │    └── submodule.py
│         └── data/               # run-time data
│
├── tests/                        # testing scripts
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
├── docs/                         # documentation resources  
│    ├── about.rst                # info about the repo
│    ├── api.rst                  # api reference using sphinx autodoc
│    ├── conf.py                  # [CHECK THIS] configuration file for sphinx
│    ├── dummy.md                 # markdown docs also works
│    ├── index.rst                # home page for documentation
│    ├── usage.rst                # instructions for using this repo
│    ├── make.bat                 # sphinx auxiliar file (optional)
│    ├── Makefile                 # sphinx auxiliar file (optional)
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
