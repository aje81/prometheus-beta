import pytest
from src.fibonacci import compute_fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert compute_fibonacci(0) == 0
    assert compute_fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    for n, expected in test_cases:
        assert compute_fibonacci(n) == expected, f"Failed for n={n}"

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        compute_fibonacci(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        compute_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        compute_fibonacci("5")

def test_fibonacci_large_input():
    """Test computation of larger Fibonacci numbers."""
    # Verify some larger Fibonacci numbers
    assert compute_fibonacci(20) == 6765
    assert compute_fibonacci(30) == 832040

def test_fibonacci_zero_input():
    """Specific test for zero input."""
    assert compute_fibonacci(0) == 0, "Zero input should return 0"