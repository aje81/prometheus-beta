import pytest
from src.string_utils import first_non_repeating_character

def test_first_non_repeating_character_basic():
    """Test basic functionality of finding first non-repeating character."""
    assert first_non_repeating_character("leetcode") == 'l'
    assert first_non_repeating_character("loveleetcode") == 'v'

def test_first_non_repeating_character_no_unique():
    """Test case where no non-repeating character exists."""
    assert first_non_repeating_character("aabb") is None
    assert first_non_repeating_character("aaaa") is None

def test_first_non_repeating_character_single_char():
    """Test with a single character string."""
    assert first_non_repeating_character("a") == 'a'

def test_first_non_repeating_character_multiple_unique():
    """Test when multiple unique characters exist."""
    assert first_non_repeating_character("abcde") == 'a'
    assert first_non_repeating_character("abcdea") == 'b'

def test_first_non_repeating_character_invalid_input():
    """Test handling of invalid input."""
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        first_non_repeating_character("")
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        first_non_repeating_character("AbCdE")
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        first_non_repeating_character("123")
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        first_non_repeating_character("hello!")