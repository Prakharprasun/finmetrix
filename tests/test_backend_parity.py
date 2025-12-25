import math
import pytest

from finmetrix import twr
from finmetrix._backend import BACKEND, twr_impl


def test_backend_available():
    """C++ backend should be importable when present."""
    if BACKEND != "cpp":
        pytest.skip("C++ backend not available")

    assert twr_impl is not None


def test_twr_numerical_parity():
    """C++ backend must match Python reference numerically."""
    if twr_impl is None:
        pytest.skip("C++ backend not available")

    test_cases = [
        [0.05],
        [0.1, -0.1],
        [0.05, 0.03, -0.02],
        [0.001] * 100,
        [-0.5, 0.5, -0.3, 0.3],
    ]

    for returns in test_cases:
        python_result = twr(returns)        # public API (Python path)
        cpp_result = twr_impl(returns)      # direct backend call

        assert math.isclose(
            python_result,
            cpp_result,
            rel_tol=1e-14,
            abs_tol=1e-15,
        ), (
            f"Mismatch for {returns}: "
            f"Python={python_result}, C++={cpp_result}"
        )


def test_twr_validation_through_python():
    """
    C++ backend must only receive validated inputs.
    Invalid inputs should fail in Python before reaching C++.
    """
    with pytest.raises(ValueError):
        twr([])

    with pytest.raises(ValueError):
        twr([float("nan")])

    with pytest.raises(ValueError):
        twr([-1.0])
