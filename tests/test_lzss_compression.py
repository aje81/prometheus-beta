"""
Test suite for LZSS Compression Algorithm.

This module contains comprehensive tests for the LZSSCompressor class,
covering various scenarios including edge cases and error handling.
"""

import pytest
import random
import string
from src.lzss_compression import LZSSCompressor

def generate_random_data(length, mode='mixed'):
    """
    Generate random test data.
    
    :param length: Length of data to generate
    :param mode: Type of data to generate ('mixed', 'text', 'binary')
    :return: Generated data
    """
    if mode == 'text':
        return ''.join(random.choices(string.ascii_letters + string.whitespace, k=length))
    elif mode == 'binary':
        return bytes(random.getrandbits(8) for _ in range(length))
    else:  # mixed
        return bytes(random.getrandbits(8) for _ in range(length))

class TestLZSSCompressor:
    def test_empty_input(self):
        """Test compression and decompression of empty input."""
        compressor = LZSSCompressor()
        
        # Test empty string
        empty_str = ''
        compressed_str = compressor.compress(empty_str)
        assert compressor.decompress(compressed_str) == b''
        
        # Test empty bytes
        empty_bytes = b''
        compressed_bytes = compressor.compress(empty_bytes)
        assert compressor.decompress(compressed_bytes) == b''
    
    def test_simple_compression(self):
        """Test basic compression and decompression."""
        compressor = LZSSCompressor()
        
        # Simple repeating pattern
        test_data = b'ABCABCABCABC'
        compressed = compressor.compress(test_data)
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == test_data
    
    def test_random_data_compression(self):
        """Test compression with random data of various lengths."""
        compressor = LZSSCompressor()
        
        # Test multiple data lengths and types
        test_lengths = [10, 100, 1000, 10000]
        test_modes = ['mixed', 'text', 'binary']
        
        for length in test_lengths:
            for mode in test_modes:
                test_data = generate_random_data(length, mode)
                
                compressed = compressor.compress(test_data)
                decompressed = compressor.decompress(compressed)
                
                assert decompressed == test_data, f"Failed for {mode} data of length {length}"
    
    def test_text_compression(self):
        """Test text-based compression."""
        compressor = LZSSCompressor()
        
        # Test with repetitive text
        test_data = "Hello world! " * 100
        compressed = compressor.compress(test_data)
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == test_data.encode('utf-8')
    
    def test_custom_window_sizes(self):
        """Test compression with different window sizes."""
        window_sizes = [512, 1024, 2048, 4096]
        
        for window_size in window_sizes:
            compressor = LZSSCompressor(window_size=window_size)
            test_data = generate_random_data(5000, 'mixed')
            
            compressed = compressor.compress(test_data)
            decompressed = compressor.decompress(compressed)
            
            assert decompressed == test_data
    
    def test_error_handling(self):
        """Test error handling for invalid compressed data."""
        compressor = LZSSCompressor()
        
        # Test incomplete match
        with pytest.raises(ValueError, match="Incomplete match information"):
            compressor.decompress(b'\x00\x01')
        
        # Test incomplete literal
        with pytest.raises(ValueError, match="Incomplete literal"):
            compressor.decompress(b'\x01')
        
        # Test invalid flag
        with pytest.raises(ValueError, match="Invalid compression flag"):
            compressor.decompress(b'\x02')
    
    def test_compression_ratio(self):
        """Basic test to ensure some level of compression."""
        compressor = LZSSCompressor()
        
        # Highly repetitive data
        test_data = b'ABCDEFG' * 1000
        
        compressed = compressor.compress(test_data)
        
        # Compressed data should be significantly smaller than original
        assert len(compressed) < len(test_data)
        
        # Ensure round-trip works
        decompressed = compressor.decompress(compressed)
        assert decompressed == test_data