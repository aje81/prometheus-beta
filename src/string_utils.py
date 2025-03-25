def first_non_repeating_character(s: str) -> str | None:
    """
    Find the first non-repeating character in a string.

    Args:
        s (str): Input string containing only lowercase letters.

    Returns:
        str | None: The first non-repeating character, or None if no such character exists.

    Raises:
        ValueError: If the input string contains non-lowercase letters or special characters.

    Example:
        >>> first_non_repeating_character("leetcode")
        'l'
        >>> first_non_repeating_character("aabb")
        None
    """
    # Validate input 
    if not s or not all(char.islower() for char in s):
        raise ValueError("Input must be a non-empty string with only lowercase letters")

    # Count occurrences of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find first character with count of 1
    for char in s:
        if char_counts[char] == 1:
            return char
    
    # No non-repeating characters found
    return None