def is_valid_parentheses(s: str) -> bool:
    """
    Determine if a string of parentheses is valid.
    
    A string is considered valid if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses characters
    
    Returns:
        bool: True if the parentheses are valid, False otherwise
    
    Examples:
        >>> is_valid_parentheses("()")
        True
        >>> is_valid_parentheses("()[]{}")
        True
        >>> is_valid_parentheses("(]")
        False
        >>> is_valid_parentheses("([)]")
        False
        >>> is_valid_parentheses("{[]}")
        True
    """
    # Dictionary to map closing to opening parentheses
    brackets_map = {')': '(', ']': '[', '}': '{'}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the input string
    for char in s:
        # If it's a closing bracket
        if char in brackets_map:
            # If stack is empty or top doesn't match corresponding opening bracket
            if not stack or stack[-1] != brackets_map[char]:
                return False
            # Remove the matching opening bracket
            stack.pop()
        else:
            # If it's an opening bracket, push to stack
            stack.append(char)
    
    # Valid if stack is empty (all brackets matched)
    return len(stack) == 0