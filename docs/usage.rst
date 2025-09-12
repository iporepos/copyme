Usage
############################################

.. _quickview:

Quick Overview
********************************************

.. develop some entry notes [CHANGE THIS]:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla mollis tincidunt erat eget iaculis.
Mauris gravida ex quam, in porttitor lacus lobortis vitae.
In a lacinia nisl. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas. Morbi et tempor sem.

.. _installation:

Installation
********************************************

.. develop installation instructions [CHANGE THIS]:

For causal users, add ``copyme`` to a python 3 environment via terminal:

.. code-block:: console

    python -m pip install git+https://github.com/iporepos/copyme.git@main

Now test some basic scripting:

.. code-block:: python

    from copyme import module
    n = module.add(1, 2)
    print(n)
    # Output >>> 3

.. _guides:

Guides
********************************************

.. develop guiding instructions [CHANGE THIS]:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla mollis tincidunt erat eget iaculis.
Mauris gravida ex quam, in porttitor lacus lobortis vitae.
In a lacinia nisl. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas. Morbi et tempor sem.


.. _development:

Development
********************************************

.. develop development instructions [CHANGE THIS]:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla mollis tincidunt erat eget iaculis.
Mauris gravida ex quam, in porttitor lacus lobortis vitae.
In a lacinia nisl. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas. Morbi et tempor sem.

Cloning
============================================
Use your IDE for authenticate in GitHub and clone this repo
in your local system.

.. important::

   Git must be set as the VCS

Alternatively, clone via terminal:

.. code-block:: console

    git clone <this-repository-url>


Setup VENV
--------------------------------------------
For developing, it's recommended to setup a
Virtual Environment (VENV) locally for the repo.

Move to the repo root:

.. code-block:: console

    cd ./path/to/<thislib>

Create a VENV:

.. code-block:: console

    python -m venv .venv

Activate the VENV on Unix:

.. code-block:: console

    source .venv/bin/activate

Activate the VENV on Windows:

.. code-block:: console

    . .venv\Scripts\Activate.ps1

Now, in the VENV session, install all
dependencies in live mode (including dev and docs):

.. code-block:: console

    python -m pip install -e .[dev,docs]

This will install all dependecies needed both for
developing and documentation.

Documentation
============================================

.. develop documentation instructions [CHANGE THIS]:

Documentation-driven development is recommended.
Every feature must be documented with standard
Sphinx (rST) format.

Build docs locally
--------------------------------------------
Use Sphinx for building the documentation website
locally. Run this via terminal:

.. code-block:: console

    sphinx-build -b html .\docs .\docs\_build --write-all

.. important::

   Build documentation under a virtual environment session.


.. note::

   The docs website is generated under ``docs/_build/index.html``


Testing
============================================

.. develop testing instructions [CHANGE THIS]:

Test-driven development is recommended.
Test are splitted in unit tests and benchmark tests.

* Unit tests: short and targeting feature behaviour.
* Benchmark tests: may be longer,
  targeting full performance, including outputs.


Run all tests via terminal:

.. code-block:: console

    python -m unittest discover -s tests -p "test_*.py" -v


For single test module:

.. code-block:: console

    python -m tests.unit.test_module


.. important::

   Run tests under a virtual environment session.


Benchmark tests
--------------------------------------------
Benchmark tests are test related to full-integration
of features, sometimes associated with intput and
output data.

Some benchmark tests will install heavy datasets
from provided URLs.

Enable benchmark tests
--------------------------------------------
For running benchmark tests, they must be enabled.
This is because benchmarks may take too long and
deplete resources for CI services.


Enabling benchmarks on Unix:

.. code-block:: console

    RUN_BENCHMARKS=1


Enabling benchmarks on Windows:

.. code-block:: console

    $env:RUN_BENCHMARKS="1"


Enable large benchmark tests
--------------------------------------------
Large benchmark tests are exceptional large tests.
The same logic applies:

Enabling large benchmark tests on Unix:

.. code-block:: console

    RUN_BENCHMARKS_XXL=1


Enabling large benchmark tests on Windows:

.. code-block:: console

    $env:RUN_BENCHMARKS_XXL="1"

