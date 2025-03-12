def rotate_list(lst, k):
    """
    Rotate a list to the right by k positions.
    
    Args:
        lst (list): The input list to be rotated.
        k (int): Number of positions to rotate the list to the right.
    
    Returns:
        list: A new list rotated k positions to the right.
    
    Raises:
        TypeError: If input is not a list or k is not an integer.
        ValueError: If k is negative.
    
    Examples:
        >>> rotate_list([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate_list([1, 2, 3], 0)
        [1, 2, 3]
    """
    # Validate input types
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not isinstance(k, int):
        raise TypeError("Rotation amount must be an integer")
    
    # Handle edge cases
    if not lst:  # Empty list
        return []
    
    # Normalize k to be within list length
    k = k % len(lst) if len(lst) > 0 else 0
    
    # Perform rotation
    return lst[-k:] + lst[:-k] if k > 0 else lst.copy()