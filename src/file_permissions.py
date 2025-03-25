import os

def is_file_read_only(file_path: str) -> bool:
    """
    Determine if a file is read-only.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is read-only, False otherwise.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Use os.access to check write permissions
    return not os.access(file_path, os.W_OK)