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
    
    # Ensure exact case matching
    if not any(str1[i] == str2[j] for i in range(len(str1)) for j in range(len(str2))):
        return ""
    
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Dynamic programming to find longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and end index if needed
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                # Reset dynamic programming table
                dp[i][j] = 0
    
    # Return the longest common substring
    substring = str1[end_index - max_length + 1 : end_index + 1] if max_length > 0 else ""
    
    # Ensure substring meets our requirement of being a complete substring
    for i in range(len(str2) - len(substring) + 1):
        if substring == str2[i:i+len(substring)]:
            return substring
    
    return ""