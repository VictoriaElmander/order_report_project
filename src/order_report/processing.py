import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)

def load_orders(path: Path) -> pd.DataFrame:
    data = pd.read_csv(path)
    logger.info("Loaded %d rows", len(data))
    return data

def validate_data(data: pd.DataFrame) -> None:
    required = {
            "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "discount",
            "returned",
        }
    
    missing_columns = []

    for column in required:
        if column not in data.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    logger.info("Data validation completed")


def format_column_text(column: pd.Series) -> pd.Series:
    return (column.fillna("Unknown").astype(str).str.strip().str.title())


def format_column_nbr(column: pd.Series) -> pd.Series:
    return pd.to_numeric(column, errors="coerce")

def format_column_boolean(column: pd.Series) -> pd.Series:
    return (column.fillna("false").astype(str).str.strip().str.lower()
            .isin(["true", "yes", "1", "ja"])
    )


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data["region"] = format_column_text(data["region"])
    data["product_category"] = format_column_text(data["product_category"])

    data["quantity"] = format_column_nbr(data["quantity"]).fillna(1)
    data["unit_price"] = format_column_nbr(data["unit_price"])
    data["unit_price"] = data["unit_price"].fillna(data["unit_price"].median())
    data["discount"] = format_column_nbr(data["discount"]).fillna(0)

    data["returned"] = format_column_boolean(data["returned"])

    return data        


def calculate_columns(data: pd.DataFrame) -> pd.DataFrame:
    data["order_value"] = data["quantity"] * data["unit_price"]
    data["discounted_value"] = data["order_value"] * (1 - data["discount"])

    return data


if __name__ == "__main__":
    data = load_orders(Path("data/orders.csv"))
    validate_data(data)
    data = clean_data(data)
    data = calculate_columns(data)

    print(data.head())
