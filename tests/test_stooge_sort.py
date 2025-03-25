import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == sorted([64, 34, 25, 12, 22, 11, 90])
    assert arr == sorted([64, 34, 25, 12, 22, 11, 90])  # Ensure in-place sorting

def test_stooge_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == arr

def test_stooge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5]

def test_stooge_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == [42]

def test_stooge_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

def test_stooge_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, 2, -10, 0, 3, -7, 1]
    sorted_arr = stooge_sort(arr)
    assert sorted_arr == sorted([-5, 2, -10, 0, 3, -7, 1])

def test_stooge_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        stooge_sort("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        stooge_sort(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        stooge_sort(None)