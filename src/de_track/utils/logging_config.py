"""
Logging configuration helper.

Why:
- Consistent logs across scripts and pipelines.
- Later this maps cleanly to cloud logging (e.g., CloudWatch).
"""

import logging
import os


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: Usually __name__ from the calling module.

    Returns:
        A configured logging.Logger instance.
    """
    level_str = os.getenv("LOG_LEVEL", "INFO").upper()

    # Convert text level like "INFO" into logging.INFO
    level = getattr(logging, level_str, logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if get_logger() is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
