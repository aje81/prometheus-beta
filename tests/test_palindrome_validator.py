import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("Madam, I'm Adam") == True

def test_case_insensitive():
    """Test that palindrome check is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("123 456") == False

def test_special_characters():
    """Test palindromes with various special characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2@#$%^&*()b1a") == True
    assert is_palindrome("hello") == False

def test_edge_cases():
    """Test edge cases for palindrome validation."""
    assert is_palindrome(" ") == True
    assert is_palindrome("   ") == True
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False