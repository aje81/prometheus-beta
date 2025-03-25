import os
import pytest
from pathlib import Path
from src.file_exists import check_file_exists

def test_existing_file(tmp_path):
    """Test that an existing file returns True."""
    test_file = tmp_path / "existing_file.txt"
    test_file.write_text("Test content")
    assert check_file_exists(test_file) == True

def test_non_existing_file(tmp_path):
    """Test that a non-existing file returns False."""
    non_existing_file = tmp_path / "non_existing_file.txt"
    assert check_file_exists(non_existing_file) == False

def test_directory(tmp_path):
    """Test that a directory returns False."""
    assert check_file_exists(tmp_path) == False

def test_invalid_path_type():
    """Test handling of invalid path types."""
    assert check_file_exists(None) == False
    assert check_file_exists(123) == False

def test_empty_string():
    """Test handling of empty string path."""
    assert check_file_exists("") == False

def test_relative_path(tmp_path):
    """Test file existence with relative paths."""
    current_dir = os.getcwd()
    try:
        os.chdir(tmp_path)
        test_file = Path("test_relative.txt")
        test_file.write_text("Relative path test")
        assert check_file_exists(test_file) == True
    finally:
        os.chdir(current_dir)