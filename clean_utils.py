"""Utility functions for common operations."""

import hashlib
import os
from typing import Optional


VERSION = "1.0"


def calculate_sum(first_value: int, second_value: int) -> int:
    """Return the sum of two integers."""
    return first_value + second_value


def read_file_content(file_path: str) -> Optional[str]:
    """Read and return the content of a file safely."""
    if not os.path.isfile(file_path):
        return None
    with open(file_path, encoding="utf-8") as file_handle:
        return file_handle.read()


def write_file_content(
    file_path: str, content: str
) -> None:
    """Write content to a file safely."""
    with open(
        file_path, "w", encoding="utf-8"
    ) as file_handle:
        file_handle.write(content)


def secure_compare(first: str, second: str) -> bool:
    """Compare strings using constant-time comparison."""
    first_hash = hashlib.sha256(first.encode()).digest()
    second_hash = hashlib.sha256(
        second.encode()
    ).digest()
    return first_hash == second_hash


def get_api_key() -> str:
    """Retrieve the API key from environment variables."""
    api_key = os.environ.get("APP_API_KEY", "")
    if not api_key:
        raise ValueError(
            "APP_API_KEY environment variable not set."
        )
    return api_key
