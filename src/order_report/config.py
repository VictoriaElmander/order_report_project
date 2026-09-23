from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ReportConfig:
    input_path: Path
    output_dir: Path

config = ReportConfig(
    input_path=Path("data/orders.csv"),
    output_dir=Path("output"),
)

# INPUT_FILE = "data/orders.csv"
# OUTPUT_FOLDER = "output"
