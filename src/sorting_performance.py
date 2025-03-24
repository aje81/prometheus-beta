import time
import random
import typing

def compare_sorting_algorithms(
    algorithm1: typing.Callable[[list], list], 
    algorithm2: typing.Callable[[list], list], 
    input_list: list, 
    num_runs: int = 5
) -> dict:
    """
    Compare the performance of two sorting algorithms.
    
    Args:
        algorithm1 (callable): First sorting algorithm to compare
        algorithm2 (callable): Second sorting algorithm to compare
        input_list (list): Input list to be sorted
        num_runs (int, optional): Number of times to run each algorithm. Defaults to 5.
    
    Returns:
        dict: Performance comparison results with timing and other metrics
    
    Raises:
        ValueError: If input_list is empty or num_runs is less than 1
    """
    # Input validation
    if not input_list:
        raise ValueError("Input list cannot be empty")
    
    if num_runs < 1:
        raise ValueError("Number of runs must be at least 1")
    
    # Create copies to ensure fair comparison
    results = {
        'algorithm1': {
            'name': algorithm1.__name__,
            'times': [],
            'average_time': None
        },
        'algorithm2': {
            'name': algorithm2.__name__,
            'times': [],
            'average_time': None
        },
        'comparison': {}
    }
    
    # Run performance tests
    for _ in range(num_runs):
        # Test algorithm1
        input_copy1 = input_list.copy()
        start_time = time.time()
        algorithm1(input_copy1)
        end_time = time.time()
        results['algorithm1']['times'].append(end_time - start_time)
        
        # Test algorithm2
        input_copy2 = input_list.copy()
        start_time = time.time()
        algorithm2(input_copy2)
        end_time = time.time()
        results['algorithm2']['times'].append(end_time - start_time)
    
    # Calculate average times
    results['algorithm1']['average_time'] = sum(results['algorithm1']['times']) / num_runs
    results['algorithm2']['average_time'] = sum(results['algorithm2']['times']) / num_runs
    
    # Compare performance
    results['comparison'] = {
        'faster_algorithm': (
            results['algorithm1']['name'] 
            if results['algorithm1']['average_time'] < results['algorithm2']['average_time'] 
            else results['algorithm2']['name']
        ),
        'performance_difference_percent': abs(
            (results['algorithm1']['average_time'] - results['algorithm2']['average_time']) 
            / max(results['algorithm1']['average_time'], results['algorithm2']['average_time']) 
            * 100
        )
    }
    
    return results