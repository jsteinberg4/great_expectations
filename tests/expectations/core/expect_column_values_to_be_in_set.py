import pandas as pd

from great_expectations.core.expectation_configuration import \
    ExpectationConfiguration
from great_expectations.core.expectation_validation_result import \
    ExpectationValidationResult
from great_expectations.expectations.core.expect_column_values_to_be_in_set import \
    ExpectColumnValuesToBeInSet


def test_expect_column_values_to_be_in_set_impl():
    df = pd.DataFrame({"a": [1, 2, 3]})
    expectationConfiguration = ExpectationConfiguration(
        expectation_type="expect_column_values_to_be_in_set",
        kwargs={"column": "a", "value_set": [1, 2], "mostly": 1},
    )
    expectation = ExpectColumnValuesToBeInSet(expectationConfiguration)
    result = expectation.validate(df, expectationConfiguration)
    assert result == ExpectationValidationResult(success=False,)