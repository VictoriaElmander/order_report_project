from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ReportConfig:
    input_path: Path
    output_dir: Path
    overview_file: str
    category_sales_file: str 
    region_sales_file: str 
    category_returns_file: str 

config = ReportConfig(
    input_path=Path("data/orders.csv"),
    output_dir=Path("output"),
    overview_file = "overview.csv",
    category_sales_file = "sales_by_category.csv",
    region_sales_file = "sales_by_region.csv",
    category_returns_file = "returns_by_category.csv",

)


