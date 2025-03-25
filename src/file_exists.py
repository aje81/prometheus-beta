import os
from typing import Union, Optional, PathLike

def check_file_exists(file_path: Union[str, PathLike]) -> bool:
    """
    Check if a file exists at the specified path.

    Args:
        file_path (str or PathLike): The path to the file to check.

    Returns:
        bool: True if the file exists and is a file, False otherwise.

    Notes:
        - Uses os.path.isfile() to verify the path points to a file
        - Handles both relative and absolute paths
        - Returns False for directories or non-existent paths
    """
    try:
        return os.path.isfile(file_path)
    except TypeError:
        # Handle cases with invalid path type
        return False