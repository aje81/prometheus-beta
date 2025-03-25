def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    It works by recursively sorting the first 2/3 of the list, then the last 2/3, and then the first 2/3 again.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Recursive Stooge Sort implementation
    def _stooge_sort(arr, i, j):
        # If the first element is larger than the last, swap them
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
        # If there are more than 2 elements
        if j - i + 1 > 2:
            t = (j - i + 1) // 3
            
            # Recursively sort first 2/3
            _stooge_sort(arr, i, j - t)
            
            # Recursively sort last 2/3
            _stooge_sort(arr, i + t, j)
            
            # Recursively sort first 2/3 again
            _stooge_sort(arr, i, j - t)
        
        return arr
    
    # Call the recursive helper function
    return _stooge_sort(arr, 0, len(arr) - 1)