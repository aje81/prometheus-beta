"""
Multi-line logging utility with separation lines.

This module provides a function for logging multi-line messages with 
customizable separation lines to improve readability.
"""

def log_multiline(message, 
                  sep_char='-', 
                  sep_length=40, 
                  logger=print):
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (str): The message to log
        sep_char (str, optional): Character used for separation lines. Defaults to '-'.
        sep_length (int, optional): Length of separation lines. Defaults to 40.
        logger (callable, optional): Logging function. Defaults to print.

    Raises:
        ValueError: If message is empty or sep_char is invalid
        TypeError: If inputs are of incorrect type

    Returns:
        str: The logged message (useful for testing/verification)
    """
    # Input validation
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not message.strip():
        raise ValueError("Message cannot be empty")
    
    if not isinstance(sep_char, str) or len(sep_char) != 1:
        raise ValueError("Separation character must be a single character")
    
    if not isinstance(sep_length, int) or sep_length < 1:
        raise ValueError("Separation length must be a positive integer")
    
    # Create separation line
    sep_line = sep_char * sep_length
    
    # Prepare multi-line message
    log_output = f"{sep_line}\n{message}\n{sep_line}"
    
    # Log the message
    logger(log_output)
    
    return log_output