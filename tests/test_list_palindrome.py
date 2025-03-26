import pytest
from src.list_palindrome import is_palindrome

def test_empty_list_is_palindrome():
    """Test that an empty list is considered a palindrome."""
    assert is_palindrome([]) is True

def test_single_element_list_is_palindrome():
    """Test that a single-element list is a palindrome."""
    assert is_palindrome([42]) is True

def test_simple_palindrome_list():
    """Test a simple palindrome list of integers."""
    assert is_palindrome([1, 2, 1]) is True

def test_simple_non_palindrome_list():
    """Test a list that is not a palindrome."""
    assert is_palindrome([1, 2, 3]) is False

def test_longer_palindrome_list():
    """Test a longer palindrome list."""
    assert is_palindrome([1, 2, 3, 2, 1]) is True

def test_longer_non_palindrome_list():
    """Test a longer list that is not a palindrome."""
    assert is_palindrome([1, 2, 3, 4, 5]) is False

def test_negative_numbers_palindrome():
    """Test a palindrome list with negative numbers."""
    assert is_palindrome([-1, 0, -1]) is True

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome(None)