"""
{Short module description (1-3 sentences)}
todo docstring

Features
--------
todo docstring

 - {feature 1}
 - {feature 2}
 - {feature 3}
 - {etc}

Overview
--------
todo docstring
{Overview description}

Examples
--------
todo docstring

Print a message

.. code-block:: python

    # print message
    print("Hello world!")
    # [Output] >> 'Hello world!'


"""
# ***********************************************************************
# IMPORTS
# ***********************************************************************
# import modules from other libs


# Native imports
# =======================================================================
import os
from pathlib import Path
# ... {develop}

# External imports
# =======================================================================
import numpy as np    # <-- [CHECK THIS]
import pandas as pd   # <-- [CHECK THIS]
# ... {develop}

# Project-level imports
# =======================================================================
# import {module}
# ... {develop}


# ***********************************************************************
# CONSTANTS
# ***********************************************************************
# define constants in uppercase


# Project-level
# =======================================================================

# Paths
# -----------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
# ... {develop}

# Files
# -----------------------------------------------------------------------
DATA_FILE = DATA_DIR / "test_data.csv"
# ... {develop}

# Names
# -----------------------------------------------------------------------
REPO_NAME = os.path.basename(Path(BASE_DIR).parent)
# ... {develop}

# Benchmark tests
# -----------------------------------------------------------------------
# Regular benchmark tests enabled -- default to "1" (true)
RUN_BENCHMARKS = os.getenv("RUN_BENCHMARKS", "1") == "1"
# Heavy benchmark tests disabled -- default to "0" (false)
RUN_BENCHMARKS_XXL = os.getenv("RUN_BENCHMARKS_XXL", "0") == "1"
# ... {develop}

# Module-level
# =======================================================================
# {develop}


# ***********************************************************************
# FUNCTIONS
# ***********************************************************************


# Project-level
# =======================================================================

def testprint(s):
    # todo docstring
    s2 = f"{REPO_NAME} -- tests >>> {s}".lower()
    return s2

def make_output():
    # todo docstring
    testprint("making output dir")
    os.mkdirs(OUTPUT_DIR, exist_ok=True)
    return None

def make_data():
    # todo docstring
    testprint("making data")
    if not os.path.isfile(DATA_FILE):
        v = np.random.randint(low=10, high=100, size=100)
        v2 = np.random.randint(low=10, high=100, size=100)
        v3 = v2 / v
        df = pd.DataFrame(
            {
                "v1": v,
                "v2": v2,
                "v3": v3
            }
        )
        df.to_csv(DATA_FILE, sep=";", index=False)
        testprint("data created")
    else:
        testprint("data already available")
    return None

def load_data():
    # todo docstring
    testprint("loading numbers data")
    df = pd.read_csv(DATA_NUMBERS_FILE, sep=";")
    return df

def download_dataset(name, url, overwrite=True):
    # todo docstring
    testprint(f"downloading dataset {name} from {url}")
    # setup paths
    dataset_path = DATA_DIR / name
    zip_path = DATA_DIR / f"{name}.zip"

    # Download zip (handles URL/network errors)
    download_zip(url, zip_path)

    # Extract and cleanup
    extract_and_cleanup(zip_path, dataset_path, overwrite=overwrite)

    return dataset_path

# ... {develop}

# Module-level
# =======================================================================

def download_zip(url, zip_path):
    # todo docstring
    try:
        print(testprint(f"downloading dataset from {url}..."))
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()  # Raises HTTPError for bad HTTP responses
    except requests.exceptions.RequestException as e:
        raise DatasetDownloadError(f"Failed to download dataset from {url}: {e}")

    with open(target_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(testprint(f"saved zip to {target_path}"))
    return None

# ... {develop}

# ***********************************************************************
# CLASSES
# ***********************************************************************

# Project-level
# =======================================================================
# {develop}

# Module-level
# =======================================================================

class DatasetDownloadError(Exception):
    """
    Custom exception for dataset download issues.
    """
    pass

# ... {develop}

# ***********************************************************************
# SCRIPT
# ***********************************************************************
# standalone behaviour as a script

if __name__ == "__main__":

    # Script section
    # ===================================================================
    testprint("conftest.py")
    
    # Make data
    # -------------------------------------------------------------------
    make_data()
  
    # ... {develop}

  
    # Script subsection
    # -------------------------------------------------------------------
    # ... {develop}
