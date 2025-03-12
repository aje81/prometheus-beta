import pytest
from src.string_converter import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces():
    """Test basic lowercase conversion."""
    assert convert_to_lowercase_with_spaces("Hello World") == "hello world"

def test_convert_already_lowercase():
    """Test string that is already lowercase."""
    assert convert_to_lowercase_with_spaces("hello world") == "hello world"

def test_mixed_case():
    """Test mixed case conversion."""
    assert convert_to_lowercase_with_spaces("HeLLo WoRLD") == "hello world"

def test_with_numbers_and_punctuation():
    """Test conversion with numbers and punctuation."""
    assert convert_to_lowercase_with_spaces("Hello, World! 123") == "hello, world! 123"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase_with_spaces("") == ""

def test_spaces_only():
    """Test conversion of a string with only spaces."""
    assert convert_to_lowercase_with_spaces("   ") == "   "

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)