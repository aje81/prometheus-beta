import pytest
from src.huffman_coding import (
    huffman_encode, 
    huffman_decode, 
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes
)

def test_build_frequency_dict():
    """Test frequency dictionary generation."""
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    
    # Edge case: empty string
    assert build_frequency_dict("") == {}

def test_huffman_encode_decode():
    """Test complete Huffman encoding and decoding process."""
    test_strings = [
        "hello world",
        "abracadabra",
        "mississippi",
        "aaabbbcccddd"
    ]
    
    for original_data in test_strings:
        # Encode
        encoded_data, tree_root = huffman_encode(original_data)
        
        # Decode
        decoded_data = huffman_decode(encoded_data, tree_root)
        
        # Verify
        assert decoded_data == original_data

def test_huffman_encode_exceptions():
    """Test error handling for encoding."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        huffman_encode("")

def test_huffman_decode_exceptions():
    """Test error handling for decoding."""
    with pytest.raises(ValueError, match="Encoded data and tree root must be provided"):
        huffman_decode("", None)
    
    with pytest.raises(ValueError, match="Encoded data and tree root must be provided"):
        huffman_decode(None, None)

def test_build_huffman_tree_exceptions():
    """Test error handling for tree building."""
    with pytest.raises(ValueError, match="Frequency dictionary cannot be empty"):
        build_huffman_tree({})

def test_build_huffman_codes():
    """Test Huffman code generation."""
    # Create a simple test scenario
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    tree_root = build_huffman_tree(freq_dict)
    codes = build_huffman_codes(tree_root)
    
    # Validate basic properties
    assert len(codes) == len(freq_dict)
    for char, code in codes.items():
        assert set(code) <= {'0', '1'}  # Only 0 and 1 allowed
        assert len(code) > 0  # Non-empty codes

def test_edge_cases():
    """Test various edge cases."""
    # Single character string
    single_char_data = "a" * 10
    encoded, tree = huffman_encode(single_char_data)
    decoded = huffman_decode(encoded, tree)
    assert decoded == single_char_data

    # String with unique characters
    unique_chars_data = "abcdefg"
    encoded, tree = huffman_encode(unique_chars_data)
    decoded = huffman_decode(encoded, tree)
    assert decoded == unique_chars_data