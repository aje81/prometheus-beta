def convert_to_alternating_header_case(input_string):
    """
    Convert a string to alternating header case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating header case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_alternating_header_case("hello world")
        'HeLlO WoRlD'
        >>> convert_to_alternating_header_case("python is awesome")
        'PyThOn Is AwEsOmE'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating case preserving word boundaries
    words = input_string.split()
    
    # Convert each word with alternating case
    result_words = []
    for word in words:
        # Convert the word to alternating case
        word_chars = list(word)
        for i in range(len(word_chars)):
            word_chars[i] = word_chars[i].upper() if i % 2 == 0 else word_chars[i].lower()
        result_words.append(''.join(word_chars))
    
    return ' '.join(result_words)