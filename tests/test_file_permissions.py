import os
import pytest
import tempfile
import stat

from src.file_permissions import is_file_read_only

def test_is_file_read_only_normal_writable_file():
    """Test a normal writable file returns False."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write("test content")
        temp_file_path = temp_file.name
    
    try:
        assert is_file_read_only(temp_file_path) is False
    finally:
        os.unlink(temp_file_path)

def test_is_file_read_only_read_only_file():
    """Test a read-only file returns True."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write("test content")
        temp_file_path = temp_file.name
    
    try:
        # Change file permissions to read-only
        os.chmod(temp_file_path, stat.S_IRUSR)
        
        assert is_file_read_only(temp_file_path) is True
    finally:
        os.unlink(temp_file_path)

def test_is_file_read_only_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        is_file_read_only("nonexistent_file_123456.txt")

def test_is_file_read_only_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        is_file_read_only(123)
    
    with pytest.raises(TypeError):
        is_file_read_only(None)