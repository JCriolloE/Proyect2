"""Tests for `itesm_mlops` package."""

import pandas as pd
import pytest
from mlops_proyect.preprocess.custom_transformers import MissingIndicator


def test_missing_indicator_transform():
    """
    Test the `transform` method of the MissingIndicator transformer.

    This test checks if the transformer correctly adds indicator features
    for missing values in the specified variables and returns the modified
    DataFrame.

    The test case uses a sample DataFrame with missing values and a custom
    transformer instance.

    It checks if the transformer successfully adds indicator features for
    the specified variables, and the transformed DataFrame has the expected
    additional columns.

    Note: Make sure to replace 'your_module' with the actual module name
    where the MissingIndicator class is defined.
    """
    # Sample DataFrame with missing values
    data = {
        'age': [25, 30, None, 40],
        'income': [50000, None, 75000, 60000],
        'gender': ['M', 'F', 'M', 'F']
    }
    df = pd.DataFrame(data)

    # Instantiate the custom transformer with specified variables
    missing_indicator = MissingIndicator(variables=['age', 'income'])

    # Transform the DataFrame using the custom transformer
    df_transformed = missing_indicator.transform(df)

    # Check if the transformed DataFrame has the expected additional columns
    expected_columns = ['age_nan', 'income_nan', 'gender']
    assert all(col in df_transformed.columns for col in expected_columns), \
        "The transformed DataFrame should have the "\
        "following additional columns: {expected_columns}"

    # Check if the values in the added indicator columns are correct
    expected_values = [0, 0, 1, 0]
    assert all(df_transformed['age_nan'] == expected_values), \
        f"Expected values for 'age_nan': {expected_values}"

    expected_values = [0, 1, 0, 0]
    assert all(df_transformed['income_nan'] == expected_values), \
        f"Expected values for 'income_nan': {expected_values}"

    # Check if the original DataFrame is not modified
    assert 'age_nan' not in df.columns, "The original DataFrame should "\
        "not be modified."


if __name__ == "__main__":
    pytest.main()
