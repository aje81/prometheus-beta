import pytest
import random
import src.sorting_performance as sp

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def test_compare_sorting_algorithms_basic():
    # Test with a small random list
    test_list = [random.randint(1, 1000) for _ in range(100)]
    
    result = sp.compare_sorting_algorithms(bubble_sort, quick_sort, test_list)
    
    # Check result structure
    assert 'algorithm1' in result
    assert 'algorithm2' in result
    assert 'comparison' in result
    
    # Check times are recorded
    assert len(result['algorithm1']['times']) == 5
    assert len(result['algorithm2']['times']) == 5
    
    # Check average times are calculated
    assert result['algorithm1']['average_time'] is not None
    assert result['algorithm2']['average_time'] is not None
    
    # Check comparison details
    assert 'faster_algorithm' in result['comparison']
    assert 'performance_difference_percent' in result['comparison']

def test_compare_sorting_algorithms_edge_cases():
    # Test empty list raises ValueError
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        sp.compare_sorting_algorithms(bubble_sort, quick_sort, [])
    
    # Test invalid number of runs
    with pytest.raises(ValueError, match="Number of runs must be at least 1"):
        sp.compare_sorting_algorithms(bubble_sort, quick_sort, [1,2,3], num_runs=0)

def test_sorting_results():
    # Ensure the sorting actually works
    test_list = [random.randint(1, 1000) for _ in range(100)]
    
    result = sp.compare_sorting_algorithms(bubble_sort, quick_sort, test_list)
    
    # Verify sorted correctly with first algorithm
    test_list1 = test_list.copy()
    sorted_list1 = bubble_sort(test_list1)
    assert sorted_list1 == sorted(test_list)
    
    # Verify sorted correctly with second algorithm
    test_list2 = test_list.copy()
    sorted_list2 = quick_sort(test_list2)
    assert sorted_list2 == sorted(test_list)

def test_algorithm_names():
    # Test that algorithm names are correctly captured
    test_list = [random.randint(1, 1000) for _ in range(100)]
    
    result = sp.compare_sorting_algorithms(bubble_sort, quick_sort, test_list)
    
    assert result['algorithm1']['name'] == 'bubble_sort'
    assert result['algorithm2']['name'] == 'quick_sort'