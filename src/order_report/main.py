import logging

from order_report.config import config
from order_report.processing import (
    load_orders,
    validate_data,
    clean_data,
    remove_invalid_rows,
    calculate_columns,
)
from order_report.reporting import (
    create_overview,
    create_sales_summary,
    create_returns_by_category,
    save_report,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Startar orderrapport")

    data = load_orders(config.input_path)
    validate_data(data)
    data = clean_data(data)
    data = remove_invalid_rows(data)
    data = calculate_columns(data)

    overview = create_overview(data)

    sales_by_category = create_sales_summary(data, "product_category")
    sales_by_region = create_sales_summary(data, "region")

    returns_by_category = create_returns_by_category(data)

    logger.info("Reports created")

    save_report(overview, config.output_dir, config.overview_file)
    save_report(sales_by_category, config.output_dir, config.category_sales_file)
    save_report(sales_by_region, config.output_dir, config.region_sales_file)
    save_report(returns_by_category, config.output_dir, config.category_returns_file)


if __name__ == "__main__":
    main()