import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function"""
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(11) == True
    assert is_palindrome(0) == True

def test_palindrome_pair_basic_cases():
    """Test basic scenarios of palindrome pair function"""
    # No palindrome difference pairs
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([2, 4, 6, 8]) == False
    assert palindrome_pair([10, 20, 30, 40]) == False

def test_palindrome_pair_with_palindrome_diff():
    """Test cases where palindrome differences exist"""
    assert palindrome_pair([10, 11, 21, 31]) == True   # 11-10 = 1 (palindrome)
    assert palindrome_pair([1, 2, 12, 22]) == False    # No special pairs
    assert palindrome_pair([5, 15, 16, 25]) == False   # No special pairs

def test_palindrome_pair_edge_cases():
    """Test edge cases of palindrome pair function"""
    # Empty list
    assert palindrome_pair([]) == False
    
    # Single element list
    assert palindrome_pair([1]) == False

def test_palindrome_pair_error_handling():
    """Test error handling for invalid inputs"""
    # Non-list input
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    # List with non-integer elements
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "3", 4])

def test_palindrome_pair_complex_cases():
    """Comprehensive test cases for palindrome differences"""
    assert palindrome_pair([5, 15, 25, 35]) == False
    assert palindrome_pair([-1, 0, 1, 2]) == False