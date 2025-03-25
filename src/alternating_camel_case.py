def to_alternating_camel_case(input_string: str) -> str:
    """
    Convert a string to alternating camel case.
    
    Alternating camel case means the first letter is lowercase, 
    and subsequent words start with alternating case (lower/upper).
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating camel case
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    
    Examples:
        >>> to_alternating_camel_case("hello world python")
        'helloWorldPython'
        >>> to_alternating_camel_case("HELLO WORLD PYTHON")
        'helloWorldPython'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string.strip():
        raise ValueError("Input string cannot be empty")
    
    # Split the string and remove any extra whitespace
    words = input_string.strip().split()
    
    # Convert to alternating camel case
    if not words:
        return ""
    
    # First word always starts lowercase
    result_words = [words[0].lower()]
    
    # Alternate capitalization for subsequent words
    for i, word in enumerate(words[1:], 1):
        # Alternate between lower and upper case
        if i % 2 == 1:
            # Capitalize alphabetic words, keep numbers and non-alphabetic as-is
            if any(c.isalpha() for c in word):
                result_words.append(word.capitalize())
            else:
                result_words.append(word)
        else:
            # Use lowercase for even-indexed words
            result_words.append(word.lower())
    
    return ''.join(result_words)