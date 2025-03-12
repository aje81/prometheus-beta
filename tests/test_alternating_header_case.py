import pytest
from src.alternating_header_case import convert_to_alternating_header_case

def test_basic_conversion():
    """Test basic string conversion to alternating header case."""
    assert convert_to_alternating_header_case("hello world") == "HeLlO WoRlD"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert convert_to_alternating_header_case("python is awesome") == "PyThOn Is AwEsOmE"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_header_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert convert_to_alternating_header_case("a") == "A"

def test_special_characters():
    """Test conversion with special characters and mixed case."""
    assert convert_to_alternating_header_case("hello, WORLD!") == "HeLlO, WoRlD!"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_header_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_header_case(None)

def test_numeric_string():
    """Test conversion of a string with numbers."""
    assert convert_to_alternating_header_case("123 abc") == "123 AbC"