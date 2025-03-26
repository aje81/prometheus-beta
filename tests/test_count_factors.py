import pytest
from src.count_factors import count_factors

def test_prime_number():
    """Test a prime number which should have exactly 2 factors."""
    assert count_factors(7) == 2

def test_composite_number():
    """Test a composite number."""
    assert count_factors(12) == 6  # Factors are 1, 2, 3, 4, 6, 12

def test_perfect_square():
    """Test a perfect square which has an odd number of factors."""
    assert count_factors(16) == 5  # Factors are 1, 2, 4, 8, 16

def test_large_number():
    """Test a larger number to ensure scalability."""
    assert count_factors(100) == 9  # Factors are 1, 2, 4, 5, 10, 20, 25, 50, 100

def test_smallest_positive_integer():
    """Test the smallest positive integer."""
    assert count_factors(1) == 1

def test_invalid_input_zero():
    """Test that zero raises a ValueError."""
    with pytest.raises(ValueError):
        count_factors(0)

def test_invalid_input_negative():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError):
        count_factors(-5)

def test_invalid_input_non_integer():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        count_factors(3.14)
    with pytest.raises(TypeError):
        count_factors("12")