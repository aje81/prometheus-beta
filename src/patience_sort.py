from typing import List, TypeVar, Comparable as TypeComparable, Protocol

T = TypeVar('T')

class Comparable(Protocol):
    def __lt__(self: T, other: T) -> bool: ...

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort is an algorithm that sorts a list by treating it like 
    playing a game of Patience (Solitaire), creating piles and then merging them.
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    """
    # If the list is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (stacks) to represent the sorting process
    piles = []
    
    # Process each element in the input array
    for item in arr:
        # Find the correct pile to place the current item
        placed = False
        for pile in piles:
            # If the current item can be placed on top of this pile
            if not pile or item >= pile[-1]:
                pile.append(item)
                placed = True
                break
        
        # If no existing pile works, create a new pile
        if not placed:
            piles.append([item])
    
    # Merge the piles using a min-heap based approach
    result = []
    while piles:
        # Find the pile with the smallest top element
        smallest_pile_index = min(range(len(piles)), key=lambda i: piles[i][-1])
        
        # Remove the top element from the chosen pile and add to result
        result.append(piles[smallest_pile_index].pop())
        
        # Remove the pile if it becomes empty
        if not piles[smallest_pile_index]:
            piles.pop(smallest_pile_index)
    
    return result