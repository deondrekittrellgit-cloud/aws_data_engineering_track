"""
Pattern A demo: run a Python script from your repo environment.

What this checks:
- you're running the Python from your .venv
- prints Python version + executable path
- prints current time
- checks whether DE_DB_URL is set in your environment
"""

import os
import sys
from datetime import datetime


def main() -> None:
    print("=== Pattern A Demo ===")

    # Shows exactly which Python is running (should point inside .venv)
    print(f"Python Executable: {sys.executable}")
    print(f"Python Version: {sys.version.split()[0]}")

    # Timestamp
    print(f"Current Time: {datetime.now().isoformat(timespec='seconds')}")

    # Environment variable check
    db_url = os.getenv("DE_DB_URL")
    if db_url:
        print("DE_DB_URL is set ✅")
        print(f"DE_DB_URL value: {db_url}")
    else:
        print("DE_DB_URL is not set (that's ok for this demo).")

    print("Done.")


if __name__ == "__main__":
    main()
