"""test1 - Core package for the project."""

__version__ = "0.1.0"

from test1.config import settings
from test1.logging import get_logger

__all__ = ["get_logger", "settings"]
