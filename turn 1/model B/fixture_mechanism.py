import pandas as pd
import pytest


@pytest.fixture
def get_data():
    data = {
        "customer_id": [1, 2, 3, 4],
        "order_amount": [100, 50, 300, 200],
        "payment_method": ["credit_card", "debit_card", "paypal", "bank_transfer"]
    }
    df = pd.DataFrame(data)
    yield df


@pytest.mark.parametrize("sensitivity_level", ["high", "medium", "low"])
def test_data_sensitivity(get_data, sensitivity_level):
    df = get_data.copy()

    # Function to perform sensitivity analysis
    def analyze_sensitivity(df, sensitivity_level):
        if sensitivity_level == "high":
            # Simulate some data modification for high sensitivity
            df["payment_method"] = df["payment_method"].mask(df["order_amount"] > 150, "high_sensitive")
        return df

    # Actual test logic
    result = analyze_sensitivity(df.copy(), sensitivity_level)
    expected = df.copy()
    if sensitivity_level == "high":
        expected["payment_method"].loc[expected["order_amount"] > 150] = "high_sensitive"

    pd.testing.assert_frame_equal(result, expected, "Dataframes are not equal")
