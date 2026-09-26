import pandas as pd
import pytest

from order_report.processing import calculate_columns, validate_data, remove_invalid_rows


def test_calculate_columns():
    data = pd.DataFrame(
        {
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.25],
        }
    )

    result = calculate_columns(data)

    assert result.loc[0, "order_value"] == 200
    assert result.loc[0, "discounted_value"] == 150


def test_validate_data_missing_column():
    data = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2026-01-01"],
            "customer_id": [100],
            "region": ["North"],
            "product_category": ["Books"],
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.1],
        }
    )

    with pytest.raises(ValueError):
        validate_data(data)

def test_remove_invalid_rows():
    data = pd.DataFrame(
        {
            "quantity": [2, -1, 3],
            "unit_price": [100, 200, 300],
            "discount": [0.1, 0.2, 0.3],
        }
    )

    result = remove_invalid_rows(data)

    assert len(result) == 2
    assert -1 not in result["quantity"].values