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
    
    # LZJB compression variables
    output = bytearray()
    input_length = len(data)
    current_pos = 0
    
    while current_pos < input_length:
        # Look-ahead buffer size
        look_ahead = min(input_length - current_pos, 256)
        
        # Try to find the longest match
        best_length = 1
        best_offset = 0
        
        # Search back up to 1024 bytes
        search_start = max(0, current_pos - 1024)
        
        for j in range(search_start, current_pos):
            match_length = 0
            
            # Check for match length
            while (match_length < look_ahead and 
                   j + match_length < current_pos and 
                   data[j + match_length] == data[current_pos + match_length]):
                match_length += 1
                
                # Stop if we've reached max match length
                if match_length >= 15:
                    break
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = current_pos - j
        
        # Encode the token
        if best_length > 2:
            # Compressed token: offset and length
            token = ((best_offset & 0x3FF) << 3) | (best_length - 1)
            output.append((token >> 8) & 0xFF)  # High byte
            output.append(token & 0xFF)         # Low byte
            current_pos += best_length
        else:
            # Literal token
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
        # For single byte data or literals up to 31
        if current_pos >= input_length or compressed_data[current_pos] < 32:
            if current_pos >= input_length:
                break
            output.append(compressed_data[current_pos])
            current_pos += 1
            continue
        
        # Ensure we have at least 2 bytes
        if current_pos + 1 >= input_length:
            raise ValueError("Malformed compressed data")
        
        # Read token bytes
        high_byte = compressed_data[current_pos]
        low_byte = compressed_data[current_pos + 1]
        token = (high_byte << 8) | low_byte
        
        # Decode offset and length
        offset = ((token >> 3) & 0x3FF)
        length = (token & 0x7) + 1
        
        # Validate offset and length
        if offset == 0 or offset > len(output):
            raise ValueError("Invalid offset in compressed data")
        
        # Copy matched sequence
        start = len(output) - offset
        for i in range(length):
            output.append(output[start + i])
        
        current_pos += 2
    
    return bytes(output)