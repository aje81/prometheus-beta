import os
import stat

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
    
    # Get file mode
    file_mode = os.stat(file_path).st_mode
    
    # Check if user/group/others have no write permissions
    return not bool(file_mode & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))