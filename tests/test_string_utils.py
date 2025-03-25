import pytest
from src.string_utils import switch_cases

def test_switch_cases_basic():
    """Test basic case swapping."""
    result = switch_cases('Hello', 'WORLD')
    assert result == ('hELLO', 'world')

def test_switch_cases_mixed_case():
    """Test switching cases with mixed case strings."""
    result = switch_cases('HeLLo', 'wOrLd')
    assert result == ('hEllO', 'WoRlD')

def test_switch_cases_empty_strings():
    """Test switching cases with empty strings."""
    result = switch_cases('', '')
    assert result == ('', '')

def test_switch_cases_only_letters():
    """Test switching cases with strings containing only letters."""
    result = switch_cases('AbCdE', 'fGhIj')
    assert result == ('aBcDe', 'FgHiJ')

def test_switch_cases_with_numbers_and_symbols():
    """Test switching cases with strings containing numbers and symbols."""
    result = switch_cases('Hello123!', 'WORLD456@')
    assert result == ('hELLO123!', 'world456@')

def test_switch_cases_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Both inputs must be strings"):
        switch_cases(123, 'test')
    
    with pytest.raises(TypeError, match="Both inputs must be strings"):
        switch_cases('test', None)
    
    with pytest.raises(TypeError, match="Both inputs must be strings"):
        switch_cases([], {})