import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)

def load_orders(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    data = pd.read_csv(path)

    if data.empty:
        raise ValueError(f"Input file contains no data: {path}")

    logger.info("Loaded %d rows from %s", len(data), path)
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

    data["quantity"] = format_column_nbr(data["quantity"])
    invalid_quantity_count = data["quantity"].isna().sum()
    if invalid_quantity_count > 0:
        logger.warning(
            "Found %d invalid quantity values; replacing with 1",
            invalid_quantity_count,
        )
    data["quantity"] = data["quantity"].fillna(1)

    data["unit_price"] = format_column_nbr(data["unit_price"])
    invalid_unit_price_count = data["unit_price"].isna().sum()
    if invalid_unit_price_count > 0:
        logger.warning(
            "Found %d invalid unit price values; replacing with median",
            invalid_unit_price_count,
        )
    data["unit_price"] = data["unit_price"].fillna(data["unit_price"].median())

    data["discount"] = format_column_nbr(data["discount"])
    invalid_discount_count = data["discount"].isna().sum()
    if invalid_discount_count > 0:
        logger.warning(
            "Found %d invalid discount values; replacing with 0",
            invalid_discount_count,
        )
    data["discount"] = data["discount"].fillna(0)

    data["returned"] = format_column_boolean(data["returned"])

    logger.info("Data cleaning completed")
    return data        


def remove_invalid_rows(data: pd.DataFrame) -> pd.DataFrame:
    invalid_quantity = data["quantity"] < 0
    invalid_unit_price = data["unit_price"] < 0
    invalid_discount = (data["discount"] < 0) | (data["discount"] > 1)

    invalid_rows = (
        invalid_quantity
        | invalid_unit_price
        | invalid_discount
    )

    invalid_count = invalid_rows.sum()

    if invalid_count > 0:
        logger.warning(
            "Removing %d rows with unreasonable values",
            invalid_count,
        )

    data = data[~invalid_rows].reset_index(drop=True)

    return data

def calculate_columns(data: pd.DataFrame) -> pd.DataFrame:
    data["order_value"] = data["quantity"] * data["unit_price"]
    data["discounted_value"] = data["order_value"] * (1 - data["discount"])

    return data
