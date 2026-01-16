"""
Mini pipeline: CSV -> Postgres staging table.

Run:
  python3 -m de_track.pipelines.file_to_postgres --csv data/samples/sample_people.csv

Notes:
- This expects Postgres to be running and reachable via env vars.
- Later we will add better error handling and idempotent loads.
"""

from pathlib import Path
import argparse

from de_track.io.csv_reader import read_csv_rows
from de_track.db.postgres import get_connection
from de_track.utils.logging_config import get_logger

logger = get_logger(__name__)


def ensure_table_exists() -> None:
    """
    Create a simple staging table if it doesn't exist.
    """
    create_sql = """
    CREATE TABLE IF NOT EXISTS staging_people (
        id      INT,
        name    TEXT,
        city    TEXT
    );
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(create_sql)
        conn.commit()


def load_csv_to_table(csv_path: Path) -> int:
    """
    Load CSV rows into staging_people.

    Args:
        csv_path: Path to CSV file.

    Returns:
        Number of rows inserted.
    """
    inserted = 0

    insert_sql = """
    INSERT INTO staging_people (id, name, city)
    VALUES (%s, %s, %s);
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            for row in read_csv_rows(csv_path):
                # CSV values are strings; convert id safely
                person_id = int(row["id"])
                name = row["name"]
                city = row["city"]

                cur.execute(insert_sql, (person_id, name, city))
                inserted += 1

        conn.commit()

    return inserted


def main() -> None:
    """
    CLI entrypoint.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to input CSV file")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    logger.info("Ensuring staging table exists...")
    ensure_table_exists()

    logger.info("Loading CSV into Postgres: %s", csv_path)
    inserted = load_csv_to_table(csv_path)

    logger.info("Done. Inserted %s rows.", inserted)


if __name__ == "__main__":
    main()
