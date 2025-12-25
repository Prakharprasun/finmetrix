# finmetrix/_validation.py
"""Internal validation helpers for finmetrix."""

from typing import Sequence


def validate_returns(returns: Sequence[float]) -> None:
    """
    Validate a sequence of returns for finmetrix operations.

    Parameters
    ----------
    returns : sequence of float
        Returns to validate. Must be non-empty, finite, numeric values.

    Raises
    ------
    ValueError
        If returns is empty, contains NaN/inf, or has values <= -1.0
    TypeError
        If returns contains non-numeric values
    """
    if not returns:
        raise ValueError("Cannot compute with no returns")

    for i, r in enumerate(returns):
        # Type check
        if not isinstance(r, (int, float)):
            raise TypeError(
                f"Return at index {i} must be numeric, got {type(r).__name__}"
            )

        # NaN check (NaN != NaN is the standard check)
        if r != r:
            raise ValueError(f"Return at index {i} is NaN")

        # Infinity check
        if r in (float("inf"), float("-inf")):
            raise ValueError(f"Return at index {i} is infinite")

        # Total loss
        if r == -1.0:
            raise ValueError(
                f"Total loss (-1.0 return) at index {i}; "
                "subsequent returns undefined"
            )

        # Below -100% (leverage/debt)
        if r < -1.0:
            raise ValueError(
                f"Return at index {i} is {r:.6f}, less than -1.0 "
                "(implies leverage or debt, outside TWR scope)"
            )