import pytest
from src.word_counter import count_unique_words

def test_basic_unique_words():
    """Test basic unique word counting"""
    assert count_unique_words("Hello, hello! How are you?") == 4

def test_empty_string():
    """Test empty string input"""
    assert count_unique_words("") == 0

def test_whitespace_only():
    """Test string with only whitespace"""
    assert count_unique_words("   ") == 0

def test_case_insensitive():
    """Test that word counting is case-insensitive"""
    assert count_unique_words("Hello hello HELLO hELLo") == 1

def test_punctuation_removal():
    """Test removal of punctuation"""
    assert count_unique_words("Hello, world! Hello-world") == 2

def test_multiple_spaces():
    """Test handling of multiple spaces"""
    assert count_unique_words("one  two   three") == 3

def test_special_characters():
    """Test handling of special characters"""
    assert count_unique_words("word1! @word2# $word3%") == 3

def test_none_input():
    """Test handling of None input"""
    assert count_unique_words(None) == 0