import re

def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string while preserving word integrity.
    
    Args:
        input_string (str): The input string to be processed.
    
    Returns:
        str: A string with words in reversed order, handling multiple spaces 
             and ignoring non-alphabetic characters.
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        'World Hello'
        >>> reverse_words("Hello123 World456")
        'World Hello'
    """
    # Remove leading and trailing whitespace
    input_string = input_string.strip()
    
    # Extract words (only alphabetic characters from the beginning and end of tokens)
    words = re.findall(r'[A-Za-z]+', input_string)
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words with a single space
    return ' '.join(reversed_words)