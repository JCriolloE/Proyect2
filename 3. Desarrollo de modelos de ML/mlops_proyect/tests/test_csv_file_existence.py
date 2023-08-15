"""Tests for `itesm_mlops` package."""
import os

import pytest


def test_csv_file_exists():
    # Get the file list in the current directory
    files = os.listdir()

    # Filter CSV files
    csv_files = [file for file in files if file.endswith(".csv")]

    # Make sure there is at least one CSV file
    assert csv_files


if __name__ == "__main__":
    pytest.main()
