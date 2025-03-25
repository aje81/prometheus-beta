import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion to alternating camel case."""
    assert to_alternating_camel_case("hello world python") == "helloWorldpython"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_camel_case("HELLO world PYTHON") == "helloWorldpython"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_camel_case("hello") == "hello"

def test_multiple_spaces():
    """Test conversion with multiple spaces between words."""
    assert to_alternating_camel_case("hello   world   python") == "helloWorldpython"

def test_leading_trailing_spaces():
    """Test conversion with leading and trailing spaces."""
    assert to_alternating_camel_case("  hello world python  ") == "helloWorldpython"

def test_error_empty_string():
    """Test that empty string raises ValueError."""
    with pytest.raises(ValueError):
        to_alternating_camel_case("")

def test_error_whitespace_only():
    """Test that whitespace-only string raises ValueError."""
    with pytest.raises(ValueError):
        to_alternating_camel_case("   ")

def test_error_non_string_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)

def test_numbers_and_words():
    """Test conversion with numbers and words."""
    assert to_alternating_camel_case("hello 42 world 17 python") == "hello42worldPython"