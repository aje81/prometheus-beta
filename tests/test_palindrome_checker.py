import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True
    assert is_palindrome("") == True

def test_complex_palindromes():
    """Test palindromes with spaces and mixed case."""
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("Race a car") == False

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("1234") == False

def test_mixed_palindromes():
    """Test palindromes with mixed alphanumeric characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False

def test_non_palindromes():
    """Test non-palindrome scenarios."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test edge cases."""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Space
    assert is_palindrome("!!!") == True  # Non-alphanumeric characters
    assert is_palindrome("a.b,c!d d c b a") == True  # Punctuation and spaces