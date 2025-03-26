from collections import Counter
from typing import Dict, List


def count_word_frequencies(file_path: str) -> Dict[str, int]:
    """
    Read a text file and count the occurrences of each word.

    Args:
        file_path (str): Path to the text file containing words 
                         separated by commas and spaces.

    Returns:
        Dict[str, int]: A dictionary of word frequencies sorted in 
                        descending order of occurrence.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file is empty or contains invalid content.
    """
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read().strip()

        # Handle empty file case
        if not content:
            raise ValueError("The input file is empty.")

        # Split the content by comma and space, remove any extra whitespace
        words = [word.strip() for word in content.split(',')]

        # Remove any empty strings that might result from splitting
        words = [word for word in words if word]

        # Handle case with no valid words
        if not words:
            raise ValueError("No valid words found in the file.")

        # Count word frequencies and sort in descending order
        word_counts = Counter(words)
        return dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except Exception as e:
        raise ValueError(f"Error processing the file: {str(e)}")


def get_total_word_count(file_path: str) -> int:
    """
    Get the total number of words in the file.

    Args:
        file_path (str): Path to the text file containing words.

    Returns:
        int: Total number of words in the file.
    """
    frequencies = count_word_frequencies(file_path)
    return sum(frequencies.values())