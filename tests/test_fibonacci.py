import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
    ]
    for n, expected in test_cases:
        assert fibonacci(n) == expected

def test_fibonacci_memoization():
    """Verify that memoization works by using a pre-existing memo dictionary."""
    memo = {0: 0, 1: 1}
    assert fibonacci(5, memo) == 5
    assert fibonacci(6, memo) == 8
    assert 5 in memo
    assert 6 in memo

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_large_numbers():
    """Test larger Fibonacci numbers to ensure performance and correctness."""
    # These numbers are chosen to check performance with memoization
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040