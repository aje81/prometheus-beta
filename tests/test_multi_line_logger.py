"""
Tests for multi-line logging utility.
"""

import pytest
from src.multi_line_logger import log_multiline
import io
import sys

def test_basic_multiline_logging():
    """Test basic multi-line logging functionality."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    log_multiline("Hello\nWorld")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert output.count('-') == 80  # 2 lines of 40 '-'
    assert "Hello" in output
    assert "World" in output

def test_custom_separator():
    """Test custom separator character and length."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    result = log_multiline("Test", sep_char='*', sep_length=10)
    
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert output.count('*') == 20  # 2 lines of 10 '*'
    assert result.startswith('**********')
    assert result.endswith('**********')

def test_custom_logger():
    """Test using a custom logger function."""
    custom_log = []
    def test_logger(msg):
        custom_log.append(msg)
    
    log_multiline("Custom Logger", logger=test_logger)
    
    assert len(custom_log) == 1
    assert "Custom Logger" in custom_log[0]

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        log_multiline(123)  # Non-string input
    
    with pytest.raises(ValueError):
        log_multiline("")  # Empty message
    
    with pytest.raises(ValueError):
        log_multiline("Test", sep_char="too long")  # Invalid separator
    
    with pytest.raises(ValueError):
        log_multiline("Test", sep_length=0)  # Invalid length