# finmetrix/__init__.py
"""finmetrix: Explicit finance metrics library."""

from ._version import __version__
from .returns import twr

__all__ = [
    "__version__",
    "twr",
]