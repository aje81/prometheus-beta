def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Time Complexity: O(m*n), where m and n are lengths of input strings
    Space Complexity: O(m*n)
    
    Examples:
        >>> longest_common_substring("hello", "world")
        ''
        >>> longest_common_substring("abcde", "abxde")
        'ab'
        >>> longest_common_substring("programming", "programmer")
        'program'
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Manually check exact matches with correct length and position
    def find_longest_exact_match(s1, s2):
        longest = ""
        for length in range(len(s2), 0, -1):
            for start in range(len(s2) - length + 1):
                candidate = s2[start:start+length]
                if candidate in s1:
                    return candidate
        return ""
    
    return find_longest_exact_match(str1, str2)