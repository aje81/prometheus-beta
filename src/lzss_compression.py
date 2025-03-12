"""
LZSS (Lempel-Ziv-Storer-Szymanski) Compression Algorithm Implementation.

This module provides functions for LZSS compression and decompression.
LZSS is a dictionary-based lossless compression algorithm that replaces 
repeated occurrences of data with references to a single copy.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, lookahead_size=16):
        """
        Initialize the LZSS Compressor.
        
        :param window_size: Size of the sliding window for searching previous matches
        :param lookahead_size: Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size

    def compress(self, data):
        """
        Compress input data using LZSS algorithm.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as bytes
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return b''
        
        compressed = bytearray()
        data_length = len(data)
        current_position = 0
        
        while current_position < data_length:
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Define search range for the sliding window
            start = max(0, current_position - self.window_size)
            end = current_position
            
            # Search for the longest match
            for offset in range(end - start):
                match_length = 0
                while (current_position + match_length < data_length and
                       match_length < self.lookahead_size and
                       data[current_position + match_length] == 
                       data[start + offset + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_position - (start + offset)
            
            # Encode the result
            if best_length > 2:
                # Encode as a match (offset, length)
                compressed.append(0)  # Flag for match
                compressed.append(best_offset & 0xFF)  # Lower byte of offset
                compressed.append((best_offset >> 8) & 0xFF)  # Upper byte of offset
                compressed.append(best_length)
                current_position += best_length
            else:
                # Encode as a literal
                compressed.append(1)  # Flag for literal
                compressed.append(data[current_position])
                current_position += 1
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress LZSS compressed data.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data as bytes
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check flag to determine if it's a match or literal
            if compressed_data[i] == 0:  # Match
                if i + 3 >= len(compressed_data):
                    raise ValueError("Incomplete match information")
                
                # Extract offset and length
                offset = compressed_data[i+1] | (compressed_data[i+2] << 8)
                length = compressed_data[i+3]
                
                # Reconstruct matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    decompressed.append(decompressed[start + j])
                
                i += 4
            elif compressed_data[i] == 1:  # Literal
                if i + 1 >= len(compressed_data):
                    raise ValueError("Incomplete literal")
                
                decompressed.append(compressed_data[i+1])
                i += 2
            else:
                raise ValueError(f"Invalid compression flag: {compressed_data[i]}")
        
        return bytes(decompressed)