"""
LZJB Compression Algorithm Implementation

This module provides an implementation of the LZJB (LZ Jake Bilbrey) compression algorithm.
LZJB is a fast compression algorithm designed for speed over maximum compression ratio.
"""

def compress(data):
    """
    Compress input data using the LZJB compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    output = bytearray()
    input_length = len(data)
    current_pos = 0
    
    while current_pos < input_length:
        # Look for the longest matching sequence
        best_length = 0
        best_offset = 0
        
        # Search back window (max 1024 bytes)
        search_start = max(0, current_pos - 1024)
        search_end = current_pos
        
        for j in range(search_start, search_end):
            match_length = 0
            
            # Check match length, stop at 15 or end of input
            while (current_pos + match_length < input_length and 
                   match_length < 15 and 
                   data[j + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = current_pos - j
        
        # Encode token
        if best_length > 2:
            # Compressed token: offset and length 
            # 3 bits for length, rest for offset
            token = ((best_offset & 0x3FF) << 3) | (best_length - 1)
            output.append((token >> 8) & 0xFF)  # High byte
            output.append(token & 0xFF)         # Low byte
            current_pos += best_length
        else:
            # Literal byte
            output.append(data[current_pos])
            current_pos += 1
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data compressed with the LZJB algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or malformed
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    output = bytearray()
    input_length = len(compressed_data)
    current_pos = 0
    
    while current_pos < input_length:
        # Check if it's a literal byte (first byte < 32)
        if compressed_data[current_pos] < 32:
            output.append(compressed_data[current_pos])
            current_pos += 1
            continue
        
        # Ensure we have 2 bytes for token processing
        if current_pos + 1 >= input_length:
            raise ValueError("Malformed compressed data")
        
        # Read 2-byte token
        high_byte = compressed_data[current_pos]
        low_byte = compressed_data[current_pos + 1]
        token = (high_byte << 8) | low_byte
        
        # Decode offset and length
        # Last 3 bits are length, rest are offset
        offset = (token >> 3) & 0x3FF
        length = (token & 0x7) + 1
        
        # Validate offset
        if offset == 0 or offset > len(output):
            # Fallback to literal if invalid offset
            output.append(compressed_data[current_pos])
            current_pos += 1
            continue
        
        # Copy sequence from previous match
        start = len(output) - offset
        for _ in range(length):
            output.append(output[start])
            start += 1
        
        current_pos += 2
    
    return bytes(output)