import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindromic substring scenarios."""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_char_palindromes():
    """Test scenarios with single character inputs."""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("abc") == "a"

def test_full_string_palindromes():
    """Test when entire string is a palindrome."""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("level") == "level"

def test_multiple_palindromes():
    """Test scenarios with multiple potential palindromes."""
    assert longest_palindromic_substring("aacabdkacaa") == "aca"

def test_even_length_palindromes():
    """Test palindromes with even number of characters."""
    assert longest_palindromic_substring("abcddcba") == "abcddcba"
    assert longest_palindromic_substring("abccba") == "abccba"

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)

def test_complex_palindromes():
    """Test more complex palindrome scenarios."""
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"