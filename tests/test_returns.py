import math
import time
import pytest

from finmetrix import twr


def test_twr_single_period():
    """Single period return should equal input."""
    assert math.isclose(twr([0.05]), 0.05, abs_tol=1e-10)


def test_twr_multiple_periods_flat():
    """Equal gain and loss should result in net loss due to compounding."""
    result = twr([0.1, -0.1])
    assert math.isclose(result, -0.01, abs_tol=1e-10)


def test_twr_zero_returns():
    """Zero returns should compound to zero."""
    assert math.isclose(twr([0.0, 0.0, 0.0]), 0.0, abs_tol=1e-15)


def test_twr_positive_compounding():
    """Positive returns should compound correctly."""
    # (1.05 * 1.03) - 1 = 0.0815
    result = twr([0.05, 0.03])
    assert math.isclose(result, 0.0815, abs_tol=1e-10)


def test_twr_with_zero_in_sequence():
    """Zero return in sequence should not affect other periods."""
    assert math.isclose(twr([0.0, 0.05]), 0.05, abs_tol=1e-10)
    assert math.isclose(twr([0.05, 0.0]), 0.05, abs_tol=1e-10)


def test_twr_order_invariant():
    """TWR should be invariant to order of returns."""
    r1 = [0.1, 0.2, -0.1]
    r2 = [-0.1, 0.2, 0.1]
    r3 = [0.2, -0.1, 0.1]

    v1 = twr(r1)
    v2 = twr(r2)
    v3 = twr(r3)

    assert math.isclose(v1, v2, rel_tol=1e-14, abs_tol=1e-15)
    assert math.isclose(v1, v3, rel_tol=1e-14, abs_tol=1e-15)


def test_twr_accepts_tuple():
    """Should accept tuples, not just lists."""
    assert math.isclose(
        twr((0.01, 0.02)),
        twr([0.01, 0.02]),
        abs_tol=1e-15,
    )


def test_twr_accepts_generator():
    """Should accept generators and iterables."""
    gen = (x for x in [0.01, 0.02])
    assert math.isclose(twr(gen), twr([0.01, 0.02]), abs_tol=1e-10)


def test_twr_empty_raises():
    """Empty returns should raise ValueError."""
    with pytest.raises(ValueError, match="no returns"):
        twr([])


def test_twr_non_numeric_raises():
    """Non-numeric values should raise TypeError."""
    with pytest.raises(TypeError, match="numeric"):
        twr([0.1, "0.2"])


def test_twr_nan_raises():
    """NaN values should raise ValueError."""
    with pytest.raises(ValueError, match="NaN"):
        twr([0.1, float("nan")])


def test_twr_inf_raises():
    """Infinite values should raise ValueError."""
    with pytest.raises(ValueError, match="infinite"):
        twr([0.1, float("inf")])

    with pytest.raises(ValueError, match="infinite"):
        twr([0.1, float("-inf")])


def test_twr_total_loss_raises():
    """Total loss (-1.0) should raise ValueError."""
    with pytest.raises(ValueError, match="Total loss"):
        twr([0.1, -1.0])

    with pytest.raises(ValueError, match="Total loss"):
        twr([-1.0, 0.1])


def test_twr_below_minus_one_raises():
    """Returns below -1.0 should raise ValueError."""
    with pytest.raises(ValueError, match="less than -1.0"):
        twr([0.1, -1.01])

    with pytest.raises(ValueError, match="less than -1.0"):
        twr([-1.5])


def test_twr_large_sequence():
    """Should handle moderately large sequences."""
    returns = [0.001] * 1000
    result = twr(returns)
    # (1.001)^1000 ≈ 2.7169
    assert result > 1.7


def test_twr_very_small_returns():
    """Should handle very small returns without precision loss."""
    returns = [1e-10] * 100
    result = twr(returns)
    assert math.isclose(result, 1e-8, rel_tol=0.01)


def test_twr_near_total_loss():
    """Should handle returns very close to -1.0."""
    result = twr([-0.9999])
    assert math.isclose(result, -0.9999, abs_tol=1e-10)


def test_twr_alternating_signs():
    """Should handle alternating positive/negative returns."""
    returns = [0.1, -0.05, 0.08, -0.03]
    result = twr(returns)

    expected = 1.1 * 0.95 * 1.08 * 0.97 - 1
    assert math.isclose(result, expected, abs_tol=1e-10)


def test_twr_baseline_performance():
    """Baseline performance measurement."""
    returns = [0.001] * 10_000

    start = time.perf_counter()
    for _ in range(100):
        twr(returns)
    elapsed = time.perf_counter() - start

    print(f"\nPython twr: {elapsed:.4f}s for 100 iterations (10k returns each)")
