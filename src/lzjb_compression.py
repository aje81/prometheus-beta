"""
LZJB Compression Algorithm Implementation

A simplified implementation of LZJB compression.
"""

def compress(data):
    """
    Compress input data using a simplified LZJB compression algorithm.
    
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
        # Define search window
        search_start = max(0, current_pos - 1024)
        search_end = current_pos
        
        # Initialize tracking variables
        best_length = 0
        best_offset = 0
        
        # Find longest matching sequence
        for j in range(search_start, search_end):
            match_length = 0
            while (current_pos + match_length < input_length and
                   match_length < 15 and
                   data[j + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = current_pos - j
        
        # Encode token
        if best_length > 2:
            # Compressed token: offset (10 bits) + length (3 bits) - 1
            token = ((best_offset & 0x3FF) << 3) | (best_length - 1)
            output.append((token >> 8) & 0xFF)   # High byte
            output.append(token & 0xFF)          # Low byte
            current_pos += best_length
        else:
            # Literal byte
            output.append(data[current_pos])
            current_pos += 1
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data compressed with the simplified LZJB algorithm.
    
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
        # Detect token type
        current_byte = compressed_data[current_pos]
        
        # Literal byte for values less than 32
        if current_byte < 32:
            output.append(current_byte)
            current_pos += 1
            continue
        
        # Ensure 2 bytes available for token
        if current_pos + 1 >= input_length:
            break
        
        # Read 2-byte token
        high_byte = current_byte
        low_byte = compressed_data[current_pos + 1]
        token = (high_byte << 8) | low_byte
        
        # Decode offset and length
        offset = (token >> 3) & 0x3FF
        length = (token & 0x7) + 1
        
        # Safe copy of repeated sequence
        if offset > len(output):
            output.append(current_byte)
            current_pos += 1
            continue
        
        # Copy repeated sequence
        start = len(output) - offset
        for _ in range(length):
            output.append(output[start])
            start += 1
        
        current_pos += 2
    
    return bytes(output)