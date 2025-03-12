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
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(input_string):
        # Uppercase for even indices, lowercase for odd indices
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)