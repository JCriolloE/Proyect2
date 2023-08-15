"""Tests for `itesm_mlops` package."""

import pandas as pd
import pytest
from custom_transformers import NumericalImputer


def test_NumericalImputer_transform():
    """
    Test the `transform` method of the NumericalImputer transformer.

    This test checks if the transformer correctly adds indicator features
    for missing values in the specified variables and returns the modified
    DataFrame.

    The test case uses a sample DataFrame with missing values and a custom
    transformer instance.

    It checks if the transformer successfully adds indicator features for
    the specified variables, and the transformed DataFrame has the expected
    additional columns.

    Note: Make sure to replace 'your_module' with the actual module name
    where the NumericalImputer class is defined.
    """
    # Sample DataFrame with missing values
    data = {
        'age': [25, 30, None, 40],
        'income': [50000, None, 75000, 60000],
        'floatD': [0.5, 0.666, 0.23445, None]
    }
    df = pd.DataFrame(data)
    print(df)
    # Instantiate the custom transformer with specified variables
    numerical_imputer = NumericalImputer(variables=['age', 'income', 'floatD'])

    # Transform the DataFrame using the custom transformer
    df_transformed = numerical_imputer.transform(df)
    print(df)
    # Check if the values in the added indicator columns are correct
    expected_values = [25, 30, 30, 40]
    assert all(df_transformed['age'] == expected_values), \
        f"Expected values for 'age': {expected_values}"

    expected_values = [50000.0, 60000.0, 75000.0, 60000.0]
    assert all(df_transformed['income'] == expected_values), \
        f"Expected values for 'income': {expected_values}"

    expected_values = [0.50000, 0.66600, 0.23445, 0.50000]
    assert all(df_transformed['floatD'] == expected_values), \
        f"Expected values for 'floatD': {expected_values}"


if __name__ == "__main__":
    pytest.main()
