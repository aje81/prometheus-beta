import pytest
from src.parentheses_validator import is_valid_parentheses

def test_valid_simple_parentheses():
    """Test basic valid parentheses combinations"""
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("{[]}") == True

def test_invalid_parentheses():
    """Test invalid parentheses combinations"""
    assert is_valid_parentheses("(]") == False
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("(((") == False
    assert is_valid_parentheses(")))") == False

def test_edge_cases():
    """Test edge cases for parentheses validation"""
    # Empty string should be valid
    assert is_valid_parentheses("") == True
    
    # Single bracket should be invalid
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    
    # Mismatched nested brackets
    assert is_valid_parentheses("([{]})") == False

def test_complex_valid_cases():
    """Test more complex valid parentheses arrangements"""
    assert is_valid_parentheses("({[]})") == True
    assert is_valid_parentheses("(){}[({})]") == True

def test_large_input():
    """Test a larger input of nested and mixed brackets"""
    large_valid = "(" * 1000 + ")" * 1000
    large_invalid = "(" * 1000 + ")" * 999
    
    assert is_valid_parentheses(large_valid) == True
    assert is_valid_parentheses(large_invalid) == False