import pytest
from src.string_utils import longest_common_substring

def test_basic_common_substring():
    """Test basic common substring scenarios"""
    assert longest_common_substring("programming", "programmer") == "program"
    assert longest_common_substring("hello", "world") == ""
    assert longest_common_substring("abcde", "abxde") == "ab"

def test_edge_cases():
    """Test edge cases"""
    # Empty strings
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("abc", "") == ""
    assert longest_common_substring("", "xyz") == ""
    
    # Identical strings
    assert longest_common_substring("python", "python") == "python"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_substring("Python", "python") == ""

def test_multiple_common_substrings():
    """Test scenarios with multiple possible common substrings"""
    assert longest_common_substring("ABABC", "BABCA") == "BABC"
    assert longest_common_substring("abcabcabc", "bcabcabc") == "bcabcabc"

def test_single_character_common_substring():
    """Test single character common substrings"""
    assert longest_common_substring("a", "a") == "a"
    assert longest_common_substring("abc", "def") == ""