import os
import gzip
import shutil

def compress_file(input_path, output_path=None):
    """
    Compress a file using gzip compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.gz' to input path.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are insufficient permissions to read/write files.
        IsADirectoryError: If input_path is a directory instead of a file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path must be a file, not a directory: {input_path}")

    # Explicit read and write permission checks
    try:
        # Attempt to open the file to verify read permissions
        with open(input_path, 'rb'):
            pass
    except PermissionError:
        raise PermissionError(f"No read permission for file: {input_path}")

    # If no output path is specified, create one by appending .gz
    if output_path is None:
        output_path = input_path + '.gz'

    # Check write permissions for output path
    output_dir = os.path.dirname(output_path) or '.'
    if not os.access(output_dir, os.W_OK):
        raise PermissionError(f"No write permission for directory: {output_dir}")

    # Compress the file
    try:
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to read {input_path} or write {output_path}")

    return output_path