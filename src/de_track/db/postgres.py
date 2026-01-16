"""
Postgres connection helpers.

Later weeks will expand this with:
- safer inserts / upserts
- staging + marts loaders
- integration tests that actually connect to Postgres
"""

import os
import psycopg2
from psycopg2.extensions import connection


def get_connection() -> connection:
    """
    Create a Postgres connection from environment variables.

    Returns:
        A psycopg2 connection object.
    """
    host = os.getenv("PG_HOST", "localhost")
    port = int(os.getenv("PG_PORT", "5432"))
    dbname = os.getenv("PG_DB", "de_track")
    user = os.getenv("PG_USER", "de_user")
    password = os.getenv("PG_PASSWORD", "de_password")

    return psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password,
    )
