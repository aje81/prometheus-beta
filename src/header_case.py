def convert_to_header_case(input_string: str) -> str:
    """
    Convert a given string to header case.
    
    Header case is where the first letter of each word is capitalized,
    and words are separated by spaces.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_header_case("hello world")
        'Hello World'
        >>> convert_to_header_case("hello_world")
        'Hello World'
        >>> convert_to_header_case("hello-world")
        'Hello World'
        >>> convert_to_header_case("helloWorld")
        'Hello World'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Replace common separators with spaces
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Handle camelCase or PascalCase
    words = []
    current_word = normalized[0].upper()
    for char in normalized[1:]:
        if char.isupper():
            # Start a new word when we encounter an uppercase letter
            words.append(current_word)
            current_word = char
        elif char.isspace():
            # Append current word and reset
            words.append(current_word)
            current_word = ''
        else:
            current_word += char
    
    # Append the last word
    if current_word:
        words.append(current_word)
    
    # Capitalize each word and join with spaces
    return ' '.join(word.capitalize() for word in words if word)