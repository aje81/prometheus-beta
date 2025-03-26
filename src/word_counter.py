import re

def count_unique_words(text: str) -> int:
    """
    Count the number of unique words in a given text, ignoring case and punctuation.
    
    Args:
        text (str): The input text to analyze
    
    Returns:
        int: Number of unique words in the text
    
    Examples:
        >>> count_unique_words("Hello, hello! How are you?")
        4
        >>> count_unique_words("")
        0
        >>> count_unique_words("  ")
        0
    """
    # Handle None or empty input
    if not text:
        return 0
    
    # Convert to lowercase and replace hyphens and other punctuation with spaces
    cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
    
    # Split into words, remove extra whitespace, and filter out empty strings
    words = [word for word in cleaned_text.split() if word]
    
    # Return count of unique words
    return len(set(words))