"""
Unit tests for CSV reader.

Unit tests run fast and do not require external services.
"""

from pathlib import Path
from de_track.io.csv_reader import read_csv_rows


def test_read_csv_rows(tmp_path: Path) -> None:
    # Create a temporary CSV file for testing
    p = tmp_path / "x.csv"
    p.write_text("id,name\n1,Ada\n2,Grace\n", encoding="utf-8")

    rows = list(read_csv_rows(p))
    assert len(rows) == 2
    assert rows[0]["id"] == "1"
    assert rows[0]["name"] == "Ada"
