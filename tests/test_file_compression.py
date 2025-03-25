import os
import gzip
import pytest
import tempfile
import shutil
from src.file_compression import compress_file

@pytest.fixture
def sample_file():
    """Create a temporary sample file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("This is a test file for compression.")
        temp_file_path = temp_file.name
    yield temp_file_path
    os.unlink(temp_file_path)

def test_compress_file(sample_file):
    """Test basic file compression."""
    compressed_file = compress_file(sample_file)
    
    # Check compressed file is created
    assert os.path.exists(compressed_file)
    assert compressed_file.endswith('.gz')
    
    # Check file can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for compression."
    
    # Clean up
    os.unlink(compressed_file)

def test_compress_file_with_custom_output(sample_file):
    """Test compression with a custom output path."""
    custom_output = sample_file + '.custom.gz'
    compressed_file = compress_file(sample_file, custom_output)
    
    assert compressed_file == custom_output
    assert os.path.exists(compressed_file)
    
    # Clean up
    os.unlink(compressed_file)

def test_nonexistent_file():
    """Test compression of a non-existent file."""
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_directory_compression():
    """Test attempting to compress a directory."""
    with pytest.raises(IsADirectoryError):
        compress_file(tempfile.gettempdir())

def test_file_permissions(sample_file):
    """Simulate a permission error by making the input file read-only."""
    # Make the file read-only
    os.chmod(sample_file, 0o444)
    
    with pytest.raises(PermissionError):
        compress_file(sample_file)
    
    # Reset permissions
    os.chmod(sample_file, 0o666)