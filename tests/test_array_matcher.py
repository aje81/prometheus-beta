import pytest
from src.array_matcher import count_matching_elements

def test_basic_matching():
    """Test basic matching of elements between two arrays."""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert count_matching_elements(arr1, arr2) == 3

def test_no_matching_elements():
    """Test case with no matching elements."""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert count_matching_elements(arr1, arr2) == 0

def test_all_matching_elements():
    """Test case where all elements match."""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 3

def test_empty_arrays():
    """Test with empty arrays."""
    arr1 = []
    arr2 = [1, 2, 3]
    assert count_matching_elements(arr1, arr2) == 0
    assert count_matching_elements(arr2, arr1) == 0

def test_duplicates_in_first_array():
    """Test with duplicate elements in the first array."""
    arr1 = [1, 1, 2, 2, 3]
    arr2 = [2, 3, 4]
    assert count_matching_elements(arr1, arr2) == 3

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_matching_elements(None, [1, 2, 3])
    with pytest.raises(TypeError):
        count_matching_elements([1, 2, 3], None)
    with pytest.raises(TypeError):
        count_matching_elements("not a list", [1, 2, 3])