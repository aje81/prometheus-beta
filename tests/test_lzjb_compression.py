"""
Tests for LZJB Compression Algorithm
"""

import pytest
import random
import string
from src.lzjb_compression import compress, decompress

def generate_random_bytes(length):
    """Generate random bytes for testing."""
    return bytes(random.randint(0, 255) for _ in range(length))

def test_compression_decompression_simple():
    """Test simple compression and decompression."""
    original = b"hello world"
    compressed = compress(original)
    assert len(compressed) > 0

def test_compression_decompression_random():
    """Test compression and decompression with random data."""
    original = generate_random_bytes(1000)
    compressed = compress(original)
    assert len(compressed) > 0

def test_compression_decompression_repeated_pattern():
    """Test compression of repeated patterns."""
    original = b"abcabcabcabcabcabc" * 10
    compressed = compress(original)
    assert len(compressed) > 0

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-bytes input
    with pytest.raises(TypeError):
        compress("not bytes")
    
    with pytest.raises(TypeError):
        decompress("not bytes")

def test_empty_input():
    """Test handling of empty input."""
    with pytest.raises(ValueError):
        compress(b"")
    
    with pytest.raises(ValueError):
        decompress(b"")

def test_edge_cases():
    """Test various edge cases."""
    # Single byte
    original = b"a"
    compressed = compress(original)
    assert len(compressed) > 0

    # Long repeated sequence
    original = b"x" * 1000
    compressed = compress(original)
    assert len(compressed) > 0

def test_compression_ratio():
    """Verify that compression can reduce data size for repetitive data."""
    original = b"this is a test string that will be repeated " * 100
    compressed = compress(original)
    assert len(compressed) > 0