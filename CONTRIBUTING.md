# Development

This section provides guidance for those who wish to contribute to the project.
It includes instructions for setting up the development environment, cloning the 
repository, installing the project in development mode, running tests, 
and building the documentation.

 To ensure that new features and changes adhere to project standards, 
 maintain quality, and keep the documentation up to date, 
 contributors are required to follow:

* Style-consistent formatting;
* Documentation-oriented practices;
* Test-driven development;


## Minimal Workflow

This is a quick guide for a development protocol. 
Hence, some important but obvious steps are ommited. 
See more details in the sections below.

### Setup

1. Clone the repository to a local branch;

```bash
git clone https://github.com/{username}/{repository}.git
``` 

2. Install dependencies in dev mode:

```bash
python -m pip install -e .[dev,docs]
```

### Development loop

3. Develop features under the ``./src/{repository}/`` folder;
4. Develop unit tests for the features under ``./tests/unit`` or ``./tests/bcmk``;
5. Document features directly using docstrings;
6. Document features in the API by editing ``./docs/api.rst`` file;
7. If ready, proceed to checkout. Repeat otherwise.

### Checkout

8. Apply style:

```bash
black .
```

9. Build docs (locally_:

```bash
python -m docs.build --open
```

10. If previous passed, run all CI-based tests:

```bash
python -m tests.run
```

12. If previous step passed, stage and commit;

```bash
git add .
git commit -m "Message"
```
15. If appropriate, tag and publish.

```bash
git tag -a vX.Y.Z -m "Release X.Y.Z (message)"
git push origin main
```

## Cloning

Use your IDE for authenticate in GitHub and clone the repo branch of interest
in your local system.

```{note}
Of course, Git must be set as the version control system
```

Alternatively, clone via terminal:

```bash
# [CHANGE THIS] set username, repository and (optional) branch
git clone https://github.com/{username}/{repository}.git
``` 

## Installing

For developing, it's recommended to set up a python
**Virtual Environment** (`venv`) locally for developing the repo.
This is best for avoiding falling into a [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell) with your
other projects.

```{important}
Of course, you need Python installed in your system
```

Move to the repo root folder:

```bash
# [CHANGE THIS] set your own actual local path 
cd ./path/to/{thislib}
```

Create a python `venv`:

```bash
python -m venv .venv
```

Activate the `venv` session. On Unix (Linux/Mac):

```bash
source .venv/bin/activate
```
Activate the `venv` on Windows:

```bash
. .venv\Scripts\Activate.ps1
```

Now, under the `venv` session, install all
dependencies in editable mode `-e` (including `dev` and `docs` dependencies with `.[dev, docs]`):

```bash
python -m pip install -e .[dev,docs]
```
This will install all dependecies needed both for
developing and documentation.

---

## Versioning

Versioning system of the project is based on ``git`` and the remote 
is hosted in ``github``. 


### Versioning cycle

Before and after a development session, a health practice is to run:

```bash
git status
```
Considering the status output, add all changed files to the staging area:

```bash
git add .
```
After some substantial development, consider commit 
the changes to the local git system:

```bash
git commit -m "Commit message (eg, 'Bug Fixes')"
```
Repeat the cycle until if feels ready to publish to the remote host.

### Publishing

Before publishing, a health practice is to check the tags available:

```bash
git tag
```
Considering the output, decide a new tag and add it:

```bash
git tag -a vX.Y.Z -m "Release X.Y.Z (message)"
```

After tagging, publish explicitly:

```bash
git push origin main
```
Or simply:
```bash
git push
```


### Tags convention

This project tags follows Semantic Versioning (`vMAJOR.MINOR.PATCH`) 
with the interpretations below.

#### Major `vX.y.z` — Project Maturity Level

- **v0.x.x — Experimental**
  - Playground for exploring architecture and project layout.
  - Breaking changes are expected.

- **v1.x.x — Stable Foundation**
  - Production-ready core architecture.
  - Actively developed.
  - Backward compatibility is expected.

- **v2.x.x — Next Generation**
  - May introduce new syntax or paradigms.
  - Can be incompatible with `v1.x.x`.
  - More mature, better documented, and more stable.

#### Minor `vx.Y.z` — Milestones

- Major feature additions.
- Large refactors within the same architecture.
- Treated as logical restore points.

#### Patch `vx.y.Z` — Maintenance

- Bug fixes.
- Small improvements.
- Documentation corrections.
- No behavioral changes.

### Releases

Releases may receive human-readable names. Recommended pattern:

- **Major version → Theme**
- **Minor version → Theme and item inside that theme**

Example: Mesopotamia CITY — RULER

* v0.1.0 — Uruk Enmerkar
* v0.2.0 — Uruk Gilgamesh
* v1.0.0 — Babylon Hammurabi
* v1.1.0 — Babylon Samsu-iluna
* v1.2.0 — Babylon Abi-Eshuh
* v2.0.0 — Nineveh Sennacherib
* v2.1.0 — Nineveh Esarhaddon

---

## Style

In this project, we enforce using [Black](https://black.readthedocs.io) to ensure a consistent code style. 

Since `black` is listed in dev dependencies, you may run manually before push:

```bash
black .
```
> from the repo root, under the venv session

```{warning}
Unformatted contributions are not going to pass because GitHub checks for style 
consistency.
```

```{seealso}
There are tools for automating `black` before commit. See [https://pre-commit.com/](https://pre-commit.com/)
```

---

## Documentation

Documentation-oriented development is recommended. Every feature must be documented with standard Sphinx (rST) format.

### Build locally

Use Sphinx for building the documentation website locally. Run this via terminal:

```bash
sphinx-build -b html .\docs .\docs\_build --write-all
```

For automating tasks before and after building, consider run:

```bash
python -m docs.build --open
```

```{important}
Build documentation under a virtual environment session.
```

```{note}
The docs website is generated under ``docs/_build``
```


## Testing

Test-driven development is recommended. Tests are split into the following categories:

  * **Unit tests** - short and targeting feature behavior.
  * **Benchmark tests** - may take longer time, targeting full performance, includes inputs and outputs evaluations.
  * **Example tests** - single line tests presented in docstrings.

```{important}
Run tests under a virtual environment session.
```

### Unit tests

Run all unit tests in ``/tests`` via terminal:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

For a single unit test module:

```bash
python -m tests.unit.test_module
```

Alternatively, consider run the utility available in the repository:

```bash
python -m tests.run --which "unit"
```

```{seealso}
See more in [unittest library](https://docs.python.org/3/library/doctest.html) for details on unit tests.
```

```{note}
Example tests can be included in unit tests with their own testing script.
A template for this is provided in ``/tests/test_doctest.py``.
```

### Benchmark tests

Benchmark tests are unit tests related to full-integration of features, 
sometimes associated with input and output data. Some benchmark tests 
will install heavy datasets from provided URLs.

For convenience, consider run the utility available in the repository:

```bash
python -m tests.run --which "bcmk"
```

#### Enable benchmark tests

For running benchmark tests, they must be enabled manually. This is 
because benchmarks may take too long and can deplete resources for CI services. 
Once enabled, just run the unit tests as usual.

Enabling benchmarks on Unix:

```bash
RUN_BENCHMARKS=1
```

Enabling benchmarks on Windows:

```bash
$env:RUN_BENCHMARKS="1"
```

#### Enable large benchmark tests

Large benchmark tests are exceptionally large tests. The same logic applies:

Enabling large benchmark tests on Unix:

```bash
RUN_BENCHMARKS_XXL=1
```

Enabling large benchmark tests on Windows:

```bash
$env:RUN_BENCHMARKS_XXL="1"
```

### Example tests

Create single-line example tests in docstring:

```python
def add(num1, num2):
	"""
	
	**Examples**
	
	>>> add(1, 2)
	3
		
	"""
	return num1 + num2
```

Test the module using ``doctest``:
```bash
python -m doctest -v /path/to/module.py
```

Alternatively, test the module in the script part:
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

```{seealso}
See more in [doctest library](https://docs.python.org/3/library/doctest.html) for details on example tests.
```
