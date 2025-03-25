import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test max subarray sum with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test max subarray sum when all numbers are negative."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test max subarray sum with a single element."""
    assert max_subarray_sum([42]) == 42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")

def test_zero_sum_subarray():
    """Test scenario with zero-sum subarrays."""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3

def test_alternating_signs():
    """Test max subarray sum with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 1, -1, 1]) == 1