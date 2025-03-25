import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization scenarios."""
    assert get_prime_factors(1) == []
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    """Test prime numbers have themselves as factors."""
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(11) == [11]
    assert get_prime_factors(17) == [17]

def test_prime_factors_large_number():
    """Test prime factorization of a larger number."""
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        get_prime_factors("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)

def test_prime_factors_is_sorted():
    """Ensure factors are returned in ascending order."""
    assert get_prime_factors(24) == [2, 2, 2, 3]
    assert get_prime_factors(360) == [2, 2, 2, 3, 3, 5]