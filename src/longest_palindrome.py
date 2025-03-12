def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
    
    Raises:
        TypeError: If input is not a string
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if len(s) < 2:
        return s
    
    # Initialize variables to track the longest palindrome
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around a center point to find palindrome length.
        
        Args:
            left (int): Left index to start expanding
            right (int): Right index to start expanding
        
        Returns:
            int: Length of the palindrome found
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return length of palindrome (right - left - 1)
        return right - left - 1
    
    # Check all possible centers
    for i in range(len(s)):
        # Check odd-length palindromes (single character center)
        length1 = expand_around_center(i, i)
        
        # Check even-length palindromes (two character center)
        length2 = expand_around_center(i, i + 1)
        
        # Take the maximum length
        current_max = max(length1, length2)
        
        # Update start and max_length if we found a longer palindrome
        if current_max > max_length:
            start = i - (current_max - 1) // 2
            max_length = current_max
    
    # Return the longest palindromic substring
    return s[start:start + max_length]