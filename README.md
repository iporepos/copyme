# copyme

![](https://img.shields.io/badge/status-development-red.svg)

A simple template for python development. 

Use this repository as a template for developing a python library or package. 

# Layout

A standard python repo may use the following layout. 
This layout is known as `src` layout, since it stores the source code under a `src/repo` folder.

```bash
copyme/
│
├── LICENSE
├── README.md
├── .gitignore
├── pyproject.toml                # configuration of python project
├── MANIFEST.in                   # configuration of source distribution
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
│    ├── conftest.py              # configuration file of tests
│    ├──unit/                     # unit tests package     
│    │    ├── __init__.py
│    │    └── test_module.py      # template module for unit tests
│    ├── bcmk/                    # benchmarking tests package
│    │    ├── __init__.py               
│    │    └── test_bcmk.py
│    └── data/                    # test-only data
│         ├── test_data.csv
│         ├── outputs/            # [ignored by git] tests outputs
│         └── dataset1/           # [ignored by git] tests outputs
│
├── docs/                         # documentation resources  
│    ├── docs1.md   
│    ├── docsx.rst
│    ├── index.rst             
│    ├── about.rst              
│    ├── usage.rst              
│    ├── api.rst               
│    ├── conf.py                  # configuration file for sphinx
│    ├── make.bat                 # sphinx auxiliar file (optional)
│    ├── Makefile                 # sphinx auxiliar file (optional)
│    ├── figs/                    # figs-only data
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
