import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'multiply': 2})
    assert result == [[2, 4], [6, 8]]

def test_add_operation():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'add': 5})
    assert result == [[6, 7], [8, 9]]

def test_transpose_operation():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'transpose': True})
    assert result == [[1, 3], [2, 4]]

def test_matrix_multiplication():
    arr = [[1, 2], [3, 4]]
    matrix = [[2, 0], [0, 2]]
    result = multiArrayManipulator(arr, {'matrix': matrix})
    assert result == [[2, 4], [6, 8]]

def test_multiple_operations():
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {
        'multiply': 2, 
        'add': 1, 
        'transpose': True
    })
    assert result == [[3, 7], [5, 9]]

def test_error_empty_array():
    with pytest.raises(ValueError):
        multiArrayManipulator([], {})

def test_error_invalid_multiply():
    with pytest.raises(TypeError):
        multiArrayManipulator([[1, 2]], {'multiply': 'invalid'})

def test_error_invalid_add():
    with pytest.raises(TypeError):
        multiArrayManipulator([[1, 2]], {'add': 'invalid'})

def test_error_incompatible_matrix_multiplication():
    with pytest.raises(ValueError):
        multiArrayManipulator([[1, 2]], {'matrix': [[1], [2], [3]]})