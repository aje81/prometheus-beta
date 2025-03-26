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
    # Pairs with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # 4-3 = 1, 5-4 = 1 (palindrome)
    
    # No palindrome difference pairs
    assert palindrome_pair([10, 20, 30, 40]) == False
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([2, 4, 6, 8]) == False

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

def test_palindrome_pair_comprehensive():
    """Comprehensive test cases for palindrome differences"""
    # Various scenarios
    assert palindrome_pair([1, 11, 21, 31]) == True  # 11-1 = 10, 21-11 = 10 (palindrome)
    assert palindrome_pair([5, 15, 25, 35]) == False
    assert palindrome_pair([-1, 0, 1, 2]) == True  # 1 - (-1) = 2, 2 - 1 = 1 (palindromes)
    assert palindrome_pair([10, 20, 30, 40, 50]) == False