.. _usage:

Usage
#######################################################################

.. _quickview:

Overview
***********************************************************************

.. develop some entry notes [CHANGE THIS]:

For casual users, the installation instructions allow quick setup and testing of
basic functionality. Additional resources, including example Jupyter notebooks
and live interactive versions, are available to explore features and usage patterns in detail.

.. seealso::

   For those who want to contribute, see :ref:`Development <development>`


.. _installation:

Installation
***********************************************************************


Install as a Python package
============================================

For Python regular users, install the latest package deploy
to a Python 3 environment via pip:

.. code-block:: console

    python -m pip install copyme

Or any desired branch or version via github url:

.. code-block:: console

    python -m pip install git+https://github.com/iporepos/copyme.git@main

Install in Windows 11
============================================

For users seeking only the tool experience in Windows 11:

1. Make sure the latest Python 3 is installed and added to PATH: https://www.python.org

2. Download the installer PowerShell file ``install-copyme.ps1`` from the GitHub repository;

3. Right-click the installer file and click the option ``Run with PowerShell``;

4. Follow the instructions prompted until the end;

Comments:

The app will live in ``C:\Users\{You}\AppData\Local\copyme``.

To check if the app is alive, open ``PowerShell`` and type:

.. code-block:: console

    copyme check

The output should result in no error or warning.



.. _guides:

Guides
***********************************************************************

.. develop guiding instructions [CHANGE THIS]:

For those seeking practical guidance on using the tools available in the repo, relevant resources are provided.

Example Jupyter notebooks are available in the repository’s examples folder, along with live, interactive versions on platforms such as Google Colab. These resources illustrate the project’s features, demonstrate typical usage patterns, and allow experimentation with the functionality directly.

.. develop guiding resources here [CHANGE THIS]:

Examples
============================================

Develop examples here

A basic script
--------------------------------------------

.. code-block:: python

    from copyme import module


.. code-block:: python

    v = module.add(num1=3, num2=4)


.. code-block:: python

    print(v)
    # [out]: 7


.. [ADD MORE IF NEEDED]

Advanced script
--------------------------------------------

Develop examples here

.. [ADD MORE IF NEEDED]