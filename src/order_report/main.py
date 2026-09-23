import logging

from order_report.config import config
from order_report.processing import (
    load_orders,
    validate_data,
    clean_data,
    calculate_columns,
)
from order_report.reporting import (
    create_overview,
    create_sales_summary,
    create_returns_by_category,
    save_report
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
    data = calculate_columns(data)

    overview = create_overview(data)

    sales_by_category = create_sales_summary(data, "product_category")
    sales_by_region = create_sales_summary(data, "region")

    returns_by_category = create_returns_by_category(data)

    save_report(overview, config.output_dir, "overview.csv")
    save_report(sales_by_category, config.output_dir, "sales_by_category.csv")
    save_report(sales_by_region, config.output_dir, "sales_by_region.csv")
    save_report(returns_by_category, config.output_dir, "returns_by_category.csv")

    
    #print(data.head())
    #print(overview)


if __name__ == "__main__":
    main()