import pytest
from src.prime_finder import find_primes_in_range

def test_basic_prime_range():
    """Test finding primes in a standard range"""
    assert find_primes_in_range(1, 10) == [2, 3, 5, 7]

def test_range_with_no_primes():
    """Test a range with no prime numbers"""
    assert find_primes_in_range(1, 1) == []

def test_single_prime_range():
    """Test a range with a single prime"""
    assert find_primes_in_range(7, 7) == [7]

def test_larger_prime_range():
    """Test finding primes in a larger range"""
    assert find_primes_in_range(20, 50) == [23, 29, 31, 37, 41, 43, 47]

def test_lower_bound_larger_than_upper_bound():
    """Test that an exception is raised when lower bound > upper bound"""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        find_primes_in_range(10, 5)

def test_negative_bounds():
    """Test that an exception is raised for negative bounds"""
    with pytest.raises(ValueError, match="Both bounds must be non-negative integers"):
        find_primes_in_range(-5, 10)

def test_lower_negative_bound():
    """Test exception for negative lower bound"""
    with pytest.raises(ValueError, match="Both bounds must be non-negative integers"):
        find_primes_in_range(-1, 10)

def test_zero_range():
    """Test range starting at zero"""
    assert find_primes_in_range(0, 10) == [2, 3, 5, 7]

def test_empty_range_below_two():
    """Test ranges that should return empty list"""
    assert find_primes_in_range(0, 1) == []
    assert find_primes_in_range(1, 1) == []