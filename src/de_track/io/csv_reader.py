"""
CSV reading utilities.

We keep I/O code isolated so pipelines remain clean and easy to test.
"""

from pathlib import Path
import csv
from typing import Dict, Iterable


def read_csv_rows(path: Path) -> Iterable[Dict[str, str]]:
    """
    Stream rows from a CSV file as dictionaries.

    Args:
        path: Path to a CSV file.

    Yields:
        Each row as a dict: {column_name: value}
    """
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
