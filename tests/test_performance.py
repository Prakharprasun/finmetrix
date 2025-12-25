# tests/test_performance.py
import time
import pytest


def benchmark_twr(implementation, returns, iterations=1000):
    """Helper to benchmark TWR implementations."""
    start = time.perf_counter()
    for _ in range(iterations):
        implementation(returns)
    elapsed = time.perf_counter() - start
    return elapsed


def test_twr_performance_comparison():
    """Compare Python vs C++ performance."""
    from finmetrix.returns import _twr_python
    from finmetrix._backend import twr_impl, BACKEND

    if BACKEND != "cpp":
        pytest.skip("C++ backend not available")

    # Test with different sizes
    test_cases = [
        ("small", [0.001] * 10),
        ("medium", [0.001] * 100),
        ("large", [0.001] * 1000),
    ]

    print("\n" + "=" * 60)
    print("TWR Performance Comparison (1000 iterations each)")
    print("=" * 60)

    for name, returns in test_cases:
        python_time = benchmark_twr(_twr_python, returns)
        cpp_time = benchmark_twr(twr_impl, returns)
        speedup = python_time / cpp_time

        print(f"\n{name.upper()} ({len(returns)} returns):")
        print(f"  Python: {python_time:.4f}s")
        print(f"  C++:    {cpp_time:.4f}s")
        print(f"  Speedup: {speedup:.2f}x")

    print("\n" + "=" * 60)