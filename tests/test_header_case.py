import pytest
from src.header_case import convert_to_header_case

def test_basic_space_separated():
    """Test basic space-separated string conversion."""
    assert convert_to_header_case("hello world") == "Hello World"

def test_snake_case():
    """Test snake_case conversion."""
    assert convert_to_header_case("hello_world") == "Hello World"

def test_kebab_case():
    """Test kebab-case conversion."""
    assert convert_to_header_case("hello-world") == "Hello World"

def test_camel_case():
    """Test camelCase conversion."""
    assert convert_to_header_case("helloWorld") == "Hello World"

def test_pascal_case():
    """Test PascalCase conversion."""
    assert convert_to_header_case("HelloWorld") == "Hello World"

def test_mixed_case():
    """Test mixed case conversion."""
    assert convert_to_header_case("hello_world-test") == "Hello World Test"

def test_empty_string():
    """Test empty string handling."""
    assert convert_to_header_case("") == ""

def test_single_word():
    """Test single word conversion."""
    assert convert_to_header_case("hello") == "Hello"

def test_multiple_separators():
    """Test string with multiple different separators."""
    assert convert_to_header_case("hello_world-test_case") == "Hello World Test Case"

def test_error_handling():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError):
        convert_to_header_case(123)
    
    with pytest.raises(TypeError):
        convert_to_header_case(None)