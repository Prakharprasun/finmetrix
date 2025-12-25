# finmetrix/returns.py
"""Return-based metrics: TWR, CAGR."""

from typing import Sequence
from ._validation import validate_returns
from ._backend import twr_impl


def _twr_python(returns: Sequence[float]) -> float:
    """Pure Python TWR implementation (reference)."""
    result = 1.0
    for r in returns:
        result *= (1.0 + r)
    return result - 1.0


def twr(returns: Sequence[float]) -> float:
    """
    Compute time-weighted return.

    [Keep same docstring as before]
    """
    # Materialize and validate
    returns = list(returns)
    validate_returns(returns)

    # Use C++ backend if available, otherwise Python
    if twr_impl is not None:
        return twr_impl(returns)

    return _twr_python(returns)