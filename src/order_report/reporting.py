import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

def create_overview(data: pd.DataFrame) -> pd.DataFrame:
    total_sales = round(data["discounted_value"].sum(),2,)
    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    overview = pd.DataFrame(
            {
                "metric": [
                    "total_sales",
                    "order_count",
                    "return_count",
                ],
                "value": [
                    total_sales,
                    number_of_orders,
                    number_of_returns,
                ],
            }
        )

    return overview

def create_sales_summary(data: pd.DataFrame, group_by: str) -> pd.DataFrame:
    result = (
            data.groupby(
                group_by,
                as_index=False,
            )
            .agg(
                order_count=("order_id", "nunique"),
                total_sales=("discounted_value", "sum"),
                returns=("returned", "sum"),
            )
        )

    result["total_sales"] = (
        result["total_sales"].round(2)
    )

    result["return_rate"] = (
        result["returns"]
        / result["order_count"]
    ).round(3)

    result = (
        result
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    return result


def create_returns_by_category(data: pd.DataFrame) -> pd.DataFrame:
    returns_by_category = (
        data.groupby(
            "product_category",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    returns_by_category["return_rate"] = (
        returns_by_category["returns"]
        / returns_by_category["order_count"]
    ).round(3)

    returns_by_category = (
        returns_by_category
        .sort_values(
            "return_rate",
            ascending=False,
        )
        .reset_index(drop=True)
    )
    return returns_by_category

def save_report(report: pd.DataFrame, output_dir: Path, filename: str) -> None:
    file_path = output_dir / filename
    report.to_csv(file_path, index = False)
    logger.info("Report saved to %s", file_path)


