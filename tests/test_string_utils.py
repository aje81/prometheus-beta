import pytest
from src.string_utils import reverse_words

def test_basic_reverse():
    """Test basic word reversal."""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert reverse_words("  Hello   World  ") == "World Hello"

def test_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_words("One Two Three Four") == "Four Three Two One"

def test_alphanumeric():
    """Test ignoring non-alphabetic characters."""
    assert reverse_words("Hello123 World456") == "World Hello"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words("") == ""

def test_single_word():
    """Test handling of single word."""
    assert reverse_words("Hello") == "Hello"

def test_whitespace_only():
    """Test handling of strings with only whitespace."""
    assert reverse_words("   ") == ""