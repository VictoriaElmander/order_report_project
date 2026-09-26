import pandas as pd

from order_report.reporting import create_sales_summary


def test_create_sales_summary():
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "product_category": ["Books", "Books", "Electronics"],
            "discounted_value": [100, 200, 500],
            "returned": [False, True, False],
        }
    )

    result = create_sales_summary(data, "product_category")
    
    assert result.loc[0, "product_category"] == "Electronics"
    assert result.loc[0, "total_sales"] == 500

    assert result.loc[1, "product_category"] == "Books"
    assert result.loc[1, "total_sales"] == 300