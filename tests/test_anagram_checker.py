import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram cases"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("triangle", "integral") == True

def test_case_insensitive():
    """Test that anagram checking is case-insensitive"""
    assert anagram_checker("Tea", "Eat") == True
    assert anagram_checker("LISTEN", "silent") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False

def test_same_word():
    """Test a word with itself"""
    assert anagram_checker("python", "python") == True

def test_whitespace_handling():
    """Test anagrams with whitespace"""
    assert anagram_checker("debit card", "bad credit") == True

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test non-string inputs
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    with pytest.raises(TypeError):
        anagram_checker("test", [1, 2, 3])

def test_empty_strings():
    """Test error handling for empty strings"""
    with pytest.raises(ValueError):
        anagram_checker("", "test")
    with pytest.raises(ValueError):
        anagram_checker("test", "")
    with pytest.raises(ValueError):
        anagram_checker("", "")