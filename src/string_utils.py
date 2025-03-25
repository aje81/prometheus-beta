def switch_cases(str1, str2):
    """
    Swap the character cases between two input strings.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
    
    Returns:
        str: A new string where characters from str1 have their case swapped,
             and characters from str2 have their case swapped.
    
    Raises:
        TypeError: If either input is not a string.
    
    Examples:
        >>> switch_cases('Hello', 'WORLD')
        'hELLO', 'world'
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Helper function to swap case for a single string
    def swap_case_str(s):
        return ''.join(c.lower() if c.isupper() else c.upper() for c in s)
    
    return swap_case_str(str1), swap_case_str(str2)